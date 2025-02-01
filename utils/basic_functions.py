# basic_functions.py
import os
from dotenv import load_dotenv

# pull secrets when needed
def get_secret(secret_key):
    # initialization
    if not os.getenv(secret_key):
        # Get the portfolio directory path
        portfolio_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Go up two levels to get to the clone directory, then to .gitignore/.env
        clone_dir = os.path.dirname(os.path.dirname(portfolio_dir))
        env_path = os.path.normpath(os.path.join(clone_dir, '.gitignore', '.env'))
        print(f"Looking for .env file at: {env_path}")
        load_dotenv(dotenv_path=env_path)

    # iteration
    value = os.getenv(secret_key)
    if value is None:
        print(f"Environment variable '{secret_key}' not found")
        raise ValueError(f"Secret '{secret_key}' not found.")

    return value
