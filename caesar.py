# TODO-1: Import and print the logo from art.py when the program starts.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    new_word = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            new_word += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            new_word += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result:{new_word}")



# TODO-3: Can you figure out a way to restart the cipher program?

print(art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    again = input("Do you want to continue ?")
    if again == "yes":
        continue
    elif again == "no":
        print("Thank you for playing!")
        break

