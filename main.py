import csv
# [MODIFIED] VERSION OF  IMPORTING SPY_DETAILS.
# IMPORT TIME USED TO DELAY DISPLAY OUTPUT TIME .
import time
# Importing classes from spy_details .
from spy_details import Spy , Chat_messages , Bg , Fg
from spy_details import spy , friends
from steganography.steganography import Steganography
import os
# import os / os.path  To check whether file path exists or not.

# [CUSTOMIZATION] variables for customizing the strings .
reset    ='\033[0m'
bold     ='\033[01m'
disable  ='\033[02m'
underline='\033[04m'
reverse  ='\033[07m'
strike_thro='\033[09m'
invisible='\033[08m'

# spy.name = '%s%s'%(spy.salutation , spy.name)

# [ Defining - List ]
STATUS_MESSAGES = ["Born leader" , "Thug life  " , "James bond " ]


#=======================================================================================================================

           ######    #     #    ##    #    ######    #######    #     #######    ##    #
           #         #     #    # #   #    #            #       #     #     #    # #   #
           #####     #     #    #  #  #    #            #       #     #     #    #  #  #
           #         #     #    #   # #    #            #       #     #     #    #   # #
           #         #######    #    ##    ######       #       #     #######    #    ##

#=======================================================================================================================


#******************************************** +@ LOAD FRIENDS MODULE @+ ************************************************


# [Defining - Function] load_friend() .
# load_friends method used to load all the friends data from the friends.csv file .
def load_friends() :
    # Opening file friends.csv in read mode i.e rb = read in binary .
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)
        print("\n"+bold+Fg.dark_grey+Bg.white+" THESE ARE YOUR FRIENDS : "+reset+"\n")
        time.sleep(2)
        for row in reader :
            print ((bold+Fg.white+Bg.cyan).join(row)+reset)
# [END] of function block load_friend() .


#******************************************** +@ ADD STATUS MODULE @+ **************************************************


# [ Defining - Function ] add_status() so that it can be called anywhere.
def add_status(current_status):
    updated_status = None

    if current_status != None :
        print (bold+Fg.white+Bg.red+' Your current status message is'+bold+Fg.white+Bg.cyan+' %s ' % (current_status)+reset)
    else:
        print ("\n"+reverse+Fg.light_cyan+Bg.black+' You don\'t have any status message currently '+reset)

    default = raw_input("\n"+bold+Fg.red+Bg.white+" Do you want to select from older status ? "+reverse+Fg.yellow+Bg.black+"(Y/N)"+reset+" : ")
    print("\n")

    if (default.upper() == 'N'):
        new_status = raw_input(reverse+Fg.dark_grey+Bg.yellow+" What status message do you want to set ? "+reset+" : ")

        if len(new_status) > 0 :
            updated_status = new_status
            # We could also use[ .append() ] in place of [.insert()] ,but it inserts item at the end of the list.
            # With [ insert(index,item) ] we can provide the item with index where it should be stored.
            STATUS_MESSAGES.insert(0,updated_status)
            # status.append(update_status)
            print (STATUS_MESSAGES)

    elif (default.upper() == "Y") :
        item_position = 1          #[ Initializing ] the status message index to 1 .

        for message in STATUS_MESSAGES :
            print ( reverse+Fg.light_blue+Bg.black+' %d.' % (item_position)+Bg.purple+' %s ' % (message)+reset)
            item_position += 1         #[ Incrementing ] status index
            # item_position = item_position + 1

        message_selection = input(reverse+Fg.dark_grey+Bg.white+" Choose from the above messages "+reset+" : ")
        if len(STATUS_MESSAGES) >= message_selection :
            updated_status = STATUS_MESSAGES[message_selection - 1]

    return updated_status
# [END] of function block add_status() .


#******************************************** +@ ADD A FRIEND MODULE @+ ************************************************


