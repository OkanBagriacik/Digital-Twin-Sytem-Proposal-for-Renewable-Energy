
import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

query = ("SELECT SolarPV_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,SolarPV_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from Solar Power    ".format(
    Year, Mounth, day,SolarPV_Consumption))

retrieve = "Select AVG(SolarPV_Consumption) AS average from turkeyocak;"

cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in Solar Power is :" + str(i[0]))




cursor.close()
cnx.close()