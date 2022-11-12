# jrpc.py - A easy to use python library for Xx jAmes t xX's Xbox 360 JRPC plugin.
jrpc.py is a simple python library for using JRPC2 RGH/JTAG plugin by Xx jAmes t xX functions.

## Installation:
```
pip install git+https://github.com/brokeboienige/jrpc.py
```

## Usage:
In order to use this you will need the JRPC2 plugin running on your Xbox 360 RGH or JTAG. Download it [here](https://mega.nz/file/dMAS0bzT#7_BgBVURaD3PsAoX1brNHzfvScajJO5RN7rNz82rRE4). (It's inside JRPC2 folder)

### Example script
```py
from jrpc import xboxConsole, xNotifyLogos

xbox = xboxConsole("192.168.1.2") # Creating the console class
try:
    xbox.connect() # Creating the connection
except: # Connection error
    exit("Connection error")
xbox.xNotify("Hey, it's jrpc.py!", xNotifyLogos.FLASH_LOGO) # Send notify
```
