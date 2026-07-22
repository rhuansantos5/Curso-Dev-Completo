from datetime import datetime

media = float(input("Média do aluno: "))

if media >= 7.0:
    print("Passou direto!")
elif (media >= 4.0) and (media < 7):
    print("Recuperação.")
     
    data_prazo = datetime(2026, 1, 31)
    formato_data = "%d/%m/%Y"
    
    while True:
        try:    
            data_prova_str = input("Quando o aluno fez a prova? (formato dd/mm/aaaa): ").strip()
            data_prova_date = datetime.strptime(data_prova_str, formato_data)
            break
        except ValueError:
            print("Formato de data inválido. Use dd/mm/aaaa")

    if data_prova_date <= data_prazo:
        nota_rec = float(input("Nota de recuperação: "))

        if nota_rec >= 7.0:
            print("Passou na recuperação.")
        else:
            print("Reprovou na recuperação.")
    else:
        print("Prova feita fora do prazo. Aluno reprovado")


else:
    print("Reprovou direto.")