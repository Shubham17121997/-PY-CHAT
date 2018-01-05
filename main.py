print ("Hello!")
print ('yo! what\'s up')
print ('Let\'s get started')
print ('Welcome to spy chat , firstly I need to know you ha..ha..ha.... ')

# Getting spy's {NAME}.
spy_name = raw_input ("What is your name ?\n") # raw_input() can also be used *

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
     print ("SORRY..! you are not eligible yet.\nplay (chidi..udd..kaa..udd.) ha.ha.haaa..")

else :
    print ('SORRY..! NO NAME. \nPLEASE!! TRY AGAIN..')
