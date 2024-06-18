alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphabet2 = str.upper(alphabet)

shift = input("Enter shift: ")
text = input("Enter text: ")
key = input ('enter key:')
choice = input("Write 'e' for encode, 'd' for decode ")
final = ''
x = 0
letter_list = []

if choice == 'e':

    for letter in text:
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


elif choice == 'd':
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


else:
    print("Invalid Input")

print(final)