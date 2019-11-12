#  Student Name: Marissa Green

import math

DEBUG = False

# takes a string and returns a K x K table padded with *
def construct_encrypt_table( strng ):

    # L is the length of the original message
    L = len(strng)
    # K is the length and width of the table
    K = int(math.sqrt(L))
    if K*K < L:
        K += 1
    # M is K squared
    M = K*K

    # pad the string with asterisks enough to fill the table exactly
    padded_string = strng + '*'*(M-L)

    # initialize the unrotated table
    table = [["_" for x in range(K)] for y in range(K)] 

    row = 0
    col = 0
    # because we have a fully padded string, we can walk the table starting at 0,0
    for ch in padded_string:
        table[row][col] = ch
        if col < K:
            col += 1
        if col == K:
            col = 0
            row += 1

    if DEBUG:
        print("encrypt_table:")
        for row in table: 
            print(row)

    return table


def construct_decrypt_table( strng ):

    # L is the length of the original message
    L = len(strng)
    # K is the length and width of the table
    #K = int(math.sqrt(L))+1
    K = int(math.sqrt(L))
    if K*K < L:
        K += 1
    # M is K squared
    M = K*K

    # initialize the unrotated table
    table = [["_" for x in range(K)] for y in range(K)] 

    row = K-1
    col = 0
    # construct the rotated table by first inserting the asterisks directly into the table
    for i in range(M-L):
        table[row][col] = '*'
        if row == 0:
            row = K-1
            col += 1
        else:
            row -= 1

    row = 0
    col = 0
    index = 0
    # now insert the characters from the string from left to right and top down
    # but dont put a character in a cell that is occupied by a *
    for i in range(M):
        if table[row][col] != '*':
            table[row][col] = strng[index]
            index += 1
        if col == K-1:
            col = 0
            row += 1
        else:
            col += 1

    if DEBUG:
        print("decrypt_table:")
        for row in table: 
            print(row)

    return table


# takes a table and returns the 90 degree rotated table
def rotate_table( table, direction ):

    # initialize the rotated table
    rotated_table = [["_" for x in range(len(table))] for y in range(len(table))]

    # rotate the table 90 degrees in the direction given
    for row in range(len(table)):
        for col in range(len(table)):
            if direction == 'right':
                rotated_table[col][len(table)-row-1] = table[row][col]
            else:
                rotated_table[row][col] = table[col][len(table)-row-1]

    if DEBUG:
        print("rotated_table:")
        for row in rotated_table: 
            print(row)

    return rotated_table


# takes a string and returns the encrypted string
def encrypt ( strng ):
    # get the padded table
    table = construct_encrypt_table(strng)

    # get the rotated table
    rotated_table = rotate_table(table, 'right')

    # construct the encrypted string from the rotated table
    encrypted_string = ""
    for row in rotated_table: 
        encrypted_string += "".join(row)

    # remove the asterisks before returning the encrypted string
    return encrypted_string.replace('*', '')


# takes an encrypted string and returns the plain text version
def decrypt ( strng ):
    # get the rotated table
    rotated_table = construct_decrypt_table(strng)

    # get the padded table
    table = rotate_table(rotated_table, 'left')

    # construct the decrypted string from the padded table
    decrypted_string = ""
    for row in table: 
        decrypted_string += "".join(row)

    # remove the asterisks before returning the decrypted string
    return decrypted_string.replace('*', '')


def main():
    # open file encrypt.txt
    input_file = open("encrypt.txt","r")
    input_file_lines = input_file.readlines()
    input_file.close()
    num_messages = int(input_file_lines.pop(0))
    input_messages_list = [s.strip() for s in input_file_lines]

    # encrypt and output all lines in file encrypt.txt
    print("Encryption:")
    for message in input_messages_list:
        if DEBUG:
            print("message:", message)
        print(encrypt(message))
    print()

    # open file decrypt.txt
    input_file = open("decrypt.txt","r")
    input_file_lines = input_file.readlines()
    input_file.close()
    num_messages = int(input_file_lines.pop(0))
    input_messages_list = [s.strip() for s in input_file_lines]

    # decrypt and output all lines in file decrypt.txt
    print("Decryption:")
    for message in input_messages_list:
        if DEBUG:
            print("message:", message)
        print(decrypt(message))
    print()


main()
