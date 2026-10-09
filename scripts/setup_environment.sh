#!/usr/bin/env bash
# Create a local Python development environment; no hardware or ROS installation.
set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON_BIN:-python3}"
venv_path="$project_root/.venv"

"$python_bin" -c 'import sys; assert sys.version_info >= (3, 10), "Python 3.10+ required"'
if [[ -e "$venv_path" ]]; then
    if [[ ! -f "$venv_path/pyvenv.cfg" || ! -x "$venv_path/bin/python" ]]; then
        printf '%s
' 'Existing .venv is not a usable Python virtual environment; no files replaced.' >&2
        exit 1
    fi
else
    "$python_bin" -m venv "$venv_path"
fi

# Build and install a normal wheel; no .pth file or sys.path workaround is required.
# Re-run this script after changing package source. Build isolation may download setuptools.
"$venv_path/bin/python" -m pip install --no-deps --force-reinstall "$project_root"
"$venv_path/bin/python" -I -c 'import robot_control; print("Installed core import verified")'
"$venv_path/bin/python" "$project_root/scripts/check_environment.py"
printf '%s
' 'Local package installed. Run the integration check from tests/README.md.'
