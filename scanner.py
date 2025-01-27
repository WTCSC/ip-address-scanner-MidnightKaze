#!/bin/python3

# will remove the unneeded ones later lol
import subprocess
import ipaddress
import sys
import platform
import time

def ping_that_ip(ip):
    # b/c window and linux use differnt flags in ping, we'll account for both
    flag = "n" if platform.system().lower == "windows" else "c"
    command = ['ping', flag, '1', str(ip)]
    
    try:
        start = time.time()
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=5)
        end = time.time()

    except:
        subprocess.TimeoutExpired
    #(((end-start) * 1000), 2) >>> to get the ms