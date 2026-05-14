alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  # alphabets
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  # ...
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  # ...
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # ...


def caesar(start_text, shift_amount, cipher_direction):  # caser function :
    end_text = ""  # blank space stored in that variable
    if cipher_direction == "decode":  # If Decode:
        shift_amount *= -1  # multiply -1 from shift
    for char in start_text:  # for char in message:
        if char in alphabet:  # if the user enters an alphabet:
            position = alphabet.index(char)  # set the position according to the position of char in alphabet list
            new_position = position + shift_amount  # add shift amount in position
            end_text += alphabet[new_position]  # one by one new alphabets added in blank space
        else:  # if the user enters a number/symbol/space:
            end_text += char  # one by one this added in blank space
    print(f"Here's the {cipher_direction}d result: {end_text}")  # Here is a decode/encode result ....


from art import logo  # import logo

print(logo)  # print logo
should_end = False  # if YES : Not End
while not should_end:  # while loop continues
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  # input direction
    text = input("Type your message:\n").lower()  # input message
    shift = int(input("Type the shift number:\n"))  # input shift
    shift = shift % 26  # if the user enters a shift number greater than 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)  # caser function calling
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")  # [restart YES or NO]
    if restart == "no":  # if NO :
        should_end = True  # End
        print("Goodbye")  # print Goodbye
