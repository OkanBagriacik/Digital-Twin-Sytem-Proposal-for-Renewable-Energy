import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

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
