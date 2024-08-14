
from connexion import connection


def create(data):
    conn=connection()
    cur=conn.cursor()
    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    sexe=data.get('sexe')
    date_naissance=data.get('date')
    telephone=data.get('telephone')
    password=data.get('password')

    # Vérification si l'utilisateur existe déjà dans la base de données
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM patient WHERE email = '{email}'")
    result = cur.fetchone()
    user_exists = result[0] > 0

    if user_exists:
        return False
    else:
        # Insertion des données dans la table patient
        cur.execute(f"INSERT INTO patient (nom,prenom,date_naissance,email,password,sexe,telephone) VALUES ('{nom}', '{prenom}','{date_naissance}','{email}','{password}','{sexe}','{telephone}')")

        conn.commit()  # Valider la transaction
        cur.close()
        conn.close()
        return True
def login(data):
    conn=connection()
    email = data.get('email')
    password=data.get('password')
    # Vérification si l'utilisateur existe déjà dans la base de données
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM patient WHERE email = '{email}' AND password = '{password}'")
    result = cur.fetchone()
    if result:
        user = {
            'patient_id': result[0],  # Supposons que la première colonne est l'ID de l'utilisateur
            'nom': result[1],
            'prenom': result[2],
            'email': result[4],
                # Ajoutez d'autres champs utilisateur si nécessaire
            }
        cur.close()
        conn.close()
        return user,True
    else:
        return None,False

   
    
def update_patient(data):
    conn=connection()
    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    password = data.get('password')
    patient_id = data.get("patient_id")

    try:
        cur = conn.cursor()
        update_query = """
                  UPDATE patient
                 SET nom = %s, prenom = %s, email = %s, password = %s
                  WHERE patient_id = %s
                """
        cur.execute(update_query, (nom, prenom, email, password, patient_id))
        conn.commit()
        cur.close()
        return True
    except Exception as e:
         return ({'error': str(e)}), 500
   


