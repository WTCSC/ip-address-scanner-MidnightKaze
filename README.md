[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17891882)

# Ip Address Scanner
Have you ever wanted to ping every IP host from one simple CIRD address? The answer to that is probably, "I've never ever wanted to do that." Well hopefully that answer will change after you run into this really cool and amazing tool. Whether you actually want to scan a whole network range or if you want to just try it out this tool makes it pretty easy to do so.

Feed one CIDR address into the python script and watch it work its magic as it tells you the status, response time, and possible error of each valid host.

## Set up and Installation

To get started, clone `scanner.py` using whatever method you'd like. After that, setting up and installing is as simple as ensuring the python file is inside of your working or current directory.

To start using the script type this simple command below:

- `python3 scanner.py [CIDR address]` This is all it takes to get the script running. Please ensure that you use a network that has given you permission to run a scan, and make sure that the range isn't super long (unless you want a million scans which would take a long time). 
        
    __*Note: If you're just looking to try it out, try `192.168.1.0/24`. It will scan a smaller network range (about 255 hosts in total) than some of the other private ranges.*__