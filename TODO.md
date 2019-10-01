### TODO Add in future: 
- Google Cloud Command Line Utilities
    1. bq
    2. gsutil
    3. gcloud ...
    4. cbt
- ai platform update in training data analyst
- modifying qwiklabs for ai platform & nano... & installing package again. 
- bigquery update to standard in Lab 3 of dataflow. Change the instructions in qwikalbs as well. Will need to create the view again for the purposes of standar format. 
- change bigquery labs in legacy format from bigquery labs. 
- Machine Learning
    - Lab 2. Reset the kernel instruction is not clear. Expand on that. 
    - Lab 3. Add further experiments on how to ml modelling in that.. 
    - Lab 6. Remove JupyterLab via datalab. Make it platform indendant
    - Lab 7. Python 2, problem in packages. For python 3, how to make it work? Check david's repository. For dataflow job, can run it externally and simply use python 3 in the ai platform notebook.. The query is not correct. it doesn't select the subset. 
    
# Qwilabs Updates
1. Day 1. Lab 1. replace nano with cloudshell edit
2. Day 1. Lab 1. Version 1.2 for component gateaway doesn't work. Version should be more than 1.3.29
3. Day 1. Lab 1. Remove the  image option 1.2 verion for creation of cluster. 
4. Day 1. lab 1. Highlight executing the source instruction
5. Day 1. Lab 1. Highlight, zone should be present inside the region. 
6. Day 1. lab 1. Give details on what is zone vs region. 
7. Day 1. Lab 1. replace n1-standard-2 with 2vCPUs
8. Day 1. Lab 2. Task 1. Instruction 3. source myenv before doing gsutil cp $BUCKET
9. Day 1. Lab 1. After gsutil cp $BUCKET, do gsutil ls.. Before gsutil $BUCKET, do echo $BUCKET and source execute. 
10. Day 1. lab 3. While copying spark code in vim, the syntax gets wrong. either paste via echo "" > wordcount or get it from github. wordcount.py needs to be uploaded
11. IF NOT SET TO PROJECT ID. gcloud config set project "qwiklabs-project-id" **frequently happens**
12. Day 4. Lab 1. Nano to be replaced with cat

# MISC Info
1. devshell_project_id
2. gsutil how to use
3. gcloud products to work with most of the products
   1. bq to interact with bigquery
   2. python code to launch dataflow pipeline
4. Nano guide
5. Replace all nano with cat
6. Bigquery, how to create dataset on new ui. update the instructions
7. quering streaming data in bigquery, doesn't tell you data process

# Trouble Shooting
1. Dataproc. HDFS error. Login to master not cloudshell
2. Dataproc something error. Check BUCKET
3. Firewall rule important stage which most miss
4. Dataflow. gsutil cp error. Check value in BUCKET.