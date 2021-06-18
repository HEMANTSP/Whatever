import psycopg2
from flask import Flask,request,render_template
import jinja2

app=Flask("new",template_folder='templates')

dc=psycopg2.connect("dbname=heros")
c=dc.cursor()

@app.route("/")
def home():
  return render_template("homepage.html")

@app.route("/next")
def next():
    d=c.execute("select name ,gender from heros")
    data=c.fetchall()
    '''
    l=[]
    for a,b in c.fetchall():
    x= f" NAME :: {a}  GENDER :: {b}"
    l.append(x)
    l="\n".join(l)
    return (render_template("nextpage.html", r=l))
    '''
    return (render_template("nextpage.html",data=data))
 
def main():
  app.run(debug=True)
if __name__=="__main__":
  main()


