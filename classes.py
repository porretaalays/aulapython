from random import randint

NAIPES = ('Paus','Copas','Espadas','Ouros')
RANKS = ('As',1)
( 'Dois',2)
( 'Tres',3)
( 'Quatro',4)
('Cinco',5)
('Seis',6)
('Sete',7)
('Oito',8)
('Nove',9)
('Dez',10)
('Valete',10)
('Dama',10)
('Rei',10)
class Carta():
    def __init__(self, naipe, rank, valor):
        self.naipe = naipe
        self.rank = rank
        self.valor = valor

    def __str__(self):
        return f'{self.rank} de {self.naipe}  [{self.valor}] '

class Baralho():
    def __init__(self):
        self.cartas = []
        for naipe in NAIPES:
            for rank in RANKS:
                carta = Carta(naipe, rank[0], rank[1])
                self.adicionar_cartas(carta)

    def __str__(self):
        if len(self.cartas) == 0:
            return'[VAZIO]'

        string = ''
         
        for carta in self.cartas:
            string +=str(carta)
            string += ','
            
        return string

    def adicionar_cartas(self,carta):
        self.cartas.append(carta)

    def remover_carta(self):
       return self.cartas.pop(0)

    def sortear(self):
     numero_sorteado = randint(0,len(self.cartas) -1 )
     return self.cartas.pop(numero_sorteado)
# class Jogo21():
#     def __init__():
#         baralho = Baralho()
#         carta1 = baralho.sortear()
#         carta2 = baralho.sortear()
#         self.pontuacao = carta1.pontuacao + carta2.pontuacao






        