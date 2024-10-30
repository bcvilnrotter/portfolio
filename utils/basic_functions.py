# basic_functions.py
import os
from dotenv import load_dotenv

# pull secrets when needed
def get_secrets(*secret_keys):
    # initialization
    load_dotenv(dotenv_path=".gitignore\.env")
    secrets = {}

    # iteration
    for key in secret_keys:
        value = os.getenv(key)
        if value is None:
            ValueError(f"Secret '{key}' no found.")
        secrets[key] = value

    return secrets