# jrpc.py - A easy to use python library for Xx jAmes t xX's Xbox 360 JRPC plugin.
jrpc.py is a simple python library for using JRPC2 RGH/JTAG plugin by Xx jAmes t xX functions.

## Installation:
```
pip install git+https://github.com/Enige1337/jrpc.py
```

## Usage:
```py
from jrpc import xboxConsole, xNotifyLogos

xbox = xboxConsole("192.168.1.2") # Creating the console class
try:
    xbox.connect() # Creating the connection
except: # Connection error
    exit("Connection error")
xbox.xNotify("Hey, it's jrpc.py!", xNotifyLogos.FLASH_LOGO) # Send notify
```