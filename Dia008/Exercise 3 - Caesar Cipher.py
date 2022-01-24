alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def escolha():
    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    else:
        print("escolha uma opçao valida")
def encrypt():
    for letra in (text):
        if letra not in alphabet:
            print(letra,end='')

        else:
            posicao = alphabet.index(letra) + shift
            if posicao > 25:
                posicao = posicao - 26

            print(alphabet[posicao],end='')

def decrypt():
    for letra in (text):
        if letra not in alphabet:
            print(letra,end='')

        else:
            posicao = alphabet.index(letra) - shift

            print(alphabet[posicao],end='')

escolha()
