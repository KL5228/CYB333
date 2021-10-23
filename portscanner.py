
import socket
import subprocess
import sys

# Colorama is used to add color to text
from colorama import init, Fore

from datetime import datetime


# Using Green for open ports
init()
GREEN = Fore.GREEN

# cls for Python 3.x (Clears screen)
subprocess.call('cls', shell=True)

# Ask for input
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)


print ("*" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("This may take a while, please do not exit")
print ("*" * 60)

# Check what time the scan started
t1 = datetime.now()


# Set range from 1 to 1025
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print (GREEN, "Port {}: 	 Open".format(port))
        sock.close()


# Added error handling methods

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Print total time scanner was running
print ('Scanning Completed in: ', total)