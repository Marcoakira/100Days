def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# jeito 1
# def days_in_month(ano,mes):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ano_bi = is_leap(ano)
#     if ano_bi is True:
#         month_days[1] = 29
#     return month_days[mes-1]

# Jeito 2
def days_in_month(ano, mes):
    """Essa é uma Função que Verifica se o Ano é bi-cesto, e quantos
    Dias tem o mês"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap(ano)
    if is_leap(ano):
        month_days[1] = 29
    return month_days[mes - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
