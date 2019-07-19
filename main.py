from classes import Carta, Baralho


carta1 = Carta('Paus','As',1)
carta2 = Carta('Copas','Rei',10)
carta3 = Carta('Espadas', 'Cinco',5)
baralho = Baralho()

baralho.adicionar_cartas(carta1)
baralho.adicionar_cartas(carta2)
baralho.adicionar_cartas(carta3)
baralho.remover_carta()

print(baralho.remover_carta())

