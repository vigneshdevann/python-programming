a=int(raw_input(""))
if(((a%4==0) or (a%400==0)) and (a%100!=0)):
	print("yes")
else:
	print("no")
