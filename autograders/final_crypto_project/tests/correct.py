### TODO: add the correct function implementations
### TODO: include the main program at the end of the file, in the def main()
import math
import random
import os
import string


def print_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    """
    print("==========================")
    for key, item in menu.items():
        print(f"{key} = {item}")
    print("==========================")

def create_matrix(row_length, column_length):
    """
    The function takes two integers `row_length` and `column_length`
    as input and outputs a matrix of dimension `row_length` x 
    `column_length` which contains space characters(`' '`)
    """
    main_list = []
    for i in range(row_length):
        temp_list = []
        for j in range(column_length):
            temp_list.append(' ')
        main_list.append(temp_list)
    
    return main_list

def encode_to_matrix(message_string, column_length):
    """
    The function takes a string `message_string` and an integer
    `column_length` as integer and "writes" the message string
    on to a matrix that has `column_length` many columns.
    """
    import math
    row_length = math.ceil(len(message_string)/column_length)
    matrix = create_matrix(row_length, column_length)
    k = 0
    for i in range(row_length):
        for j in range(column_length):
            matrix[i][j] = message_string[k]
            k += 1
            if k == len(message_string):
                break
        if k == len(message_string):
            break
    
    return matrix

if __name__ == '__main__':
    message = input() # TODO: Take the input as a string from user
    columns = int(input()) # TODO: Take the input as an integer from user
    # Call the function to get the encoded matrix and print the
    # statement
    print(f'The encoded matrix is {encode_to_matrix(message, columns)}')
    assert encode_to_matrix("CSWEIGHT TEACHES US PROGRAMMING", 5) == [['C', 'S', 'W', 'E', 'I'], ['G', 'H', 'T', ' ', 'T'], ['E', 'A', 'C', 'H', 'E'], ['S', ' ', 'U', 'S', ' '], ['P', 'R', 'O', 'G', 'R'], ['A', 'M', 'M', 'I', 'N'], ['G', ' ', ' ', ' ', ' ']]
    assert encode_to_matrix("YELLOW SUBMARINE", 2) == [['Y', 'E'], ['L', 'L'], ['O', 'W'], [' ', 'S'], ['U', 'B'], ['M', 'A'], ['R', 'I'], ['N', 'E']]
    assert encode_to_matrix("CHECK OUT THE HOOK WHILE MY DJ REVOLVES IT", 9) == [['C', 'H', 'E', 'C', 'K', ' ', 'O', 'U', 'T'], [' ', 'T', 'H', 'E', ' ', 'H', 'O', 'O', 'K'], [' ', 'W', 'H', 'I', 'L', 'E', ' ', 'M', 'Y'], [' ', 'D', 'J', ' ', 'R', 'E', 'V', 'O', 'L'], ['V', 'E', 'S', ' ', 'I', 'T', ' ', ' ', ' ']]
    assert encode_to_matrix("I LIKE CRYPTOGRAPHY", 19) == [['I', ' ', 'L', 'I', 'K', 'E', ' ', 'C', 'R', 'Y', 'P', 'T', 'O', 'G', 'R', 'A', 'P', 'H', 'Y']]


# A. Scytale Cipher Functions
# A1. Function that creates the matrix, Finished!!!
def create_matrix(message, nColumns):
    """
    This function creates a matrix while using the nColumns to find the number of rows of that matrix.
    :param message: (str) Message to be encrypted. It is a helper function for encrypt_transposition() and
    decrypt_transposition().
    :param nColumns: (str) The number of columns for the matrix.
    :return: Nested list that acts as a matrix.
    """
    nColumns = int(nColumns)
    message_length = len(message)  # Get length of message
    nRows = math.ceil(message_length / nColumns)  # Find number of nRows by dividing message_length by nColumns
    new_matrix = []
    for row_index in range(nRows):  # Make new matrix by making each new row then appending empty columns
        new_matrix.append([])  # Append row of matrix
        for column_index in range(nColumns):
            new_matrix[row_index] += ' '  # Add number of empty spaces based on nColumns
    return new_matrix

# A2. This function encodes the message to the given matrix for encryption, Finished!!!
def encode_to_matrix(message, matrix):
    """
    This function encodes a message to a given matrix for encryption when the matrix is read off of. It is a helper
    function for encrypt_transposition(). Inputs message into matrix left to right by row then top to bottom so that
    encoded message can be made by reading it off by top to bottom by column then left to right by
    encrypt_transposition().
    Input Characters; Left --> Right by row then Top --> Bottom
    :param message: (str) Message that must be added to matrix.
    :param matrix: (nested list) Nested list used for matrix.
    :return: Matrix with message inside it.
    """
    letter_index = 0  # Set up letter index
    for row_index, row in enumerate(matrix):  # Choose one row at a time to iterate over and add column values to
        for column_index in range(len(row)):
            if letter_index == len(message):  # Stop loop once no more letters to add
                return matrix
            letter = message[letter_index]  # Find the given letter to add to the matrix by indexing
            matrix[row_index][column_index] = letter  # Add given letter to matrix
            letter_index += 1  # Increment letter_index to go to next letter
    return matrix

# A3. This function encodes the message to the given matrix for decryption, Finished!!!
def encode_to_matrix_decrypt(message, matrix):
    """
    This function encodes an encrypted message to a given matrix to get it to be decrypted when the matrix is read off.
    It is a helper function for decrypt_transposition(). Inputs message into matrix top to bottom by column then left to
    right so that it can be read off left to right by row then top to bottom by decrypt_transposition() to get the
    decrypted message.
    Input characters; Top --> Bottom by column then Left --> Right
    :param message: (str) Encrypted message that must be added to matrix.
    :param matrix: (nested list) Nested list used for matrix.
    :return: Matrix with encrypted message inside it.
    """
    letter_index = 0  # Define letter index
    nRows = len(matrix)  # Find number of rows
    nColumns = len(matrix[0])  # Find number of columns (0th row always present)
    for column_index in range(nColumns):  # Keep column index same while changing row index to fill by column
        for row_index in range(nRows):
            if letter_index == len(message):  # Done to avoid indexing with numbers greater than string length
                return matrix
            letter = message[letter_index]  # Index to find the letter to add to the matrix
            matrix[row_index][column_index] = letter  # Add letter to the given index
            letter_index += 1  # Increment the letter index in order to go on to the next letter in the message
    return matrix

# A4. Function that encrypts message for scytale cipher, Finished!!!
def encrypt_transposition(message, nColumns):
    """
    Accepts plaintext (readable text) as a string and an integer value for the nColumns. The function
    should return the encrypted message. Used create_matrix() and encode_to_matrix() (inputs message into matrix left
    to right by row then top to bottom so that encoded message can be made by reading it off by top to bottom by column
    then left to right by this function) as helper functions.
    :param message: (str) Message to be encrypted.
    :param nColumns: (int) The number of columns for the matrix.
    :return: The encrypted message as a string.
    """
    matrix = create_matrix(message, nColumns)  # This function creates a matrix with the given parameters
    encoded_matrix = encode_to_matrix(message, matrix)  # This function encodes the message to the matrix
    encoded_message = ""  # Using string concatenation so will add each letter individually to this empty string
    for column_index in range(len(encoded_matrix[0])):  # Keep column the same while iterating through row
        for row_index in range(len(encoded_matrix)):
            letter = encoded_matrix[row_index][column_index]  # Find the current letter using indexing
            encoded_message += letter  # Add the current letter to the message
    return encoded_message

# A5. Function that decrypts message for scytale cipher, Finished!!!
def decrypt_transposition(message, nColumns):
    """
    Accepts the encoded message as a string and an integer value for the nColumns that was used in encrypting the
    message. The function returns the plaintext (readable) message - the message that the sender encrypted and
    wanted you to understand. Remember to remove any trailing whitespace from the returned plaintext message. Used
    create_matrix() and encode_to_matrix_decrypt() (inputs message into matrix top to bottom by column then left to
    right so that it can be read off left to right by row then top to bottom in this function to get the decrypted
    message) as helper functions.
    :param message: (str) Message to be decrypted.
    :param nColumns: (int) The number of columns for the matrix.
    :return: The decrypted message as a string.
    """
    matrix = create_matrix(message, nColumns)  # This function creates a matrix with the given parameters
    encoded_matrix = encode_to_matrix_decrypt(message, matrix)  # Encodes to matrix so read off it left to right
    decrypted_message = ""  # Start with empty string to concatenate
    for row_index, row in enumerate(encoded_matrix):  # Keep row the same while switching through columns
        for column_index in range(len(row)):
            letter = encoded_matrix[row_index][column_index]  # Find current letter using indexing
            decrypted_message += letter  # Concatenate current letter to decrypted message
    decrypted_message_stripped = decrypted_message.strip()  # Strip the decrypted message to avoid unneeded whitespace
    return decrypted_message_stripped



# B. Vigenere Cipher Functions
# B1. Function that makes the key, Finished!!!
def extend_vigenere(message, secret):
    """
    Accepts the string parameters message representing the plaintext message and secret representing the secret
    phrase/word. The function returns a new key that matches the plaintext message in length, extending or shrinking
    the passed secret if necessary. Returns a new object, do not modify the original argument. Helper function whenever
    a key is needed.
    :param message: (str) The message to find the length of to find the length of the key.
    :param secret: (str) The secret is the unit of the key.
    :return: The key to encode the secret message.
    """
    message_length = len(message)  # Find the length of the message
    secret_length = len(secret)  # Find the length of the secret
    num_repeated_secrets = message_length // secret_length  # Find the number of times secret should repeat in key
    remainder_letters = message_length % secret_length  # Number of remaining letters is one more than slice index
    if secret_length <= message_length:
        key = secret * num_repeated_secrets + secret[:remainder_letters]  # Concatenate and end index not included
    else:
        key = secret[:remainder_letters]  # Off case where the message is shorter than the secret
    return key

# B2. Function that makes the alphabet, Finished!!!
def get_alphabet_vigenere():
    """
    Does not have any parameters and returns the string containing the entire alphabet. For this lab, the alphabet
    will be: uppercase English letters followed by 0123456789, followed by lowercase English letters.
    :return: The given alphabet as a string. Helper function whenever an alphabet is need.
    """
    abc = "abcdefghijklmnopqrstuvwxyz"  # Make the abc's
    ABC = abc.upper()  # Turn the abc's to capital letters
    numbers = "0123456789"  # Get numbers 0-9
    alphabet = ABC + numbers + abc  # String concatenation to get alphabet
    return alphabet

# B3. Function that encrypts the message, Finished!!!
def encrypt_vigenere(message, secret):
    """
    Accepts the strings for plaintext and the secret word and returns the encrypted message. Uses
    get_alphabet_vigenere() and extend_vigenere() as helper functions.
    :param message: (str) The message that is going to be encrypted.
    :param secret: (str) The base unit for the key.
    :return: The encrypted message as a string.
    """
    alphabet = get_alphabet_vigenere()  # Get the alphabet
    key = extend_vigenere(message, secret)  # Get the key using the secret
    encoded_message = ""  # Start encoded message concatenation
    if message == "" or secret == "":  # Deal with empty case
        return encoded_message
    if (' ' in message) or (' ' in secret):  # Deal with space case
        return -1
    for index in range(len(message)):  # Iterate over message to decode entire message
        letter_m = message[index]  # Find the given letter for message
        index_m_alphabet = alphabet.find(letter_m)  # Find the message letter index in the alphabet
        letter_k = key[index]  # Find the key letter
        index_k_alphabet = alphabet.find(letter_k)  # Find the key letter index in the alphabet
        new_index = index_m_alphabet + index_k_alphabet  # Find the new index by adding the two previous indexes
        if new_index >= len(alphabet):  # Deal with case where index needs to loop because to big
            looped_index = new_index % len(alphabet)  # Get index of character where need to loop back to start
            new_letter = alphabet[looped_index]  # Get new letter
        else:
            new_letter = alphabet[new_index]  # Get new letter in case where index does not need to loop
        encoded_message += new_letter  # Concatenate the encoded message with the new letter
    return encoded_message

# B4. Function that decrypts a message
def decrypt_vigenere(message, secret):
    """
    Accepts string arguments as the encrypted message and secret word that was used for encryption (not extended) to
    decrypt the encrypted message. Uses get_alphabet_vigenere() and extend_vigenere() as helper functions. Also strips
    whitespace off the final decoded message.
    :param message: (str) The encrypted message.
    :param secret: (str) The base unit for the key.
    :return: The decrypted message as a string
    """
    alphabet = get_alphabet_vigenere()  # Get the alphabet
    key = extend_vigenere(message, secret)  # Get the key using the secret
    decoded_message = ""  # Start encoded message concatenation
    if message == "" or secret == "":  # Deal with empty case
        return decoded_message
    if ' ' in message or ' ' in secret:  # Deal with space case
        return -1
    for index in range(len(message)):  # Iterate over message to decode it
        letter_m = message[index]  # Find the given letter for coded message
        index_m_alphabet = alphabet.find(letter_m)  # Find the coded message letter index in the alphabet
        letter_k = key[index]  # Find the key letter
        index_k_alphabet = alphabet.find(letter_k)  # Find the key letter index in the alphabet
        new_index = index_m_alphabet - index_k_alphabet  # Get index of decoded letter
        new_letter = alphabet[new_index]  # Get new letter
        decoded_message += new_letter  # Concatenate the encoded message with the new letter
    return decoded_message

def main():

    the_menu = {
        "E" : "Encrypt a message",
        "D" : "Decrypt a message",
        "S" : "Save encryption to file",
        "R" : "Retrieve decryption from file",
        "Q" : "Quit this program"} # TODO 1: add the options from the instructions

    cipher_menu = {
        "T": "Scytale Cipher",
        "V": "Vigenere Cipher"
    }

    opt = None

    while True:
        print_menu(the_menu) # TODO 2: define the function, uncomment, and call with the menu as an argument
        opt = input("::: Enter a menu option\n> ")
        opt = opt.upper() # to allow us to input lower- or upper-case letters

        if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
            print(f"WARNING: {opt} is an invalid menu option.\n")
            continue

        print(f"You selected option {opt} to > {the_menu[opt]}.")

        if opt == 'Q': # TODO 4: quit the program
            print("Goodbye!")
            break # exit the main `while` loop
     ###********************************************************************************
        if opt == 'E':
            print("::: Which cipher to use?")
            print_menu(cipher_menu) # TODO 5: reuse the function with the cipher menu dictionary
            cipher = input("> ").upper()
            if cipher == 'T':
                message = input("::: Message > ") # TODO 6: get the input as a string
                nColumns = input("::: Key > ") # TODO 7: get the input as an integer
                # TODO 8: if the string is not a valid integer, output a warning
                if not nColumns.isnumeric():
                    print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                    continue
                else:
                    nColumns = int(nColumns)

                # TODO 9: Call the function `encrypt_transposition` to encrypt the message
                result = encrypt_transposition(message, nColumns)
            elif cipher == 'V':
                message = input("::: Message > ") # TODO: get the input as a string
                secret = input("::: Secret > ") # TODO: get the input as a string
                # TODO: Call the function `encrypt_vigenere` to encrypt the message
                result = encrypt_vigenere(message, secret)
            else:
                print(f"WARNING: {cipher} is an invalid cipher.\n")
                continue # back to the main menu

            # Print the message after obtaining the encrypted result
            print(f"Encryption using the {cipher_menu[cipher]}:") # TODO
            print(result)
     ###********************************************************************************
        if opt == 'D':
            print("::: Which cipher to use?")
            print_menu(cipher_menu) # TODO 5: reuse the function with the cipher menu dictionary
            cipher = input("> ").upper()
            if cipher == 'T':
                message = input("::: Ciphertext > ") # TODO 6: get the input as a string
                nColumns = input("::: Key > ") # TODO 7: get the input as an integer
                # TODO 8: if the string is not a valid integer, output a warning
                if not nColumns.isnumeric():
                    print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                    continue
                else:
                    nColumns = int(nColumns)

                # TODO 9: Call the function `encrypt_transposition` to encrypt the message
                result = decrypt_transposition(message, nColumns)
            elif cipher == 'V':
                message = input("::: Ciphertext > ") # TODO: get the input as a string
                secret = input("::: Secret > ") # TODO: get the input as a string
                # TODO: Call the function `encrypt_vigenere` to encrypt the message
                result = decrypt_vigenere(message, secret)
            else:
                print(f"WARNING: {cipher} is an invalid cipher.\n")
                continue # back to the main menu

            # Print the message after obtaining the encrypted result
            print(f"Decrypted message using the {cipher_menu[cipher]}:") # TODO
            print(result)

###********************************************************************************
        if opt == 'S':
            print("::: Proceed to save the message that was previously encoded?")
            proceed = input("Press 'y' to continue.\n> ")
            if proceed != 'y':
                continue
            else:
                filename = input("Enter the name of the file.\n> ")
                ...
                print(f"Saved '{filename}'")

###********************************************************************************
        if opt == 'R':
            filename = input("Enter the name of the file to open.\n> ")
            if filename: # TODO: check that the file exists
                print(f"Contents of '{filename}':")
                ...
            else:
                print(f"File '{filename}' was not found.")


        # Pause before going back to the main menu
        input("::: Press Enter to return to main menu")

# the message to display before quitting the program
    print("Your secrets are safe with me.")


if __name__ == '__main__':
    pass
##    param_list = [
##        # list cases
##        ["L", "A"],
##        ["L", "C"],
##        ["L", "I"],
##        # add cases
##        ["A", "invalid", "y",
##         ",,,,", "y",
##         "implement get_new_task(),,,,", "y",
##         "implement get_new_task(),,5,,", "y",
##         "implement get_new_task(),,5,6/1/22,", "y",
##         "implement get_new_task(),,5,6/1/2022,", "y",
##         "implement get_new_task(),, 5, 6/1/2022, y", "y",
##         "implement get_new_task(),, 5, 6/1/2022, no", "n"],
##        # update
##        ["U", "invalid", "y",
##         "1", "info", "Call 123-456-7890", "y",
##         "1", "invalid", "m"],
##        # delete
##        ["D",
##         "invalid", "y",
##         "1", "y",
##         "A", "Yes"],
##        # restore
##        ["R", "test.csv", "y",
##         "missing-date.csv", "y",
##         "combined.csv", "y",
##         "single-task.csv","n"],
##        # save
##        ["S", "invalid", "y",
##         "my-tasks.csv"],
##        ["random"]
##    ]
##
##    for params in param_list:
##        input_val = "\n".join(params) + "\n\nQ\n"
##        print(input_val)
