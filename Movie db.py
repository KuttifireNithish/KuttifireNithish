import sqlite3

conn = sqlite3.connect('movie.db')
"""
conn.execute('''CREATE TABLE MOVIE
         (ID INT PRIMARY KEY     NOT NULL,
         Movie_name           TEXT    NOT NULL,
         Lead_actor            TEXT     NOT NULL,
         Lead_actress        TEXT       NOT NULL,
         Year_of_release        INT     NOT NULL,
         Director_name      TEXT        NOT NULL);''')
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (1, '96', 'Vijay Sethupathi', 'Thrisha', 2018, 'C. Premkumar')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (2, 'iru mugan', 'Vikram', 'Nayanthara', 2016, 'Anand Shankar')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (3, 'Karate kid', 'Jaden smith', 'Wenwen han', 2010, ' Harald Zwart')");
conn.commit()
conn.close()
"""


print(" 1. 96 \n 2. Iru mugan\n 3. Karate kid")
choice = int(input("Enter your choice: "))

val = conn.execute("SELECT * from MOVIE WHERE ID is "+str(choice))
for v in val:
    A = v[0]
    B = v[1]
    C = v[2]
    D = v[3]
    E = v[4]
    F = v[5]
print("Movie ID      : ",A)
print("Movie Name    : ",B)
print("Lead Actor    : ",C)
print("Lead Actress  : ",D)
print("Released Year : ",E)
print("Director      : ",F)
