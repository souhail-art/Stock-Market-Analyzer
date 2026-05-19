# Stock Market Analyzer 

## Présentation du projet

Le **Stock Market Analyzer ** est une application développée en Python permettant d’analyser des données financières en temps réel issues du marché boursier.

L’application propose une interface graphique permettant de sélectionner plusieurs actions, de récupérer leurs données financières, de les comparer, de les visualiser sous forme de graphiques et de les exporter en fichier Excel.

Ce projet simule un outil d’analyse financière proche des solutions utilisées dans les domaines de la finance, de la banque et de la data analyse.

---

## Objectifs du projet

Les objectifs principaux sont :

- Automatiser la récupération de données financières
- Structurer et transformer des données boursières
- Analyser plusieurs actions simultanément
- Visualiser les performances sous forme de graphiques
- Générer des exports exploitables en Excel
- Construire un pipeline de données de type ETL (Extract, Transform, Load)

---

## Fonctionnalités

### Sélection multi-actions
L’utilisateur peut sélectionner plusieurs entreprises du marché français.

### Récupération des données financières
Pour chaque action, l’application récupère :

- Prix actuel
- Prix d’ouverture
- Plus haut de la journée
- Plus bas de la journée
- Volume échangé
- Capitalisation boursière

### Analyse comparative
Les données sont regroupées dans un tableau unique pour comparer les actions.

### Visualisation graphique
Un histogramme permet de comparer les prix des différentes actions.

### Export Excel
Les données peuvent être exportées au format Excel (.xlsx).

---

## Technologies utilisées

- Python
- Tkinter (interface graphique)
- yfinance (données financières)
- pandas (traitement de données)
- matplotlib (visualisation)
- openpyxl (export Excel)

---

## Source des données

Les données sont récupérées depuis :

https://finance.yahoo.com

---

## Architecture du projet
