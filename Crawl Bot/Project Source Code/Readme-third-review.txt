$ yum install docker-engine 

$ sudo docker pull seppinho/cdh5-hadoop-mrv1:latest

$ sudo docker run -it -v /home/User/final_project:/mypython -p 50030:50030 -p 8000:8000 seppinho/cdh5-hadoop-mrv1:latest run-hadoop-initial.sh

# apt-get update

# apt-get upgrade

# apt-get build-essential

# apt-get install libread line-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

# apt-get install python

# apt-get install python-dev

# apt-get install python-pip

# pip install beautifulsoup4

# pip install pandas

# pip install ipython

# pip install jupyter

# pip install plotly

# pip install mathplotlib

# exit

$ sudo docker commit container-ID (5bb3361cf74) hadoop_project

{ $ docker ps }

$ sudo docker run -it -v /home/User/mypython:/mypython -p 50030:50030 -p 8000:8000 hadoop_project run-hadoop-initial.sh

# cd mypython

# sh execute.sh 

"""
    The following commands are executed under execute.sh
"""

#python soupy.py

#cd ..

#sudo -u cloudgene hadoop fs -mkdir input1
#sudo -u cloudgene hadoop fs -mkdir input2
#sudo -u cloudgene hadoop fs -mkdir input3
#sudo -u cloudgene hadoop fs -mkdir input4

#sudo -u cloudgene hadoop fs -mkdir input5
#sudo -u cloudgene hadoop fs -mkdir input6
#sudo -u cloudgene hadoop fs -mkdir input7
#sudo -u cloudgene hadoop fs -mkdir input8


#sudo -u cloudgene hadoop fs -put /mypython/cs2401.txt input1
#sudo -u cloudgene hadoop fs -put /mypython/cs2402.txt input2
#sudo -u cloudgene hadoop fs -put /mypython/cs2403.txt input3
#sudo -u cloudgene hadoop fs -put /mypython/mg2452.txt input4

#sudo -u cloudgene hadoop fs -put /mypython/cs2041.txt input5
#sudo -u cloudgene hadoop fs -put /mypython/it2024.txt input6
#sudo -u cloudgene hadoop fs -put /mypython/cs2405.txt input7
#sudo -u cloudgene hadoop fs -put /mypython/cs2406.txt input8


#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input1 output1
#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input2 output2
#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input3 output3
#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input4 output4

#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input5 output5
#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input6 output6
#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input7 output7
#sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input8 output8

#cd mypython

#sudo -u cloudgene hadoop fs -get output1/part-r-00000 cs2401
#sudo -u cloudgene hadoop fs -get output2/part-r-00000 cs2402
#sudo -u cloudgene hadoop fs -get output3/part-r-00000 cs2403
#sudo -u cloudgene hadoop fs -get output4/part-r-00000 mg2452

#sudo -u cloudgene hadoop fs -get output5/part-r-00000 cs2041
#sudo -u cloudgene hadoop fs -get output6/part-r-00000 it2024
#sudo -u cloudgene hadoop fs -get output7/part-r-00000 cs2405
#sudo -u cloudgene hadoop fs -get output8/part-r-00000 cs2406

#python prediction.py marks.csv

#rm cs2401.txt cs2402.txt cs2403.txt mg2452.txt cs2041.txt it2024.txt cs2405.txt cs2406.txt cs2401 cs2402 cs2403 mg2452 cs2041 it2024 cs2405 cs2406

"""
    End of the commands executed by execute.sh
"""


