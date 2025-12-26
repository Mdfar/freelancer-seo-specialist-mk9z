from openai import OpenAI import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_seo_brief(primary_kw, secondary_kws): prompt = f""" Act as a Senior SEO Strategist. Create a detailed content brief for the primary keyword: "{primary_kw}". Include these semantic secondary keywords: {', '.join(secondary_kws)}.

Requirements:
- Title Tag (max 60 chars)
- Meta Description (max 155 chars)
- H1, H2, and H3 structure
- Target audience and search intent
- Key questions to answer (PPA)
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

return response.choices[0].message.content