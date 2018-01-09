from spy_details import spy_name , spy_salutation , spy_age , spy_rating

# [ Defining - List ]
STATUS_MESSAGES = ["Born leader" , "Thug life" , "James bond" ]

friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

print ("Hello!!!!\nyo! what\'s up")
print ('Let\'s get started')
print ('Welcome to spy chat , firstly I need to know you... ')

# This is a question for spy to to continue as default user (Y) or define a new user.
question = "Do you want to continue as %s?(Y/N)\n" % (spy_name) # spy_name was updated with salutation in [ spy_details.py ]
# question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?"
existing_spy = raw_input(question)


# [ Defining - Function ] add_status() so that it can be called anywhere.
def add_status(current_status):
    updated_status = None

    if current_status != None:
        print 'Your current status message is %s \n' % (current_status)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("do you want to select from older status (Y/N) : ")

    if (default.upper() == 'N'):
        new_status = raw_input("what status message do you want to set ? : ")

        if len(new_status) > 0 :
            updated_status = new_status
            # We could also use[ .append() ] in place of [.insert()] ,but it inserts item at the end of the list
            # With [ insert(index,item) ] we can provide the item with index where it should be stored
            STATUS_MESSAGES.insert(0,updated_status)
            # status.append(update_status)
            print (STATUS_MESSAGES)

    elif (default.upper() == "Y") :
        item_position = 1          #[ Initializing ] the status message index to 1 .

        for message in STATUS_MESSAGES :
            print '%d. %s' % (item_position, message)
            # print ( str(item_position) + "." + (message) )
            item_position += 1         #[ Incrementing ] status index
            # item_position = item_position + 1

        message_selection = input("\nChoose from the above messages : ")
        if len(STATUS_MESSAGES) >= message_selection :
            updated_status = STATUS_MESSAGES[message_selection - 1]

    return updated_status
# [END] of function block add_status() .


# [Defining - Function] add_friend() .
def add_friend():

    new_name = raw_input("Please add your friend's name : ")
    new_salutation = raw_input("Are they Mr. or Ms.? : ")

    # new_name = new_salutation + "." + new_name
    new_name = "%s.%s"%(new_salutation , new_name)

    new_age = input("Age         :")

    new_rating = input("Spy rating : ")


    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)
# [END] of function block add_friend() .


# [Defining - Function] start_chat() .
def start_chat(spy_name , spy_age , spy_rating):
    current_status = None
    # No need to update spy_name as it was updated in [ spy_details.py ] file.
    if (12 < spy_age < 50) :
        print("Authentication completed.\n Welcome %s\n  Age    : %d\n  Rating : %.1f\n Proud to have you back."
              % (spy_name,spy_age,spy_rating))

        # { Initialized } show to True so that We can keep showing the menu again after
        # every operation completes until the user wants to exit the application.
        show = True
        #[ While ] statement [executes] till (show) is {True} and [terminates] when (show) is {False}
        while show :
            menu_choices = input ("what do you want to do ?\n 1. Add a status update\n 2. Add friend\n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. [Exit]\n")
            # [Add/UPDATE  status]
            if (menu_choices == 1) :
                current_status = add_status(current_status) #status = raw_input ("Write your status : ")
                print ("...............................Status updated to...[%s]" % (current_status))
            # [Add friend]
            elif (menu_choices == 2) :
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            # [EXIT]
            elif (menu_choices == 6) :
                print "Thanks for visiting spy_chat!    Logging out..."
                show = False
            # [END] of function block start_chat().

if (existing_spy.upper() == "Y") :
    #Continue with the default user/details imported from the helper file.
    # Calling the function start_chat defined above
    start_chat(spy_name, spy_age, spy_rating,)

else :
    # Getting spy's {NAME}.
    spy_name = raw_input ("What is your name ?\n") # input() can also be used but give input in ("") double quotes  *

    # This if statement executes when spy types his / her name . For no name it will execute else statement.
    if len(spy_name) > 0 :  # len() function determines the length of string.

       print ('Welcome '+spy_name+'.\nGlad to have you back with us.')

       # Getting spy's {SALUTATION}.
       spy_salutation = raw_input ('What you would like to be called ( Mr. or Ms.)?\n') # input() can be used in ver3.x *

       # {UPDATING} spy's name.
       spy_name = spy_salutation+'.'+spy_name

       print ('Alright ' +spy_name+' I\'d like to know a little bit more about you .')

        #{ DUCK TYPING }
       spy_age = 0           # type integer
       spy_rating = 0.0      # type float
       spy_is_online = False # type boolean

       # Getting more details about spy.
       spy_age = input("What is your age ?\n") # inputs spy age
       spy_age = int(spy_age)

       # Age eligibility criteria.
       if spy_age > 15 and spy_age < 50 :
           print ("You are eligible :)")

           # Inputs spy rating.
           spy_rating = raw_input("What is your spy rating ?\n")
           spy_rating = float(spy_rating)

           # Different categories of rating
           if spy_rating > 4.5 :                           # Category 1
               print ("GREAT ACE !!")
           elif spy_rating <= 4.5 and spy_rating > 3.5 :   # Category 2
               print ("You are one of the good ones.")
           elif spy_rating <= 3.5 and spy_rating >= 2.5 :  # Category 3
               print ("You can always do better.")
           else :                                          # Category 4
               print ("We can always use somebody to help in the office.")

           # Spy status whether he/she is online or not.
           spy_is_online = True

           # Using {PLACE HOLDERS}
           print("Authentication completed.\n Welcome %s\n  Age    : %d\n  Rating : %.1f\n Proud to have you on-board." % (spy_name,spy_age,spy_rating))
           # We can also use give below statement, but according to zen of python we use above one ...
           # String integer objects typecasting using str() , repr() or backtick.
           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + str(spy_age) + "\n Rating : " + str(spy_rating) + "\n Spy is online : " + str(spy_is_online))
           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + repr(spy_age) + "\n Rating : " + repr(spy_rating))
           #print("Authentication completed.\n Welcome " + spy_name + "\n Age : " + `spy_age` + "\n Rating : " + `spy_rating` + ")
       else :
         print ("SORRY..! you are not eligible yet. ")  #"play (chidi..udd..kaa..udd.) ha.ha.haaa..")

    else :
        print ('SORRY..! NO NAME !. \nPLEASE!! TRY AGAIN..')
