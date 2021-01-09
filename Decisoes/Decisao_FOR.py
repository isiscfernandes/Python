tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(0,11,1): #(inicio, fim, incremento)
	print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))