l, r = input().split(" ")
l = int(l)
r = int(r)

if l==r and l==0:
	print("Not a moose")
elif l ==r:
	print("Even", l*2)
elif l>r:
	print("Odd", l*2)
else:
	print("Odd", r*2)