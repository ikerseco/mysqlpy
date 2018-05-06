import os





class read(object):
    def __init__(self, fitxategia,url,tabla,zutabeak):
        self.fitxategia = fitxategia
        self.url = url
        self.tabla = tabla
        self.zutabeak = zutabeak
    
    def val(self):
        os.chdir(self.url)
        fichategia = open(self.fitxategia,'rt')
        ""#"insert into "+t_izena +" (" + datuak + ") values " + value + ";"
        value = "("+self.tabla+") values "
        ar = fichategia.readlines()
        for k in range(len(ar)):
            if k != 0:
                 value += "(" + ar[k].rstrip('\n')+ "),"
        return value[:-1]
        

    def idatzi(self):
         os.chdir(self.url)
         fi = self.fitxategia
         fichategia = open(fi,'wt')
         fichategia.write(self.tabla + "\n")
         if self.zutabeak != []:
             for x in range(len(self.zutabeak)):
                 fichategia.write(self.zutabeak[x] + "\n")
         fichategia.close()
    


#reads = read("inser.txt","D:\gitpro\mysqlpy\inser_t")
#r = read.val()


#os.chdir("D:\gitpro\mysqlpy\inser_t")
#fichategial = open("inser.od.csv",'rt')
#irakurri =  fichategial.read()
#print(irakurri)
