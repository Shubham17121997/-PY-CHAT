# [MODIFIED] spy_details file using [CLASS].

# IMPORTING datetime library .
from datetime import  datetime

# Creating "Spy" class .
class Spy :
    def __init__(self , name , salutation , age , rating):
        self.name       = name
        self.salutation = salutation
        self.age        = age
        self.rating     = rating
        self.is_online  = True
        self.chats      = []
        self.current_status = None

# Creating "Chat_messages" class .
class Chat_messages :
    def __init__(self , message , sent_by_me) :
        self.message    = message
        time            = datetime.now()
        self.time       = time.strftime(reverse+Fg.yellow+Bg.black+"DATE - %d/%b/%Y"+reset+"       "
                                                  +bold+Fg.white+Bg.cyan+"TIME - [%I:%M:%S %p]"+reset)
        self.sent_by_me = sent_by_me


# [INSTANTIATION]
# Creating an object 'spy' of class 'Spy()' or instantiation of class .
spy = Spy('Shubham' , 'Mr.' , 20 , 3.0 )

# [INSTANTIATION]
# Creating default friends objects of class 'Spy' .
friend_1 = Spy( 'Dhruv'  , 'Mr.' , 21 , 5.0 )
friend_2 = Spy( 'Lethal' , 'Mr.' , 23 , 7.0 )
friend_3 = Spy( 'Remo'   , 'Ms.' , 25 , 6.0 )

# Adding default friends objects.
# Storing friend objects in the "list" .
friends = [ friend_1 , friend_2 , friend_3 ]


# [CUSTOMIZATION] variables for customizing the strings .
reset    ='\033[0m'
bold     ='\033[01m'
disable  ='\033[02m'
underline='\033[04m'
reverse  ='\033[07m'
strike_thro='\033[09m'
invisible='\033[08m'


# [FOREGROUND] CLASS
class Fg:
    # black  ='\033[30m'
    red    ='\033[31m'
    green  ='\033[32m'
    brown  ='\033[33m'
    blue   ='\033[34m'
    purple ='\033[35m'
    cyan   ='\033[36m'
    light_grey   ='\033[37m'
    white        ='\033[38m'
    dark_grey    ='\033[90m'
    light_red    ='\033[91m'
    light_green  ='\033[92m'
    yellow       ='\033[93m'
    light_blue   ='\033[94m'
    light_magenta='\033[95m'
    light_cyan   ='\033[96m'
    black        ='\033[97m'

# [BACKGROUND] CLASS
class Bg:
    black  ='\033[49m'
    red    ='\033[41m'
    green  ='\033[42m'
    brown  ='\033[43m'
    blue   ='\033[44m'
    purple ='\033[45m'
    cyan   ='\033[46m'
    white  ='\033[40m'
    light_grey   ='\033[47m'
    light_black  ='\033[100m'
    light_red    ='\033[101m'
    light_green  ='\033[102m'
    yellow       ='\033[103m'
    light_blue   ='\033[104m'
    pink         ='\033[105m'
    light_cyan   ='\033[106m'
    light_white  ='\033[107m'
    
    
    
    


