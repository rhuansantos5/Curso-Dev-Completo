from datetime import datetime

# # sequencia = ano, mes, dia
# minha_data = date(2026, 9, 7)

# print(minha_data)




# # condicionais

# natal = date(2026, 12, 25)

# if (natal.day == 25) and (natal.month == 12):
#     print("É natal!")
# else:
#     print("Não é natal")




# strptime (string convertida para tempo)

data_string = "20/06/2026"
data_formato = "%d/%m/%Y"


data_date = datetime.strptime(data_string, data_formato).date()
print(data_date)