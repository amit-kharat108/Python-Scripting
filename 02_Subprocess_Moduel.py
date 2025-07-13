#!/usr/bin/env python3.8

import subprocess
import os

# Run 'ls -la /home/akharat/python-scripting' with subprocess module.

subprocess.run(["ls", "-la", "/home/akharat/python-scripting"])

# Capture the output of 'uname -r' and store it in a variable

KERNEL_VERSION=subprocess.run(['uname', '-r'], capture_output=True, text=True)

print(f"Kernel Version: {KERNEL_VERSION.stdout.strip()}")


# Run a command using subprocess and check if it failed.

result = subprocess.run(['ls', '/not_a_directory'], capture_output=True, text=True)

if result.returncode != 0:
    print(f"Directory does not exist and the error is: {result.stderr.strip()}")
else:
    print(f"Directory exist and here are the contents of the directory: {result.stout.strip()}")

# Method check_output to get the output directly

output = subprocess.check_output(['date'], text=True)

print(output)

# Piping data with Popen

PIPE_1 = subprocess.Popen(['ls', '-lh'], stdout=subprocess.PIPE, text=True)
PIPE_2 = subprocess.Popen(['grep', 'py'], stdin=PIPE_1.stdout, stdout=subprocess.PIPE, text=True)

PIPE_1.stdout.close()

OUTPUT, _ = PIPE_2.communicate()

print(f"Files found with contains py in them:\n {OUTPUT}")


# Write something to existing file or create a new file

with open('/home/akharat/FCBarcelona.txt', 'w') as f:
    subprocess.run(['echo', 'I Love Barcelona. Cuz it is not just a team but a family'], stdout=f)

# Run command with environment variables

my_env = os.environ.copy()

my_env["MY_VAR"]='FCBarcelona'

print(subprocess.run(['bash','-c','echo $MY_VAR'], env=my_env))


# Complex pipeline: ps aux | grep python | sort -rk3


PIPE_1=subprocess.Popen(['ps','aux'], stdout=subprocess.PIPE, text=True)

PIPE_2=subprocess.Popen(['grep', 'python'], stdin=PIPE_1.stdout, stdout=subprocess.PIPE, text=True)

PIPE_1.stdout.close()

PIPE_3=subprocess.Popen(['sort', '-rk3'], stdin=PIPE_2.stdout, stdout=subprocess.PIPE, text=True)

PIPE_2.stdout.close()

OUTPUT, _ = PIPE_3.communicate()

print(OUTPUT)