# [ MODIFIED ] using [DICTIONARY] data type variable.
# [Defining - Function] add_friend() .
def add_friend():
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("\n"+bold+Fg.white+Bg.cyan+" Please add your friend's name "+reset+" : ")
    new_friend.salutation = raw_input("\n"+bold+Fg.white+Bg.cyan+" Are they "+reverse+Fg.yellow+Bg.black+" Mr. or Ms.? "+reset+" : ")

    # new_name = new_salutation + "." + new_name
    # new_friend.name = "%s.%s"%(new_friend.salutation , new_friend.name)

    new_friend.age = input("\n"+bold+Fg.white+Bg.cyan+" Age "+reset+"       "+reset+" : ")

    new_friend.rating = input("\n"+bold+Fg.white+Bg.cyan+"Spy rating "+reset+" : ")


    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating :
        friends.append(new_friend)
        print (Fg.light_green+'Friend Added!'+'\n')
        # Opening file friends.csv in append mode i.e  'a' = append in given file .
        # In place of 'a' we can also use 'wb' = write in binary but,
        # this will remove the previous friends, means write on previous data .
        with open('friends.csv','a') as friends_data :
            #writing the friends details to file friends.csv
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name , new_friend.salutation , new_friend.age , new_friend.rating , new_friend.is_online])
        print ( bold+Fg.yellow+"%s.%s "% (new_friend.salutation , new_friend.name)+Fg.blue+ "is added to your friend list as a new spy")
    else :
        print (reverse+bold+Fg.yellow+Bg.black+' SORRY !!!'+Fg.white+Bg.brown+'Invalid entry. We can\'t add spy with the details you provided')

    return len(friends)
# [END] of function block add_friend() .


#******************************************** +@ SELECT A FRIEND MODULE MODULE @+ **************************************************


# [Defining - Function] select_a_friend() .
def select_a_friend() :
    friend_position = 1
    for friend in friends:
        # friend.name = (bold+Fg.black+Bg.yellow+' %s%s   '%(friend.salutation,friend.name)+reset)
        print (bold+Fg.white+Bg.light_white+' %d.)'%(friend_position)+bold+Fg.black+Bg.yellow+' %s%s '%(friend.salutation,friend.name)+Fg.white+Bg.light_black+' aged-%d  with  rating-%.2f is online' %( friend.age, friend.rating)+reset)
        friend_position += 1
    index = True
    while index :
        friend_selection = raw_input(Bg.light_white+"Choose from the above friends : "+reset)
        if len(friend_selection) > 0 :
            friend_selection = int(friend_selection)
            if len(friends) >= friend_selection and friend_selection != 0:
                friend_selection_position = friend_selection - 1
                index = False
                return friend_selection_position
            else :
                print (reverse+bold+Fg.yellow+Bg.black+" SORRY..!"+Fg.white+Bg.brown+"!!!!!!SELECTING BLANK FRIEND ."+reset+"    "+Fg.white+Bg.cyan+"[ Restarting...]"+reset+"\n")
                return select_a_friend()

        else :
            print(reverse+bold+Fg.yellow+Bg.black+" SORRY..!"+Fg.white+Bg.brown+" NO INDEX SELECTED!!! ."+reset+"\n")
# [END] of function block select_a_friend() .


#******************************************** +@ SEND A SECRET MESSAGE MODULE @+ ***************************************


