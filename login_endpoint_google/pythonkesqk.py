import mysql.connector

conn = mysql.connector.connect(
   user='root', password='Hm24011998', host='127.0.0.1', database='data')

cursor = conn.cursor()


insert_stmt = (
   "insert into datauser(nama_depan,nama_belakang,email,iat,at_hash)"
   "VALUES (%s, %s, %s, %s, %s)"
)
data = ('Hansen ', 'Marcelino Azali', 'hansenmarcelino54@gmail.com', 1638255376, 'edwKcZsQw3nAktAZ-fN23A')

try:
  
   cursor.execute(insert_stmt, data)
   
  
   conn.commit()

except:
  
   conn.rollback()

print("Data inserted")


conn.close()