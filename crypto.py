import base64
import hashlib
import bcrypt
from cryptography.fernet import Fernet

# Hashing is a one-way function, meaning that it is computationally infeasible to
# reverse the hash to obtain the original password. 
# This makes it a secure way to store passwords, 
# as even if the hash is compromised, 
# the original password cannot be easily retrieved.


# bcrypt is a popular password hashing library that provides a secure way to 
# hash and verify passwords.
# The hash_password function takes an input password, encodes it to bytes, and
# then uses bcrypt's hashpw function to generate a hashed password.

# The bcrypt.gensalt() function is used to generate a random salt, which adds an
# additional layer of security to the hashing process. 
# The resulting hashed password is returned as a byte string.

#hashpw is a function provided by the bcrypt library that takes two arguments: 
#the password to be hashed (in bytes) and a salt (also in bytes).
# The hashpw function combines the password and salt, applies the bcrypt hashing algorithm,
# and returns the resulting hash as a byte string.

def hash_password(input_password):
    return bcrypt.hashpw(input_password.encode(),bcrypt.gensalt())

# The verify_password function takes an input password and a hashed password as arguments.
# It uses the bcrypt library's checkpw function to compare the input password 
#(after encoding it to bytes) with the hashed password.
# The checkpw function returns True if the input password matches the hashed password,
# and False otherwise. This allows you to verify if a user's input password is correct
# without needing to store the original password, enhancing security.

# the checkpw function is designed to handle the hashing and salting internally,
# so you don't need to worry about the salt when verifying passwords.
#what it does is it takes the input password, hashes it using the same salt that was used
# to create the original hashed password, and then compares the two hashes to 
# determine if they match.

# 1. Take stored_hash
# 2. Extract salt from it
# 3. Use that SAME salt
# 4. Hash the input password again
# 5. Compare results


def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode(), hashed_password)

#bcrypt generates a DIFFERENT hash every time you hash the same password,
# because it uses a random salt each time.
# This is a security feature that makes it more difficult for attackers to use precomputed
# hash tables (like rainbow tables) to crack passwords, 
# as each hash is unique even for the same password.


#----------------------------------------------------------------------------------------
# The generate_key function takes a password as input, encodes it to bytes, and then
# uses the SHA-256 hashing algorithm to create a hash of the password.
# The resulting hash is a 32-byte value, which is then encoded using base64 to create
# a URL-safe key that can be used for encryption and decryption with the Fernet library.

#Fernet requires a specific formate
# The key must be 32 bytes long and URL-safe, 
# which is why we use base64 encoding to ensure that the generated key meets 
# these requirements.
#-----------------------------------------------------------------------------------------

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest() # Generate a 32-byte hash of the password
    return base64.urlsafe_b64encode(key) # Encode the hash using base64 to create a URL-safe key for Fernet

#------------------------------------------------------------------------------------------
# The encrypt_password function takes a password and a key as input, 
# creates a Fernet object using the key, and then encrypts the password using the Fernet 
# object's encrypt method.
# The encrypted password is returned as a string after decoding it from bytes.
#-------------------------------------------------------------------------------------------

def encrypt_password(password,key):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(encrypt_password,key):
    f = Fernet(key)
    return f.decrypt(encrypt_password.encode()).decode()

#Inoder to use the Fernet library for encryption and decryption,
#First, we need to generate a key that meets the requirements of the Fernet library.
#We Need to create a Fernet object using the generated key, 
#and then we can use that object to encrypt and decrypt passwords securely.



#------------->  f.encrypt(password.encode()).decode()  <----------------

#1. password.encode() converts the password string into bytes, 
# which is required by the Fernet library for encryption.

#2. f.encrypt(...) takes the byte-encoded password and encrypts it using the Fernet 
# object created with the provided key.

#3. The result of the encryption is a byte string, 
# which is then decoded back into a regular string using .decode() for easier storage 
# and handling.