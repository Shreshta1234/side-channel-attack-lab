# vulnerable.py

SECRET = "hackkey"

def check_secret(user_input):

    if len(user_input) != len(SECRET):
        return "Invalid length"
    
  
    if user_input == SECRET:
        return "Access granted"
    
    return "Wrong password"


# For manual testing
if __name__ == "__main__":
    while True:
        user_input = input("Enter password: ")
        print(check_secret(user_input))