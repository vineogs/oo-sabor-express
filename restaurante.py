class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    def listar_restaurantes():
        print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Pizza')

Restaurante.listar_restaurantes()