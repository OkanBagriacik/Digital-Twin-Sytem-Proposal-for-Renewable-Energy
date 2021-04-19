import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

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
