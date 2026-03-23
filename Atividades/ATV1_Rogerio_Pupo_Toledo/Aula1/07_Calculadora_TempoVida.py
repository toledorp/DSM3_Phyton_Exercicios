nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
anos_vida = idade * 365
horas_vida = anos_vida * 24
minutos_vida = horas_vida * 60
segundos_vida = minutos_vida * 60
print(f"{nome}, você já viveu aproximadamente {anos_vida} dias.") 
print(f"{nome}, você já viveu aproximadamente {horas_vida} horas.") 
print(f"{nome}, você já viveu aproximadamente {minutos_vida} minutos.") 
print(f"{nome}, você já viveu aproximadamente {segundos_vida} segundos.") 