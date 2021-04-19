import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

query = ("SELECT FossilFuel_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,FossilFuel_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from FossilFuel Power    ".format(
    Year, Mounth, day,FossilFuel_Consumption))

retrieve = "Select AVG(FossilFuel_Consumption) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in FossilFuel Power is :" + str(i[0]))