#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Sean Leahy 11/1


#import modules
import crypt    
import os

# function to test password
def test_password(algorithm_salt, hashed_password, password, password_guess)
    #Use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)
    # Compare salted guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False
# load dictionary file
dir_path = os.path.dirnam(os.path.realpath(__file__))
#open file for writing
f = open(dir_path + "/top10.txt", "r")
# Read file and print to screen
passwords = f.readlines()


# Prompt user for algorithm/salt
algorithm_salt = input("what is the algorithm and salt? ")
# Prompt user for salted hash
hashed_password = input("what is the full hashed password? ")

# loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("Match found: {0}".format(password))
        break