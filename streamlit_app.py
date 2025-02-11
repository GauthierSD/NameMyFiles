import streamlit as st
import pandas as pd
import os

# Titre de l'application
st.title("Liste des fichiers à envoyer")

# Créez deux colonnes
col1, col2 = st.columns(2)

# Téléchargez un ou plusieurs fichiers
uploaded_files = st.file_uploader("Choisissez des fichiers", accept_multiple_files=True)

# Si des fichiers sont téléchargés
if uploaded_files:
    # Crée une liste des noms de fichiers (sans extensions)
    file_names = [os.path.splitext(file.name)[0] for file in uploaded_files]
    
    # Crée un DataFrame avec des informations sur les fichiers
    file_info = pd.DataFrame({
        "Nom du fichier": file_names
    })
    
    # Affiche le tableau à gauche sans la colonne d'index
    with col1:
        st.write("Détails des fichiers :")
        st.dataframe(file_info, use_container_width=True, hide_index=True)
    
    # Affiche la liste des fichiers à droite, séparée par des retours à la ligne
    with col2:
        st.write("Liste des fichiers :")
        st.text("\n".join(file_names))
else:
    st.write("Veuillez télécharger des fichiers pour voir leurs informations.")