# [Defining - Function] send_message() .
def send_message() :
    friend_selection = select_a_friend()    # Calling function select_a_friend().
    original_image = raw_input(Fg.black+Bg.red+" What is the name of the image ? "+reset+" : ")
    # ext = os.path.splitext(original_image)[-1].lower()
    # ext = original_image.split(".")[1]
    # the above code outputs when printed['input', 'mp3']
    file_name,ext = os.path.splitext(original_image)           # file_name = [file name]eg. input , ext = [file extension]eg. jpeg
    # os.path.splitext(file) will return a tuple with two values (the filename without extension + just the extension).
    #  The second index ([1]) will therefor give you just the extension.
    # The cool thing is, that this way you can also access the filename pretty easily, if needed!
    # os.path provides many functions for manipulating paths/file_names.
    # os.path.splitext takes a path and splits the file extension from the end of it.

    if ( ext == '.jpeg' or ext == '.png' or ext == '.jpg' or ext == '.gif') :
        print ("\n "+reverse+bold+Fg.light_blue+Bg.black+" It is valid image format with extension :"+bold+Fg.cyan+" %s " % ext+"\n")

        if (os.path.exists(original_image)) : # This statement checks whether the file exists or not.
             print (reverse+bold+Fg.green+Bg.black+" Verified!..! file "+bold+Fg.white+Bg.cyan+"[%s]"% (original_image)+
                    reverse+bold+Fg.green+Bg.black+" exists"+reset+"\n" )
             output_path = raw_input(Fg.yellow+Bg.light_white+' Enter the valid name of the secret coded image '+reset+' : ')
             text = raw_input("\n"+Fg.black+Bg.white+" What is your secret message ? "+reset+" : ")
             # [ENCODING] the message in the image using encode method .
             Steganography.encode(original_image,output_path,text)
             sent_by_me = True

             new_chat = Chat_messages(text,True)

             with open ('chats.csv', 'ab') as chat_data:
                                write = csv.writer(chat_data)
                                write.writerow([spy.name , friends[friend_selection].name, new_chat.message, new_chat.time, sent_by_me])

             friends[friend_selection].chats.append(new_chat)
             print (Fg.black+Bg.yellow+" Your secret message image is ready!"+reset+"\n")
        else :
            print (reverse+bold+Fg.yellow+Bg.black+" SORRY !!"+Fg.white+Bg.brown+" This file does not exist. "+reset+"\n")

    else :
         print (reverse+bold+Fg.yellow+Bg.black+" SORRY !!"+Fg.white+Bg.brown+" It is "+bold+Fg.white+Bg.cyan+
                "[ %s ]" % (ext)+bold+Fg.white+Bg.brown+" format which is not an image format."+reset )
# [END] of function block send_message() .


#******************************************** +@ READ A SECRET MESSAGE MODULE @+ ***************************************


# [Defining - Function] read_message() .
def read_message() :
    sender = select_a_friend()
    output_path = raw_input("\n"+Fg.black+Bg.light_red+" What is the name of the file ? "+reset+" : ")
    file_name,ext = os.path.splitext(output_path)
    if ( ext == '.jpeg' or ext == '.png' or ext == '.jpg' or ext == '.gif') :
        print ("\n"+reverse+bold+Fg.light_blue+Bg.black+" It is valid image format ."+reset)

        if (os.path.exists(output_path)) : # This statement checks whether the file exists or not.

            print ("\n"+reverse+bold+Fg.green+Bg.black+" Verified !..! file "+bold+Fg.white+Bg.cyan+"[%s]" % (output_path)+
                   reverse+bold+Fg.green+Bg.black+" exists"+reset)

            # [DECODING] the message from the image using decode method .
            secret_text = Steganography.decode(output_path)
            print (bold+Fg.yellow+" SECRET MESSAGE - "+bold+Fg.black+Bg.white+secret_text+reset+"\n")

            #converting the secret_txt to uppercase
            new = (secret_text.upper()).split()

            #checking emergency templates for help
            if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new or "RESCUE" in new or "ALERT" in new:
                  print (bold+reverse+Bg.yellow+Fg.black+"====================!! W A R N I N G !!====================="+reset)
                  time.sleep(2)
                  print (Fg.black+Bg.yellow+" Your friend the sender of this message need an emergency. "+reset)
                  print (Fg.black+Bg.yellow+" Please help your friend by sending him a helping message. "+reset)
                  print (Fg.black+Bg.yellow+" Select that friend to send him a helping message.         "+reset+"\n")

                  #calling send_help_msg() to send the help
                  send_help_msg()

                  print (Fg.cyan+" You have sent a message to help your friend")

                  sent_by_me = False
                  # Creating new chat.
                  new_chat = Chat_messages(secret_text,sent_by_me)
                  # Appending to chats.
                  friends[sender].chats.append(new_chat)

            else :
                  sent_by_me = False
                  new_chat = Chat_messages(secret_text, sent_by_me)
                  friends[sender].chats.append(new_chat)
                  print ("\n"+Fg.blue+" Your secret message has been saved!"+reset+"\n")

        else :
            print (reverse+bold+Fg.yellow+Bg.black+" SORRY!!!"+Fg.white+Bg.brown+" This file does not exist. "+reset)
    else :
         print (reverse+bold+Fg.yellow+Bg.black+" SORRY !!"+Fg.white+Bg.brown+" It is  is not an image format."+reset )
