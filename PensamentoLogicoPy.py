import random # importa a biblioteca random para trabalharmos com o jogo da aleatoriedade.


def soma_digitos(texto):  # Cria a função soma_digitos que recebe o valor texto
    soma = 0  # Faz a variável soma ser 0, ou seja, quando formos somar, vai começar em 0
    digitos = []  # A variável digitos vai armazenar os digitos encontrados para retornarmos no fim do código.

    for string in texto:  # Percorre cada caractere da string fornecida na variável 'entrada'
        if string.isdigit():  # Após percorrer todos os caracteres, o método .isdigit() irá verificar qual é número
            soma += int(string)  # Soma += é como se fizéssemos soma = soma + (string), ou seja, transformamos a string em número e somamos
            digitos.append(string)  # o .append irá enviar os dígitos encontrados para a lista "digitos"

    return soma, digitos  # Retorna a soma e os dígitos encontrados para podermos trabalhar com eles


def contar_maiusculas_minusculas(texto):  # Cria a função contar_maiusculas_minusculas que recebe o valor texto
    maiusculas = 0  # Mesma ideia da varíavel criada em soma, iniciaremos somando a partir do 0
    minusculas = 0
    numeros = 0
    caracteres = 0

    for string in texto:  # Percorre cada caractere da string fornecida na variável 'entrada'
        if string.isupper():  # Verifica se o caractere é uma letra maiúscula usando o método .isupper()
            maiusculas += 1  # Se for maiúscula, adiciona 1 à variável maiusculas para a contagem
        elif string.islower():  # Verifica se o caractere é uma letra minúscula usando o método .islower()
            minusculas += 1  # Se for minúscula, adiciona 1 à variável minusculas para a contagem
        elif string.isdigit(): # Se for um digito, adiciona 1 à variável numeros para a contagem
            numeros += 1 # Se for um digito, adiciona 1 à variável numeros.
        elif not string.isdigit() and not string.isalpha(): # Se não for um numero e nem uma letra
            caracteres += 1 # Se for caractere especial, adiciona 1 à variável Cacaracteres.

    print("\n--------------------------------------\n")
    print(f"Letras maiúsculas: {maiusculas}")
    print(f"Letras minúsculas: {minusculas}")
    print("\n--------------- EXTRAS ---------------\n")
    print(f"Números: {numeros}") 
    print(f"Caracteres especiais: {caracteres}")
    print("\n--------------------------------------\n")


while True:
    nome = input("Qual o seu nome?:").strip().capitalize()
    if nome.isalpha(): # Verifica se a string recebida possui apenas letras.
        break # Caso sim, ela continua o código.
    else: # Do contrário, retornará uma mensagem e pedirá novamente o nome do usuário.
        print("\nPor favor, digite apenas letras (sem números ou símbolos ou espaços).\n")
        continue

def inicio():  # Cria o menu principal
    while True:
        print("\n--------------------------------------")
        print(f"Olá {nome}, tudo bem? Qual função você deseja testar?")
        escolha = input("\n1 - Soma de dígitos em texto\n2 - Contar Maiúsculas e Minúsculas\n3 - Jogo da aleatoriedade\n\n--------------------------------------\n")

        if escolha == "1":
            while True:  # Permite repetir a função 1 sem voltar ao menu
                texto = input("Digite um texto: ")  # Recebe a informação do usuário
                resultado, digitos = soma_digitos(texto)  # Chama a função e recebe a soma e os dígitos encontrados
                print("\n--------------------------------------\n")
                print(f"Digitos encontrados: {', '.join(digitos)}")  # O "','.join" separa os dígitos com vírgula
                print(f"Soma dos dígitos: {resultado}")  # Exibe a soma
                print("\n--------------------------------------\n")

                # Pergunta se o usuário quer repetir ou voltar ao menu
                continuar = input("\nPressione ENTER para se manter nessa função, ou digite 'VOLTAR' para voltar ao menu principal:\n").strip().capitalize()
                if continuar == "":
                    continue  # repete a escolha 1
                elif continuar.lower() == "voltar":
                    break  # volta para o menu
                else:
                    print("\nVocê não escolheu uma opção válida\n")

        elif escolha == "2":
            while True:
                entrada = input("Digite um texto: ") # Recebe a informação do usuário para a funão contar_maiusculas_minusculas(texto)
                contar_maiusculas_minusculas(entrada) # Retorna as informações armazenadas no (texto) 

                # Pergunta se o usuário quer repetir ou voltar ao menu
                continuar = input("\nPressione ENTER para se manter nessa função, ou digite 'VOLTAR' para voltar ao menu principal:\n").strip().capitalize()
                if continuar == "":
                    continue  # Repete a escolha 2
                elif continuar.lower() == "voltar":
                    break  # volta para o menu
                else:
                    print("\nVocê não escolheu uma opção válida\n")

        elif escolha == "3":
            jogo_adivinhacao() # Leva até a função adivinhacao
            break # Sai do loop

        else:
            print("Você não escolheu uma opção válida (1/2/3), tente novamente!")  # Validação de opção
            continue # Retorna para o Loop


