import csv
import sys
import psycopg2

def dump(fname):
  dbcon = psycopg2.connect ("dbname=heros")
  c= dbcon.cursor()
  
  f= open(fname,"w")
  writer=csv.writer(f)
  c.execute("SELECT name,gender FROM  heros");
  for a,b in c.fetchall():
    print(a,b)
    writer.writerow([a,b])
  #print(c.fetchall()[0])
    
  dbcon.commit()
    
  f.close()
    
def main():
  fname=sys.argv[1]
  dump(fname)

main()
