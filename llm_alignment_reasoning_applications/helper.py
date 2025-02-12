import os
from dotenv import load_dotenv

def get_openai_api_key():
    """Gets the OpenAI API key from environment variables or .env file."""

    # Construct .env file path using working directory
    dotenv_path = os.path.join(os.getcwd(), ".env") 

    # Try loading from .env file
    try:
        load_dotenv(dotenv_path)  
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key
    except FileNotFoundError:
        pass  # Ignore if .env file not found

    # If not found in .env, try Colab environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key

    # If still not found, raise an error
    raise ValueError("Missing OpenAI API key. Set it in .env file or Colab environment variables.")