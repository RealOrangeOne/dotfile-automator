import subprocess

def call(command):
    shell = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = shell.communicate()
    return str(output), error
