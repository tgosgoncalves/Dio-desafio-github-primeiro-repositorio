distancia = int(input('Digite a distancia: '))

diametro_01 = int(input('Digite o primeiro diametro: '))
diametro_02 = int(input('Digite o segundo diametro: '))

calculo = round(float(distancia/(diametro_01 + diametro_02)), 2)



print(calculo)


# o que passou

entrada = input().split()





distancia = int(entrada[0])

diametro1 = int(entrada[1])

diametro2 = int(entrada[2])







resultado = (distancia / (diametro1 + diametro2))



resultado_p = '{:0.2f}'.format(resultado)





print(resultado_p)