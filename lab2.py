"""
    Author: Connor Li
    Date: 2023-09-28
    Acknowledgements: This code was developed with assistance from AI tools such as GitHub Copilot and OpenAI's GPT-4.
"""


def main():
    # Test docstrings

    help(decrypt)
    help(get_input_file)


    while True:
        try:
            if get_user_choice() == "encrypt":
                with open(get_input_file(True), "w") as file:
                    key = int(input("Please enter a key: "))
                    message = input("Please enter a message: ")
                    file.write(str(key) + "\n")
                    file.write(encrypt(message, key))
            else:
                with open(get_input_file(False)) as file:
                    key = int(file.readline())
                    for line in file:
                        line = line.split()
                        line = ' '.join(line)
                        print(decrypt(line, int(key)))
        except ValueError:
            print("Invalid key. Please enter an integer.")




def get_user_choice():
    """
        Function: get_user_choice
        Purpose: To ask the user whether they want to encrypt, decrypt, or quit.
        Returns:
            str: The user's choice, either 'encrypt' or 'decrypt'.
    """
    while True:
        try:
            choice = input("Please choose an option: \n1. Encrypt \n2. Decrypt \n3. Quit \n> ")

            if choice == "3":
                exit()
            elif choice == "1" or choice == "2":
                return "encrypt" if choice == "1" else "decrypt"
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter either '1' or '2'.")

    pass



def decrypt(message, offset):
    """
        Function: decrypt
        Purpose: Decrypts a given message by shifting the letters by a specified offset in the opposite direction.
        Parameters:
            - message (str): The message to be decrypted.
            - offset (int): The number of positions each letter in the message needs to be shifted.
        Returns:
            - str: The decrypted message.
    """
    message = message.lower()

    to_return = []
    for i in range(len(message)):
        c = message[i]
        if 'a' <= c <= 'z':
            to_return.append(apply_offset(c, -offset))
        else:
            to_return.append(c)

    return ''.join(to_return)



def encrypt(message, offset):
    """
        Function: encrypt
        Purpose: Encrypts a given message by shifting the letters by a specified offset.
        Parameters:
            - message (str): The message to be encrypted.
            - offset (int): The number of positions each letter in the message needs to be shifted.
        Returns:
            - str: The encrypted message.
    """
    message = message.lower()

    to_return = []
    for i in range(len(message)):
        c = message[i]
        if 'a' <= c <= 'z':
            to_return.append(apply_offset(c, offset))
        else:
            to_return.append(c)

    return ''.join(to_return)




def apply_offset(c, offset):
    """
        Function: apply_offset
        Arguments:
            c: A character to which the offset will be applied, should be a lowercase letter.
            offset: An integer specifying a cyclic offset, i.e., after 'z', it goes back to 'a'.
        Purpose: To apply a cyclic offset to a given character and return the resulting character.
        Return: Returns a character that results from applying the specified offset to `c` following a cyclic pattern in the English alphabet.
    """

    if abs(offset) > 26:
        offset = offset % 26

    offset_applied_ascii = ord(c) + offset
    ascii_max = ord('z')
    ascii_min = ord('a')
    if offset_applied_ascii > ascii_max:
        return chr(ascii_min + (offset_applied_ascii - ascii_max) - 1)
    elif offset_applied_ascii < ascii_min:
        return chr(ascii_max - (ascii_min - offset_applied_ascii) + 1)
    else:
        return chr(offset_applied_ascii)




def get_input_file(new_file: bool):
    """
        Function: get_input_file
        Purpose: To get the input file name from the user. If the new_file parameter is True, a new file with the given name is created. If False, the function attempts to open an existing file with the given name.
        Parameters:
            new_file (bool): Determines whether a new file should be created or an existing file should be opened.
        Returns:
            file_name (str): The valid name of the text file as a string. If the file name provided by the user does not end with ".txt", the function will append this extension.
        Raises:
            FileNotFoundError: If the file does not exist and new_file is False, or if the file name provided by the user does not end with ".txt".
    """

    while True:
        file_name = ""

        try:
            file_name = input("Enter the input filename: ")

            if not file_name.endswith(".txt"):
                file_name = file_name.split(".")[0]
                raise FileNotFoundError

            if new_file:
                file = open(file_name, "w")
            else:
                file = open(file_name, "r")

            file.close()
            return file_name


        except FileNotFoundError:
            print(f"Invalid filename extension. Please re-enter the input filename: {file_name}.txt")


main()
