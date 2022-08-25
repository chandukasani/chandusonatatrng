import  pyodbc
server = 'HYDTRNG7\SQLEXPRESS'
database = 'traininghyd'
username = 'sa'
password = 'admin@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor = cnxn.cursor()
res = mycursor.execute("select * from emp")
myrecs = res.fetchall();
print(myrecs)