def jogo_adivinhacao():
    numero_secreto = random.randint(0, 10) # Usa a biblioteca random e define que os números randomicos só podem ir de 0 - 10 e salva na variável numero_secreto
    try: # Avalia o bloco de comando abaixo para ver se encontra algum erro.
        aposta = float(input("Digite o valor da sua aposta em reais: R$ ").replace(",", ".")) # Recebe um valor float da aposta e transforma todas as virgulas em pontos e armazena em aposta.
        if aposta < 1:
            print("\nVocê não pode deixar de fazer apostas, ou apostar números negativos, tente novamente!\n")
            jogo_adivinhacao()

        palpite = int(input("Tente adivinhar o número (de 0 a 10): ")) # Recebe o valor inteiro da aposta (0 a 10) e armazena em palpite
        if palpite > 10 or palpite < 0:
            print("\nVocê deve colocar um número válido para fazer seu palpite de 0 à 10.\n")
            jogo_adivinhacao()

    except ValueError: # Se comunica com o try, caso o ValueError seja identificado (por colocar uma string em vez de número) ele executará o else, e retornará para o loop da função.
        print("\nEntrada inválida! Use números válidos.\n")
        jogo_adivinhacao()

    print(f"Número sorteado: {numero_secreto}") # Mostra o número que foi sorteado pela biblioteca random.
    
    if palpite == numero_secreto:  # Se o número que o usuário digitou (palpite) for igual ao número secreto sorteado...
        premio = aposta * 2  # O prêmio será o dobro do valor apostado.
        print(f"Parabéns! Você acertou! Prêmio: R$ {premio:.2f}")  # Exibe uma mensagem de acerto com o valor do prêmio formatado com 2 casas decimais.

    elif abs(palpite - numero_secreto) == 1:  # Se a diferença entre o palpite e o número secreto for exatamente 1 (ou seja, o usuário errou por 1 número)...
    # O abs remove o sinal antes do número, então se o palpite - o numero sorteado for igual a 1
        premio = aposta * 1.5  # O prêmio será 1.5 vezes o valor apostado (50% a mais).
        print(f"Quase lá! Você errou por 1. Prêmio: R$ {premio:.2f}")  # Exibe uma mensagem de quase acerto com o valor do prêmio.

    else:  # Se o usuário errar o número e a diferença for maior que 1...
        print("Você errou. Não ganhou nada!")  # Exibe mensagem informando que não houve prêmio.

    while True:
        continuar = input("\nPressione ENTER para se manter nessa função, ou digite 'VOLTAR' para voltar ao menu principal:\n").strip().capitalize()
        if continuar == "":
            jogo_adivinhacao()
        elif continuar.lower() == "voltar":
            inicio()
            break  # volta para o menu
        else:
            print("\nVocê não escolheu uma opção válida\n")
            continue

inicio()  # Inicia o programa
