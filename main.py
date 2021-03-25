
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

query = ("SELECT Wave_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,Wave_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from Wave Power    ".format(
    Year, Mounth, day,Wave_Consumption))

retrieve = "Select AVG(Wave_Consumption) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in Wave Power is :" + str(i[0]))


query = ("SELECT Wind_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,Wind_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from Wind Power    ".format(
    Year, Mounth, day,Wind_Consumption))

retrieve = "Select AVG(Wind_Consumption) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in Wind Power is :" + str(i[0]))

query = ("SELECT Wind_Consumption, day, Mounth, Year FROM turkeyocak "
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

query = ("SELECT LnadfillGas_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,LnadfillGas_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from LnadfillGas Power    ".format(
    Year, Mounth, day,LnadfillGas_Consumption))

retrieve = "Select AVG(LnadfillGas_Consumption) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in LnadfillGas Power is :" + str(i[0]))


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


query = ("SELECT LowCarbon_Consumption, day, Mounth, Year FROM turkeyocak "
         )
cursor.execute(query)
for (Year, Mounth, day,LowCarbon_Consumption) in cursor:
  print("{} energy was produced in , {}, {}, {} from LowCarbon Power    ".format(
    Year, Mounth, day,LowCarbon_Consumption))

retrieve = "Select AVG(LowCarbon_Consumption) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in LowCarbon Power is :" + str(i[0]))


retrieve = "Select AVG((Wind_Consumption+Wave_Consumption+SolarPV_Consumption+Hydro_Consumption+LnadfillGas_Consumption+FossilFuel_Consumption+LowCarbon_Consumption) / 7) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in Renewable Power is :" + str(i[0]))

cursor.close()
cnx.close()