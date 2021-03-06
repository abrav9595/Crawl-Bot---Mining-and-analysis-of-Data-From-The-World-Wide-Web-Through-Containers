#!/bin/bash
# This script executes the "Hello World" of MapReduce.
chmod 777 /final_project/mypython_4
#calculate the time as a performance metric...(In the case of a Linux Container).
starttime=$(date +%s)

#execute the python program
python soupy.py
cd ..

# Create an input directory
sudo -u cloudgene hadoop fs -mkdir input1
sudo -u cloudgene hadoop fs -mkdir input2
sudo -u cloudgene hadoop fs -mkdir input3
sudo -u cloudgene hadoop fs -mkdir input4

sudo -u cloudgene hadoop fs -mkdir input5
sudo -u cloudgene hadoop fs -mkdir input6
sudo -u cloudgene hadoop fs -mkdir input7
sudo -u cloudgene hadoop fs -mkdir input8
# Add some data to the input directory
pwd
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/cs2401.txt input1
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/cs2402.txt input2
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/cs2403.txt input3
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/mg2452.txt input4

sudo -u cloudgene hadoop fs -put /final_project/mypython_4/cs2041.txt input5
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/it2024.txt input6
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/cs2405.txt input7
sudo -u cloudgene hadoop fs -put /final_project/mypython_4/cs2406.txt input8

# Execute Wordcount

sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input1 output1
sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input2 output2
sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input3 output3
sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input4 output4

sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input5 output5
sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input6 output6
sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input7 output7
sudo -u cloudgene /usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/hadoop-examples.jar wordcount input8 output8

#copy output to local directory
cd mypython_4

sudo -u cloudgene hadoop fs -get output1/part-r-00000 /final_project/mypython_4/cs2401
sudo -u cloudgene hadoop fs -get output2/part-r-00000 /final_project/mypython_4/cs2402
sudo -u cloudgene hadoop fs -get output3/part-r-00000 /final_project/mypython_4/cs2403
sudo -u cloudgene hadoop fs -get output4/part-r-00000 /final_project/mypython_4/mg2452

sudo -u cloudgene hadoop fs -get output5/part-r-00000 /final_project/mypython_4/cs2041
sudo -u cloudgene hadoop fs -get output6/part-r-00000 /final_project/mypython_4/it2024
sudo -u cloudgene hadoop fs -get output7/part-r-00000 /final_project/mypython_4/cs2405
sudo -u cloudgene hadoop fs -get output8/part-r-00000 /final_project/mypython_4/cs2406

#calculating the total time for hadoop mapreduce..(In the case of a linux container).
endtime=$(date +%s)
cost=$(($endtime-$starttime))
echo -e "\n\nTime taken to execute Hadoop Map reduce for our data (In Linux Container) = $cost Seconds\n\n"

#calculate informtion gain and construct decision tree using the python program
python prediction.py marks.csv

#delete the files
rm cs2401.txt cs2402.txt cs2403.txt mg2452.txt cs2041.txt it2024.txt cs2405.txt cs2406.txt cs2401 cs2402 cs2403 mg2452 cs2041 it2024 cs2405 cs2406
