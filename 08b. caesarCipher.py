# --------------------------------------------------------------
# ---------------------- CAESAR CIPHER  ------------------------
# ------------------ (FUNCTION PARAMETERS) ---------------------
# --------------------------------------------------------------

from _08b_caesarCipherArt import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(textMessage, shiftNumber, direction):
    tempTxt = ""
    shiftNumber = shiftNumber % 25
    print(shiftNumber)
    if direction == 'decode':
            shiftNumber *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            tempPosition = position + shiftNumber
            if tempPosition > 25:
                tempPosition -= 26
            newLetter = alphabet[tempPosition]
            tempTxt += newLetter
        else:
            tempTxt += char
    print(f"The {direction}d text is {tempTxt}")

shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ifRepeat = input("Type 'yes' to continue, else type 'no'")
    if ifRepeat == 'no':
        shouldContinue = False
        print("Goodbye")


'''
TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet
     by the shift amount and print the encrypted text.  
    e.g. 
    plain_text = "hello"
    shift = 5
    cipher_text = "mjqqt"
    print output: "The encoded text is mjqqt"
    #HINT: How do you get the index of an item in a list:
    https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount
     and print the decrypted text.  
    e.g. 
    cipher_text = "mjqqt"
    shift = 5
    plain_text = "hello"
    print output: "The decoded text is hello"
TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
    Then call the correct function based on that 'drection' variable. You should be able to test the code to 
    encrypt *AND* decrypt a message.
TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().
TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

TODO-9: Import and print the logo from art.py when the program starts.
TODO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?
    Try running the program and entering a shift number of 45.
    Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    Hint: Think about how you can use the modulus (%).
TODO-11: What happens if the user enters a number/symbol/space?
    Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    e.g. start_text = "meet me at 3"
    end_text = "•••• •• •• 3"
TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
    e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
'''


# ------ OLD STEPS -----------
# def decrypt(textMessage, shiftNumber):
#     decryptTxt =""
#     for letter in text:
#         position = alphabet.index(letter)
#         tempPosition = position - shift
#         newLetter = alphabet[tempPosition]
#         decryptTxt += newLetter
#     print(f"The decoded text is {decryptTxt}")

# def encrypt(textMessage, shiftNumber):
#     cipherTxt =""
#     for letter in text:
#         position = alphabet.index(letter)
#         tempPosition = position + shift
#         if tempPosition > 25:
#             tempPosition -= 26
#             newLetter = alphabet[tempPosition]
#             cipherTxt += newLetter
#         else:
#             newLetter = alphabet[tempPosition]
#             cipherTxt += newLetter
#     print(f"The encoded text is {cipherTxt}")


# def caesar(textMessage, shiftNumber, direction):
#     tempTxt = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         if direction == 'encode':
#             tempPosition = position + shiftNumber
#             if tempPosition > 25:
#                 tempPosition -= 26
#         if direction == 'decode':
#             tempPosition = position - shiftNumber
#         newLetter = alphabet[tempPosition]
#         tempTxt += newLetter
#     print(f"The {direction}d text is {tempTxt}")