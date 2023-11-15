nome = input("Digite seu nome: ")
horas = int(input("Que horas são:"))

if 6 <= horas < 12:
    print(nome, "Bom dia!")
elif 12 <= horas < 18:
    print(nome, "Boa tarde!")
elif 18 <= horas < 24 or 0 <= horas < 6:
    print(nome, "Boa noite!")
else:
    print(nome, "Por favor, digite um horário válido")
