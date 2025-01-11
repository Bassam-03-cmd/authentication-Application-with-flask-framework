import os
from urllib.parse import quote_plus  # quote_plus important to encode strings for URLs to avoide URL conflicts
from dotenv import load_dotenv  # import load_dotenv for loading environment (.env) that we created for DB server

# Load the environment variables from the .env file
load_dotenv()

class Settings:
    # Define the environment variables
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_NAME = os.getenv("DATABASE_NAME")

    # Configure the JWT settings.
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ['headers', 'cookies']

    # Configure the SQLAlchemy settings.
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{quote_plus(DATABASE_USERNAME)}:"
        f"{quote_plus(DATABASE_PASSWORD)}@"
        f"{DATABASE_HOST}/{DATABASE_NAME}"
    )
