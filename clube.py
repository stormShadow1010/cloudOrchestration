class Clube():
    def __init__(self, nome, jogos=0, pts=0, vit=0, emp=0, der=0, gp=0, gc=0, sg=0):
        self.nome = nome
        self.jogos = jogos
        self.pts = pts
        self.vit = vit
        self.emp = emp
        self.der = der
        self.gp = gp
        self.gc = gc
        self.sg = sg
    
    def ganhou(self):
        self.vit += 1
        self.pts += 3
    
    def empatou(self):
        self.emp += 1
        self.pts += 1

    def perdeu(self):
        self.der += 1

    def estatisticas(self):
        print(self.nome, " ", 
              "J: ", self.jogos, " " ,
              "P: ", self.pts, " " ,
              "V: ", self.vit, " " ,
              "E: ", self.emp, " " ,
              "D: ", self.der, " " ,
              "GP: ", self.gp, " " ,
              "GC: ", self.gc, " " ,
              "SG: ", self.sg
            )
    