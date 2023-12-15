# Standalone script to connect to the PlanetScale database
# Author: Indrajit Ghosh
# Created On: Dec 15, 2023

from dotenv import load_dotenv
load_dotenv()
import os
from sqlalchemy import create_engine

DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = create_engine(
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
    connect_args={
        "ssl" : {
            "ssl_ca" : "/etc/ssl/cert.pem"
        }
    }
)
  