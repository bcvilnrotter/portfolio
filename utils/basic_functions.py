# basic_functions.py
import os
from dotenv import load_dotenv

# pull secrets when needed
def get_secret(secret_key):
    # initialization
    load_dotenv(dotenv_path=".gitignore\.env")

    # iteration
    value = os.getenv(secret_key)
    if value is None:
        ValueError(f"Secret '{secret_key}' no found.")

    return value