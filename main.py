import cipher
exit = False
while exit == False:
    print("Welcome to the Caesar Cipher Mini-Project!")
    print("Would you like to Encrypt or Decrypt")
    choice = input()

    if choice.lower() == "encrypt":
        print("Enter a message to encrypt:")
        unencrypted = input()
        print(f"Your message is: {unencrypted}")

        print("Enter an integer to shift by:")
        shift = int(input())
        print(f"You are shifting by {shift}")

        encrypted = cipher.encrypt(unencrypted, shift)

        print(f"Your new message is {encrypted}!")
    else:
        print("Enter a message to decrypt:")
        encrypted = input()
        print(f"Your encrypted message is: {encrypted}")

        print("Enter an integer to shift back by:")
        shift = int(input())
        print(f"You are shifting back by {shift}")

        decrypted = cipher.decrypt(encrypted, shift)

        print(f"Your decrypted message is {decrypted}")
    print("Would you like to exit?")
    choice = input()
    if choice.lower() == "yes":
        exit = True


