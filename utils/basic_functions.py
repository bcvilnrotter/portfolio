# basic_functions.py
import os
from dotenv import load_dotenv

# pull secrets when needed
def get_secret(secret_key):
    # initialization
    if not os.getenv(secret_key):
        env_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..\..','.gitignore\.env'))
        load_dotenv(dotenv_path=env_path)

    # iteration
    value = os.getenv(secret_key)
    if value is None:
        ValueError(f"Secret '{secret_key}' no found.")

    return value
