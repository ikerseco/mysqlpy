

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

    def search(self,array,hitza):
      print(array)
      #print(hitza)
      lotura = ""
      for x in range(len(array)):
        for t in range(len(array[x])):
          lotura += array[x][t]
          if lotura == hitza:
           print(array[x])
           lotura = ""
          else:
            if len(lotura) == len(hitza):
             lotura = ""
          if array[x][t] == " ":
             lotura = ""


print("kaixo")
datuak = "kaixo ta ixo ,ixo gaur mendira noa eguna pasatxera,ixo muturra"
string = input("karakterea:")
emaitza =  explot(datuak,string)
array = emaitza.arry()
emaitza.search(array,"ixo")


