# [MODIFIED] VERSION OF  IMPORTING SPY_DETAILS.
from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime
import os
# import os / os.path  To check whether file path exists or not.

spy['name'] = '%s%s'%(spy['salutation'],spy['name'])

# [ Defining - List ]
STATUS_MESSAGES = ["Born leader" , "Thug life" , "James bond" ]

friends = []

print ("Hello!!!!\nyo! what\'s up.\nLet\'s get started.\nWelcome to spy chat , firstly I need to know you... ")

# This is a question for spy to to continue as default user (Y) or define a new user.
# [MODIFIED-VERSION] USING [DICTIONARY] DATA TYPE ELEMENTS.
question = "Do you want to continue as %s?(Y/N)\n" % (spy['name'])
existing_spy = raw_input(question)


# [ Defining - Function ] add_status() so that it can be called anywhere.
def add_status(current_status):
    updated_status = None

    if current_status != None :
        print 'Your current status message is %s \n' % (current_status)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("do you want to select from older status (Y/N) : ")

    if (default.upper() == 'N'):
        new_status = raw_input("what status message do you want to set ? : ")

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
            print '%d. %s' % (item_position, message)
            item_position += 1         #[ Incrementing ] status index
            # item_position = item_position + 1

        message_selection = input("\nChoose from the above messages : ")
        if len(STATUS_MESSAGES) >= message_selection :
            updated_status = STATUS_MESSAGES[message_selection - 1]

    return updated_status
# [END] of function block add_status() .

# [ MODIFIED ] using [DICTIONARY] data type variable.
# [Defining - Function] add_friend() .
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name'] = raw_input("Please add your friend's name : ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.? : ")

    # new_name = new_salutation + "." + new_name
    new_friend['name'] = "%s.%s"%(new_friend['salutation'] , new_friend['name'])

    new_friend['age'] = input("Age        : ")

    new_friend['rating'] = input("Spy rating : ")


    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating'] :
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)
# [END] of function block add_friend() .


# [Defining - Function] select_a_friend() .
def select_a_friend() :
    friend_position = 1
    for friend in friends:
        print '%d.) %s aged - %d with rating - %.2f is online' %(friend_position,friend['name'], friend['age'], friend['rating'])
        friend_position += 1
    friend_selection = input("Choose from the above friends : ")
    if len(friends) >= friend_selection and friend_selection != 0:
        friend_selection_position = friend_selection - 1
        return friend_selection_position
    else :
        print ("!!!!!!selecting blank friend.  [ Restarting..]")
        return start_chat(spy)
# [END] of function block select_a_friend() .


# [Defining - Function] send_message() .
def send_message() :
    friend_selection = select_a_friend()    # Calling function select_a_friend().
    original_image = raw_input("What is the name of the image ? : ")
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
        print ("It is valid image format with extension : %s " % ext)

        if (os.path.exists(original_image)) : # This statement checks whether the file exists or not.
             print ("Verified!..! file [%s] exists" % (original_image))
             output_path = 'output.jpeg'
             text = raw_input("What do you want to say?")
             Steganography.encode(original_image,output_path,text)

             new_chat = {
                'message'   : text ,
                'time'      : datetime.now() ,
                'sent_by_me': True
             }

             friends[friend_selection]['chats'].append(new_chat)
             print ("Your secret message image is ready!")
        else :
            print ("Sorry!! This file does not exist. ")

    else :
         print ("It is [ %s ] format which is not an image format." % ext)
# [END] of function block send_message() .


