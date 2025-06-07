import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.recommend import get_recommendations
from src.preprocessing import df

# Titre de l'application
st.set_page_config(page_title="Recommender Éducatif", layout="centered")
st.title("📚 Système de Recommandation de Ressources Pédagogiques")

# Liste déroulante avec les titres disponibles
selected_title = st.selectbox(
    "Sélectionnez une ressource pour obtenir des recommandations similaires :",
    options=df["title"].tolist()
)

# Bouton de recommandation
if st.button("🔍 Recommander"):
    recommendations = get_recommendations(selected_title, n=3)
    
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.subheader("✨ Ressources recommandées :")
        for i, row in recommendations.iterrows():
            st.markdown(f"**📘 {row['title']}**")
            st.markdown(f"- **Sujet :** {row['topic']}")
            st.markdown(f"- **Format :** {row['format']}")
            st.markdown(f"- **Niveau :** {row['difficulty']}")
            st.markdown("---")
