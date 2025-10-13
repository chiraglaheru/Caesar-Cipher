alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:  
            shifted_position = alphabet.index(letter) + shift_amount 
            shifted_position %= len(alphabet)  
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)  
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the decoded result: {output_text}")

should_continue = True

while should_continue:

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

restart = input("type 'yes if you want to go again or type 'no'\n").lower()
if restart ==  "no":
    should_continue = False
    print("Get out!!! :)")
    

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid direction! Please type 'encode' or 'decode'.")

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if letter in original_text:
        output_text += letter
    else:
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    
    action = "encoded" if encode_or_decode == "encode" else "decoded"
    print(f"Here is the {action} result: {output_text}")

ceaser(text, shift, direction)
