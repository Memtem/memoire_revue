# Critères de la checklist organisés par catégorie
# Chaque critère a un id, un libellé et les étapes où il s'applique

CRITERES = [
    # --- PROBLÉMATIQUE (6 critères) ---
    {"id": "P1", "categorie": "Problématique", "label": "La problématique est formulée sous forme de question",
     "etapes": ["problematique", "plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "P2", "categorie": "Problématique", "label": "La problématique est en lien direct avec le contexte professionnel",
     "etapes": ["problematique", "plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "P3", "categorie": "Problématique", "label": "La problématique est ni trop large ni trop restrictive",
     "etapes": ["problematique", "plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "P4", "categorie": "Problématique", "label": "La problématique permet une analyse approfondie (pas une simple description)",
     "etapes": ["problematique", "plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "P5", "categorie": "Problématique", "label": "La problématique est claire et compréhensible",
     "etapes": ["problematique", "plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "P6", "categorie": "Problématique", "label": "La problématique est originale ou apporte un angle nouveau",
     "etapes": ["problematique", "plan", "plan_detaille", "v1", "version_finale"]},

    # --- PLAN / STRUCTURE (6 critères) ---
    {"id": "PL1", "categorie": "Plan", "label": "Le plan comporte 2 ou 3 grandes parties équilibrées",
     "etapes": ["plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "PL2", "categorie": "Plan", "label": "Les parties suivent une progression logique (théorie → pratique → préconisations)",
     "etapes": ["plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "PL3", "categorie": "Plan", "label": "Les sous-parties sont cohérentes avec le titre de la partie",
     "etapes": ["plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "PL4", "categorie": "Plan", "label": "Le plan répond à la problématique de manière structurée",
     "etapes": ["plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "PL5", "categorie": "Plan", "label": "Les titres sont informatifs et non génériques",
     "etapes": ["plan", "plan_detaille", "v1", "version_finale"]},
    {"id": "PL6", "categorie": "Plan", "label": "Le plan évite les redondances entre parties",
     "etapes": ["plan", "plan_detaille", "v1", "version_finale"]},

    # --- INTRODUCTION (7 critères) ---
    {"id": "I1", "categorie": "Introduction", "label": "L'introduction présente le contexte général du sujet (accroche)",
     "etapes": ["plan_detaille", "v1", "version_finale"]},
    {"id": "I2", "categorie": "Introduction", "label": "L'entreprise et le contexte professionnel sont présentés",
     "etapes": ["plan_detaille", "v1", "version_finale"]},
    {"id": "I3", "categorie": "Introduction", "label": "La problématique est clairement énoncée dans l'introduction",
     "etapes": ["plan_detaille", "v1", "version_finale"]},
    {"id": "I4", "categorie": "Introduction", "label": "Le plan (annonce des parties) est présent en fin d'introduction",
     "etapes": ["plan_detaille", "v1", "version_finale"]},
    {"id": "I5", "categorie": "Introduction", "label": "L'introduction crée un entonnoir du général au particulier",
     "etapes": ["plan_detaille", "v1", "version_finale"]},
    {"id": "I6", "categorie": "Introduction", "label": "Les motivations personnelles et/ou professionnelles sont évoquées",
     "etapes": ["plan_detaille", "v1", "version_finale"]},
    {"id": "I7", "categorie": "Introduction", "label": "L'introduction fait 1 à 2 pages maximum",
     "etapes": ["plan_detaille", "v1", "version_finale"]},

    # --- PARTIE THÉORIQUE (6 critères) ---
    {"id": "T1", "categorie": "Partie théorique", "label": "Les concepts clés sont définis avec des sources fiables",
     "etapes": ["v1", "version_finale"]},
    {"id": "T2", "categorie": "Partie théorique", "label": "Les sources sont variées (livres, articles, rapports)",
     "etapes": ["v1", "version_finale"]},
    {"id": "T3", "categorie": "Partie théorique", "label": "La revue de littérature est synthétique et non un simple copier-coller",
     "etapes": ["v1", "version_finale"]},
    {"id": "T4", "categorie": "Partie théorique", "label": "Les citations sont correctement référencées (auteur, année)",
     "etapes": ["v1", "version_finale"]},
    {"id": "T5", "categorie": "Partie théorique", "label": "Le lien entre théorie et problématique est explicite",
     "etapes": ["v1", "version_finale"]},
    {"id": "T6", "categorie": "Partie théorique", "label": "La partie théorique aboutit à des hypothèses ou un cadre d'analyse",
     "etapes": ["v1", "version_finale"]},

    # --- PARTIE PRATIQUE / TERRAIN (7 critères) ---
    {"id": "PR1", "categorie": "Partie pratique", "label": "La méthodologie de recherche est décrite et justifiée",
     "etapes": ["v1", "version_finale"]},
    {"id": "PR2", "categorie": "Partie pratique", "label": "Le terrain d'étude est présenté (entreprise, échantillon)",
     "etapes": ["v1", "version_finale"]},
    {"id": "PR3", "categorie": "Partie pratique", "label": "Les données collectées sont présentées de manière structurée",
     "etapes": ["v1", "version_finale"]},
    {"id": "PR4", "categorie": "Partie pratique", "label": "L'analyse des données est rigoureuse et argumentée",
     "etapes": ["v1", "version_finale"]},
    {"id": "PR5", "categorie": "Partie pratique", "label": "Les résultats sont mis en lien avec la partie théorique",
     "etapes": ["v1", "version_finale"]},
    {"id": "PR6", "categorie": "Partie pratique", "label": "Des exemples concrets illustrent les analyses",
     "etapes": ["v1", "version_finale"]},
    {"id": "PR7", "categorie": "Partie pratique", "label": "Les limites de l'étude sont mentionnées",
     "etapes": ["v1", "version_finale"]},

    # --- PRÉCONISATIONS (5 critères) ---
    {"id": "RE1", "categorie": "Préconisations", "label": "Les préconisations découlent logiquement de l'analyse",
     "etapes": ["v1", "version_finale"]},
    {"id": "RE2", "categorie": "Préconisations", "label": "Les préconisations sont concrètes et réalisables",
     "etapes": ["v1", "version_finale"]},
    {"id": "RE3", "categorie": "Préconisations", "label": "Les préconisations sont argumentées (pourquoi, comment)",
     "etapes": ["v1", "version_finale"]},
    {"id": "RE4", "categorie": "Préconisations", "label": "Un plan d'action ou planning de mise en œuvre est proposé",
     "etapes": ["v1", "version_finale"]},
    {"id": "RE5", "categorie": "Préconisations", "label": "Les préconisations répondent à la problématique",
     "etapes": ["v1", "version_finale"]},

    # --- CONCLUSION (4 critères) ---
    {"id": "C1", "categorie": "Conclusion", "label": "La conclusion synthétise les résultats principaux",
     "etapes": ["v1", "version_finale"]},
    {"id": "C2", "categorie": "Conclusion", "label": "La conclusion répond explicitement à la problématique",
     "etapes": ["v1", "version_finale"]},
    {"id": "C3", "categorie": "Conclusion", "label": "Une ouverture pertinente est proposée",
     "etapes": ["v1", "version_finale"]},
    {"id": "C4", "categorie": "Conclusion", "label": "La conclusion ne contient pas de nouveaux éléments",
     "etapes": ["v1", "version_finale"]},

    # --- FORME ET RÉDACTION (7 critères) ---
    {"id": "F1", "categorie": "Forme", "label": "L'orthographe et la grammaire sont soignées",
     "etapes": ["v1", "version_finale"]},
    {"id": "F2", "categorie": "Forme", "label": "Le style est professionnel et académique (pas de langage familier)",
     "etapes": ["v1", "version_finale"]},
    {"id": "F3", "categorie": "Forme", "label": "Les transitions entre parties sont fluides",
     "etapes": ["v1", "version_finale"]},
    {"id": "F4", "categorie": "Forme", "label": "La mise en page est homogène (polices, espacements, marges)",
     "etapes": ["v1", "version_finale"]},
    {"id": "F5", "categorie": "Forme", "label": "Le sommaire est présent et à jour",
     "etapes": ["v1", "version_finale"]},
    {"id": "F6", "categorie": "Forme", "label": "La bibliographie est présente et correctement formatée",
     "etapes": ["v1", "version_finale"]},
    {"id": "F7", "categorie": "Forme", "label": "Les annexes sont pertinentes et référencées dans le texte",
     "etapes": ["v1", "version_finale"]},
]


def get_criteres_for_etape(etape):
    """Retourne les critères applicables pour une étape donnée."""
    if etape == 'sujet':
        return []  # Évaluation libre pour le sujet
    return [c for c in CRITERES if etape in c['etapes']]


def get_criteres_by_categorie(etape):
    """Retourne les critères groupés par catégorie."""
    criteres = get_criteres_for_etape(etape)
    categories = {}
    for c in criteres:
        cat = c['categorie']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(c)
    return categories


SYSTEM_PROMPT = """Tu es un tuteur pédagogique expert en suivi de mémoires professionnels (niveau Bac+3 à Bac+5 en gestion de projet, management, RH, etc.).

Ton rôle :
- Évaluer le document soumis selon les critères fournis
- Être bienveillant mais rigoureux : encourager les points forts tout en identifiant clairement les axes d'amélioration
- Donner des commentaires précis avec des exemples tirés du document de l'apprenant
- Adapter ton niveau d'exigence selon l'étape (plus indulgent en V1, plus exigeant en version finale)

Tu dois TOUJOURS répondre en JSON valide selon le format demandé."""


def build_review_prompt(etape, document_text, previous_reviews=None):
    """Construit le prompt utilisateur pour l'analyse."""
    criteres = get_criteres_for_etape(etape)

    if etape == 'sujet':
        return _build_sujet_prompt(document_text, previous_reviews)

    criteres_text = "\n".join(
        f"- [{c['id']}] {c['categorie']} : {c['label']}"
        for c in criteres
    )

    exigence = "bienveillante (c'est un travail en cours)" if etape == 'v1' \
        else "exigeante (c'est le rendu final)" if etape == 'version_finale' \
        else "constructive"

    historique = ""
    if previous_reviews:
        historique = "\n\n--- HISTORIQUE DES RETOURS PRÉCÉDENTS ---\n"
        for rev in previous_reviews:
            historique += f"\nÉtape : {rev['etape']} ({rev['created_at']})\n"
            historique += f"Appréciation : {rev.get('appreciation', 'N/A')}\n"
            historique += f"Améliorations demandées : {rev.get('ameliorations', 'N/A')}\n"
        historique += "\nSi l'apprenant a tenu compte des retours précédents, mentionne-le positivement. Si des points n'ont pas été corrigés, signale-le.\n"

    prompt = f"""Analyse le document suivant pour l'étape « {etape} » d'un mémoire professionnel.

Évaluation {exigence}.

CRITÈRES À ÉVALUER :
{criteres_text}
{historique}
DOCUMENT DE L'APPRENANT :
\"\"\"
{document_text}
\"\"\"

Réponds en JSON avec EXACTEMENT ce format :
{{
  "criteres": [
    {{
      "id": "P1",
      "label": "La problématique est formulée sous forme de question",
      "categorie": "Problématique",
      "statut": "OK",
      "commentaire": "Ton commentaire précis avec exemple du document"
    }}
  ],
  "points_forts": "Liste des 2-3 points forts principaux, avec exemples du document",
  "ameliorations": "Liste des 2-3 améliorations prioritaires, avec suggestions concrètes",
  "appreciation": "Appréciation générale de 3-4 phrases, ton pédagogique et encourageant"
}}

Règles pour le champ "statut" :
- "OK" : le critère est rempli de manière satisfaisante
- "Partiel" : le critère est partiellement rempli, des améliorations sont nécessaires
- "Non" : le critère n'est pas rempli ou absent

IMPORTANT : Évalue CHAQUE critère listé ci-dessus. Le nombre de critères dans ta réponse doit correspondre exactement au nombre de critères fournis."""

    return prompt


def _build_sujet_prompt(document_text, previous_reviews=None):
    """Prompt spécifique pour l'évaluation du sujet (évaluation libre)."""
    return f"""Analyse le sujet de mémoire suivant.

IMPORTANT — DISTINCTION SUJET / PROBLÉMATIQUE :
Le « sujet » est le futur TITRE du mémoire. Il définit le thème général et le périmètre large de la réflexion. Il est plus généraliste et englobant que la problématique.
La « problématique » (évaluée à une étape ultérieure) est une question de recherche précise, délimitée, à laquelle le mémoire devra répondre.
À cette étape, l'apprenant propose uniquement son SUJET (titre). Il n'a pas encore formulé de problématique. Tu dois donc évaluer la qualité du sujet en tant que titre de mémoire, sans exiger de problématique. Tu peux en revanche suggérer des pistes de problématiques que ce sujet pourrait soulever.

Évalue les points suivants :
- La pertinence du sujet par rapport à un mémoire professionnel en AMOA
- Le périmètre : le sujet est-il suffisamment cadré pour un mémoire tout en restant assez large pour permettre une réflexion approfondie ?
- La faisabilité (accès aux données, terrain d'étude envisageable)
- L'originalité et l'intérêt du sujet
- La clarté et la qualité de la formulation en tant que titre de mémoire
- Les pistes de problématiques que ce sujet pourrait soulever (suggestions pour l'étape suivante)
- L'ancrage dans le référentiel de compétences RNCP AMOA (voir ci-dessous)

RÉFÉRENTIEL DES 46 COMPÉTENCES RNCP - Consultant AMOA (RNCP35269) :

BC01 - Etude des besoins métier et études fonctionnelles :
1. Réaliser un diagnostic de la situation existante en décrivant et en évaluant les forces et faiblesses de l'organisation, des processus et du SI existants
2. Modéliser des processus métiers en définissant des cas d'utilisation afin de cadrer le périmètre global du projet
3. Détailler la cible métier en termes d'organisation, de processus et de SI sur la base d'une étude comparative de différents scénarios de changement
4. Recueillir et formaliser les besoins métier en utilisant diverses techniques de collecte et de formalisation de l'information
5. Rationaliser la gestion des besoins en utilisant des outils informatiques pour industrialiser la gestion des besoins métier
6. Etudier des solutions informatiques en élaborant une grille de choix pour comparer plusieurs solutions
7. Modéliser une architecture fonctionnelle en formalisant les composants du SI et leurs interactions
8. Réaliser ou valider l'analyse fonctionnelle d'une solution informatique en décrivant les fonctionnalités attendues et les règles de gestion

BC02 - Test des solutions informatiques :
9. Définir la stratégie de test d'une solution informatique en précisant les modalités des procédures tests
10. Concevoir le plan de tests fonctionnel d'une solution informatique en élaborant des scénarios de tests
11. Concevoir le plan de tests métier pour couvrir les process métier
12. Constituer un patrimoine de tests de non-régression (TNR)
13. Exécuter des scénarios de test en analysant les résultats des tests
14. Exécuter des tests métier en accompagnant les utilisateurs dans le déroulement de ces tests
15. Suivre la résolution des anomalies en assurant la remontée et la qualification des anomalies
16. Faire un bilan des tests réalisés en détaillant les résultats obtenus
17. Faire des tests post-mise en service de la solution informatique
18. Faciliter la gestion et l'automatisation des tests en utilisant des outils informatiques
19. Accompagner la mise en œuvre des processus de tests (DevOps, Intégration Continue)

BC03 - Coordination et gestion de projet :
20. Définir les objectifs et les enjeux du projet au niveau de l'organisation, des processus et du SI
21. Définir la valeur ajoutée et la rentabilité du projet (retour sur investissement)
22. Définir une organisation projet en choisissant une méthodologie adaptée
23. Définir les risques associés à un projet en les priorisant
24. Définir le planning d'un projet en tenant compte des différents chantiers et du chemin critique
25. Définir la gestion documentaire à mettre en œuvre dans le projet
26. Préparer les comités de pilotage ou de direction
27. Suivre le budget d'un projet en mettant en place des outils de suivi budgétaire
28. Coordonner les activités du projet en fonction de la méthodologie
29. Gérer les conflits au sein de l'équipe projet
30. Assurer une bonne communication ascendante et descendante au sein de l'équipe projet
31. Identifier les parties prenantes et catégoriser les utilisateurs et acteurs impactés
32. Réaliser une étude d'impact sur les activités des groupes d'utilisateurs
33. Accompagner le changement en planifiant des actions de communication et de formation
34. Définir le support utilisateur à mettre en place une fois le projet en production
35. Etablir une stratégie de déploiement de la solution informatique

BC04 - Travail en contexte Agile :
36. Personnifier les différentes catégories d'utilisateurs (Persona)
37. Définir la vision du Produit informatique pour évaluer l'opportunité du lancement du projet
38. Formaliser une liste initiale des besoins métier sous forme de Product Backlog (épopées et récits utilisateurs)
39. Animer une réunion de planification de sprint
40. Gérer le product backlog (ajout, modification, suppression, repriorisation des user stories)
41. Collecter le feedback des utilisateurs lors des revues de sprint
42. Définir les hypothèses et le périmètre du produit minimum nécessaire (MVP, MMF, MMR, MMP)
43. Définir des jalons de mise à disposition des versions majeures (plan de release)
44. Animer les réunions d'équipes (cérémonies Agile)
45. S'assurer que toutes les parties prenantes comprennent et acceptent la méthodologie Agile retenue
46. Définir les rôles et responsabilités des membres d'une équipe Agile à l'échelle

VÉRIFICATION OBLIGATOIRE - COMPÉTENCES RNCP :
L'apprenant DOIT mentionner au moins 3 compétences du référentiel ci-dessus que son sujet de mémoire permettra de mobiliser. Vérifie si le document mentionne explicitement des compétences du référentiel RNCP AMOA. Si au moins 3 compétences sont identifiées, le critère est "OK". Si 1 ou 2 sont identifiées, le critère est "Partiel". Si aucune n'est mentionnée, le critère est "Non". Dans tous les cas, liste les compétences identifiées (par leur numéro et intitulé) et suggère des compétences pertinentes par rapport au sujet si l'apprenant n'en a pas mentionné suffisamment.

SUJET PROPOSÉ :
\"\"\"
{document_text}
\"\"\"

Réponds en JSON avec EXACTEMENT ce format :
{{
  "criteres": [
    {{
      "id": "S1",
      "label": "Pertinence du sujet en tant que titre de mémoire AMOA",
      "categorie": "Sujet",
      "statut": "OK",
      "commentaire": "Le sujet est-il en lien avec le métier de consultant AMOA et adapté à un mémoire professionnel ?"
    }},
    {{
      "id": "S2",
      "label": "Périmètre et cadrage du sujet",
      "categorie": "Sujet",
      "statut": "OK",
      "commentaire": "Le sujet est-il suffisamment cadré sans être trop restrictif ? Permet-il une réflexion approfondie ?"
    }},
    {{
      "id": "S3",
      "label": "Faisabilité",
      "categorie": "Sujet",
      "statut": "OK",
      "commentaire": "L'apprenant pourra-t-il accéder à un terrain d'étude et à des données pour traiter ce sujet ?"
    }},
    {{
      "id": "S4",
      "label": "Originalité et intérêt",
      "categorie": "Sujet",
      "statut": "OK",
      "commentaire": "Le sujet apporte-t-il un angle intéressant ou une plus-value par rapport aux sujets classiques ?"
    }},
    {{
      "id": "S5",
      "label": "Qualité de la formulation du titre",
      "categorie": "Sujet",
      "statut": "OK",
      "commentaire": "Le titre est-il clair, concis et évocateur du contenu du mémoire ?"
    }},
    {{
      "id": "S6",
      "label": "Pistes de problématiques envisageables",
      "categorie": "Sujet",
      "statut": "OK",
      "commentaire": "Quelles questions de recherche précises ce sujet pourrait-il soulever ? (suggestions pour l'étape suivante)"
    }},
    {{
      "id": "S7",
      "label": "Ancrage dans le référentiel RNCP AMOA (min. 3 compétences)",
      "categorie": "Référentiel RNCP",
      "statut": "OK",
      "commentaire": "Liste des compétences RNCP identifiées dans le document et suggestions de compétences pertinentes si moins de 3 sont mentionnées"
    }}
  ],
  "points_forts": "Points forts du sujet",
  "ameliorations": "Suggestions d'amélioration ou de recentrage",
  "appreciation": "Appréciation générale encourageante de 3-4 phrases"
}}"""
