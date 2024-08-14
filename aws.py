# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# @api.route('/envoyer_donnees', methods=['GET'])
# def envoyer_donnees():
#     # Récupérer les données envoyées dans la requête GET
#     parametre1 = request.args.get('parametre1')
#     parametre2 = request.args.get('parametre2')

#     # Configuration de l'URL de votre API AWS avec les paramètres
#     url_api_aws = 'URL_DE_VOTRE_API_AWS'

#     # Données à envoyer à l'API AWS (si nécessaire)
#     donnees = {
#         'parametre1': parametre1,
#         'parametre2': parametre2
#     }

#     try:
#         # Envoyer les données à l'API AWS en utilisant requests
#         response = requests.get(url_api_aws, params=donnees)
        
#         # Vérifier le statut de la réponse
#         if response.status_code == 200:
#             return jsonify({"message": "Données envoyées avec succès à l'API AWS"})
#         else:
#             return jsonify({"error": "Erreur lors de l'envoi des données à l'API AWS"})
#     except Exception as e:
#         return jsonify({"error": str(e)})  # Gérer les erreurs

# if __name__ == '__main__':
#     app.run(debug=True)
