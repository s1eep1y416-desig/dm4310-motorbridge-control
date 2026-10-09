#!/usr/bin/env python3
"""Report the current interpreter's metadata without importing hardware SDKs."""
from importlib import metadata
import json
import os
import platform
import shutil
import sys


def report():
    packages = {}
    for name in ("motorbridge", "numpy", "pin", "pinocchio", "mujoco"):
        try:
            dist = metadata.distribution(name)
            packages[name] = {
                "distribution_name": dist.metadata.get("Name", name),
                "version": dist.version,
                "location": str(dist.locate_file("")),
            }
        except metadata.PackageNotFoundError:
            packages[name] = None
    return {
        "scope": "Current interpreter metadata only; no SDK import or device access.",
        "platform": platform.platform(),
        "machine": platform.machine(),
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "packages": packages,
        "commands_on_path": {name: shutil.which(name) for name in ("git", "ros2", "colcon")},
        "ros_distro_environment": os.environ.get("ROS_DISTRO"),
        "notes": [
            "Missing metadata does not prove absence from other environments.",
            "The pin and pinocchio distribution names are reported without asserting equivalence.",
            "Metadata presence does not validate native ABI, firmware, or hardware compatibility.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(report(), ensure_ascii=False, indent=2))
