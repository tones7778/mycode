# Import the module
import subprocess

# Ask the user for input
host =  (['172.16.20.2', '172.16.20.3'])

# Set up the echo command and direct the output to a pipe
for i in host:
    p1 = subprocess.Popen(['ping', '-c 2', i], stdout=subprocess.PIPE)

# Run the command
    output = p1.communicate()[0]

    print output
