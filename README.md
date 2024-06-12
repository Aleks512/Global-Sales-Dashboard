# Global-Sales-Dashboard
Une application de bureau conçue pour aider la direction de la maison mère à visualiser et analyser les performances des ventes de ses filiales à travers le monde.

# Sales Data Management Application

## Description
Cette application de gestion des données de vente est une application de bureau développée avec PySide6 pour l'interface utilisateur et SQLite pour la gestion des données. Elle permet de visualiser, analyser et générer des rapports sur les indicateurs clés de performance (KPI) basés sur les données de vente.

## Fonctionnalités
- **Affichage des données de vente** : Les données de vente sont affichées dans des tableaux interactifs.
- **Calcul et affichage des KPI** : Calcul des revenus totaux, des coûts totaux et des revenus nets.
- **Génération de rapports PDF** : Création de rapports PDF détaillant les KPI et les données de vente.
- **Création de graphiques** : Génération de graphiques pour visualiser les revenus et les coûts par pays.

## Prérequis
- Python 3.11
- PySide6
- pandas
- matplotlib
- reportlab

## Installation
1. Clonez le repository :
   ```bash
   git clone https://github.com/Aleks512/Global-Sales-Dashboard.git
   cd Global-Sales-Dashboard
   ```
2. Créez un environnement virtuel et activez-le :
   ``python -m venv env``
   ``.\env\Scripts\activate``
3. Installez les dépendances :
   ``pip install -r requirements.txt
   ``
4. Exécutez l'application :
   ``python main.py
   ``
5. Utilisez l'interface pour ajouter, supprimer et modifier des données de vente.
6. Visualisez les KPI et les tableaux de données.
7. Génèrez des rapports PDF détaillés en cliquant sur le bouton approprié.
## Packages Utilisés

### PySide6
- `QMainWindow`, `QVBoxLayout`, `QTableWidget`, `QTableWidgetItem`, `QPixmap`, `QImage` : Utilisés pour créer et gérer l'interface utilisateur.

### pandas
- `read_sql_query`, `DataFrame` : Utilisés pour manipuler et analyser les données sous forme de DataFrames.

### matplotlib
- `pyplot`, `FigureCanvasAgg` : Utilisés pour créer des graphiques et les afficher dans l'application.

### reportlab
- `SimpleDocTemplate`, `Table`, `TableStyle`, `Paragraph`, `Spacer`, `getSampleStyleSheet`, `colors`, `A4`, `inch` : Utilisés pour générer des rapports PDF détaillés.

### os
- `os.path` : Utilisé pour les opérations de chemin de fichier et de manipulation de l'environnement.

