# Projects-from-Simplon-Lyon

Extraction et nettoyage : Nous avons commencé par extraire les données des matchs de coupe du monde à partir de trois fichiers différents ("data_2018.json", "matches_19302010.csv", et "WorldCupMatches2014.csv"). Cela a inclus la normalisation des noms de colonnes et l'harmonisation des formats de données pour assurer la cohérence à travers les différentes sources.

Création de DataFrame : Après le nettoyage initial, nous avons créé des DataFrames pour chaque fichier. Chaque DataFrame a été structuré pour inclure des informations telles que les équipes jouant à domicile et à l'extérieur, les résultats des matchs, les dates, et d'autres données pertinentes.

Enrichissement des données : Pour le fichier de l'édition 2022, qui manquait initialement, nous avons recherché et formaté des données à partir de sources complémentaires pour compléter notre base de données.

Unification des DataFrames : Toutes les données nettoyées ont été combinées en un seul DataFrame. Cela impliquait l'ajustement des indices et la création d'un identifiant unique pour chaque match pour faciliter les analyses et les requêtes futures.

Ajout de données calculées : Pour enrichir notre modèle prédictif, nous avons ajouté des colonnes calculées, telles que 'city' et 'edition' pour chaque match, offrant des détails supplémentaires qui pourraient influencer les prédictions de l'application.

Validation et préparation pour intégration : Le DataFrame final a été vérifié pour l'intégrité des données et préparé pour l'intégration dans une base de données structurée, qui alimentera l'application de prédiction des résultats des matchs.
