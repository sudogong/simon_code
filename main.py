import os
import argparse
from dotenv import load_dotenv
from google import genai

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise Exception("GEMINI_API_KEY not found in .env")
    
    # Generate Gemini client
    client = genai.Client(api_key=api_key)

    # Use argparser to extract question from command argument
    parser = argparse.ArgumentParser(description="Simon Code")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)
    
    if response.usage_metadata == None:
        raise Exception(RuntimeError)
    
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(f"Response: \n{response.text}")


if __name__ == "__main__":
    main()
