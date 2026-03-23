

u = float(input("Digite a Tensão (em volts): "))
r = float(input("Digite a Resistência (em ohms): "))
i = float(input("Digite a Corrente (em amperes): "))

print("***************** CÁLCULO DE GRANDEZAS ELÉTRICAS *****************")
print("| 1 - Calcular a Tensão (V) usando a Lei de Ohm (V = I * R)      |")
print("| 2 - Calcular a Resistência (R) usando a Lei de Ohm (R = V / I) |")
print("| 3 - Calcular a Corrente (I) usando a Lei de Ohm (I = V / R)    |")
print("******************************************************************")
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

match opcao:
  case 1:    
    tensao = i * r
    print(f"A Tensão (V) é: {tensao:.2f} volts")
  case 2:    
    resistencia = u / i
    print(f"A Resistência (R) é: {resistencia:.2f} ohms")
  case 3:    
    corrente = u / r
    print(f"A Corrente (I) é: {corrente:.2f} amperes")
  case _:    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")