def wallis(x):
  p=1
  for i in range(1,x):
    p*= (4*(i**2)/((4*(i**2))-1))
  return (2*p)
  

