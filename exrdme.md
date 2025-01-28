[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tp86o73G)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17729462)

# MAC Address Changer
Ever thought about changing your MAC address. Honestly probably not, but if you have or if you want to now, this address changer has got you covered. But why? Well why not? Maybe you want to steal someone's wifi (legally and with consent) or you want to impersonate someone's computer (also legally and with consent). Or maybe you just want to becuase there doesn't have to be a reason for everything.

In short, MAC Address Changer is a basic shell script that will change the MAC address of any online network interface to whatever you want.

## Set up and Installation

To get started, clone `changer.sh` using whatever method you'd like. After that setting up and installing is as simple as ensuring the shell file is inside of your working or current directory.

Actually changing your MAC address is as simple as running this string of commands in a terminal.

1. `ip link show` This will show you all of the avaliable network interfaces, in case you didn't know, as well as your current MAC address. __It's important to note your current MAC address so you can easily change it back later!__

2. `sudo ./changer.sh [interface] [MAC address]` This is where the magic happens. Simply type out the name of the interface as seen when you ran `ip link show` and then type (or paste) in the new MAC address you want. The code will do all of it's magic behind the scenes and will return a lovely message when it works! An address change request and a successful return message will look like this:

    ![title](screen_shots/example1.png)

## Features of the Changer

I took a lot of my time to build in a few features that are really cool.

- __Error Detection.__ Should there be any problems with either the inputs you provide or simply the process of changing the address, the code will give you a message telling you the error and or how to fix it. Some possible errors you may encounter are listed:

    - __Failed to bring the interface down / up.__ This is most usually more of a backend error, and isn't usually the error that will occur. If it does happen simply try again.

    - __Failed to change the MAC address.__ This usually happens with randomly generated MAC address if you happen to use one. Most randomly generated MAC addresses usually don't follow unicast or multicast prefixes. Try a different MAC address or try a known to be valid address instead.

    - __Invalid MAC Address or Interface.__ Sometimes you just happen to type something wrong, but if the MAC address doesn't match the accepted format or if the  interface you want to use isn't online then this error will occur. Always double check the address and use `ip link show` to double check avaliable interfaces.

- __MAC Address Archive.__ I know I said to write down your MAC address before changing and while I still encourage that, the script will also archive all of your MAC address prior to the change in a text file. This applies to the specific network interface you are altering. So should you forget where you wrote your old address, or if your dog eats it, it will always be stored in a text file in the directory called `archive.txt`.

    - __Enhanced MAC Address Archive.__ Because I'm really nice I enhanced the MAC archive with extra features. Should you ever somehow accidentally delete the `achive.txt` file, it'll just a new one for you. And why not have time stamped archive entries? What if you went to a cafe the other week and you don't remember what address you used? Well just look through the archive for the date. After a few changes the MAC Archive will look like this:

        ![title](screen_shots/example2.png)