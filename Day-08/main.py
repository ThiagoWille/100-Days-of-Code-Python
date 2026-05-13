alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import logo_caesar

print(logo_caesar.logo, "\n")

def encrypt(code_text, shift_int):
    cipher_text = ""

    for letter in code_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_int)
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
        
    
    print(f"Encoded message: {cipher_text}")

def decrypt(uncode_text, shift_int):
    output_text = ""

    for letter in uncode_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_int)
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Decoded message: {output_text}")


def caesar(encode_or_decode, original_text, shift_amount):
    if encode_or_decode == "encode":
        encrypt(code_text=original_text, shift_int=shift_amount)
    else:
        decrypt(uncode_text=original_text, shift_int=shift_amount)

end_program = False

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
    
    reset = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()

    if reset == "no":
        end_program = True
    elif reset != "yes" and "no":
        print("Ivalid Option!")
        end_program = True