import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


st.title("Analyse des Données Beans & Pods")


def load_data():
    data = pd.read_csv('BeansDataSet.csv')  
    return data

data = load_data()


st.write("Colonnes disponibles :", data.columns)


columns_for_total_sales = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Cappuccino']


missing_columns = [col for col in columns_for_total_sales if col not in data.columns]
if missing_columns:
    st.warning(f"Les colonnes suivantes sont manquantes : {missing_columns}. Elles seront ignorées dans le calcul des ventes totales.")
    columns_for_total_sales = [col for col in columns_for_total_sales if col in data.columns]


data['TotalSales'] = data[columns_for_total_sales].sum(axis=1)


st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Choisissez une section", ["Accueil", "Exploration des Données", "Tendances Clés", "Recommandations", "Données Supplémentaires"])


if menu == "Accueil":
    st.header("Bienvenue dans l'analyse des données Beans & Pods")
    st.write("""
    Beans & Pods est un fournisseur familial à croissance rapide de grains de café et de gousses. 
    Cette application permet d'explorer les données de ventes et de fournir des recommandations pour une campagne de marketing ciblée.
    """)
    st.write("**Jeu de données :**")
    st.write(data.head())


elif menu == "Exploration des Données":
    st.header("Exploration des Données")
    
   
    if st.checkbox("Afficher les données brutes"):
        st.write(data)
    
   
    st.subheader("Statistiques Descriptives")
    st.write(data.describe())


elif menu == "Tendances Clés":
    st.header("Tendances Clés dans les Données")
    
  
    st.subheader("Ventes par Canal")
    sales_by_channel = data.groupby('Channel')['TotalSales'].sum()
    fig, ax = plt.subplots()
    sns.barplot(x=sales_by_channel.index, y=sales_by_channel.values, palette='coolwarm', ax=ax)
    ax.set_title('Ventes par Canal')
    st.pyplot(fig)

    st.write("""**Observation :** Les ventes en magasin sont plus élevées que les ventes en ligne.""")
 
    st.subheader("Ventes par Région")
    sales_by_region = data.groupby('Region')['TotalSales'].sum()
    fig, ax = plt.subplots()
    sns.barplot(x=sales_by_region.index, y=sales_by_region.values, palette='viridis', ax=ax)
    ax.set_title('Ventes par Région')
    st.pyplot(fig)

    st.write("""**Observation :** La région Sud génère le plus de ventes, suivie par le Nord et le Centre.""")

    
    st.subheader("Ventes par Produit")
    product_sales = data[columns_for_total_sales].sum()
    fig, ax = plt.subplots()
    sns.barplot(x=product_sales.index, y=product_sales.values, palette='crest', ax=ax)
    ax.set_title('Ventes par Produit')
    st.pyplot(fig)

    st.write("""**Observation :** Les produits les plus vendus sont Robusta et le Expresso None.""")


elif menu == "Recommandations":
    st.header("Recommandations pour la Campagne Marketing")
    st.write("""
    Sur la base des tendances identifiées, voici nos recommandations :
    1. **Promouvoir les produits les plus vendus** :
       - Mettre en avant l'Arabica et le Cappuccino dans les campagnes publicitaires.
       - Offrir des promotions sur ces produits pour stimuler davantage les ventes.
    2. **Renforcer la présence en ligne** :
       - Étant donné que les ventes en ligne sont plus élevées, investir dans des campagnes digitales (réseaux sociaux, publicités en ligne).
       - Améliorer l'expérience utilisateur sur la plateforme en ligne.
    """)


elif menu == "Données Supplémentaires":
    st.header("Données Supplémentaires à Collecter")
    st.write("""
    Pour améliorer l'analyse et les décisions marketing, nous recommandons de collecter les données suivantes :
    1. **Données démographiques des clients** : Âge, sexe, revenu, etc.
    2. **Données sur les habitudes d'achat** : Fréquence d'achat, montant moyen dépensé, etc.
    3. **Données sur les préférences des clients** : Préférences en matière de goût, d'emballage, etc.
    """)


st.sidebar.header("conclusion")
st.sidebar.write("""
Vous pouvez utiliser un modèle d'ensemble pour prédire les ventes totales en fonction de différentes caractéristiques du jeu de données.
""")
