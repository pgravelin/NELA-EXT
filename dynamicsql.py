###

## select id, gameid, airdate from games where airdate = date '2018-01-10'

## select id, gameid, airdate from games where airdate = to_date('10-01-2018','DD-MM-YYYY')

​

### Dynamic SQL
import psycopg2 as dbapi2

db = dbapi2.connect (port=5433,
                     database="sibeladali",
                     user="sibeladali",
                     password="sibeladali")

cur = db.cursor()
print ("first version")
cur.execute("select * from events")

for row in cur:
    print (row[0],row[1],row[2],row[3])

attrs = ["day","time"]

q = "select "
for attr in attrs:
    q += "{}, ".format(attr)

q = q.strip().strip(",")    
q += " from events where price<=10 and "

conditions = ["M","12:00"]

for i in range(len(attrs)):
    q += "{}='{}' ".format(attrs[i], conditions[i])
    if i < len(attrs)-1:
        q += "and "

print ("second version")
print (q)

cur.execute(q)
for row in cur:
    print (row[0],row[1])