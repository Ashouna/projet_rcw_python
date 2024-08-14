import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,roc_curve


def classification(data):
    # Charger les données
    df = pd.read_csv("dataset\Disease_symptom_and_patient_profile_dataset.csv")
    df = df.drop_duplicates()
    
    # Encodage des variables catégorielles
    for i in ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']:
        df[i] = df[i].replace({'Yes': 1, 'No': 0})
    for i in ['Blood Pressure', 'Cholesterol Level']:
        df[i] = df[i].replace({'Low': 1, 'Normal': 2, 'High': 3})
    df['Outcome Variable'] = df['Outcome Variable'].replace({'Positive': 1, 'Negative': 0})
    df['Gender'] = df['Gender'].replace({'Male': 1, 'Female': 0})
    
    # Séparation des caractéristiques et de la variable cible
    x = df.drop(['Disease', 'Outcome Variable'], axis=1) # Supprimer la colonne 'classe'
    y = df['Disease']
    
    # Séparer les données en ensembles d'entraînement et de test
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.30, random_state=42)

    # Initialiser le modèle de classification
    model = DecisionTreeClassifier()
    model.fit(xtrain, ytrain)
    
    # Évaluer les performances du modèle
    y_pred_train = model.predict(xtrain)
    print("The TRAIN accuracy is", accuracy_score(ytrain, y_pred_train))

    # Faire une prédiction avec le modèle entraîné
    input_data = pd.DataFrame([data])
    predicted_outcome = model.predict(input_data)
    print(f"Predicted Outcome: {predicted_outcome}")
    
    # Récupérer le nom de la maladie prédite
    predicted_disease = predicted_outcome[0]
    print(f"Predicted Disease: {predicted_disease}")
    return predicted_disease


