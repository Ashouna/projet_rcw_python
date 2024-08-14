import snowflake.connector

def connection():
    # Configuration des informations de connexion
    account = 'bxdiufm-ut52258'
    username = 'laura'
    password = 'Laura2003@'
    warehouse='COMPUTE_WH'
    database='Sante'
    schema='public' 

    # Connexion à Snowflake
    conn = snowflake.connector.connect(
        user=username,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema 
    )

    # Vérification de la connexion
    if conn:
        print("Connecté à Snowflake!")
        return conn
    else:
        print("Échec de la connexion à Snowflake.")
        return 
connection()