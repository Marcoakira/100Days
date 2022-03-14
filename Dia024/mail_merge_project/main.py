

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



