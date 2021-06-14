from flask import Flask, request
import psycopg2
import sys
app=Flask("random")
@app.route("/")
def hello():
  #name = sys.argv[1]
  return ("hello")
items = ["python", "perl", "ruby"]
@app.route("/hero")
def show_from_db():
  dc= psycopg2.connect("dbname = heros")
  c=dc.cursor()
  x=c.execute("select name,gender from heros")
  r=[]
  for n,g in c.fetchall():
    if g=='m':
      x=f" hero name: {n}:: hero gender: {g} "
      r.append(x)
  r="</br>".join(r)
  return f"Here you go! </br> {r}"  
@app.route("/vere")    
def add_item():
    item = request.args.get("item")
    items.append(item)
    return f"No. of items is now {len(items)}"
    

def main():
  #n=sys.argv[1]
  app.run(debug=True)
  #hello() 
  
if __name__ =='__main__':
  main()
 

  
