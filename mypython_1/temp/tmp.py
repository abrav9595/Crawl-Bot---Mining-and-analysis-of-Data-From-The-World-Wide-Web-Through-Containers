s = open("it2024","r").read()
a = ''
d={}
c=0
for word in s.split():
	if(c%2==0):
		a = word
	else :
	    d[a] = word
	c = c+1
c,m,i=0,0,''
for key in d.iterkeys():
    if(int(d[key])>m): 
        m = int(d[key])
        i = key
    c = c+int(d[key])
print c,m,i 
