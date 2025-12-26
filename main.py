import pandas as pd from scripts.keyword_clustering import cluster_keywords from scripts.content_engine import generate_seo_brief

def run_seo_pipeline(file_path): print("🚀 Initializing AI SEO Pipeline...")

# 1. Load keywords from Ahrefs/SEMrush export
df = pd.read_csv(file_path)

# 2. Semantic Clustering
print("📊 Clustering keywords by intent...")
clustered_df = cluster_keywords(df)

# 3. Generate Briefs for Top Clusters
top_clusters = clustered_df['cluster'].unique()[:5]
for cluster_id in top_clusters:
    cluster_data = clustered_df[clustered_df['cluster'] == cluster_id]
    primary_kw = cluster_data.iloc[0]['Keyword']
    
    print(f"📝 Generating brief for: {primary_kw}")
    brief = generate_seo_brief(primary_kw, list(cluster_data['Keyword']))
    
    with open(f"output/brief_{cluster_id}.md", "w") as f:
        f.write(brief)


if name == "main": run_seo_pipeline("data/keywords.csv")