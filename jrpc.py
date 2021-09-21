from socket import *
import time

class xboxConsole():
    connected = False

    def __init__(self, ip, port=730, debug=False):
        self.ip = ip
        self.port = port
        self.debug = debug

    def connect(self):
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((self.ip, self.port))
            response = s.recv(1024)
            if response.decode("cp1252").startswith("201-"):
                self.connected = True
            else:
                raise ValueError("Invalid address")
        except:
            raise ValueError("Invalid address")

    def getConsoleType(self):
        return self.sendTextCommand("consolefeatures ver=2 type=17 params=\"A\\0\\A\\0\\\"")

    def sendTextCommand(self, command):
        if self.connected:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((self.ip, self.port))
            s.send(bytes(command,"cp1252"))
            data = s.recv(1024)
            time.sleep(5)
            if self.debug == True:
                print(command)
                print(data)
            s.close
            return data
        else:
            raise ValueError("Not connected to any console")
    
    def setMemory(self, address, data):
        self.sendTextCommand("setmem addr="+address+" data="+data+"\r\n")

    def xNotify(self, message, logo):
        if logo > 76 or logo < 0:
            raise ValueError("Invalid xNotifyLogo")
        self.sendTextCommand("consolefeatures ver=2 type=12 params=\"A\\0\\A\\2\\2/"+str(len(message))+"\\"+message.encode("cp1252").hex().upper()+"\\1\\"+str(logo)+"\\\"\r\n")

class xNotifyLogos():
    XBOX_LOGO = 0
    NEW_MESSAGE_LOGO = 1
    FRIEND_REQUEST_LOGO = 2
    NEW_MESSAGE = 3
    FLASHING_XBOX_LOGO = 4
    GAMERTAG_SENT_YOU_A_MESSAGE = 5
    GAMERTAG_SINGED_OUT = 6
    GAMERTAG_SIGNEDIN = 7
    GAMERTAG_SIGNED_INTO_XBOX_LIVE = 8
    GAMERTAG_SIGNED_IN_OFFLINE = 9
    GAMERTAG_WANTS_TO_CHAT = 10
    DISCONNECTED_FROM_XBOX_LIVE = 11
    DOWNLOAD = 12
    FLASHING_MUSIC_SYMBOL = 13
    FLASHING_HAPPY_FACE = 14
    FLASHING_FROWNING_FACE = 15
    FLASHING_DOUBLE_SIDED_HAMMER = 16
    GAMERTAG_WANTS_TO_CHAT_2 = 17
    PLEASE_REINSERT_MEMORY_UNIT = 18
    PLEASE_RECONNECT_CONTROLLERM = 19
    GAMERTAG_HAS_JOINED_CHAT = 20
    GAMERTAG_HAS_LEFT_CHAT = 21
    GAME_INVITE_SENT = 22
    FLASH_LOGO = 23
    PAGE_SENT_TO = 24
    FOUR_2 = 25
    FOUR_3 = 26
    ACHIEVEMENT_UNLOCKED = 27
    FOUR_9 = 28
    GAMERTAG_WANTS_TO_TALK_IN_VIDEO_KINECT = 29
    VIDEO_CHAT_INVITE_SENT = 30
    READY_TO_PLAY = 31
    CANT_DOWNLOAD_X = 32
    DOWNLOAD_STOPPED_FOR_X = 33
    FLASHING_XBOX_CONSOLE = 34
    X_SENT_YOU_A_GAME_MESSAGE = 35
    DEVICE_FULL = 36
    FOUR_7 = 37
    FLASHING_CHAT_ICON = 38
    ACHIEVEMENTS_UNLOCKED = 39
    X_HAS_SENT_YOU_A_NUDGE = 40
    MESSENGER_DISCONNECTED = 41
    BLANK = 42
    CANT_SIGN_IN_MESSENGER = 43
    MISSED_MESSENGER_CONVERSATION = 44
    FAMILY_TIMER_X_TIME_REMAINING = 45
    DISCONNECTED_XBOX_LIVE_11_MINUTES_REMAINING = 46
    KINECT_HEALTH_EFFECTS = 47
    FOUR_5 = 48
    GAMERTAG_WANTS_YOU_TO_JOIN_AN_XBOX_LIVE_PARTY = 49
    PARTY_INVITE_SENT = 50
    GAME_INVITE_SENT_TO_XBOX_LIVE_PARTY = 51
    KICKED_FROM_XBOX_LIVE_PARTY = 52
    NULLED = 53
    DISCONNECTED_XBOX_LIVE_PARTY = 54
    DOWNLOADED = 55
    CANT_CONNECT_XBL_PARTY = 56
    GAMERTAG_HAS_JOINED_XBL_PARTY = 57
    GAMERTAG_HAS_LEFT_XBL_PARTY = 58
    GAMER_PICTURE_UNLOCKED = 59
    AVATAR_AWARD_UNLOCKED = 60
    JOINED_XBL_PARTY = 61
    PLEASE_REINSERT_USB_STORAGE_DEVICE = 62
    PLAYER_MUTED = 63
    PLAYER_UNMUTED = 64
    FLASHING_CHAT_SYMBOL = 65
    UPDATING = 76