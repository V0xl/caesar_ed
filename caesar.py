# Define variables
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphabet2 = str.upper(alphabet)

shift = input("Enter shift: ")
text = input("Enter text: ")
final = ''
x = 0
choice = input("Write 'e' for encode, 'd' for decode ")
letter_list = []

# Encode function
def encode(text, x, final, shift):

    for i in range (0, len(text)):
        single_letter = text[x]
        numberified_letter = alphabet.find(text[x])
        numberified_letter2 = alphabet2.find(text[x])

        if numberified_letter == -1:
            alphabet2.find(text[x])

            if numberified_letter2 == -1:
             
             final += single_letter

            else:
                final += str(alphabet2[alphabet2.find(text[x]) + int(shift)])


        else : final += str(alphabet[alphabet.find(text[x]) + int(shift)])

        x = x + 1

    return final

# Decode function
def decode(text, x, final ,shift):

    rev = alphabet[::-1]
    rev2 = alphabet2[::-1]

    for letter in text:
        single_letter = text[x] 
        numberified_letter = alphabet.find(text[x])
        numberified_letter2 = alphabet2.find(text[x])


        if numberified_letter == -1:
            alphabet2.find(text[x])

            if numberified_letter2 == -1 :
                 final = final + single_letter

            else:
                final = final + str(rev2[rev2.find(text[x]) + int(shift)])

        else :
            final = final + str(rev[rev.find(text[x]) + int(shift)])

        x = x + 1

    return final

if choice == 'e':
    print(encode(text, x, final, shift))

elif choice == 'd':
    bruteforce = input("Go through all shifts (1-26)? (y)es or (n)o: ")
    key = input("Enter optional keyword to look for: ")

    if bruteforce == 'n':
        print(decode(text, x ,final ,shift))
    elif bruteforce == 'y':

        shift = 1
        for i in range(1,26):
           output = decode(text, x, final, shift)
           shift += 1
           if key in output:
                print(output)
                
    else:
        print('Invalid Input')
else:
    print("Invalid Input")
