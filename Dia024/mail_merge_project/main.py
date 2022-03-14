#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

list_names = []
with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()
    for name in names:
        name = name.strip()
        name = name.replace('\n', '')
        list_names.append(name)

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    print(list_names)
    for name in list_names:
        print(name)
        new_name = letter.replace('[name]', name)
        with open('./Output/ReadyToSend/ carta_para_' + name + '.txt', 'w') as output_file:
            output_file.write(new_name)






# with open('Input/Letters/starting_letter.txt') as starting_letter:
#     letter = starting_letter.read()
# #     print(letter)
#
# letra = open('Input/Letters/starting_letter.txt')
# bomdia = letra.read()
#
#
#
# name = open('Input/Names/invited_names.txt','r')
# nname = name.readlines()
# name = nname.replace('\n','')
# print(name)
#
# testando = open('Output/testando.txt', 'w')
# testando.write(f'{bomdia}')
#



# with open('Output/Letters/invited_letters.txt', 'w') as invited_letters:
#     for name in names:
#         invited_letters.write(letter.replace('{name}', name))
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp