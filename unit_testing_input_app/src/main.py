def get_user_name():
#input function that collects username and make sur it's not empty and in one word
    username = input("Enter your name: ")
    if username.strip() == "":
        print("Username is Invalid")
        return None
    if len(username.split())>1: 
        print('Username is Invalid')
        return None
    else:
        return username 
def get_password():
#input function that collects password and makes sur it's 8 char,contain at least a lettre, anumber and a special char
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    password=input("Enter your password:")
    if len(password)<8:
        print('Invalid password')
        return None
    if not any(char.isalpha() for char in password):
        print('Invalid password')
        return None
    if not any(char.isdigit() for char in password):
        print('Invalid password')
        return None
    if not any(char in special_characters for char in password):
        print('Invalid password')
        return None
    else: 
        return password 
def get_email(): 
#input function that collects email and makes sur it contains @ and . 
    email = input("Tell me your email: ")
    if ("@" not in email or "." not in email):
        print('Email is not valid.') 
        return None
    else: 
         return email

        
          
        

        
    
   
    
