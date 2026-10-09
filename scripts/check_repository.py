#!/usr/bin/env python3
"""Read-only scaffold checks. Does not run motor code or certify stage completion."""
import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def check(root):
    errors = []
    required = [
        "AGENTS.md", "README.md", "PROJECT.md", "CURRENT_TASK.md",
        "roadmap/master-roadmap.md", "roadmap/milestones.md",
        "roadmap/backlog.md", "roadmap/prerequisites.md",
        "knowledge/index.md", "learning/progress.md", "learning/WORKFLOW.md",
        "engineering/repository-baseline.md", "engineering/motorbridge-api-baseline.md",
        "engineering/architecture/system-overview.md", "docs/source-map.md",
        "docs/source/AGENTS-V1.2.pdf", "config/README.md",
        "config/motors.example.yaml", "config/safety.example.yaml",
        "config/robot_2dof.example.yaml", "pyproject.toml",
        "src/robot_control/__init__.py", "scripts/setup_environment.sh",
        "tests/README.md", "tests/integration/test_package_imports.py",
    ]
    required += [f"templates/{name}.md" for name in (
        "theory-note", "engineering-note", "experiment-report", "troubleshooting-case",
        "code-review", "daily-task", "stage-assessment", "adr",
    )]
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")

    layout = root / "engineering/architecture/target-layout.md"
    if layout.exists():
        body = layout.read_text()
        if "```text\n" not in body:
            errors.append("Missing canonical directory tree")
        else:
            tree = body.split("```text\n", 1)[1].split("```", 1)[0]
            parents = {0: root}
            for line in tree.splitlines():
                match = re.match(r"([│ ]*)[├└]── (.+)", line)
                if not match:
                    continue
                prefix, name = match.groups()
                if name.endswith("/"):
                    depth = len(prefix) // 4
                    directory = parents[depth] / name[:-1]
                    parents[depth + 1] = directory
                    if not directory.is_dir():
                        errors.append(f"Missing scaffold directory: {directory.relative_to(root)}")

    excluded = {".git", ".venv", "venv", "build", "dist", "__pycache__"}
    markdown_files = sorted(p for p in root.rglob("*.md") if not excluded.intersection(p.relative_to(root).parts))
    local_link_count = 0
    for path in markdown_files:
        body = path.read_text(encoding="utf-8")
        # Inline links used by this scaffold; fenced examples are not navigation.
        body = re.sub(r"^```.*?^```[^\n]*$", "", body, flags=re.M | re.S)
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", body):
            target = match.group(1).strip()
            if target.startswith("<") and ">" in target:
                target = target[1:target.index(">")]
            else:
                target = target.split(' "', 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path or target.startswith("//"):
                continue
            local_link_count += 1
            if not (path.parent / unquote(parsed.path)).resolve().exists():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")

    backlog = root / "roadmap/backlog.md"
    task_ids = []
    if backlog.exists():
        task_ids = re.findall(r"^\| (S[1-8]-\d{3}) \|", backlog.read_text(), re.M)
        if not task_ids or len(task_ids) != len(set(task_ids)):
            errors.append("Task IDs are missing or duplicated")
        for stage in range(1, 9):
            if not any(t.startswith(f"S{stage}-") for t in task_ids):
                errors.append(f"No planned task for S{stage}")
        for row in backlog.read_text().splitlines():
            if re.match(r"^\| S[1-8]-\d{3} \|", row):
                for dependency in re.findall(r"S[1-8]-\d{3}", row):
                    if dependency not in task_ids:
                        errors.append(f"Unknown task dependency: {dependency}")

    milestones = root / "roadmap/milestones.md"
    if milestones.exists():
        headings = re.findall(r"^## (S[1-8])：", milestones.read_text(), re.M)
        if headings != [f"S{i}" for i in range(1, 9)]:
            errors.append("Expected ordered S1-S8 milestone definitions")

    for name in ("motors", "safety", "robot_2dof"):
        path = root / f"config/{name}.example.yaml"
        if path.exists() and not re.search(
            r"^hardware_enabled:\s*false\s*$", path.read_text(), re.M
        ):
            errors.append(f"Example hardware flag must remain false: {path.name}")

    python_files = sorted(p for directory in ("scripts", "src", "tests") for p in (root / directory).rglob("*.py"))
    for path in python_files:
        try:
            ast.parse(path.read_text(), filename=str(path))
        except SyntaxError as exc:
            errors.append(f"Syntax error: {path.name}: {exc}")

    return errors, len(markdown_files), local_link_count, len(task_ids), len(python_files)


def main():
    if len(sys.argv) > 2:
        print("Usage: python3 scripts/check_repository.py [repository_path]", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path(__file__).resolve().parents[1]
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 2
    errors, md_count, links, tasks, scripts = check(root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"PASS: {md_count} Markdown files, {links} local file links, {tasks} task IDs, {scripts} Python syntax checks.")
    print("Checks cover the scaffold only, not remote URLs, Markdown anchors, business behavior, learning mastery, or hardware safety.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
