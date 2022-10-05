valores = input().split()

tempo_gasto_em_horas = int(valores[0])
velocidade_media_kmh = int(valores[1])


distancia_percorrida_km = velocidade_media_kmh * tempo_gasto_em_horas           # Multiplicando o tempo de viagem pela velocidade média, tem-se a distancia percorrida em Km

qntd_litros_combustivel = distancia_percorrida_km / 12                          # Dividindo essa distância total pelo consumo em Km/L que o carro faz, tem-se a quantidade de combustivel necessária para viagem

qntd_litros_combustivel_float = f"{qntd_litros_combustivel:.3f}"                # Garantido que a saída atenderá aos criterios decimais do desafio

print(qntd_litros_combustivel_float)
