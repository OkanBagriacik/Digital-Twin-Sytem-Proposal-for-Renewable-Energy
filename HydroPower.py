import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

query = ("SELECT Hydro_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,Hydro_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from Hydro Power    ".format(
    Year, Mounth, day,Hydro_Consumption))

retrieve = "Select AVG(Hydro_Consumption) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in Hydro Power is :" + str(i[0]))