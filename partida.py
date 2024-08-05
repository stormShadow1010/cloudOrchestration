from clube import Clube
from jogador import Jogador

class Partida():
    def __init__(self, rodada, casa=Clube(" "), fora=Clube(" "), estadio=" ", golCasa=0, golFora=0):
        self.rodada = rodada
        self.casa = casa
        self.fora = fora
        self.estadio = estadio
        self.golCasa = golCasa
        self.golFora = golFora

    def golC(self, jogador=Jogador(" ", 0, " ", Clube(" "))):
        jogador.gol(self.casa)
        self.golCasa += 1
        self.casa.gp += 1
        self.fora.gc += 1
        self.casa.sg += 1
        self.fora.sg -= 1

    def golF(self, jogador=Jogador(" ", 0, " ", Clube(" "))):
        jogador.gol(self.fora)
        self.golFora += 1
        self.casa.gc += 1
        self.fora.gp += 1
        self.casa.sg -= 1
        self.fora.sg += 1
    
    def atualizaVED(self):
        if(self.golCasa > self.golFora):
            self.casa.ganhou()
            self.fora.perdeu()
        
        if(self.golCasa < self.golFora):
            self.casa.perdeu()
            self.fora.ganhou()

        if(self.golCasa == self.golFora):
            self.casa.empatou()
            self.fora.empatou()
    
    def placar(self):
        print(self.casa.nome, " ", self.golCasa, " x " , self.golFora, " ",self.fora.nome)
    
    def fimdeJogo(self):
        self.casa.jogos += 1
        self.fora.jogos += 1
        self.atualizaVED()
        
