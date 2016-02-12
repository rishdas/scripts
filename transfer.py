import time
import subprocess
import os
import datetime

start = datetime.datetime.now()
subprocess.call(["globus-url-copy", "-v", "ftp://172.16.105.3/pub/sample.txt", "Downloads/"])
end = datetime.datetime.now()
print (end-start)