# [END] of function block read_message() .


#******************************************** +@ READ CHAT MESSAGE MODULE @+ ***************************************


# [Defining - Function] read_chats() .
def read_chats():

     read_from = select_a_friend()

     with open ('chats.csv', 'rb') as chat_data :  # opening chats to to read chat
         read = csv.reader(chat_data)
         print("\n"+bold+Fg.dark_grey+Bg.white+" THESE ARE YOUR CHAT HISTORY : "+reset+"\n")
         time.sleep(2)
         for row in read :
             print ((bold+Fg.white+Bg.light_white).join(row)+reset)
     print("\n")
# [END] of function block read_chats() .


#==================================================HELP_MESSAGE====================================================


# [Defining - Function] send_help_msg() .
def send_help_msg():

    # Selecting the friend
    friend_selection = select_a_friend()

    # The text response
    txt = Fg.yellow+"Don't panic I am on my way to reach you!"

    # Creating new chat
    new_chat = Chat_messages(txt , True)

    # Appending the chat
    friends[friend_selection].chats.append(new_chat)
# [END] of function block send_help_msg() .


#******************************************** +@ START CHAT MODULE @+ **************************************************


# [Defining - Function] start_chat() .
def start_chat(spy) :
    current_status = None
    # No need to update spy_name as it was updated in [ spy_details.py ] file.
    if  (12 < spy.age < 50) :
        print ("\n"+bold+Fg.black+Bg.light_cyan+" Authentication completed."+reset+"\n"+bold+Fg.yellow+Bg.red+
              " Welcome %s " % (spy.name)        +reset+"\n"+bold+Fg.white+Bg.light_black+
              " Age    : %d     " % (spy.age)   +reset+"\n"+bold+Fg.white+Bg.light_red+
              " Rating : %.1f    " % (spy.rating) +reset+"\n"+bold+Fg.light_cyan+
              " Proud to have you on-board."     +reset+"\n")

        # USED TO DELAY OUTPUT TIME IN [SECONDS] .
        time.sleep(3)

        # { Initialized } show to True so that We can keep showing the menu again after
        # every operation completes until the user wants to exit the application.
        show_menu = True
        #[ While ] statement [executes] till (show_menu) is {True} and [terminates] when (show_menu) is {False}
        while show_menu :
            menu_choice = input (bold+Fg.red+Bg.white+" what do you want to do ?  "+reset+"\n"+reverse+Fg.dark_grey+Bg.white+
            " 1."+Fg.white+Bg.light_white+" Add a status update    "+reset+"\n"+reverse+Fg.dark_grey+Bg.white+
            " 2."+Fg.white+Bg.light_white+" Add friend             "+reset+"\n"+reverse+Fg.dark_grey+Bg.white+
            " 3."+Fg.white+Bg.light_white+" Send a secret message  "+reset+"\n"+reverse+Fg.dark_grey+Bg.white+
            " 4."+Fg.white+Bg.light_white+" Read a secret message  "+reset+"\n"+reverse+Fg.dark_grey+Bg.white+
            " 5."+Fg.white+Bg.light_white+" Read Chats from a user "+reset+"\n"+bold+Fg.white+Bg.red+
            " 6. [Exit]                 "+reset+"\n")
            # [Add/UPDATE  status]
            if (menu_choice == 1) :
                current_status = add_status(current_status) #status = raw_input ("Write your status : ")
                print ("\n...............................Status updated to..."+Fg.black+Bg.yellow+"[%s]" % (current_status)+reset)
                time.sleep(3)
            # [Add friend]
            elif (menu_choice == 2) :
                number_of_friends = add_friend()
                print ('\n'+Fg.purple+' You have %d friends' % (number_of_friends)+'\n')
                time.sleep(3)
            # [Send a secret message]
            elif (menu_choice == 3) :
                print (bold+Fg.yellow+" %s "% (spy.name)+bold+Fg.light_cyan+" you should have secrecy let\'s send secret messages to your friends." )
                send_message()
                time.sleep(3)
            # [Read a secret message]
            elif (menu_choice == 4) :
                print (bold+Fg.yellow+" %s "% (spy.name)+bold+Fg.light_cyan+" let\'s read personal messages ")
                read_message()
                time.sleep(3)
            # [Read Chats from a user]
            elif (menu_choice == 5) :
                print (bold+Fg.light_cyan+" Oh Yea!!\n"+
                       bold+Fg.yellow+" %s "% (spy.name)+bold+Fg.light_cyan+"now let\'s read chats from other users")
                read_chats()
                time.sleep(3)
            # [EXIT]
            elif (menu_choice == 6) :
                print (bold+Fg.light_red+" Thanks for visiting spy_chat! "+reset+"    "+
                       bold+Fg.white+Bg.cyan+"[ Logging out...]"+reset)
                show_menu = False
            # [END] of function block start_chat().

    else:
            print (reverse+bold+Fg.yellow+Bg.black+' SORRY !!'+Fg.white+Bg.brown+' you are not of the correct age to be a spy'+reset)
