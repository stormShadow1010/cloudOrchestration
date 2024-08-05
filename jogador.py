from clube import Clube

class Jogador():
    def __init__(self, nome, num, pos, clube=Clube(" ")):
        self.nome = nome
        self.num = num
        self.pos = pos
        self.clube = clube
    
    def transferir(self, num, clube=Clube(" ")):
        self.num = num
        self.clube = clube
    
    def gol(self, clube=Clube(" ")):
        if clube != self.clube:
            print(f'{clube.nome}: Gol contra de {self.nome}')
            return

        print(f'{clube.nome}: Gol de {self.nome}')
        
    
