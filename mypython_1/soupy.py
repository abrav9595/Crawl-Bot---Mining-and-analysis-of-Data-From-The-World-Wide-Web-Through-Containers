"""
    This code scrapes the marks from the webpage and saves it to marklist.csv file.
    At the same time, the grades for each subject is being stored in text files, which are then processed by using HDFS to find the probability of grades in each subject. 
"""


from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("marklist.html"),"html.parser")

f = csv.writer(open("marklist.csv", "w"))   # Open the output file for writing before the loop

f1 = csv.writer(open("marks.csv","w"))

trs = soup.find_all('tr')

s1 = open("cs2401.txt","w")
s2 = open("cs2402.txt","w")
s3 = open("cs2403.txt","w")
s4 = open("mg2452.txt","w")
s5 = open("cs2041.txt","w")
s6 = open("it2024.txt","w")
s7 = open("cs2405.txt","w")
s8 = open("cs2406.txt","w")


f.writerow(["Sno","Reg no","Name","CS2401","CS2402","CS2403","MG2452","CS2041","IT2024","CS2405","CS2406","GPA","CLASS"])
f1.writerow(["CS2401","CS2402","CS2403","MG2452","CS2041","IT2024","CS2405","CS2406","GPA","CLASS"])

for tr in trs:
    for link in tr.find_all('a'):
        fullLink = link.get ('href')

    tds = tr.find_all("td")

    c = 0
    class_var = ''
    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        sno = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        reg = str(tds[1].get_text())
        name = str(tds[2].get_text())
        sub1 = str(tds[3].get_text())
        sub2 = str(tds[4].get_text())
        sub3 = str(tds[5].get_text())
        sub4 = str(tds[6].get_text())
        sub5 = str(tds[7].get_text())
        sub6 = str(tds[8].get_text())
        sub7 = str(tds[9].get_text())
        sub8 = str(tds[10].get_text())
        gpa = str(tds[11].get_text())

        
        if(len(sub1)==1): 
            s1.write(sub1+"\n")
        if(len(sub2)==1): 
            s2.write(sub2+"\n")
        if(len(sub3)==1): 
            s3.write(sub3+"\n")
        if(len(sub4)==1): 
            s4.write(sub4+"\n")
        if(len(sub5)==1): 
            s5.write(sub5+"\n")
        if(len(sub6)==1): 
            s6.write(sub6+"\n")
        if(len(sub7)==1): 
            s7.write(sub7+"\n")
        if(len(sub8)==1): 
            s8.write(sub8+"\n")
         
        #For subject one
        if(sub1=='S'):
            c = c+6
        elif(sub1=='A'):
            c = c+5
        elif(sub1=='B'):
            c = c+4
        elif(sub1=='C'):
            c = c+3
        elif(sub1=='D'):
            c = c+2
        elif(sub1=='E'):
            c = c+1
            
        #For subject two
        if(sub2=='S'):
            c = c+6
        elif(sub2=='A'):
            c = c+5
        elif(sub2=='B'):
            c = c+4
        elif(sub2=='C'):
            c = c+3
        elif(sub2=='D'):
            c = c+2
        elif(sub2=='E'):
            c = c+1
        
        #For subject three
        if(sub3=='S'):
            c = c+6
        elif(sub3=='A'):
            c = c+5
        elif(sub3=='B'):
            c = c+4
        elif(sub3=='C'):
            c = c+3
        elif(sub3=='D'):
            c = c+2
        elif(sub3=='E'):
            c = c+1
            
        #For subject four
        if(sub4=='S'):
            c = c+6
        elif(sub4=='A'):
            c = c+5
        elif(sub4=='B'):
            c = c+4
        elif(sub4=='C'):
            c = c+3
        elif(sub4=='D'):
            c = c+2
        elif(sub4=='E'):
            c = c+1
            
        #For subject five
        if(sub5=='S'):
            c = c+6
        elif(sub5=='A'):
            c = c+5
        elif(sub5=='B'):
            c = c+4
        elif(sub5=='C'):
            c = c+3
        elif(sub5=='D'):
            c = c+2
        elif(sub5=='E'):
            c = c+1
            
        #For subject six
        if(sub6=='S'):
            c = c+6
        elif(sub6=='A'):
            c = c+5
        elif(sub6=='B'):
            c = c+4
        elif(sub6=='C'):
            c = c+3
        elif(sub6=='D'):
            c = c+2
        elif(sub6=='E'):
            c = c+1
            
        #For subject seven
        if(sub7=='S'):
            c = c+6
        elif(sub7=='A'):
            c = c+5
        elif(sub7=='B'):
            c = c+4
        elif(sub7=='C'):
            c = c+3
        elif(sub7=='D'):
            c = c+2
        elif(sub7=='E'):
            c = c+1
            
        #For subject eight
        if(sub8=='S'):
            c = c+6
        elif(sub8=='A'):
            c = c+5
        elif(sub8=='B'):
            c = c+4
        elif(sub8=='C'):
            c = c+3
        elif(sub8=='D'):
            c = c+2
        elif(sub8=='E'):
            c = c+1
        
        temp = gpa
        temp1 = float(temp)
        t = int(temp1)
        
        #print t
        if (gpa!='GPA'):
            c = c+t
            
        if (c>=50) and (c<60):
            class_var = 'Eminent'
        elif (c>=40) and (c<50):
            class_var = 'Excellent'
        elif (c>=30) and (c<40):
            class_var = 'Good'
        elif (c>=20) and (c<30):
            class_var = 'Moderate'
        elif (c>=10) and (c<20):
            class_var = 'Fair'
        elif (c>=0) and (c<10):
            class_var = 'Poor'    
            
    #    print gpa
    except:
        continue #This tells the computer to move on to the next item after it encounters an error
    
   # print gpa
    if(str(tds[11].get_text())!='GPA'):
        f.writerow([sno,reg,name,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,t,class_var])
        f1.writerow([sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,t,class_var])
    

s1.close()
s2.close()
s3.close()
s4.close()
s5.close()
s6.close()
s7.close()
s8.close()
"""
    End of the program.
"""
    
