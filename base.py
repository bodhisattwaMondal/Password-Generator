import string 
import random
import time 

def generatePassword(passLength):
    """ This function will generate password based on user's input length."""

    s1 = string.ascii_lowercase  # It will yield A-Z
    s2 = string.ascii_uppercase  # It will yield a-z
    s3 = string.digits           # It will yield 0-9
    s4 = string.punctuation      # It will yield <=>?@[\]^_`{|}~.

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    

    password = "".join(random.sample(s, passLength))

    return(password)

# Driver Code :

if __name__ == "__main__":

    while True:
        passLength = int(input("Enter password length : "))
        
        print("Generating password....")
        result = generatePassword(passLength)
        time.sleep(1)
        print(f"Your newly generated password is: {result}")

        time.sleep(1)
        userChoice = input("\nDo you want to regenerate the password again (Y/N)? : ")

        if userChoice == 'Y' or userChoice == 'y':
            continue
        elif userChoice == 'N' or userChoice == 'n':
            break
        else:
            print("Wrong Input")
            break
    
