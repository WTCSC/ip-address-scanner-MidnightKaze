#!/bin/python3

import subprocess
import re
import sys

# Check that user gave a real MAC address
def mac_validation(mac):
     # Sets the match pattern to 6 pairs of hexadecimals within the acceptable range that are seperated with colons.
    mac_match = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    
    # Uses regular expressions to ensure the pattern and the input match.
    if not re.match(mac_match, mac):
        print ("Please input a valid MAC address. Double check that the address is correct or try reformatting to this format: xx:xx:xx:xx:xx:xx")
        return False
    
    return True

# Check that user gave a real interface option
def interface_validation(interface):
    # Essentially checks that the interface is up and running using ip link show.
    try:
        subprocess.check_output(['ip', 'link', 'show', interface], stderr=subprocess.STDOUT)
        return True
    
    # If subprocess returns and error then the code will also return an error.
    except:
        subprocess.CalledProcessError
        print("Please input a valid network interface. Double check your input and try again.")
        return False
    
# Putting it all together :D
def main():

    # Interface is the argument in position 1
    interface = sys.argv[1]

    # MAC is the argument in position 2
    mac = sys.argv[2]

    # Runs the validation for the MAC Address
    if not mac_validation(mac):
        exit(1)
    
    # Runs the validation for the interface
    if not interface_validation(interface):
        exit(1)
    
    # Bringing the interface down + an error messeage if it fails
    if not subprocess.run(['ip', 'link', 'set', interface, 'down']):
        print("Failed to bring the interface down.")
        exit(1)
    
    # Changing the MAC address + an error messeage if it fails
    if not subprocess.run(['ip', 'link', 'set', interface, 'address', mac]):
        print("Failed to change the MAC address.")
        subprocess.run(['ip', 'link', 'set', interface, 'up'])
        exit(1)

    # Bringing the interface up + an error messeage if it fails
    if not subprocess.run(['ip', 'link', 'set', interface, 'up']):
        print("Failed to bring the interface back up.")
        exit(1)

    # Returns some validation for the user to tell them that the change process is completed.
    print("Changed your MAC address ✧( ˶^ ᗜ ^˶ )")
    print("Run ip link show to see the changes made (there might be a little bit of delay or lag).")
    
    exit(0)

if __name__=="__main__":
    main()