from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import pandas as pd

load_dotenv(".envDbInfo")   # or ".env"

serverName = os.getenv("SERVER_NAME")
databaseName = os.getenv("DATABASE_NAME")
driver = os.getenv("DRIVER")

connection_string = (
    f"mssql+pyodbc://@{serverName}/{databaseName}"
    f"?driver={driver.replace(' ', '+')}&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as conn:
        #result = conn.execute(text("SELECT * from first"))
        df = pd.read_sql("SELECT * FROM firstTable", conn)
        df.to_sql(
            name="Copy_first_table",
            con=engine,
            if_exists="replace",  # or "append"
            index=False
        )
        print(df)

        print("Connection successful!")
        # for row in result:
        #     print(row,)
except Exception as e:
    print("Connection error:", e)
