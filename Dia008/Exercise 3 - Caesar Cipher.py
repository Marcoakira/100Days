alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#=======================================================================
#posicao = alphabet.index(text)+5


def encrypt():
    for letra in (text):
        if letra not in alphabet:
            print(letra,end='')
      #  if alphabet.index(letra):
        else:
            posicao = alphabet.index(letra) + shift
            if posicao > 25:
                posicao = posicao - 26

            print(alphabet[posicao],end='')

def decrypt()

encrypt()

# for pos, letra in enumerate(text):
#     # if pos > 25:
#     #    pos = pos - 26
#     print(alphabet.index(text) + 5)
#     print(pos,letra)



#print(alphabet.index(text)+5)

#print(alphabet[posicao])
#print(posicao)



# for pos,valor in enumerate(alphabet):
#     print(pos,valor)

#   aTODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #aTODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#aTODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.