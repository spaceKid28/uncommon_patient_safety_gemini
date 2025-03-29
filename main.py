from google import genai

def main():
    
    client = genai.Client(api_key="AIzaSyDAwLLgUMBHL8pqYkX_SEKVJWfBQigwCDc")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="What is the rate of infections in acute care facilities?"
    )
    print(response.text)

    return


if __name__ == "__main__":
    main()