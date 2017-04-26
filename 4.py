m1 = int(input ("введи m1 "))
v1 = int(input ("введи v1 "))
m2 = int(input ("введи m2 "))
v2 = int(input ("введи v2 "))
if (m1/v1)>(m2/v2):
	print ('первый плотнее')
else:
	if (m1/v1)==(m2/v2):
		print ('одинаковые')
	else:
		print ('второй плотнее')