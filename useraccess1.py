
#this python script for learning , it aimed to get user name and password to confirm their identity 
 #this time we have multi users with multi Joint password
  #any user can access through any password 

#create users function with saved users names
 #get user name and compare it with users list
def users():
        user= ['almustafa', 'Almustafa', 'ALMUSTAFA', 'reem', 'Reem', 'REEM', 'mohammed', 'Mohammed', 'MOHAMMED']
        xname= input('Enter your name please : ')
        while True:
              try:
                  xname= str(xname)
                  name= True if xname in user else False
                  if name!= True:
                     print('wrong name ! ')
                     xname= input('Enter your name as in ID card please : ')
                  else:
                      break
              except:
                  print(' Enter letters only please! ')
                  xname= input('try to enter your name again please ')
        print('Welcome back ' +xname)

 #create passwords function with multi saved passwords
  #get password from user , and compare it with passwords list
def passwords():
        pws= ['RM3690', 'MR3690', 'M36900', 'R36900']
        xpw= input('Enter your password please : ')
        while True:
              try:
                  xpw= str(xpw)
                  pw= True if xpw in pws else False
                  if pw!= True:
                     print('wrong password ! ')
                     xpw= input('Enter your password again please : ')
                  else:
                      break
              except:
                  print(' Are you sure that you are ! ')
                  xpw= input('try to enter your password again ! : ')

print('who are you ?')
 #call users function to be execute firstly
users()
print('For more security ')
 #call password function to be execute after users function
passwords()
print('user information accepted ')

#The mistake here is that all users can log in with all passwords together
 #we need to set Each user has one password assigned to him
