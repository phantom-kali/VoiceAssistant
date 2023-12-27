import subprocess
import re

def execute_linux_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr

s = execute_linux_command("wmctrl -l")
print(s)
running_programs = []

identifiers = re.finditer("0x0", s)

program = ""
for identifier in identifiers:
    print("done", identifier.start())
    program = identifier.start()
    

print(running_programs)
                




