from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('HOST')
port = int(os.getenv('PORT', 8000))

database_uri = os.getenv('DATABASE_URI')
