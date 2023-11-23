import random

cor_secreta = random.choice(['R', 'G', 'B'])

pontos_seus = 0
pontos_deles = 0

while True:
    palpite = input("adivinhe a cor (R, G, B): ").upper()

    if palpite not in ['R', 'G', 'B']:
        print("Entrada invalida. Escolha R, G ou B")
    elif palpite == cor_secreta:
        print("Parabéns!!Voce acertou!!!")
        pontos_seus = pontos_seus +  1
        cor_secreta = random.choice(['R', 'G', 'B'])
    else:
        print("OPA VOCE ERROU!!!!!!!")
        pontos_deles = pontos_deles +  1

    print('a cor era', cor_secreta)
    print(f'VOCÊ{pontos_seus} x PC {pontos_deles}')

    if pontos_seus == 3 or pontos_deles == 3:
        break
