import time
escolha=True
while escolha:
    print("\n")
    print("   Funções")
    print("""
    1. Tipos de Funções 
    0. Exit/Quit/Saída
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        figura = input("Digite o nome de uma função matemática: ").lower()
        if figura == "primeiro grau":
            print("\n\tFunção de 1ºGrau:\n\t")
            print("\n\tDescrição: \n\t"
                  "\n\tUma função de 1º grau é uma relação matemática,onde a e b são constantes.\n\t"
                  "\n\tSeu gráfico é sempre uma reta, e o valor de a indica a inclinação dela.\n\t")
            time.sleep(2)
            print("\n\tFormúla:\n\t"
                  "\n\tf(x) = ax + b\n\t\n\t"
                  " \n\ta e b são números reais (constantes).\n\t"
                  "\n\tx é a variável.")
            
            time.sleep(2)
        elif figura == "segundo grau" or figura == "segundo grau" or figura == "segundo grau":
            print("Função de 2ºGrau:\n\t")
            print("Descrição: \n\t\n\t"
                  "\n\tUma função de segundo grau, também chamada de função quadrática,\n\t"
                  
                  "\n\tO gráfico de uma função de segundo grau é uma parábola:\n\t"
                        "\n\t\n\tSe a > 0, a parábola é voltada para cima (sorri 😊 ).\n\t"
                        "\n\t\n\tSe a < 0, a parábola é voltada para baixo (triste ☹️ ).")
            time.sleep(2)
            print("Fórmula\n\t\n\t"
                  "f(x)=ax²-bx+c:\n\t"
                  "\n\ta,b e c são númeroos reais (constantes).\n\t"
                  "\n\ta =! 0 (ou seja, o coeficiente de x² não pode ser zero),\n\t"
                  "\n\tx é a variável.\n\t")
            time.sleep(2)
            print("\nCalcular Vétice :\n\t"
                  "\n\tE o ponto mais alto ou mais baixo da parábola ( depende do sinal de a). A codernada x do vértice é dada por:\n\t"
                  "\n\tX do vértice = -b / (2 * a).\n\t\n\t"
            "\n\tE o valor de y no vértice é:\n\t\n\t"
                  "y do vértice = f(x do vértice)")
            time.sleep(2)
            print("\n\tPara calcular raizes:\n\t"
                  "São valores dee x para os quais f(x) = 0."
                  "Para encontralos, usamos a fórmula de Bhaskara:\n\t\n\t"
                  "\n\t\n\tDelta:\n\t"
                  "Delta = b²-4ac\n\t"
                  "\n\t\n\tBhaskara:\n\t"
                  "x = (-b ± √(b² - 4ac)) / 2a")
                  












        else:
            print("Figura não reconhecida. Tente novamente.")

    elif escolha=="0":
      print("\n Adeus")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")

