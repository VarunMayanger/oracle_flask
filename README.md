**Docker Container Micro Service**
The repository contains the code for the python flask micro service created to fetch data from oracle database and save it in TSV format in a local directory everyday at 00:00 hrs.

Assumptions:
1)	The data is already available in the locally set oracle database
2)	The data is stored in the table with name as tdk as shown in the below screenshot.

 ![image](https://github.com/VarunMayanger/oracle_flask/assets/20820940/d0ebd8a2-40d7-4904-a2b5-5a3359961fe0)


**Explanation of Python Flask Code**

 The flask application code starts with the initialization of the flask web application and followed by route definition. The current time is store in the timestamp variable and is concatenated to the filename so that the resulting file_name variable holds the complete path and filename.
 
(A)	**Connecting  to the Database**
Connection to the oracle db is done using the connect function from oracledb module. The connect function takes the following parameters – username, password and data source name (a connection string specifying the database location). oracledb.connection() returns a connection object which is being used to execute the query  - “Select * from tdk”.

(B)**Fetching column and row data and writing to a tsv file**
Column and rows are being fetched using the context management and using the cursor object to fetch result from the oracle db.
The file is opened in the write mode and first operation is to write the column names followed by the row entries through iterations.
Building and running Docker Image
Dependencies and their versions are specified in the requirement.txt file. To build and run docker image the following steps are need to be performed in sequence.

**Step 1:** Build and tag docker image: build docker image by executing the following command in powershell or CLI – 
Syntax : docker build –t (image_tag) .
For example - docker build -t oracle_python .

**Step 2:** Run the docker image: run docker image in detached mode by mounting a volume on the host machine to a directory inside the container and map the ports of host and container. To do this execute the docker run command in CLI.
Syntax : docker run -d -v [host_app_directory]:[container_repo]  -p [host_port]:[container_port]  [image_tag]
For example: docker run -d -v E:\Varun\Personal_Stuff\tdk_case_study_repo:/app/output -p 9000:9000 oracle_python
The .tsv file with timestamp will be save in the local directory provided in the docker run command which in this case is “E:\Varun\Personal_Stuff\tdk_case_study_repo”. Below is the screenshot for reference.
 
![image](https://github.com/VarunMayanger/oracle_flask/assets/20820940/db50c51c-2300-4e4c-921b-adda9e20cf63)


**Step 3:** Adding the execution of container as CRON job for windows for saving the file on local machine daily at 00:00 hrs. 
To achieve this execute the schedule task command in CLI
Syntax - schtasks /create /tn "[task_name]" /tr "[command to be executed]” /sc daily /st [time]
For Example:  schtasks /create /tn "Export_Oracle_DB" /tr "docker run -d -v E:\Varun\Personal_Stuff\tdk_case_study_repo:/app/output -p 9000:9000 oracle_python" /sc daily /st 00:00
Once it’s executed the task is scheduled to run daily at 00:00 hrs. To cross verify open task scheduler from administrative tools in windows OS.  The task will be listed in the scheduler as shown in the below screenshot. This can also be verified by running the task manually which will result in creating a .tsv file in the specified local repository.
 

![image](https://github.com/VarunMayanger/oracle_flask/assets/20820940/21c2a477-1585-4610-8fc7-77b32fd7c30b)

.
