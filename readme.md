# Assignment 3 - Caesar Cypher

A simple model showing how the caesar cypher works. 

## Description
- This is a basic program showcasing how the caesar cypher works. It uses modulo to simulate a looping track on a-Z and shifts the letters in the string by the key amount. This feature introduces limitations that will be discussed later in this readme. 

## Table of Contents
- [Functionality](#functionality)
- [Usage](#usage)
- [Analysis](#analysis)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)

## Functionality
- The user is prompted for a string and a key
- A string, containing all the alphabets a-Z, is initialized. 
- With the given key, the letters in the string are shifted by the key amount.
- When the user inputs the correct key, the reverse occurs and the string input is returned. 

## Usage
- After making sure that Python is installed simply run the command 
```
python Assignment3.py
```
## Analysis
#### Time Complexity
- The time complexity of this algorithm is O(n<sup>2</sup>).
- Program loops through the string once
- In each loop, the .find() function has a complexity of O(n).
#### Space Complexity
- The space complexity does not scale with the input size (n) and is thus O(1).
## Limitations
- The main limitation of this program is it's low entropy, mainly becaues of the use of the looping track used to shift the input string. Becaues of the fact that the string used for the track is only 52 (lower case and capital letters of the alphabet) and modulo is used to keep all inputs within that track, the reality is that the maximum shift is 52. This makes it vulnerable to brute force attacks/frequency analysis/side-channel-attacks.  
- This results in keys other than the one used to encrypt the string being able to decrypt it successfully. For example, one could use 26 to encrypt and 52 to decrypt and the correct string could be returned.
- This encryption method is only valid for alphabets and is not suitable for encrypting digital data (binary).

## Future Improvements
- One improvement to this program would be to use a dictionary data structure to manage the shift. For example, a hashmap. 
- Because the program would no longer depend on a looping track to shift the key, this method would ensure that shifting the string by the user key only allows the correct key to decrypt the string (limitations based on Python's hashing algorithm for their hashmap, see hash collisions).
- Another benefit is that this method would sacrifice some space complexity to make the .find() equivalent O(1), as reading the value of a hashmap with a given key is linear time (assuming no collisions).
- The reality is that no matter how much optimizations one does to this algorithm, it's limitations are clear and there are better methods of encryption such as Public Key Cryptography or other similar asymetric cryptography methods.