alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import logo_caesar

print(logo_caesar.logo, "\n")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # Se for decode, o shift vira negativo. Se for encode, continua positivo.
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

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