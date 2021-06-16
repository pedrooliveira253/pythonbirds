class Pessoa:
    def __init__(self, nome = None, idade=35):
        self.idade = idade
        self.nome= nome

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    p = Pessoa('Luciano')
    print (Pessoa.comprimentar(p))
    print(id(p))
    print (p.comprimentar())
    print(p.nome)
    p.nome= 'Pedro'
    print(p.nome)
    print(p.idade)