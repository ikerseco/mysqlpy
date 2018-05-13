import pymysql.cursors
import json
from m_arr.array_explo import explot
from inser_t.insert import read
#from inser_t.insert 
"""
print("Zure datubasera konektatzen:\n")
dbi = input("\t*jarri zure databasearen izena:")
useri = input("\t*user:")
passwordi = input("\t*password:")
hosti = input("\t*host:") 
# Connect to the database
connection = pymysql.connect(host=hosti,
                             user=useri,
                             password=passwordi,
                             db=dbi,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    # select bitarteko erantzunak
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `employees`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(len(result))
        for x in range(len(result)):
         print (result[x])
         print(result[x]['firstname'])
    #tablak ikustatu
    with connection.cursor() as cursor:
        sql = "describe employees"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(len(result))
        for x in range(len(result)):
            print(result[x])
finally:
    connection.close()
"""
class data_base(object):
    def __init__(self, user, password, db, host):
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self.conec = None

    def conexioa(self):
        connection = pymysql.connect(host = self.host,
                                     user = self.user,
                                     password = self.password,
                                     db = self.db,
                                     charset = 'utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.conec = connection

    def show_t(self):
        with self.conec.cursor() as cursor:
         sql_show = "show tables"
         cursor.execute(sql_show)
         result = cursor.fetchall()
         return result
                                     
    def describe_t(self,izena):
        with self.conec.cursor() as cursor:
            sql_co = "describe " + izena
            cursor.execute(sql_co) 
            result = cursor.fetchall()
            return result 

    def select_t(self,data):
        with self.conec.cursor() as cursor:
            sql_co = "select * from "+ data
            cursor.execute(sql_co) 
            result = cursor.fetchall()
            return result
    

    
    def create_t(self,datuak,t_izena):
        with self.conec.cursor() as cursor:
            try:
                data = "CREATE TABLE "+t_izena+" (" + datuak + ") ENGINE = InnoDB;"
                cursor.execute(data)
                return("zure tabla sortu egin da zorionak!!!")
            except ValueError:               
                return("arazo bat egon da zure tabla sortzean!!!")

    def insert_t(self,t_izena,datuak):
        #¿Realmente desea ejecutar "DELETE FROM `proba` WHERE `proba`.`id` = 1"?
        with self.conec.cursor() as cursor:
            try:
                cursor.execute()
                datd = "INSERT INTO " + t_izena + " " + datuak
                print(datd)
               # cursor.execute(data)
            except ValueError:
                print("datuak ezdira sartu")


    def dlet(self,tizena):
        with self.conec.cursor()  as cursor:
            deli = "DELETE FROM "+tizena+";"
            cursor.execute(deli)
   
    def delete_t(self,data):
        with self.conec.cursor() as cursor:
            try:
             data =  "DROP TABLE IF EXISTS " + data
             cursor.execute(data)
            except ValueError:
             print("datu basearekin arazo bat dago.")

#json
data = [{'izena':'name','Funtzioa':''},{'izena':'atributoa','Funtzioa':''},{'izena':'NUll','Funtzioa':''},{'izena':'DEFAULT','Funtzioa':''}]
#funtzioak
def atributo(izen):
    atri = [{'1':'INT','2':'VARCHAR','3':'TEXT','4':'DATE'}] 
    return atri[0][izen]

def Null(izen):
    atri = [{'1':'NULL','2':'NOT NULL'}]
    return atri[0][izen]

def defektuzko(izen):
    if izen == "1":
      di = input("PERTSONALA:")
      return di
    if izen == "2":
      return "CURRENT_TIMESTAMP"
    if izen == "3":
        return ""


#programa
print(str(2))
print("Zure datubasera konektatzen:\n")
db = input("\t*jarri zure databasearen izena:")
user = input("\t*user:")
password = input("\t*password:")
host = input("\t*host:") 
while True:
 mysql = data_base( "root","",db, "localhost")
 mysql.conexioa()
 dbs = "Tables_in_" + db 
 tabla_s = mysql.show_t()
 print("\n")
 print("Tablak")
 for x in range(len(tabla_s)):
     print("\t",x,".",tabla_s[x][dbs])
 print("\t",len(tabla_s),".tabla bat sortu")
 print("\t",len(tabla_s) + 1,".tabla bat ezabatu")
 zent = input("haukeratu tabla bat:")
 #tabla bat sortzeko gauzak
 print("\n")
 if int(zent) == len(tabla_s):
  izen_tabla = input("jarri tablaren izena:")
  kanti = input("zenbat zutabe:")
  zutabeak = ""
  pry = ""
  for x in range(int(kanti)):
     print("\n")
     print(x + 1 ,"-zutabea")
     izen_zutabea = input("-jarri zutabearen izena:")
     data[0]['Funtzioa'] = izen_zutabea
     print("\n")
     print("-Aukeratu atributo bat:")
     print("\t1.INT")
     print("\t2.VARCHAR")
     print("\t3.TEXT")
     print("\t4.DATE")
     aukerTR = input("aukera:")
     a = atributo(aukerTR)
     if aukerTR != "3" and aukerTR != "4":
         luzeheraTR = input("Atributoaren luzehera:")
         a = atributo(aukerTR) + "("+luzeheraTR+")"
     data[1]['Funtzioa'] = a
     print("\n")
     print("-Null:")
     print("\t1.BAI")
     print("\t2.EZ")
     aukerNL = input("aukera:")
     n = Null(aukerNL)
     data[2]['Funtzioa'] = n
     print("\n")
     print("-Defektuzko Datua:")
     print("\t1.PERTSONALA:")
     print("\t2.CURRENT_TIMESTAMP")
     print("\t3.ez")
     aukerDF = input("aukera:")
     if aukerDF == "1":
      d = defektuzko(aukerDF)
      print(d)
      data[3]['Funtzioa'] = "DEFAULT" + " '" + d + "'"
     if aukerDF == "2":
      d = defektuzko(aukerDF)
      data[3]['Funtzioa'] = d
     if aukerDF == "3":
      d = defektuzko(aukerDF)
      data[3]['Funtzioa'] = d
     print("\n")
     zutabeak += " " + data[0]['Funtzioa'] +" "+ data[1]['Funtzioa'] +" "+ data[2]['Funtzioa'] +" "+ data[3]['Funtzioa'] +","
     pry += "\t*"+data[0]['Funtzioa']+"\n"
  print("-Prymari key:")
  print("\t1.BAI")
  print("\t2.EZ")
  a = input("aukera:")
  if a == "1":
      print("\n")
      print("zutabeak:")
      print(pry)
      zu_name = input("zutabearen izena:")
      zutabeak += "PRIMARY KEY("+zu_name+")"
      print("\n")
      print("\t1.bai")
      print("\t2.ez")
      auto = input("auto increment:")
      if int(auto) == 1:
       explots = explot(zutabeak,",")
       array = explots.arry()
       string = ""
       search_arr = explots.search(array,zu_name)
       for j in range(len(array)):
           print(search_arr[0])
           if j == search_arr[0]:
               array[j] += "AUTO_INCREMENT"
           if j != len(array) - 1:
               string += array[j] + "," 
           if j == len(array) - 1:
               string += array[j]
       print(string)
       mysql.create_t(string,izen_tabla)
      if int(auto) == 2:
       print("ez auto")
       mysql.create_t(zutabeak,izen_tabla)
  if a == "2":
      zu_name = "none"
  print("\n")
  #print(zutabeak)
  #print(izen_tabla)

 if int(zent) == len(tabla_s) + 1:
    for x in range(len(tabla_s)):
      print("\t",x,".",tabla_s[x][dbs])
    eza = input("aukeratu zutabea:")
    mysql.delete_t(tabla_s[int(eza)][dbs])
    print(tabla_s[int(eza)][dbs])
 else:
 # mysql = data_base( "cine","Art&co#2009",db, "works.artycomultimedia.com")
  print("ze nahi duzu?")
  print("\t1.visual")
  print("\t2.config")
  cv = input("aukera:")
  if int(cv) == 1:
     print("\n")
     print("aukeratu modu bat:")
     tabla_des = mysql.describe_t(tabla_s[int(zent)][dbs])
     lotura_iz = ""
     lotura_da = ""
     for x in range(len(tabla_des)):
         print("\t.",tabla_des[x]["Field"])
         tabla_sel = mysql.select_t(tabla_s[int(zent)][dbs])
         for p in range(len(tabla_sel)):
             print("\t  ",p,"* ",tabla_sel[p][tabla_des[x]["Field"]])
     print("\t. (insert) datuak sartu") 
     aukeratu = input("aukera:")
     if aukeratu == "insert":
         fyle = ""
         for j in range(len(tabla_des)):
             fyle += tabla_des[j]["Field"] + ","
         cont = []
         col = "" 
         for p in range(len(tabla_sel)):
             for x in range(len(tabla_des)):
                 col += str(tabla_sel[p][tabla_des[x]["Field"]]) + ","
             cont.append(col[:-1])
             col = ""
         fitxero = tabla_s[int(zent)][dbs] +".od.csv"
         reads = read(fitxero,"C:\\users\Admin\Desktop\python\mysqlpy\oard",fyle[:-1],cont)
         r = reads.idatzi()
         ja = input("(sartu) idatzi:")
         while (ja != "sartu"): 
             ja = input("(sartu) idatzi:")
         val = reads.val()
         print (val)
         #inssert = mysql.insert_t(tabla_s[int(zent)][dbs],val)
  if int(cv) == 2:
     tabla_des = mysql.describe_t(tabla_s[int(zent)][dbs])
     print("\n")
     print("Zutabeak:")
     #print(tabla_des)
     for x in range(len(tabla_des)):
         print("\t",[x],".Izena:",tabla_des[x]["Field"],"; Karaktere_Mota:",tabla_des[x]["Type"],"; NULL:",tabla_des[x]["Null"],"; Giltza:",tabla_des[x]["Key"],"; Defektuzko_izena:",tabla_des[x]["Default"],"; Gehigarria:",tabla_des[x]["Extra"])
     print("\t",[len(tabla_des)],".sortu zutabe berri bat:")
     print("\n")
     input("")