import art
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(choice, message, number):
    if choice == "decode":
        number *= - 1
    cypher_text = ""
    for i in message:
        position = alphabet.index(i)
        new_position = position + number
        if new_position > 26:
            new_position = new_position % 26
        shifted_letter = alphabet[new_position]
        cypher_text += shifted_letter 
    print(cypher_text)

continue_run = True
while continue_run:
    print(art.logo)        
    en_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(choice = en_dec, message = text, number = shift)
    
    repeat = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if repeat == 'no':
        continue_run = False