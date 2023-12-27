cd "E:\Varun\Personal_Stuff\tdk_case_study_repo\src"
docker build -t oracle_python .
schtasks /create /tn "Export_Oracle_DB" /tr "docker run -d -v E:\Varun\Personal_Stuff\tdk_case_study_repo:/app/output -p 9000:9000 oracle_python" /sc daily /st 00:00       