import os
import re

isEncoding = True

def E():
    return "Encode"

def D():
    return "Decode"

def C():
    return "Clear"

def encode_string(encode):
    return list(encode)
def decode_string(decode):
    return decode.split(',')

switcher = {
    "E": E,
    "D": D,
    "C": C
}

def get_action(action):
    # Get function from switcher dictionary
    func = switcher.get(action, "nothing")
    # Execute function
    return func()

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


while isEncoding: #if TRUE, Continue program else terminate

    print("\nLetter Code Converter")
    # Declare user text input
    textInput = input("\nInput Message:")
    #Check if text input is upper case
    if(textInput.islower()): #if TRUE, prompt user and clear screen
        screen_clear()
        print("Please enter uppercase letters only")
        continue
        
    # Declare user choice input
    userChoice = input("\nInput Encode[E], Decode[D], and Clear[C]: ").upper()
    
    #regex to determine if char is a special character or number
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,0-9]') 
    # Get User Choice on get_action dictionary
    action = get_action(userChoice)  
    # Print User chosen method
    print ("Your choice is " + action.upper())

    if action == get_action("E"): #If userChoice is equal to 'E', Encode string
        
        listChar = encode_string(textInput.lower()) #convert user text input into list and convert it to lower case
        encodedString = "" #declare string placeholder for final output
        #iterate through 'listChar' list
        for listItem in listChar:
            if listItem == ' ': #Check if item on list is whitespace
                encodedString = encodedString + " 0 " #if TRUE, concatinate 0(zero) on 'encodedString' string placeholder
            elif regex.search(listItem) != None: #Use REGEX to check if listItem is special character or number
                encodedString = encodedString + " 99 " #if TRUE, concatinate 99 on 'encodedString' string placeholder
           
            else: 
                #use ord(c) to return integer an representing the Unicode code point of the character
                #each lower case character is in the range of 97-122(26 characters)
                #subtract 96 from the ordinal of any lower case number will return its position in the alphabet assuming 'a' == '1'
                #Ex. Unicode of character 'a' is 97, 97(a) - 96 = 1
                #convert ord() output into string using str()
                #concatinate whitespace between 'encodedString' value and str() value to separate each characters
                encodedString = encodedString + " " + str((ord(listItem)-96)) + " " 
        print("Encoded Message:\n" + encodedString) #print encodedString after listChar loop
        
    elif action == get_action("D"): #if userChoice is equal to 'D', Decode string
        listChar = decode_string(textInput.lower()) #convert user text input into list using split() and convert it to lower case
        decodedString = "" #declare string placeholder for final output
         #iterate through 'listChar' list
        for listItem in listChar: 
            if listItem == "0": #Check if item on list is '0'
                decodedString = decodedString + " " #if TRUE, concatinate whitespace on 'decodedString' string placeholder
            elif (listItem.isdigit() == False or listItem == "99"): #Check if listItem is a number/digit
                decodedString = decodedString + "?" #if FALSE, concatinate '?' on 'decodedString' string placeholder
            else:
                #use chr(i) to return the character whose Unicode code point is the integer 'i'
                #each lower case character is in the range of 97-122(26 characters)
                #add 96 from the integer input will return its Unicode code point assuming 'a' == '1'
                #Ex. integer input is 1, 1 + 96 = 97. 97 is the Unicode code of lower case 'a'
                #convert chr() output to upper case
                result = chr(int(listItem)+96).upper()
                #check result if special character or number
                if regex.search(result):
                    result = "?" #if TRUE, set result to '?'
                #concatinate 'decodedString' value and 'result' value
                decodedString = decodedString + result
        print("Decoded Message:\n" + decodedString) #print decodedString after listChar loop
        
    elif action == get_action("C"): #If userChoice is equal to 'C', Clear Screen and return to Input Text
        screen_clear()
        continue


    # Continue
    while True: #While isEncoding is equal to TRUE, Continue the program else terminate
        #Prompt user after last input if user wants to continue the program
        finish = input("Do you want to continue using Text Encoder/Decoder? Yes[Y] or No[N]?: ").upper()
        if finish == "Y": #if finish == "Y", continue program
            screen_clear()
            isEncoding
        elif finish == "N": #If finish == "N", Set isEncoding to FALSE
            isEncoding = False
            print ("\nThank you for using Text Encoder/Decoder") #print closing message
        else: #if finish is not equal to "Y" or "N", prompt user to input "Y" or "N"
            print ("Please enter Yes[Y] or No[N]")
            continue
        break