from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

prompt = """
Create a modern SaaS landing page
for an AI productivity company.
"""

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

html = response.choices[0].message.content

with open(
    "generated_site.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("Website Generated")