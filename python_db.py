# Importing the required modules
from flask import Flask
import oracledb
import csv
import os
from datetime import datetime

# Definig variables
db_username = "system" #os.environ.get('db_user')
db_password = "varun" #os.environ.get('db_pass')
db_host = "host.docker.internal" #db_host = "localhost" #os.environ.get('db_host')
db_port = '1521'
db_service = "XE" #os.environ.get('db_service')


app = Flask(__name__) # Initializing the flask web application

@app.route('/copy', methods=['GET', 'POST']) # Defining route for our web application
def main():

    # Add timestamp to filename of output .tsv file
    timestamp = datetime.now().strftime("%Y%m%d")
    # Add file location
    file_name = '/app/output/tdk_'+ timestamp +'.tsv'
    print(file_name)

    connection = oracledb.connect(
        user  = db_username,
        password= db_password,
        dsn=f'{db_host}:{db_port}/{db_service}',
    )

    sql = """select * from tdk"""
  
    with connection.cursor() as cursor:
    #    print("Get all rows via an iterator")
    #    for result in cursor.execute(sql):
    #        print(result)
    #    print()

        # Fetaching all Cloumns from the Table tdk form a header in tsv
        print("Fetch all cloumns")
        cursor.execute(sql)
        columns = [col.name for col in cursor.description]
        print(columns)

        print("Fetch all rows")
        cursor.execute(sql)
        result = cursor.fetchall()
        print()
        
        print("Writing to TSV file")
        with open(file_name, 'w', newline='') as tsv_file:
            writer = csv.writer(tsv_file, delimiter='\t')

            # Writing Columns to the file
            writer.writerow(columns)

            # writing rows into the file Rows
            for row in result:
                writer.writerow(row)
    
    return "File saved successfully"

main()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000) # Making the application available to all outside requests @ port 9000