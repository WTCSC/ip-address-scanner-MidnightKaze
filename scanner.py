#!/bin/python3

# this will be better documented later on lmao

# will remove the unneeded ones later lol
import subprocess
import math
import ipaddress
import sys
import platform
import time

def ping_that_ip(ip):
    # b/c window and linux use differnt flags in ping, we'll account for both
    flag = "-n" if platform.system().lower == "windows" else "-c"
    command = ['ping', flag, '1', str(ip)]
    
    try:
        # runs the command while also keep track of the times
        start = time.time()
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=5)
        end = time.time()

        # if the command was ran succesfully (exit 0) then it will continue on by spitting out the time
        if output.returncode == 0:
            response_time = math.floor((end-start)*1000) # Returns the number of milliseconds, floored
            return "UP", response_time, None
        
        # else wise it will return an error
        else:
            return "DOWN", None, output.stderr
    
    # if it was a timeout error the follow will proceed (timeout=5 gives the code 5 seconds to exicute before it will teminate)
    except subprocess.TimeoutExpired:
        return "DOWN", None, "REQUEST TIMED OUT."
    
    # if anything gets by it'll spit this out
    except Exception as e:
        return "DOWN", None, str(e)

# LETS THROW IT ALL TOGETHER
def main():
    cidr = sys.argv[1]

    try: # <<< could use if not if you wanted to ig
        netwrk = ipaddress.ip_network(cidr, strict=True)
    except ValueError as e:
        print("Please provide a valid CIRD notation network range. Double check and try again.")
        sys.exit(1)

    print(f"Scanning network {cidr}...")
    print(f"Total number of found hosts: {netwrk.num_addresses - 2} (not including network and broadcast hosts)")

    for ip in netwrk.hosts():
        status, response_time, error = ping_that_ip(ip)

        if status == "UP":
            print(f"{ip}: UP [Response Time: {response_time} ms]")
        else:
            print(f"{ip}: DOWN [Error: {error}]")

    sys.exit(0)

if __name__=="__main__":
    main()