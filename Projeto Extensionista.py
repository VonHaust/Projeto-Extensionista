#Projeto para a Atividade Extensionista 2
#Author: Marcella Portela
#RU: 3886739

print("Bem vindo à Biblioteca!")
SECAO = input("\nInforme o dígito da SEÇÃO que deseja acessar (Seções disponíveis abaixo):\n"
                  "1 - Infantil\n"
                  "2 - Juvenil (Jovem-Adulto)\n"
                  "3 - Estrangeira\n"
                  "4 - Acadêmica\n"
                  "5 - Referência\n"
                  "6 - Braille\n"     
                  ">>") #Recebe a seção informada pelo usuário

SECAO = int(SECAO) #A variável "SECAO" é convertida para int afim da comparação com os ifs.

if (SECAO == 1):
    print("Para se dirigir à seção escolhida siga as seguintes orientações:\n"
          "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a primeira fileira horizontal de livros com a estante intitulada 'Acadêmica - Tecnologia'.\n" 
          "Após esse passo, vire à sua esquerda e siga em frente até visualizar a placa 'Infantil' que representa a seção desejada.")
elif (SECAO == 2):
    GENERO = input("A seção escolhida é dividida entre gêneros. Para sua conveniência, por favor informe o dígito do GÊNERO que deseja acessar (Gêneros disponíveis abaixo):\n"
    "1 - Juvenil: Ficção\n"
    "2 - Juvenil: Romance\n"
    "3 - Juvenil: Terror\n"
    ">>") #Recebe o gênero informado pelo usuário.

    GENERO = int(GENERO)  # A variável "GENERO" é convertida para int afim da comparação com os ifs.

    if (GENERO == 1):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a terceira fileira horizontal de estantes.\n" 
              "Pare em frente à estante intitulada 'Juvenil - Romance', vire à sua esquerda e a próxima estante em vista representa o destino desejado.")
    elif (GENERO == 2):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a terceira fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Juvenil - Romance', a qual representa o destino desejado.")
    elif (GENERO == 3):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a terceira fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Juvenil - Romance', vire à sua esquerda e ande até a segunda estante em vista, a qual representa o destino desejado.")
elif (SECAO == 3):
    GENERO = input("A seção escolhida é dividida entre gêneros. Para sua conveniência, por favor informe o dígito do GÊNERO que deseja acessar (Gêneros disponíveis abaixo):\n"
    "1 - Estrangeira: Ficção\n"
    "2 - Estrangeira: Romance\n"
    "3 - Estrangeira: Terror\n"
    ">>") #Recebe o gênero informada pelo usuário

    GENERO = int(GENERO)  # A variável "GENERO" é convertida para int afim da comparação com os ifs.

    if (GENERO == 1):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a terceira fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Juvenil - Romance', vire à sua direita e ande até a segunda estante em vista, a qual representa o destino desejado.")
    elif (GENERO == 2):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a terceira fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Juvenil - Romance', vire à sua direita e a próxima estante em vista representa o destino desejado.")
    elif (GENERO == 3):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a terceira fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Juvenil - Romance', vire à sua direita e ande até a terceira estante em vista, a qual representa o destino desejado.")
elif (SECAO == 4):
    GENERO = input("A seção escolhida é dividida entre gêneros. Para sua conveniência, por favor informe o dígito do GÊNERO que deseja acessar (Gêneros disponíveis abaixo):\n"
        "1 - Acadêmica: Política\n"
        "2 - Acadêmica: Tecnologia\n"
        "3 - Acadêmica: História\n"
        ">>") #Recebe o gênero informada pelo usuário

    GENERO = int(GENERO)  # A variável "GENERO" é convertida para int afim da comparação com os ifs.

    if (GENERO == 1):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a primeira fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Acadêmica - Tecnologia', vire à sua direita e a próxima estante em vista representa o destino desejado.")
    elif (GENERO == 2):
          print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
                "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a primeira fileira horizontal de estantes.\n"
                "Pare em frente à estante intitulada 'Acadêmica - Tecnologia', a qual representa o destino desejado.")
    elif (GENERO == 3):
          print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
                "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a primeira fileira horizontal de estantes.\n"
                "Pare em frente à estante intitulada 'Acadêmica - Tecnologia', vire à sua esquerda e a próxima estante em vista representa o destino desejado.")
elif (SECAO == 5):
    GENERO = input("A seção escolhida é dividida entre gêneros. Para sua conveniência, por favor informe o dígito do GÊNERO que deseja acessar (Gêneros disponíveis abaixo):\n"
        "1 - Referência: Monografias\n"
        "2 - Referência: Dicionários\n"
        "3 - Referência: Teses\n"
        ">>")  # Recebe o gênero informada pelo usuário

    GENERO = int(GENERO)  # A variável "GENERO" é convertida para int afim da comparação com os ifs.

    if (GENERO == 1):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a segunda fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Referência - Dicionários', vire à sua direita e a próxima estante em vista representa o destino desejado.")
    elif (GENERO == 2):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a segunda fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Referência - Dicionários', a qual representa o destino desejado.")
    elif (GENERO == 3):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a segunda fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Referência - Dicionários', vire à sua esquerda e a próxima estante em vista representa o destino desejado.")
elif (SECAO == 6):
    GENERO = input("A seção escolhida é dividida entre gêneros. Para sua conveniência, por favor informe o dígito do GÊNERO que deseja acessar (Gêneros disponíveis abaixo):\n"
        "1 - Braille: Infantil\n"
        "2 - Braille: Dicionários\n"
        "3 - Braille: Romance\n"
        ">>")  # Recebe o gênero informada pelo usuário

    GENERO = int(GENERO)  # A variável "GENERO" é convertida para int afim da comparação com os ifs.

    if (GENERO == 1):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a última fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Braille - Dicionários', vire à sua direita e a próxima estante em vista representa o destino desejado.")
    elif (GENERO == 2):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a última  fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Braille - Dicionários', a qual representa o destino desejado.")
    elif (GENERO == 3):
        print("Para se dirigir ao gênero escolhido siga as seguintes orientações:\n"
              "Estando de frente para o presente computador, vire à sua direita e siga em linha reta até a última fileira horizontal de estantes.\n"
              "Pare em frente à estante intitulada 'Braille - Dicionários', vire à sua esquerda e a próxima estante em vista representa o destino desejado.")