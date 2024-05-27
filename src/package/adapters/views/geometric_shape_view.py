import os


class GeometricShapeView:
    @staticmethod
    def mostrar_menu():
        print("\n### Menu ###")
        print("1. Adicionar Forma")
        print("2. Usar os Métodos das formas")
        print("0. Sair")

    @staticmethod
    def mostrar_menu_formas():
        print("\n### Menu ###")
        print("1. Adicionar Ponto")
        print("2. Adicionar Segmento de Reta")
        print("3. Adicionar Círculo")
        print("4. Adicionar Retângulo")
        print("5. Adicionar Triângulo")
        print("0. Retorna ao menu principal")

    @staticmethod
    def mostrar_menu_metodos():
        print("\n### Menu ###")
        print("1. Calcular a área da forma geométrica")
        print("2. Calcular o perímetro da forma geométrica")
        print("3. Calcular a distancia entre a forma geométrica e a origem")
        print("4. Calcular a distancia entre a forma geométrica e a um ponto")
        print("5. Contem ponto na forma geométrica")
        print("6. Mover forma geométrica")
        print("0. Retorna ao menu principal")

    @staticmethod
    def mostrar_mover():
        print("\n### Menu ###")
        print("1. Não e um seguimento de reta")
        print("2. E um seguimento de reta")

    @staticmethod
    def ler_opcao():
        return input("Escolha uma opção: ")

    @staticmethod
    def limpar_tela():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def obter_indice_forma_geometrica():
        print("\n### Menu ###")
        return int(input("Digite o índice da forma geométrica: ")) - 1

    @staticmethod
    def mostrar_resultado(resultado, mensagem):
        if resultado is not None:
            print(f"{mensagem}: {resultado}")
