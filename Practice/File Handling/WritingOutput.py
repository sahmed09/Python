import subprocess

# Writing python output to the files:
# check_call() method of module subprocess is used to execute a python script and write the output of that script to a file.
with open("output.txt", "wb") as f:
    subprocess.check_call(["python", "files.py"], stdout=f)
