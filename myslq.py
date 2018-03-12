import pymysql.cursors

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