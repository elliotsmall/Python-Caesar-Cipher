

def encrypt(target, shift):
    encryptedString = ""

    for char in target:
        if char.isalpha():
            #handle uppercase vs lowercase
            start = ord('A') if char.isupper() else ord('a') #if character is upper case set start to the ordinal value of uppercase A, opposite goes for lowercase a

            #shift within range of 0-25 (letters of alphabet), then wrap around with modulo if it goes past Z/z
            offset = (ord(char) - start + shift) % 26 #takes ordinal value of char and subtracts the start from it, then adds the shift to it (mod 26 ensures it doens't flow past Z/z)
            encryptedChar = chr(start + offset) #turns ordinal of A/a + the offset to give new shifted character.
            encryptedString += encryptedChar #concatenates the new character to encryptedString
        else:
            #Non-letters stay same
            encryptedString += char

    return encryptedString

def decrypt(target, shift):
    decryptedString = ""

    for char in target:
        if char.isalpha():
            #handle uppercase vs lowercase
            start = ord('A') if char.isupper() else ord('a') #if character is upper case set start to the ordinal value of uppercase A, opposite goes for lowercase a
            
            #shift within range of 0-25 (letters of alphabet), then wrap around with modulo if it goes past Z/z
            offset = (ord(char) - start - shift) % 26 #takes ordinal value of char and subtracts the start from it, then subtracts the shift to it (mod 26 ensures it doens't flow past Z/z)
            decryptedChar = chr(start + offset) #turns ordinal of A/a + the offset to give new shifted character.
            decryptedString += decryptedChar #concatenates the new character to encryptedString
        else:
            #Non-letters stay same
            decryptedString += char
            
    return decryptedString
