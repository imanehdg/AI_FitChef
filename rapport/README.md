# Rapport du projet AI FitChef

\documentclass[a4paper, 12pt, twoside]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}		
\usepackage[francais]{babel}
\usepackage{lmodern}
\usepackage{ae,aecompl}
\usepackage[top=2.5cm, bottom=2cm, 
			left=3cm, right=2.5cm,
			headheight=15pt]{geometry}
\usepackage{graphicx}
\usepackage{eso-pic}
\usepackage{array} 
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}

% Configuration pour le code
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
\lstset{style=mystyle}

\input{pagedegarde}

\title{AI FitChef - Générateur de recettes personnalisées avec IA}
\entreprise{}
\datedebut{Octobre 2025}
\datefin{06 janvier 2026}

\membrea{HADDAG Imane - 45008401}
\membreb{TAMANI Sarah - 45004397}
\membrec{}
\membred{}
\membree{}

\begin{document}
\pagedegarde

\begin{center}
\vspace{1cm}
\textbf{Lien du dépôt GitHub :} \\
\url{https://github.com/imanehdg/AI_FitChef.git}
\vspace{0.5cm}

\textbf{Lien du site hébergé :} \\
\url{https://imanehdg.pythonanywhere.com/}
\end{center}

\newpage
\section*{Remerciements}
Nous tenons à remercier M. François Delbot, notre enseignant de projet informatique, pour son accompagnement tout au long de ce projet. Nous remercions également l'Université Paris Nanterre pour nous avoir fourni les ressources nécessaires à la réalisation de cette application web innovante.

\newpage
\tableofcontents
\newpage

\section{Introduction}

Dans un contexte où l'alimentation saine et l'utilisation de l'intelligence artificielle sont de plus en plus importantes, nous avons développé AI FitChef, une application web qui combine nutrition personnalisée et technologies d'IA pour aider les utilisateurs à mieux manger.

Le projet AI FitChef est né d'un constat simple : beaucoup de personnes souhaitent adopter une alimentation plus saine mais ne savent pas comment s'organiser ni quelles recettes choisir en fonction de leurs objectifs et des ingrédients disponibles dans leur frigo. Notre solution propose un système de recommandations personnalisées basé sur le profil utilisateur et une fonctionnalité innovante de détection automatique d'ingrédients par photo.

L'objectif principal est de créer une plateforme web complète et accessible qui permette à chacun de planifier ses repas de manière intelligente et adaptée à ses besoins spécifiques, tout en découvrant de nouvelles recettes équilibrées.

\section{Environnement de travail}

Notre projet a été développé dans l'environnement technique suivant :

\begin{itemize}
    \item \textbf{Système d'exploitation :} Windows 11 et macOS (développement collaboratif)
    \item \textbf{Environnement de développement :} Visual Studio Code avec extensions Python et Flask
    \item \textbf{Langages de programmation :} 
    \begin{itemize}
        \item Python 3.11 (backend)
        \item HTML5, CSS3, JavaScript (frontend)
        \item SQL pour la base de données
    \end{itemize}
    \item \textbf{Gestionnaire de versions :} Git 2.42 avec GitHub pour l'hébergement du code
    \item \textbf{Plateforme d'hébergement :} PythonAnywhere pour le déploiement
\end{itemize}

\section{Description du projet et objectifs}

\subsection{Présentation générale}

AI FitChef est une application web de nutrition intelligente qui utilise plusieurs modèles d'intelligence artificielle pour offrir une expérience personnalisée. L'application s'adresse à toute personne souhaitant améliorer son alimentation, que ce soit pour perdre du poids, prendre de la masse musculaire ou simplement maintenir une alimentation équilibrée.

Les utilisateurs cibles sont principalement des jeunes adultes et adultes actifs qui cherchent des solutions pratiques pour mieux s'alimenter au quotidien, sans avoir besoin de connaissances approfondies en nutrition.

\subsection{Objectifs du projet}

Les objectifs principaux que nous nous sommes fixés sont :

\textbf{Objectifs fonctionnels :}
\begin{itemize}
    \item Créer un système d'authentification sécurisé avec profils personnalisés
    \item Développer un système de recommandations de recettes basé sur les objectifs utilisateur
    \item Implémenter une fonctionnalité de détection d'ingrédients par photo utilisant l'IA
    \item Générer des plannings alimentaires hebdomadaires personnalisés avec l'IA Groq
    \item Créer un système de motivation avec challenges quotidiens et suivi de progression
    \item Intégrer un chatbot nutritionnel intelligent utilisant Groq
\end{itemize}

\textbf{Objectifs techniques :}
\begin{itemize}
    \item Maîtriser le framework Flask pour le développement web en Python
    \item Intégrer des API d'intelligence artificielle (Groq et Mistral)
    \item Concevoir et gérer une base de données SQLite
    \item Déployer une application web fonctionnelle en ligne
    \item Créer une interface utilisateur moderne et responsive
\end{itemize}

\section{Bibliothèques, Outils et technologies}

\subsection{Framework et bibliothèques Python}

\begin{itemize}
    \item \textbf{Flask 3.0} : Framework web léger utilisé comme base de notre application. Il gère le routing, les sessions utilisateur et le rendu des templates HTML.
    
    \item \textbf{SQLite3} : Système de gestion de base de données intégré à Python. Nous l'utilisons pour stocker les utilisateurs, recettes, données de motivation et messages de contact.
    
    \item \textbf{Werkzeug} : Bibliothèque de sécurité fournie avec Flask pour le hachage des mots de passe (generate\_password\_hash, check\_password\_hash) et la gestion sécurisée des fichiers uploadés.
    
    \item \textbf{Groq} : SDK Python pour interagir avec l'API Groq qui utilise le modèle Llama 3.3 70B. Utilisé pour générer les plannings alimentaires et alimenter le chatbot nutritionnel.
    
    \item \textbf{Mistral AI (Pixtral 12B)} : Modèle de vision multimodal utilisé pour la détection automatique d'ingrédients à partir de photos du frigo.
    
    \item \textbf{python-dotenv} : Gestion sécurisée des clés API via un fichier .env, évitant leur exposition dans le code source.
\end{itemize}

\subsection{Technologies frontend}

\begin{itemize}
    \item \textbf{HTML5 et Jinja2} : Templates dynamiques pour générer les pages web avec données du backend
    \item \textbf{CSS3 personnalisé} : Design moderne avec animations, dégradés et effets hover
    \item \textbf{JavaScript vanilla} : Gestion des interactions côté client (upload de fichiers, appels API asynchrones, animations)
    \item \textbf{Font Awesome 6.4} : Bibliothèque d'icônes pour enrichir l'interface utilisateur
\end{itemize}

\subsection{Outils de développement}

\begin{itemize}
    \item \textbf{Git et GitHub} : Gestion de versions et collaboration. Le dépôt contient tout l'historique du projet.
    \item \textbf{PythonAnywhere} : Plateforme d'hébergement cloud spécialisée Python, permettant le déploiement gratuit de notre application.
    \item \textbf{Visual Studio Code} : Éditeur de code avec extensions Flask, Python et Git pour un développement efficace.
\end{itemize}

\section{Travail réalisé}

\subsection{Fonctionnalités réalisées}

\begin{itemize}
    \item \checkmark \textbf{Système d'authentification complet} : Inscription avec création de profil personnalisé (taille, poids, objectif, niveau d'activité), connexion sécurisée avec mots de passe hachés, gestion de sessions Flask, et page de profil avec calcul automatique de l'IMC et des calories recommandées.
    
    \item \checkmark \textbf{Recommandations de recettes intelligentes} : Base de données de recettes avec photos, filtrage automatique selon l'objectif utilisateur (perte/gain/maintien), affichage des informations nutritionnelles (calories, temps de préparation), et système de recherche et d'affichage détaillé des recettes.
    
    \item \checkmark \textbf{Scanner de frigo IA} : Upload de photos du frigo, détection automatique d'ingrédients avec Mistral Pixtral 12B, recherche de recettes correspondant aux ingrédients détectés, système de scoring (recettes 100\% compatibles vs partielles), et affichage des ingrédients manquants.
    
    \item \checkmark \textbf{Générateur de planning hebdomadaire IA} : Génération de menus complets pour 7 jours via l'API Groq, personnalisation selon le profil utilisateur (objectif et calories), structure complète (petit-déjeuner, collations, déjeuner, dîner), affichage interactif jour par jour, et calcul automatique des calories quotidiennes.
    
    \item \checkmark \textbf{Système de motivation gamifié} : Challenges quotidiens aléatoires, suivi de progression avec barre de pourcentage, compteur de jours consécutifs (streak), statistiques personnelles (meilleur série, total complété), citations motivantes aléatoires, et conseils nutrition personnalisés.
    
    \item \checkmark \textbf{Chatbot nutritionnel IA} : Chat en temps réel propulsé par Groq (Llama 3.3), réponses personnalisées sur la nutrition et les recettes, interface moderne avec animations de typing, historique de conversation, et boutons de réponses rapides.
    
    \item \checkmark \textbf{Page de contact fonctionnelle} : Formulaire de contact avec validation, stockage des messages dans la base de données, informations de l'équipe avec liens LinkedIn, carte Google Maps de l'université.
    
    \item \checkmark \textbf{Design moderne et responsive} : Interface adaptée mobile/tablette/desktop, animations CSS fluides, navigation intuitive avec navbar fixe, footer complet avec réseaux sociaux, et palette de couleurs cohérente (vert/orange).
\end{itemize}

\subsection{Fonctionnalités non réalisées}

\begin{itemize}
    \item $\times$ \textbf{Système de favoris et likes} : Prévu initialement pour permettre aux utilisateurs de sauvegarder leurs recettes préférées. Raison : temps insuffisant pour implémenter cette fonctionnalité annexe, nous avons priorisé les fonctionnalités IA principales.
    
    \item $\times$ \textbf{Export PDF du planning} : Téléchargement du planning hebdomadaire en PDF. Raison : complexité technique (bibliothèque ReportLab) par rapport au temps disponible.
\end{itemize}

\subsection{Répartition du travail}

\begin{table}[h]
\begin{center}
\begin{tabular}{|l|p{10cm}|}
\hline 
\textbf{Membre} & \textbf{Tâches réalisées} \\ 
\hline 
Imane HADDAG & 
\begin{itemize}
    \item Développement du système d'authentification et gestion des profils
    \item Intégration de l'API Mistral pour la détection d'ingrédients
    \item Création de la base de données et requêtes SQL
    \item Création du chatbot nutritionnel IA
    \item Déploiement sur PythonAnywhere
    \item Gestion du dépôt GitHub
\end{itemize}
\\ 
\hline 
Sarah TAMANI & 
\begin{itemize}
    \item Développement du générateur de planning avec l'API Groq
    \item Design CSS de la page d'accueil et du système de motivation
    \item Design CSS des pages recettes et frigo
    \item Intégration des animations JavaScript
    \item Page de contact et formulaire
    \item Tests et debugging général
\end{itemize}
\\ 
\hline 
\end{tabular} 
\end{center}
\caption{Répartition réelle du travail entre les membres}
\label{repartition}
\end{table}

\section{Utilisation de l'IA dans le projet}

\subsection{Comment l'IA nous a aidés dans le développement}

L'intelligence artificielle a joué un rôle crucial à deux niveaux : comme outil d'aide au développement et comme fonctionnalité principale de notre application.

\textbf{Aide au développement :}

\begin{itemize}
    \item \textbf{Génération et débogage de code} : Nous avons utilisé Claude AI et ChatGPT pour générer des structures de code Flask, notamment pour les routes complexes et la gestion des sessions. Par exemple, Claude nous a aidé à créer le système de détection d'ingrédients en suggérant la structure de la fonction detect\_food\_with\_ai().
    
    
    \item \textbf{Débogage} : Lorsque nous rencontrions des erreurs (notamment avec l'API Groq), nous copions l'erreur dans Claude ou ChatGPT qui nous expliquait la cause et proposait des solutions. Cela nous a fait gagner beaucoup de temps.
    
    \item \textbf{CSS et design} : Pour créer les animations et effets visuels modernes, nous avons demandé à l'IA de suggérer des propriétés CSS avancées (transitions, keyframes, gradients).
\end{itemize}

\subsection{Fonctionnement de l'IA intégrée dans l'application}

Notre application utilise trois modèles d'IA différents pour des tâches spécifiques :

\textbf{1. Mistral Pixtral 12B (Vision multimodale) - Détection d'ingrédients :}

Ce modèle analyse les photos du frigo uploadées par l'utilisateur. Le processus est le suivant :
\begin{enumerate}
    \item L'utilisateur upload une photo via la page /frigo
    \item L'image est encodée en base64
    \item L'API Mistral reçoit l'image avec un prompt spécifique lui demandant de lister tous les aliments visibles
    \item Le modèle renvoie une liste d'ingrédients en français
    \item Notre application parse cette réponse et recherche les recettes compatibles dans la base de données
\end{enumerate}

Exemple de prompt utilisé :
\begin{lstlisting}[language=Python]
"Analyse cette image et liste TOUS les aliments visibles.
Liste les noms des aliments en francais
Separe-les par des virgules
Noms simples (ex: 'tomate' pas 'tomate rouge')
EXEMPLE: tomate, carotte, poivron, concombre"
\end{lstlisting}

\textbf{2. Groq (Llama 3.3 70B) - Génération de plannings :}

Ce modèle génère des menus hebdomadaires personnalisés. Le processus :
\begin{enumerate}
    \item Récupération du profil utilisateur (poids, taille, objectif, activité)
    \item Calcul des besoins caloriques avec une formule de Harris-Benedict
    \item Envoi d'un prompt structuré à Groq demandant un planning JSON
    \item Le modèle génère 7 jours complets avec 5 repas par jour
    \item Affichage interactif du planning sur la page web
\end{enumerate}

\textbf{3. Groq (Llama 3.3 70B) - Chatbot nutritionnel :}

Le chatbot fonctionne en temps réel :
\begin{enumerate}
    \item L'utilisateur tape une question dans le chat
    \item JavaScript envoie la question à notre API Flask (/api/chatbot)
    \item Flask transmet la question à Groq avec un system prompt définissant le rôle du bot
    \item Groq génère une réponse courte et personnalisée
    \item La réponse s'affiche avec une animation de typing dans l'interface
\end{enumerate}

System prompt du chatbot :
\begin{lstlisting}[language=Python]
"Tu es FitChef IA, un coach nutrition bienveillant 
et expert en francais. Reponds de maniere concise 
(2-4 phrases max). Utilise des emojis. Donne des 
conseils pratiques et realistes."
\end{lstlisting}

\textbf{Architecture technique :}

\begin{itemize}
    \item Les clés API sont stockées de manière sécurisée dans un fichier .env
    \item Les appels API sont gérés côté serveur (Flask) pour protéger les clés

\end{itemize}

\section{Difficultés rencontrées}

\subsection{Difficultés techniques}

\begin{itemize}
    \item \textbf{Intégration de Mistral Pixtral} : La documentation de l'API Mistral était moins détaillée que celle de Groq. Nous avons dû faire plusieurs tests pour comprendre le bon format d'envoi des images en base64. Solution : Après plusieurs essais et consultation de la documentation officielle, nous avons réussi à implémenter l'encodage correct et à structurer le prompt de manière optimale.
    
    \item \textbf{Parsing des réponses JSON de Groq} : Groq renvoyait parfois le JSON entouré de balises markdown ```json qui cassaient le parsing. Solution : Nous avons ajouté un système de nettoyage de la réponse qui retire ces balises avant le json.loads().
    
    
    \item \textbf{Upload et stockage des images} : Gestion sécurisée des fichiers uploadés avec vérification des extensions et secure\_filename(). Solution : Création d'un dossier static/uploads avec vérification des types MIME autorisés.
 
\end{itemize}

\subsection{Difficultés organisationnelles}

\begin{itemize}
    \item \textbf{Coordination à distance} : Travail en binôme.
    
    \item \textbf{Gestion du temps} : Projet à réaliser en parallèle d'autres cours et examens. Solution : Création d'un planning répartition claire des tâches.
    
    \item \textbf{Compréhension des APIs IA} : Première fois que nous utilisions des APIs d'IA professionnelles. Solution : Aide de l'IA pour comprendre les concepts.
\end{itemize}

\section{Bilan}

\subsection{Conclusion}

Le projet AI FitChef a été une expérience enrichissante qui nous a permis de développer des compétences techniques variées tout en créant une application concrète et utilisable. Nous avons atteint la majorité de nos objectifs initiaux et livrons un produit fonctionnel et déployé en ligne.

\textbf{Compétences acquises :}
\begin{itemize}
    \item Maîtrise de Flask et du développement web en Python
    \item Intégration d'APIs d'intelligence artificielle (Groq, Mistral)
    \item Conception et gestion de bases de données relationnelles
    \item Design frontend moderne avec CSS3 et JavaScript
    \item Déploiement d'applications web sur le cloud
    \item Travail collaboratif avec Git et GitHub
    \item Gestion de projet agile (sprints, jalons, répartition des tâches)
\end{itemize}

\textbf{Points forts du projet :}
\begin{itemize}
    \item Application fonctionnelle et déployée en ligne
    \item Intégration réussie de plusieurs modèles d'IA
    \item Interface utilisateur moderne et intuitive
    \item Code structuré et commenté
    \item Fonctionnalités variées et cohérentes entre elles
\end{itemize}

\textbf{Satisfaction personnelle :}

Nous sommes très satisfaites du résultat final. AI FitChef est une application que nous-mêmes utiliserions au quotidien. Ce projet nous a confirmé notre intérêt pour le développement web et l'intelligence artificielle.

\subsection{Perspectives}

Pour une version future d'AI FitChef, voici les améliorations envisagées :

\textbf{Améliorations techniques :}
\begin{itemize}
    \item Migration vers PostgreSQL pour une meilleure scalabilité
    \item Ajout de tests unitaires avec pytest
    \item Implémentation d'une API REST complète pour permettre le développement d'une application mobile
    \item Amélioration de la détection d'ingrédients avec fine-tuning du modèle Mistral
\end{itemize}

\textbf{Nouvelles fonctionnalités :}
\begin{itemize}
    \item Système de favoris et de sauvegarde de recettes
    \item Communauté avec partage de recettes entre utilisateurs
    \item Intégration avec des objets connectés (balances, montres)
    \item Recommandations de courses automatiques basées sur le planning
    \item Suivi nutritionnel détaillé (macros, vitamines, minéraux)
    \item Mode végétarien/végétalien/sans gluten
    \item Version mobile native (iOS et Android)
\end{itemize}

\textbf{Évolutions business :}
\begin{itemize}
    \item Partenariats avec nutritionnistes pour valider les conseils
    \item Monétisation via abonnement premium (plus de recettes, coaching personnalisé)
    \item Partenariats avec des supermarchés pour la livraison d'ingrédients
\end{itemize}

Le projet AI FitChef est une base solide qui pourrait réellement se transformer en startup dans le domaine de la FoodTech et de la santé connectée.

\newpage
\section{Bibliographie}

\renewcommand{\bibname}{}
\renewcommand{\refname}{}
\begin{thebibliography}{9}
   \bibitem{flask} Miguel Grinberg, \textit{Flask Web Development, 2nd Edition}, O'Reilly Media, 2018
   
   \bibitem{groq} Groq Documentation, \textit{Groq API Reference - LLaMA Models}, Groq Inc., 2024
   
   \bibitem{mistral} Mistral AI, \textit{Pixtral 12B - Multimodal Vision Language Model}, Mistral AI Documentation, 2024
   
   \bibitem{python} Mark Lutz, \textit{Learning Python, 5th Edition}, O'Reilly Media, 2013
\end{thebibliography}

\newpage
\section{Webographie}

\begin{thebibliography}{9}
   \bibitem{flask-doc} Documentation officielle Flask : \url{https://flask.palletsprojects.com/}
   
   \bibitem{groq-api} API Groq : \url{https://console.groq.com/docs}
   
   \bibitem{mistral-doc} Documentation Mistral AI : \url{https://docs.mistral.ai/}
   
   \bibitem{mdn} Mozilla Developer Network - Web Docs : \url{https://developer.mozilla.org/}
   
   \bibitem{pythonanywhere} PythonAnywhere Documentation : \url{https://help.pythonanywhere.com/}
   
   \bibitem{github} GitHub du projet : \url{https://github.com/imanehdg/AI_FitChef.git}
\end{thebibliography}

\newpage
\section{Annexes}

\appendix
\makeatletter
\def\@seccntformat#1{Annexe~\csname the#1\endcsname:\quad}
\makeatother

\section{Cahier des charges}

\subsection{Contexte}

Réalisation d'une application web de nutrition personnalisée utilisant l'intelligence artificielle pour aider les utilisateurs à mieux s'alimenter selon leurs objectifs.

\subsection{Objectifs fonctionnels}

\begin{itemize}
    \item Authentification utilisateur sécurisée
    \item Profils personnalisés avec calculs nutritionnels
    \item Recommandations de recettes adaptées
    \item Détection d'ingrédients par photo (IA)
    \item Génération de plannings hebdomadaires (IA)
    \item Système de motivation gamifié
    \item Chatbot nutritionnel intelligent (IA)
    \item Interface moderne et responsive
\end{itemize}

\subsection{Contraintes techniques}

\begin{itemize}
    \item Framework : Flask (Python)
    \item Base de données : SQLite
    \item APIs IA : Groq et Mistral
    \item Hébergement : PythonAnywhere
    \item Frontend : HTML5, CSS3, JavaScript vanilla
    \item Responsive design (mobile, tablette, desktop)
\end{itemize}

\subsection{Livrables}

\begin{itemize}
    \item Code source sur GitHub
    \item Application déployée en ligne
    \item Documentation technique (ce rapport)
    \item Base de données avec données de test
\end{itemize}

\section{Exemple d'exécution du projet}

\textit{Note : Les captures d'écran suivantes montrent l'application en fonctionnement réel sur \url{https://imanehdg.pythonanywhere.com/}}

\subsection{Page d'accueil}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_accueil.png}}
\caption{Page d'accueil avec présentation des recettes et navigation}
\label{fig:accueil}
\end{figure}

L'utilisateur arrive sur une page moderne avec une navigation claire. Les recettes sont présentées sous forme de cercles attractifs avec images. Le chatbot IA est accessible en bas à droite.

\subsection{Inscription et profil}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_register.png}}
\caption{Formulaire d'inscription avec saisie du profil nutritionnel}
\label{fig:register}
\end{figure}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_login.png}}
\caption{Formulaire de connexion }
\label{fig:login}
\end{figure}

L'utilisateur crée son compte en renseignant ses informations (nom, mot de passe, taille, poids, objectif, niveau d'activité). Le système calcule automatiquement l'IMC et les besoins caloriques.


\subsection{Scanner de frigo IA}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_frigo.png}}
\caption{Interface d'upload de photo du frigo}
\label{fig:frigo}
\end{figure}

L'utilisateur peut prendre une photo de son frigo et l'uploader. Le système affiche un aperçu de l'image avant l'analyse.

\subsection{Résultat de la détection IA}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_frigo2.png}}
\caption{Résultat de l'analyse : ingrédients détectés et recettes suggérées}
\label{fig:frigo_result}
\end{figure}

Mistral Pixtral analyse l'image et liste tous les ingrédients détectés (tomates, carottes, etc.). Le système affiche ensuite les recettes compatibles avec un système de scoring (100\% compatible, partiellement compatible).

\subsection{Planning hebdomadaire IA}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_planning.png}}
\caption{Planning alimentaire généré par l'IA Groq pour 7 jours}
\label{fig:planning}
\end{figure}

L'utilisateur clique sur "Générer mon planning" et Groq génère automatiquement un menu complet pour la semaine avec 5 repas par jour adaptés à son profil.

\subsection{Page Motivation}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_motivation.png}}
\caption{Espace motivation avec challenges, streak et conseils IA}
\label{fig:motivation}
\end{figure}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_motivation2.png}}
\caption{Espace motivation avec challenges, streak et conseils IA}
\label{fig:motivation}
\end{figure}

L'utilisateur peut suivre son challenge du jour, voir son nombre de jours consécutifs (streak), et recevoir des conseils personnalisés. Le système est gamifié pour encourager la régularité.

\subsection{Chatbot nutritionnel}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_chatbot.png}}
\caption{Chatbot IA en temps réel propulsé par Groq}
\label{fig:chatbot}
\end{figure}

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.9\textwidth]{capture_recette.png}}
\caption{Recettes proposées}
\label{fig:recettes}
\end{figure}

Le chatbot répond en temps réel à toutes les questions sur la nutrition, les recettes, et les objectifs fitness. L'interface affiche une animation de typing pendant que l'IA génère sa réponse.

\section{Manuel utilisateur}

\subsection{Inscription et première connexion}

\begin{enumerate}
    \item Rendez-vous sur \url{https://imanehdg.pythonanywhere.com/}
    \item Cliquez sur "Inscription" dans le menu
    \item Remplissez le formulaire :
    \begin{itemize}
        \item Nom d'utilisateur unique
        \item Mot de passe sécurisé
        \item Taille en centimètres
        \item Poids en kilogrammes
        \item Objectif (perte/gain/maintien)
        \item Niveau d'activité (sédentaire/moyenne/sportif)
    \end{itemize}
    \item Cliquez sur "Créer mon compte"
    \item Vous êtes redirigé vers la page de connexion
    \item Entrez vos identifiants et connectez-vous
\end{enumerate}

\subsection{Consulter son profil}

\begin{enumerate}
    \item Une fois connecté, cliquez sur "Mon Profil" dans le menu
    \item Vous verrez votre tableau de bord avec :
    \begin{itemize}
        \item Votre taille, poids, IMC calculé automatiquement
        \item Vos besoins caloriques quotidiens
        \item Votre objectif et niveau d'activité
    \end{itemize}
    \item Pour modifier vos informations, cliquez sur "Modifier profil"
\end{enumerate}

\subsection{Découvrir les recettes}

\begin{enumerate}
    \item Cliquez sur "Recettes" dans le menu
    \item Les recettes affichées sont automatiquement filtrées selon votre objectif
    \item Cliquez sur une recette pour voir :
    \begin{itemize}
        \item Liste des ingrédients
        \item Instructions détaillées
        \item Temps de préparation
        \item Nombre de calories
        \item Photo de la recette
    \end{itemize}
\end{enumerate}

\subsection{Scanner son frigo}

\begin{enumerate}
    \item Cliquez sur "Mon Frigo" dans le menu
    \item Prenez une photo claire de votre frigo ou choisissez une photo existante
    \item Cliquez sur "Parcourir mes fichiers" et sélectionnez votre image
    \item Un aperçu s'affiche, vérifiez que l'image est claire
    \item Cliquez sur "Analyser mon frigo"
    \item \textbf{L'IA analyse l'image} (cela prend 5-10 secondes)
    \item La page de résultats affiche :
    \begin{itemize}
        \item Tous les ingrédients détectés
        \item Les recettes 100\% compatibles en premier
        \item Les recettes partiellement compatibles avec les ingrédients manquants
    \end{itemize}
\end{enumerate}

\subsection{Générer un planning hebdomadaire}

\begin{enumerate}
    \item Cliquez sur "Planning" dans le menu
    \item Cliquez sur le bouton "Générer mon planning personnalisé"
    \item \textbf{L'IA génère votre planning} (15-30 secondes)
    \item Le planning s'affiche avec 7 colonnes (une par jour)
    \item Chaque jour contient :
    \begin{itemize}
        \item Petit-déjeuner
        \item Snack matin
        \item Déjeuner
        \item Rappel hydratation
        \item Snack après-midi
        \item Dîner
        \item Total des calories de la journée
    \end{itemize}
    \item Vous pouvez régénérer un nouveau planning à tout moment
\end{enumerate}

\subsection{Utiliser l'espace Motivation}

\begin{enumerate}
    \item Cliquez sur "Motivation" dans le menu
    \item Vous verrez votre challenge du jour (exemple : "Bois 2 litres d'eau et fais 30 min de marche")
    \item Progressez sur le challenge :
    \begin{itemize}
        \item Cliquez sur "+25\%" pour ajouter de la progression
        \item Ou cliquez sur "Marquer complété" si vous avez tout fait
    \end{itemize}
    \item Suivez votre streak (jours consécutifs) en haut à droite
    \item Lisez les conseils personnalisés générés par l'IA
    \item Un nouveau challenge apparaît chaque jour automatiquement
\end{enumerate}

\subsection{Discuter avec le chatbot IA}

\begin{enumerate}
    \item Sur la page d'accueil, cliquez sur l'icône de robot en bas à droite
    \item La fenêtre de chat s'ouvre
    \item Tapez votre question (exemples) :
    \begin{itemize}
        \item "Donne-moi des conseils pour perdre du poids"
        \item "Quelles sont des recettes riches en protéines ?"
        \item "Comment rester motivé pour faire du sport ?"
    \end{itemize}
    \item Appuyez sur Entrée ou cliquez sur l'icône d'envoi
    \item L'IA répond en 2-5 secondes avec des conseils personnalisés
    \item Vous pouvez utiliser les boutons de réponses rapides
\end{enumerate}

\subsection{Contacter l'équipe}

\begin{enumerate}
    \item Cliquez sur "Contact" dans le menu
    \item Remplissez le formulaire :
    \begin{itemize}
        \item Nom complet
        \item Email
        \item Téléphone (optionnel)
        \item Message
    \end{itemize}
    \item Cliquez sur "Envoyer le message"
    \item Votre message est enregistré dans notre base de données
\end{enumerate}

\subsection{Déconnexion}

\begin{enumerate}
    \item Cliquez sur "Déconnexion" dans le menu en haut à droite
    \item Vous êtes redirigé vers la page de connexion
    \item Votre session est terminée de manière sécurisée
\end{enumerate}

\vspace{1cm}

\textbf{Conseils d'utilisation :}
\begin{itemize}
    \item Pour une meilleure détection avec le scanner de frigo, prenez des photos bien éclairées et de face
    \item Mettez à jour régulièrement votre poids dans votre profil pour des recommandations précises
    \item Utilisez le chatbot pour toute question, il est disponible 24/7
    \item Complétez vos challenges quotidiens pour maintenir votre streak !
\end{itemize}

\newpage
\section*{Conclusion générale}

Le projet AI FitChef a été une expérience enrichissante qui nous a permis de créer une application web complète et fonctionnelle répondant à un véritable besoin. Nous avons réussi à intégrer plusieurs technologies d'intelligence artificielle (Groq et Mistral) pour offrir des fonctionnalités innovantes comme la détection d'ingrédients par photo et la génération de plannings personnalisés.

Au-delà des compétences techniques acquises (Flask, APIs IA, bases de données, déploiement), ce projet nous a appris l'importance du travail en équipe et de la persévérance. Nous sommes fières du résultat final : une application accessible en ligne sur \url{https://imanehdg.pythonanywhere.com/} que nous utilisons nous-mêmes au quotidien.

\vspace{0.5cm}

\begin{center}
\textit{Merci à M. François Delbot pour son encadrement,\\
et merci à l'Université Paris Nanterre pour cette opportunité de projet.}
\end{center}
 
\end{document}


