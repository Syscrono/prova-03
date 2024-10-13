# [LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. 
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número. Implemente o jogo utilizando 
# um loop while para permitir que o jogador faça múltiplas tentativas até acertar 
# ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem 
# de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso

numero_secreto = 7
tentativas = 0

while tentativas < 3:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif tentativas == 3:
        print("Que pena! Suas 3 tentativas acabaram. O número secreto era", numero_secreto)
    else:
        if palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")