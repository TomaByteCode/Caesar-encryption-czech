alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift_number):
    shifted_text = ""
    for one_letter in message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index + shift_number
            shifted_text += alphabet[new_index]
        else:
            shifted_text += one_letter
    print(f"Your encrypted text is: {shifted_text}")

def cipher(start_text, shift_number, direction):
    end_text = ""
    for one_letter in start_text:
       if one_letter != " ":
            index = alphabet.index(one_letter)
            if direction == "encode":
                new_index = index + shift_number
                end_text += alphabet[new_index]
            elif direction == "decode":
                new_index = index - shift_number
                end_text += alphabet[new_index]
            else:
                end_text += one_letter
    print(f"Vaše operace byla {direction} a výsledek je: {end_text}")

def decode(encrypted_message, shift_number):
    normal_text = ""
    for one_letter in encrypted_message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index - shift_number
            normal_text += alphabet[new_index]
        else:
            normal_text += one_letter
    print(f"Your decrypted text is: {normal_text}")


# decode("ifani", 5)

lets_continue = "yes"

while lets_continue == "yes":

    direction = input("Napište 'encode' pokud chcete zakódovat zprávu. Napište 'decode', pokud chcete dekódovat zprávu. ")
    text = input("Napište svou zprávu:\n").lower()
    shift = int(input ("Napište hodnotu posunu:\n"))

    if direction == "encode":
        cipher(text, shift, direction)
        encode(text, shift)
        lets_continue = input("Chcete zakódovat další zprávu? (yes/no): ")
    elif direction == "decode":
        cipher(text, shift, direction)
        decode(text, shift)
        lets_continue = input("Chcete dekódovat další zprávu? (yes/no): ")
    else:
        print("Neznámý požadavek.")


