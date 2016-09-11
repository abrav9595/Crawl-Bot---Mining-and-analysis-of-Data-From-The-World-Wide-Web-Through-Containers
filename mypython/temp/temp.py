s = open("baba.txt","r").read()
a = ''
d={}
c=0
for word in s.split():
	if(c%2==0):
		a = word
        else:
                d[a] = word
print d.values()
