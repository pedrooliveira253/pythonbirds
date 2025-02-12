class Pessoa:
    olhos=2

    def __init__(self, *filhos,  nome = None, idade=35):
        self.idade = idade
        self.nome= nome
        self.filhos= list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls}- olhos{cls.olhos}'

if __name__=='__main__':
    pedro = Pessoa(nome='Pedro')
    luciano = Pessoa(pedro, nome='Luciano')
    print (Pessoa.comprimentar(luciano))
    print(id(luciano))
    print (luciano.comprimentar())
    print (luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome= 'Ramalho'
    luciano.olhos=1
    del luciano.olhos
    del luciano.filhos
    print (luciano.__dict__)
    print(pedro.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(pedro.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(pedro.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_class(), luciano.nome_e_atributos_de_class())




