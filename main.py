import os

def primeira_linha():
    os.system('cls')
    try:
        numero_x = input("Digite a primeira incógnita de X: ")
        numero_y = input("Digite a primeira incógnita de y: ")
        operador = input("Digite o operador da primeira linha (+, -): ")
        resultado_primeira_linha = int(input('Digite o resultado da primeira linha: '))

        if operador != '+' and '-':
            print("Operador inválido. Use +, -, * ou /.")
            os.system('cls')

        valor_x = numero_x.replace('x', "").replace('X', "")
        valor_x = int(valor_x)
        valor_y = numero_y.replace('y', "").replace('Y', "").replace("-", "")
        valor_y = int(valor_y)

        numero_x_2 = input("Digite a segunda incógnita de X: ")
        numero_y_2 = input("Digite a segunda incógnita de y: ")
        operador_2 = input("Digite o operador da segunda linha (+, -): ")
        resultado_segunda_linha = int(input('Digite o resultado da segunda linha: '))

        if operador_2 != '+' and '-':
            print("Operador inválido. Use +, -, * ou /.")
            os.system('cls')

        valor_x_2 = numero_x_2.replace('x', "").replace('X', "")
        valor_x_2 = int(valor_x_2)
        valor_y_2 = numero_y_2.replace('y', "").replace('Y', "").replace('-', "")
        valor_y_2 = int(valor_y_2)

        if operador == "+" and operador_2 == "+":
            valor_x_diferente = valor_x * valor_y_2
            valor_y_diferente = valor_y * valor_y_2
            resultado_primeira_linha_diferente = resultado_primeira_linha * valor_y_2
            valor_x_2_diferente = (valor_x_2 * valor_y) * -1
            valor_y_2 = (valor_y_2 * valor_y) * -1
            resultado_segunda_linha_diferente = (resultado_segunda_linha * valor_y) * -1

            valor_x_total = valor_x_diferente + valor_x_2_diferente
            valor_resultado_total = resultado_primeira_linha_diferente + resultado_segunda_linha_diferente
            valor_do_x = valor_resultado_total / valor_x_total

            if valor_x_2 > 0:
                valor_do_y = resultado_segunda_linha_diferente - valor_x_2_diferente * valor_do_x
                if valor_do_y < 0 and operador_2 == '-':
                    valor_do_y = abs(valor_do_y)
            else:
                valor_do_y = resultado_segunda_linha + valor_x_2 * valor_do_x
            valor_do_y = valor_do_y / valor_y_2
            print('O valor de X é', valor_do_x, 'e o valor de Y é', valor_do_y)
            
        
        elif valor_y == valor_y_2:
            valor_x_total = valor_x + valor_x_2
            valor_resultado_total = resultado_primeira_linha + resultado_segunda_linha
            valor_do_x = valor_resultado_total / valor_x_total
            if valor_x_2 > 0:
                valor_do_y = resultado_segunda_linha - valor_x_2 * valor_do_x
                if valor_do_y < 0 and operador_2 == '-':
                    valor_do_y = abs(valor_do_y)
            else:
                valor_do_y = resultado_segunda_linha + valor_x_2 * valor_do_x
            valor_do_y = valor_do_y / valor_y_2
            print('O valor de X é', valor_do_x, 'e o valor de Y é', valor_do_y)
        elif valor_y != valor_y_2:
            valor_x_diferente = valor_x * valor_y_2
            valor_y_diferente = valor_y * valor_y_2
            resultado_primeira_linha_diferente = resultado_primeira_linha * valor_y_2
            valor_x_2_diferente = valor_x_2 * valor_y
            valor_y_2 = valor_y_2 * valor_y
            resultado_segunda_linha_diferente = resultado_segunda_linha * valor_y

            valor_x_total = valor_x_diferente + valor_x_2_diferente
            valor_resultado_total = resultado_primeira_linha_diferente + resultado_segunda_linha_diferente
            valor_do_x = valor_resultado_total / valor_x_total

            if valor_x_2 > 0:
                valor_do_y = resultado_segunda_linha_diferente - valor_x_2_diferente * valor_do_x
                if valor_do_y < 0 and operador_2 == '-':
                    valor_do_y = abs(valor_do_y)
            else:
                valor_do_y = resultado_segunda_linha + valor_x_2 * valor_do_x
            valor_do_y = valor_do_y / valor_y_2
            print('O valor de X é', valor_do_x, 'e o valor de Y é', valor_do_y) 


    except ValueError:
        print("Por favor, insira números válidos.")


primeira_linha()