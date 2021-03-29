import subprocess, sys
from datetime import datetime

try:
    subprocess.run(["git", "add", sys.argv[1]], capture_output=True)
    subprocess.run(["git", "commit", "-q", "-m", "{}".format(datetime.now())], capture_output=True)
    subprocess.run(["git", "push", "-q", "-u", "origin", "main"], capture_output=True)
except:
    pass

subprocess.run([sys.executable, sys.argv[1], sys.argv[2]])
