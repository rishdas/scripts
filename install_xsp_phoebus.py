import subprocess
import os
subprocess.call(["git", "clone", "https://github.iu.edu/sirdas/crest_share_files.git"])
os.chdir('./crest_share_files')
subprocess.call(["sudo", "yum", "install", "libxsp-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "libxsp-client-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "libxsp-debuginfo-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "libxsp-xspd-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "phoebus-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "phoebus-client-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "phoebus-debuginfo-1.0-10.x86_64.rpm"])
subprocess.call(["sudo", "yum", "install", "phoebus-server-1.0-10.x86_64.rpm"])
