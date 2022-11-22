#This python script for learning , for multi users access with one password 


 # using os module to clear the output page
#import os
#os.system('clear')

 #create users and asking for identity there name
users= ['almustafa', 'Almustafa', 'ALMUSTAFA', 'reem', 'Reem', 'REEM', 'mohammed', 'Mohammed', 'MOHAMMED']
print('who are you ?')
xname= input('Enter your name please : ')

 #operational loop identity the input type and make sure it is exist
while True:
      try:
          xname= str(xname)
          name= True if xname in users else False
          if name!= True:
             print('wrong name ! ')
             xname= input('Enter your name as in ID card please :')
          else:
              break
              
      except:
          print(' Enter letters only please! ')
          xname= input('try to enter your name again please ')
print('Welcome back ' +xname)

 #create password function to ask user for the password to be sure it is from user list
def pw():
        while True:
            password= input('For more security enter your password please : ')
            password= str(password)
            if password== 'MR3690':
                print('Password accepted ')
                break
            else:
                print('Wrong password !')
                password= input('Enter your password again : ')
                continue
 #call password function to be execute
pw()

 #Undefined error when entering wrong user name 
  #and then get the right one 
   #you will need to enter the password more than one time 
    #to get accept