# [END] of function block start_chat() .

#=======================================================================================================================

                              ##     ##     #######     #     ##    #
                              # #   # #     #     #     #     # #   #
                              #  # #  #     #######     #     #  #  #
                              #   #   #     #     #     #     #   # #
                              #       #     #     #     #     #    ##

#=======================================================================================================================


#******************************************** +@{ MAIN MODULE }@+ ******************************************************


print (bold+Fg.black+Bg.yellow+"==============================================="+reset+bold+underline+Fg.light_cyan+Bg.light_white+"@@[{{$PY-CH@T}}]@@"+reset+bold+Bg.yellow+Fg.black+"=================================================="+reset)
print (bold+Fg.light_cyan+" Hello!!!!  yo! what\'s up.\n Let\'s get started.\n"+
       reverse+bold+Fg.light_red+Bg.white+" Welcome to spy chat , firstly I need to know you..."+reset+"\n")

# USED TO DELAY OUTPUT TIME IN [SECONDS] .
time.sleep(2)

# This is a question for spy to to continue as default user (Y) or define a new user.
question = (bold+(reverse+Fg.white+Bg.black+" Do you want to continue as"+reverse+Fg.yellow+" %s ? "% (spy.name)+Bg.cyan+"(Y/N)"+reset+" : " ))
existing_spy = raw_input(question)

#Continue with the default user/details .
if (existing_spy.upper() == "Y") :
    #load_friends method testing
    load_friends()
    # Calling the function start_chat defined above
    time.sleep(4)
    start_chat(spy)

