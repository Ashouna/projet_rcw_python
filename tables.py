from connexion import connection

conn=connection()
cur=conn.cursor()
def create_table_patient():
    # Création de la table 'patient'
    create_table_query = """
        CREATE TABLE patient (
            patient_id INT AUTOINCREMENT PRIMARY KEY,
            nom VARCHAR(50),
            prenom VARCHAR(50),
            date_naissance DATE,
            email VARCHAR(100),
            password VARCHAR(100),
            sexe VARCHAR(20),
            telephone VARCHAR(20)
        )
        """
    result=cur.execute(create_table_query)
    if result:
        print("Table created successfully")
        cur.close()
        conn.close()
    else:
        print("Error creating the table")

