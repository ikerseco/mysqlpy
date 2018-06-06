

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
      #print(hitza)
      cont = []
      lotura = ""
      for x in range(len(array)):
        for t in range(len(array[x])):
          lotura += array[x][t]
          if lotura == hitza:
           lotura = ""
           cont.append(x)
          else:
            if len(lotura) == len(hitza):
             lotura = ""
          if array[x][t] == " ":
             lotura = ""
      return cont




class implot(object):
  def __init__(self, array, string):
    self.array = array
    self.string = string
  
  def mount(self,dat):
   data = ""
   datC = []
   d = ""
   for t in range(len(dat)):
     if dat[t] != ":":
       d += dat[t]
     if dat[t] == ":" or t == len(dat) -1:
       datC.append(d)
       d = ""
   for x in range(len(self.array)):
      data += datC[0] + str(self.array[x])  + datC[1] + self.string
      #print(self.array[x] , self.string)
   return data[:-1]
#array = [1,2,3,4,5]
#string = ","
#implot = implot(array,string)
#mount = implot.mount("':'")
#print("kaixo")
#datuak = "kaixo ta ixo ,ixo gaur mendira noa eguna pasatxera,ixo muturra"
#string = input("karakterea:")
#emaitza =  explot(datuak,",")
#array = emaitza.arry()
#print(emaitza.search(array,"muturra"))




