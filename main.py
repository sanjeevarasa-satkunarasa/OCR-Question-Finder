import subprocess

# Running a shell command and capturing its output
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)