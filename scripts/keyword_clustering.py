import numpy as np from sklearn.cluster import KMeans from sentence_transformers import SentenceTransformer

def cluster_keywords(df): model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings for keywords
embeddings = model.encode(df['Keyword'].tolist())

# Perform K-Means clustering
num_clusters = min(len(df) // 5, 50)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(embeddings)

return df.sort_values(by=['cluster', 'Search volume'], ascending=[True, False])