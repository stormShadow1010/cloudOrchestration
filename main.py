from clube import Clube
from partida import Partida
from jogador import Jogador

fla = Clube("Flamengo")
vas = Clube("Vasco")
flu = Clube("Fluminense")
bot = Clube("Botafogo")

j1 = Jogador("Gabi", 10, "Atacante", fla)
j2 = Jogador("Puma", 21, "Lateral", vas)
j3 = Jogador("Arrascaeta", 14, "Meia", fla)
j4 = Jogador("Capasso", 2, "Zagueiro", vas)
j5 = Jogador("Tiquinho", 9, "Atacante", bot)
j6 = Jogador("Ganso", 10, "Meia", flu)
j7 = Jogador("Joel Carli", 2, "Zagueiro", bot)
j8 = Jogador("Arias", 22, "Atacante", flu)

r1 = Partida(1, fla, vas, "Maracana")
r2 = Partida(1, bot, flu, "Nilton Santos")

r1.golC(j1)
r1.golC(j1)
r2.golC(j5)
r1.golC(j3)
r2.golC(j5)
r2.golF(j6)
r1.golC(j4)
r1.golF(j2)

r1.placar()
r2.placar()

r1.fimdeJogo()
r2.fimdeJogo()

fla.estatisticas()
flu.estatisticas()

        