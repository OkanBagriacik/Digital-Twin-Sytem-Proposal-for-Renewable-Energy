import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

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




cursor.execute("SELECT MIN(LowCarbon_Consumption) AS minimum FROM turkeyocak")

result_min = cursor.fetchall()
for i in result_min:
    minimum = float(i[0])
    print("Minimum Energy Production this Month : " + str(minimum))

cursor.execute("SELECT MAX(LowCarbon_Consumption) AS maximum FROM turkeyocak")

result_max = cursor.fetchall()

for i in result_max:
    maximum = float(i[0])
    print("Maximum Energy Production this Month :" +str(maximum))

