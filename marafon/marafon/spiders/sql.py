# import psycopg2
#
# connect = psycopg2.connect(
#   database="postgres",
#   user="postgres",
#   password="admin",
#   host="127.0.0.1",
#   port="5432"
# )
#
#
# cursor  = connect.cursor()
#
# cursor.execute(''' create table Kibersport (
# title text,
# author text,
# tag text
# )''')
#
#
#
# connect.commit()
# connect.close()