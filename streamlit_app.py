import streamlit as st
import pandas as pd
import os

# Titre de l'application
st.title("Liste de mes fichiers")

# Créez quatre colonnes pour disposer les éléments
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Personnalisation de l'upload des fichiers
css = '''
<style>
[data-testid="stFileUploaderDropzone"] div div::before {content:"Glissez et déposez vos fichiers ici";}
[data-testid="stFileUploaderDropzone"] div div span{display:none;}
[data-testid="stFileUploaderDropzone"] div div::after {font-size: .8em; content:"Limité à 200MB par fichier";}
[data-testid="stFileUploaderDropzone"] div div small{display:none;}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

titre = "Glissez vos fichiers ci-dessous pour les afficher sous forme de tableau ou de liste de texte à copier"

# Téléchargement de fichiers avec possibilité de télécharger plusieurs fichiers
uploaded_files = st.file_uploader(titre, accept_multiple_files=True)

# Si des fichiers sont téléchargés
if uploaded_files:
    # Crée une liste des noms de fichiers (sans extensions)
    file_names = [os.path.splitext(file.name)[0] for file in uploaded_files]
    
    # Crée un DataFrame avec des informations sur les fichiers
    file_info = pd.DataFrame({
        "Noms des fichiers": file_names
    })
    
    # Affiche le tableau à gauche sans la colonne d'index
    with col1:
        st.caption("Format tabulaire (pour coller dans Excel)")
        st.dataframe(file_info, use_container_width=True, hide_index=True)

    # Affiche la liste des fichiers à droite, séparée par des retours à la ligne
    with col2:
        st.caption("Format texte (pour coller dans Word/e-mail...)")
        st.text("\n".join(file_names))

    # Ajoute une section de séparation avec des instructions pour l'utilisateur
    with col3:
        st.divider()
        st.markdown("*Cliquez et glissez pour sélectionner les lignes.*")

    with col4:
        st.divider()
        st.markdown("*Pour garder la mise en page avec les retours à la ligne, collez votre texte avec* `Ctrl` `🡅` `V`")