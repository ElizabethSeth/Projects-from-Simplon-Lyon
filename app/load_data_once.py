import pandas as pd
from sqlalchemy import create_engine
import time

# Delay for DB readiness (optional safety)
time.sleep(5)

engine = create_engine("postgresql+psycopg2://user:password@db:5432/sportsdb")
df = pd.read_csv("fact_resultats_epreuves.csv")

# Load into Postgres
df.to_sql("fact_resultats_epreuves", engine, if_exists="replace", index=False)
print("✅ Data successfully loaded into PostgreSQL!")
