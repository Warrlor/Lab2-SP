t = int(input ("введи t "))
dt = int(input ("введи dt "))
s = int(input ("введи s "))
d = int(input ("введи d "))
x = dt*s
if (22<t<24) or (0<t<8):
	x=x-((x/100)*10)
if (d==6) or (d==7):
	x=x-((x/100)*5)
print (x)