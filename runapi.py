#python runapi.py
import subprocess
subprocess.run([
    "python", "-m", "pytest",
    "-s", "tests/basic/",
    "--maxfail=1",
    "--disable-warnings",
    "-v"
])