elif (existing_spy.upper() == "N") :

    spy = Spy( '' , '' , 0 , 0.0 )
    # Getting spy's {NAME}.
    spy.name = raw_input ("\n"+bold+Fg.white+Bg.cyan+" What is your name ? "+reset+" : ") # input() can also be used but give input in ("") double quotes  *

    # This if statement executes when spy types his / her name . For no name it will execute else statement.
    if len(spy.name) > 0 and spy.name.isalpha() :  # len() function determines the length of string.

       print ("\n"+reverse+Fg.yellow+Bg.black+' Welcome %s .'% (spy.name)+reset+
              Fg.red+'\nGlad to have you back with us.')

       time.sleep(2)

       # THIS STATEMENTS WORKS UNTILE THE SPY DONT PUT HIS SALUTATION .
       sal = True
       while sal :
           # Getting spy's {SALUTATION}.
           spy.salutation = raw_input ("\n"+bold+Fg.white+Bg.cyan+' What you would like to be called ? '+
                                   reverse+Fg.yellow+Bg.black+'( Mr. or Ms.)'+reset+" : ") # input() can be used in ver3.x *

           if (len(spy.salutation) != 0) :
               # {UPDATING} spy's name.
               spy.name = spy.salutation + '.' + spy.name

               print ('\n'+Fg.white+' Alright ' +Fg.yellow+"%s" % (spy.name) +Fg.white+' I\'d like to know a little bit more about you .')

                #{ DUCK TYPING }
               spy.age = 0           # type integer
               spy.rating = 0.0      # type float
               spy.is_online = False # type boolean

               ag = True
               while ag :

                   # Getting more details about spy.
                   spy.age = raw_input("\n"+bold+Fg.white+Bg.cyan+" What is your age ? "+reset+" : ") # inputs spy age

                   if len(spy.age) > 0:

                       # TYPE CASTING spy.age to integer .
                       spy.age = int(spy.age)

                       # Age eligibility criteria.
                       if spy.age > 15 and spy.age < 50 :
                           print (reverse+bold+Fg.green+Bg.black+"=========== You are eligible :) >>>>"+reset)

                           # Inputs spy rating.
                           spy.rating = raw_input("\n"+bold+Fg.white+Bg.cyan+" What is your spy rating ? "+reset+" : ")
                           spy.rating = float(spy.rating)

                           # Different categories of rating
                           if spy.rating > 4.5 and spy.rating <= 10.0 :                           # Category 1
                               print (bold+Fg.red+Bg.white+" GREAT ACE !!"+reset)
                           elif spy.rating <= 4.5 and spy.rating > 3.5 :   # Category 2
                               print (bold+Fg.white+Bg.cyan+" You are one of the good ones."+reset)
                           elif spy.rating <= 3.5 and spy.rating >= 2.5 :  # Category 3
                               print (bold+Fg.dark_grey+Bg.light_grey+" You can always do better."+reset)
                           elif 2.5 > spy.rating > 0.0 :                                          # Category 4
                               print (bold+Fg.white+Bg.brown+" We can always use somebody to help in the office."+reset)
                           else:   # This statement works when user inputs rating [more than 10] and [less than 0] i.e  negative.
                               print (Fg.white+Bg.red+"Your spy rating is fake !!!"+reset)
                               exit()

                           # Spy status whether he/she is online or not.
                           spy.is_online = True

                           # Using {PLACE HOLDERS}
                           # print("Authentication completed.\n Welcome %s\n  Age    : %d\n  Rating : %.1f\n Proud to have you on-board." % (spy.name,spy.age,spy.rating))
                           # We can also use give below statement, but according to zen of python we use above one ...
                           # String integer objects typecasting using  [ str() , repr() or backtick ].
                           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + str(spy_age) + "\n Rating : " + str(spy_rating) + "\n Spy is online : " + str(spy_is_online))
                           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + repr(spy_age) + "\n Rating : " + repr(spy_rating))
                           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + `spy_age` + "\n Rating : " + `spy_rating` + ")
                           start_chat(spy)  # Calling function start_chat
                       else :
                         print (reverse+bold+Fg.yellow+Bg.black+" SORRY..!"+Fg.white+Bg.brown+" you are not yet eligible ."+reset)  #"play (chidi..udd..kaa..udd.) ha.ha.haaa..")
                         sal = False

                       ag = False
                   else :
                       print (bold+reverse+bold+Fg.yellow+Bg.black+" SORRY..!"+Fg.white+Bg.brown+" No AGE !!!"+reset)
           else :
               print (bold+reverse+bold+Fg.yellow+Bg.black+" SORRY..!"+Fg.white+Bg.brown+" No SALUTATION !!!"+reset)

    else :
        print (reverse+bold+Fg.yellow+Bg.black+' SORRY..!'+Fg.white+Bg.brown+' NO NAME !. PLEASE!! TRY AGAIN..'+reset)
