import csv
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='csvfile')
print("database connected")

cursor=mydb.cursor()
csv_data=csv.reader(open('100000Records.csv'))

for row in csv_data:
    cursor.execute('INSERT INTO humanlist (EmpID,FirstName,EMail,FatherName,Weight,YearofJoining,MonthofJoining,DayofJoining,Salary,City,Zip,Region,UserName,Password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
    print(row)

mydb.commit()
cursor.close()
print("Done")


