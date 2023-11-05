""" The Caesar Cipher is a type of substitution cipher in which each letter of the plaintext is shifted a specific number of positions down the alphabet. To illustrate, a shift of 1 would transform 'A' into 'B', 'B' into 'C', and so forth. We've touched upon this topic during our class sessions.

Objective: The aim of this assignment is to delve deeper into various cybersecurity concepts and practices. Below is a brief overview of its mechanism. Please create an implementation of the Caesar Cipher using your preferred programming language. """

#Encryption
def encryption(key:int, inputString:str):
  ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  output = list(inputString)
#Decide on a shift value(key) `k`:
#For each character `c` in the plaintext `P`:
  for i in range(len(output)):
  #If `c` is an alphabetical character:
    if output[i].isalpha():
    #Shift `c` by `k` positions in the alphabet to get encrypted character `e`
      element = ALPHABETS.find(output[i])
      output[i] = ALPHABETS[(element+key) % 52]
#Return the encrypted text:
  return ''.join(output)

#Decryption
def decryption(key:int, inputString:str):
  ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  output = list(inputString)

#Use the same shift value(key) `k`.
#For each character `e` in the ciphertext `C`:
  for i in range(len(output)):
  #if `e` is an alphabetical character:
    if output[i].isalpha():
    #shift `e` by `-k` positions in the alphabet to get decrypted character `c`.
      element =  ALPHABETS.find(output[i])
      output[i] = ALPHABETS[abs((element-key) % 52)]
#return the decrypted text.
  return ''.join(output)


inputString =""
userKey = 0
inputString = input("Input the text to be encrypted: ")
userKey = int(input("Enter the key: "))
encryptedString = encryption(userKey, inputString)
print("The encrypted text is: ", encryptedString)
userKey = int(input("To decrypt, please input the key: " ))
print("THe decrypted text is: ", decryption(userKey, encryptedString))
