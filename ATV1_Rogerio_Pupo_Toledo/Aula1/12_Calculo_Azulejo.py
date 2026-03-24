altura_parede = float(input("Digite a altura da parede em metros: "))
largura_parede = float(input("Digite a largura da parede em metros: "))
altura_azulejo = float(input("Digite a altura do azulejo em metros: "))
largura_azulejo = float(input("Digite a largura do azulejo em metros: "))
area_parede = altura_parede * largura_parede
area_azulejo = altura_azulejo * largura_azulejo
quantidade_azulejos = area_parede / area_azulejo
print(f"A quantidade de azulejos necessária é: {quantidade_azulejos:.0f}")  
