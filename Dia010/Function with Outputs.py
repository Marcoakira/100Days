#Function with Outputs

# def format_name():
#     f_name = input("your firt name? ").capitalize()
#     l_name = input("your last name? ").capitalize()
#     return print(f_name +" "+ l_name)
#
# print(format_name())


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return " por favor digite todas as informações"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")
    return (formated_f_name + " " + formated_l_name)
# um mode de fazer
batat = format_name(f_name="AmandaA",l_name="FabiolA")
print(batat)
# Outro Modo de fazer
print(format_name(input("Qual seu primeiro nome? "),input("Qual seu Segundo Nome? ")))
