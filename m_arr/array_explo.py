

class explot(object):
    def __init__(self, datuak, string):
      self.datuak = datuak
      self.string = string

    def arry(self):
        self.datuak += ","
        luzehera = len(self.datuak)
        cont = []
        lotura = ""
        for x in range(luzehera):
          letrak = self.datuak[x]
          if letrak == ",":
             cont.append(lotura)
             lotura = ""
          else: 
             lotura += letrak
        return cont


datuak = "kaixo , ixo , muturra"
#string = input("karakterea:")
#emaitza =  explot(datuak,string)
#print(emaitza.datuak,emaitza.string)
#print(len(datuak))
#print(emaitza.arry())
def kaixo():
  return(kaixo)
  