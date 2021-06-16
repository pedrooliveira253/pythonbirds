class Pessoa:
    def __init__(self, *filhos,  nome = None, idade=35):
        self.idade = idade
        self.nome= nome
        self.filhos= list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

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
    del luciano.filhos
    print (luciano.__dict__)
    print(pedro.__dict__)


