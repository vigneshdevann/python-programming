app=int(raw_input())
bed=int(raw_input())
cat=int(raw_input())
if(app>=bed and app>=cat):
	print(app)
elif(bed>=cat):
	print(bed)
else:
	print(cat)
