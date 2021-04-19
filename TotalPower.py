import mysql.connector

cnx = mysql.connector.connect(user='root', password = 'Okan0123.', database='energy')
cursor = cnx.cursor()

retrieve = "Select AVG((Wind_Consumption+Wave_Consumption+SolarPV_Consumption+Hydro_Consumption+LnadfillGas_Consumption+FossilFuel_Consumption+LowCarbon_Consumption) / 7) AS average from turkeyocak;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average energy produced in Renewable Power is :" + str(i[0]))