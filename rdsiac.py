import boto3


def list_db(conn):
    try:
        dbs = conn.describe_db_instances()
        for db in dbs['DBInstances']:
            print(f"The MasterUsername is {db['MasterUsername']}")
            print(f"The endpoint is {db['Endpoint']['Address']}, port {db['Endpoint']['Port']}")
            print(f"The DB status is {db['DBInstanceStatus']}")
            print(db)
    except Exception as error:
        print(error)


def create_db_ins(conn):
    try:
        input_username = input("enter username:\n")
        input_password = input("enter password:\n")
        print(f'your db username is {input_username}, password is {input_password}')
        response = conn.create_db_instance(
            DBInstanceIdentifier='mypostgresdb',
            AllocatedStorage=20,
            DBInstanceClass='db.t2.micro',
            Engine='postgres',
            MasterUsername=input_username,
            MasterUserPassword=input_password,
            DBSecurityGroups=['postgres-homeaccess'],
            )
        print(response)
    except Exception as error:
        print(error)

def delete_db_ins(conn):
    try:
        response = conn.delete_db_instance(
            DBInstanceIdentifier='mypostgresdb',
            SkipFinalSnapshot = True,
        )
        print(response)
    except Exception as error:
        print(error)
