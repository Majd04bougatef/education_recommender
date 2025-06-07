import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("data/resources.csv")


# Supprimer les lignes avec des valeurs manquantes
df.dropna(inplace=True)

# Supprimer les doublons éventuels
df.drop_duplicates(inplace=True)
for col in ['description', 'topic', 'format', 'difficulty']:
    df[col] = df[col].str.lower().str.strip()

def combine_features(row):
    return f"{row['description']} {row['topic']} {row['format']} {row['difficulty']}"

df["combined_features"] = df.apply(combine_features, axis=1)

print(df[['title', 'combined_features']].head())


__all__ = ['df']