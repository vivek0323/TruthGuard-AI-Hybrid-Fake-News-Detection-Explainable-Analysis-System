from google import genai

client = genai.Client(api_key="AIzaSyA_UC4S9LRJVXKo1DtVgB6zxl2gaHqKkxc")

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)