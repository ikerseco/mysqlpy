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
        irakurri =  fichategia.read()
        return irakurri
    def idatzi(self):
         os.chdir(self.url)
         print(self.fitxategia)
         fi = self.fitxategia
         fichategia = open(fi,'wt')
         fichategia.write(self.tabla + "\n")
         if self.zutabeak != []:
             for x in range(len(self.zutabeak)):
                 fichategia.write(self.zutabeak[x] + "\n")
         print(len(self.zutabeak))
         fichategia.close()
    


#reads = read("inser.txt","D:\gitpro\mysqlpy\inser_t")
#r = read.val()


#os.chdir("D:\gitpro\mysqlpy\inser_t")
#fichategial = open("inser.od.csv",'rt')
#irakurri =  fichategial.read()
#print(irakurri)


