import csv
import sys
import psycopg2

def insert(fname):
  dbcon = psycopg2.connect ("dbname=heros")
  c= dbcon.cursor()
  
  f= open(fname)
  reader=csv.reader(f)
  for a,b in reader:
    #print(a,b)
    c.execute(" INSERT INTO heros (name,gender) VALUES (%s,%s) ",(a,b))
    dbcon.commit()
    
def main():
  fname=sys.argv[1]
  insert(fname)
  
main()
