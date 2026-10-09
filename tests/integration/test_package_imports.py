"""Architecture check: the installed core imports without hardware dependencies."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class InstalledCoreImportTest(unittest.TestCase):
    def test_imports_from_outside_repository_without_hardware_sdk(self):
        code = """
import importlib
import sys
names = ("robot_control", "robot_control.actuator", "robot_control.controllers",
         "robot_control.kinematics", "robot_control.dynamics", "robot_control.trajectory",
         "robot_control.safety", "robot_control.utils")
for name in names:
    importlib.import_module(name)
for name in ("motorbridge", "rclpy", "pinocchio", "mujoco", "can", "serial"):
    assert name not in sys.modules, f"Core import implicitly loaded {name}"
print("All core packages imported without loading optional hardware/ROS libraries")
"""
        with tempfile.TemporaryDirectory(prefix="robot-core-import-") as directory:
            result = subprocess.run(
                [sys.executable, "-I", "-c", code], cwd=Path(directory),
                capture_output=True, text=True, timeout=30,
            )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
