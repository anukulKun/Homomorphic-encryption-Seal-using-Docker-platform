import random

users = {
    "alice": "password123",
    "bob": "qwerty456",
    "charlie": "secret789"
}


def generate_code():
    code = ""
    for i in range(6):
        code += str(random.randint(0,9))
    return code

def send_code(email, code):
   
    print("Authentication code sent to " + email)


def verify_code(code, user):
   
    if code == user["auth_code"]:
        return True
    else:
        return False


def login():
 
    username = input("Username: ")
    password = input("Password: ")
    
  
    if username in users and password == users[username]:
   
        auth_code = generate_code()
        send_code(users[username]["email"], auth_code)
        
   
        entered_code = input("Enter authentication code: ")
        
   
        if verify_code(entered_code, users[username]):
            print("Login successful!")
        else:
            print("Incorrect authentication code. Please try again.")
    else:
        print("Incorrect username or password. Please try again.")

login()
