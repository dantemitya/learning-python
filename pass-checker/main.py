# BASIC PASSWORD STRENGTH CHECKER
"""
TODO: Add code for the rest of the check functions in utils.py in order to get a full score
"""

"""
Important factors for passwords are:
   - Length: Anything less than 8 chararacters is too short; more than 16 is considered strong.
   - Character variety: Should be a mix of upper, lower, numbers, symbols).
   - Unpredictability (entropy): Random strings are better than repeated inputs or common words.
   - Dictionary check: Shouldn't be a common password like '12345' or 'password123'.
   - Keyboard patterns: Shouldn't use a pattern like 'qwerty' or 'asdfghjkl' (i.e. close keys on the keyboard).
   - Personal info: Shouldn't contain obvious things like names, dates, places, etc.
"""

"""
1. Will evaluate a given password against all of the above criteria and will give a score.
2. Each check will return a score of either 1, 2, or 3 (3 being the highest).
3. After all checks have been done, will return an average score of all of the checks.
4. The final score will be between 1 and 3 (closer to 3 the better the password in theory).
"""
import time
import utils

def main():
    # display title
    utils.display("PASSWORD STRENGTH CHECKER")
       
    # get the password from the user
    password = input("Password to check: ")
    
    # a single function to run all of the checks and get a score
    score = utils.run_checks(password)

    # fluff just for fun
    utils.display("PASSWORD STRENGTH CHECKER")
    print("Running checks...")
    time.sleep(2)

    # display score
    utils.display("PASSWORD STRENGTH CHECKER")
    print(f"Password score: {score:.2f}")

if __name__ == '__main__':
    main()
