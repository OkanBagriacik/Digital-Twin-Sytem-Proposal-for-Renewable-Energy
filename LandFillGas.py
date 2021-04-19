import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

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
    print("Average energy produced in LandfillGas Power is :" + str(i[0]))