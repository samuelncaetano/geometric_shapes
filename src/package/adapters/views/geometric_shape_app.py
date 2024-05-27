# pylint: disable = R1723, E1111, E1101
from src.package.adapters.controllers.geometric_shape_controller import GeometricShapeController
from src.package.adapters.views.geometric_shape_view import GeometricShapeView
from src.package.domain import Point, Triangle


class GeometricShapeApp:
    def __init__(self, repository):
        self.__controller = GeometricShapeController(repository)
        self.__view = GeometricShapeView()
        self.__view.limpar_tela()

    def run(self):
        while True:
            self.__view.mostrar_menu()
            opcao = self.__view.ler_opcao()
            self.__view.limpar_tela()
            self.__controller.listar_formas_geometricas()

            if opcao == "1":
                self.__handle_adicionar_forma()
            elif opcao == "2":
                self.__handle_metodos_forma()
            elif opcao == "0":
                print("Encerrando o programa.")
                break

    def __handle_adicionar_forma(self):
        while True:
            self.__view.mostrar_menu_formas()
            opcao_forma = self.__view.ler_opcao()
            self.__view.limpar_tela()

            if opcao_forma == "":
                self.__controller.listar_formas_geometricas()
            elif opcao_forma == "1":
                self.__adicionar_forma(self.__controller.adicionar_ponto)
            elif opcao_forma == "2":
                self.__adicionar_forma(self.__controller.adicionar_segmento_de_reta)
            elif opcao_forma == "3":
                self.__adicionar_forma(self.__controller.adicionar_circulo)
            elif opcao_forma == "4":
                self.__adicionar_forma(self.__controller.adicionar_retangulo)
            elif opcao_forma == "5":
                forma_adicionada = self.__adicionar_forma(
                    self.__controller.adicionar_triangulo
                )
                if not isinstance(forma_adicionada, Triangle):
                    print("Erro: a forma adicionada não é um triângulo.")
            elif opcao_forma == "0":
                self.__controller.listar_formas_geometricas()
                break

    def __adicionar_forma(self, func_adicionar):
        try:
            func_adicionar()
        except ValueError as e:
            print("Erro ao adicionar forma geométrica:", e)
        self.__view.limpar_tela()
        self.__controller.listar_formas_geometricas()

    def __handle_metodos_forma(self):
        while True:
            self.__view.mostrar_menu_metodos()
            opcao_metodo = self.__view.ler_opcao()
            self.__view.limpar_tela()

            if opcao_metodo == "":
                self.__controller.listar_formas_geometricas()
            elif opcao_metodo == "1":
                self.__calcular_e_mostrar(self.__controller.calcular_area, "Área")
            elif opcao_metodo == "2":
                self.__calcular_e_mostrar(
                    self.__controller.calcular_perimetro, "Perímetro"
                )
            elif opcao_metodo == "3":
                self.__calcular_e_mostrar(self.__controller.distancia_origem, "Origem")
            elif opcao_metodo == "4":
                self.__calcular_e_mostrar_distancia_pontos()
            elif opcao_metodo == "5":
                self.__calcular_e_mostrar_contem_ponto()
            elif opcao_metodo == "6":
                self.__mover_forma()
                self.__view.limpar_tela()
                self.__controller.listar_formas_geometricas()
            elif opcao_metodo == "0":
                self.__controller.listar_formas_geometricas()
                break

    def __calcular_e_mostrar(self, func_calcular, label):
        self.__controller.listar_formas_geometricas()
        try:
            index = self.__view.obter_indice_forma_geometrica()
            resultado = func_calcular(index)
        except ValueError as e:
            print("Erro ao calcular:", e)
            return
        self.__view.mostrar_resultado(resultado, label)

    def __calcular_e_mostrar_distancia_pontos(self):
        self.__controller.listar_formas_geometricas()
        try:
            index = self.__view.obter_indice_forma_geometrica()
            ponto = Point.criar_ponto()
            distancia_pontos = self.__controller.distancia_pontos(index, ponto)
        except ValueError as e:
            print("Erro ao verificar se contém ponto:", e)
            return
        self.__view.mostrar_resultado(
            distancia_pontos, "Distancia entre o ponto e a forma geométrica"
        )

    def __calcular_e_mostrar_contem_ponto(self):
        self.__controller.listar_formas_geometricas()
        try:
            index = self.__view.obter_indice_forma_geometrica()
            ponto = Point.criar_ponto()
            contem_ponto = self.__controller.contem_ponto(index, ponto)
        except ValueError as e:
            print("Erro ao verificar se contém ponto:", e)
            return
        self.__view.mostrar_resultado(contem_ponto, "Contém Ponto")

    def __mover_forma(self):
        self.__controller.listar_formas_geometricas()
        try:
            index = self.__view.obter_indice_forma_geometrica()
        except ValueError as e:
            print("Erro ao obter índice da forma geométrica:", e)
            return

        while True:
            self.__view.mostrar_mover()
            opcao_metodo = self.__view.ler_opcao()
            self.__view.limpar_tela()

            if opcao_metodo == "1":
                self.__mover_formas(index)
                break
            elif opcao_metodo == "2":
                self.__mover_segmento_de_reta(index)
                break

    def __mover_segmento_de_reta(self, index):
        try:
            novo_ponto1 = Point.criar_ponto()
            novo_ponto2 = Point.criar_ponto()
        except ValueError as e:
            print("Erro ao adicionar ponto:", e)
            return
        self.__controller.mover_segmento_de_reta(index, novo_ponto1, novo_ponto2)

    def __mover_formas(self, index):
        try:
            novo_ponto = Point.criar_ponto()
        except ValueError as e:
            print("Erro ao adicionar ponto:", e)
            return
        self.__controller.mover_formas(index, novo_ponto)