# [Defining - Function] read_message() .
def read_message() :
    sender = select_a_friend()
    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print (secret_text)
    new_chat = {
        "message"   : secret_text ,
        "time"      : datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"
# [END] of function block read_message() .


# [Defining - Function] start_chat() .
def start_chat(spy) :
    current_status = None
    # No need to update spy_name as it was updated in [ spy_details.py ] file.
    if  (12 < spy['age'] < 50) :
        print("Authentication completed.\n Welcome %s\n  Age    : %d\n  Rating : %.1f\n Proud to have you on-board." % (spy['name'],spy['age'],spy['rating']))

        # { Initialized } show to True so that We can keep showing the menu again after
        # every operation completes until the user wants to exit the application.
        show_menu = True
        #[ While ] statement [executes] till (show_menu) is {True} and [terminates] when (show_menu) is {False}
        while show_menu :
            menu_choice = input ("what do you want to do ?\n 1. Add a status update\n 2. Add friend\n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. [Exit]\n")
            # [Add/UPDATE  status]
            if (menu_choice == 1) :
                current_status = add_status(current_status) #status = raw_input ("Write your status : ")
                print ("...............................Status updated to...[%s]" % (current_status))
            # [Add friend]
            elif (menu_choice == 2) :
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            # [Send a secret message]
            elif (menu_choice == 3) :
                print "%s you should have secrecy let\'s send secret messages to your friends" % (spy['name'])
                send_message()
            # [Read a secret message]
            elif (menu_choice == 4) :
                print "Hey %s let\'s read personal messages" % (spy['name'])
                read_message()
            # [Read Chats from a user]
            elif (menu_choice == 5) :
                print "Oh Yea!!\n %s now let\'s read chats from other users" % (spy['name'])
            # [EXIT]
            elif (menu_choice == 6) :
                print "Thanks for visiting spy_chat!    Logging out..."
                show_menu = False
            # [END] of function block start_chat().

    else:
            print 'Sorry you are not of the correct age to be a spy'

if (existing_spy.upper() == "Y") :
    #Continue with the default user/details imported from the helper file.
    # Calling the function start_chat defined above
    start_chat(spy)

else :

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }
    # Getting spy's {NAME}.
    spy['name'] = raw_input ("What is your name ?\n") # input() can also be used but give input in ("") double quotes  *

    # This if statement executes when spy types his / her name . For no name it will execute else statement.
    if len(spy['name']) > 0 and spy['name'].isalpha() :  # len() function determines the length of string.

       print ('Welcome '+spy['name']+'.\nGlad to have you back with us.')

       # Getting spy's {SALUTATION}.
       spy['salutation'] = raw_input ('What you would like to be called ( Mr. or Ms.)?\n') # input() can be used in ver3.x *

       # {UPDATING} spy's name.
       spy['name'] = spy['salutation']+'.'+spy['name']

       print ('Alright ' +spy['name']+' I\'d like to know a little bit more about you .')

        #{ DUCK TYPING }
       spy['age'] = 0           # type integer
       spy['rating'] = 0.0      # type float
       spy['is_online'] = False # type boolean

       # Getting more details about spy.
       spy['age'] = input("What is your age ?\n") # inputs spy age
       spy['age'] = int(spy['age'])

       # Age eligibility criteria.
       if spy['age'] > 15 and spy['age'] < 50 :
           print ("You are eligible :)")

           # Inputs spy rating.
           spy['rating'] = raw_input("What is your spy rating ?\n")
           spy['rating'] = float(spy['rating'])

           # Different categories of rating
           if spy['rating'] > 4.5 and spy['rating'] <= 10.0 :                           # Category 1
               print ("GREAT ACE !!")
           elif spy['rating'] <= 4.5 and spy['rating'] > 3.5 :   # Category 2
               print ("You are one of the good ones.")
           elif spy['rating'] <= 3.5 and spy['rating'] >= 2.5 :  # Category 3
               print ("You can always do better.")
           elif 2.5 > spy['rating'] > 0.0 :                                          # Category 4
               print ("We can always use somebody to help in the office.")
           else:   # This statement works when user inputs rating [more than 10] and [less than 0] i.e  negative.
               print ("your spy rating is fake !!!")
               exit()

           # Spy status whether he/she is online or not.
           spy['is_online'] = True

           # Using {PLACE HOLDERS}
           # print("Authentication completed.\n Welcome %s\n  Age    : %d\n  Rating : %.1f\n Proud to have you on-board." % (spy['name'],spy['age'],spy['rating']))
           # We can also use give below statement, but according to zen of python we use above one ...
           # String integer objects typecasting using  [ str() , repr() or backtick ].
           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + str(spy_age) + "\n Rating : " + str(spy_rating) + "\n Spy is online : " + str(spy_is_online))
           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + repr(spy_age) + "\n Rating : " + repr(spy_rating))
           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + `spy_age` + "\n Rating : " + `spy_rating` + ")
           start_chat(spy)  # Calling function start_chat
       else :
         print ("SORRY..! you are not eligible yet. ")  #"play (chidi..udd..kaa..udd.) ha.ha.haaa..")

    else :
        print ('SORRY..! NO NAME !. \nPLEASE!! TRY AGAIN..')
