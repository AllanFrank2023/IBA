#python

# Importér OpenAI GPT-3 biblioteket
import openai

# Definér din API-nøgle
api_key = "DIN_API_NØGLE_HER"

# Skriv din prompt
prompt = """
Generer et nyt våben til spillet med følgende attributter:
- Navn: [Navn på våbnet]#
- Skade: [Skadevirkning]
- Sjældenhed: [Sjældenhedsværdi fra 1 til 5]
- Egenskaber: [Eventuelle specielle egenskaber]
"""

# Anvend OpenAI's API til at generere et nyt våben baseret på prompten
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50,  # Justér dette tal afhængigt af ønsket længde på svaret
    api_key=api_key
)

# Udtræk det genererede våben fra API-responsen
generated_weapon = response.choices[0].text.strip()

# Udskriv det genererede våben
print("Det genererede våben er:")
print(generated_weapon)