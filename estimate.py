import random
def wallis(x):
  p=1
  for i in range(1,x):
    p*= (4*(i**2)/((4*(i**2))-1))
  return (2*p)
  
def monte_carlo(n):
  c=0
  s=0
  for i in range(n):
    x=random.random()
    y=random.random()
    if((x**2)+(y**2)<1):
      c+=1
    else:
      s+=1
  return (4*(c/(c+s)))
