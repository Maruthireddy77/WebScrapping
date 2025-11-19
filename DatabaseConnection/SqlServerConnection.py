#
# from sqlalchemy import create_engine
#
# engine = create_engine(
#     "mssql+pyodbc://@MARUTHIREDDY\\SQLEXPRESS/master?"
#     "driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
# )
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd


# IMPORTANT: Escape the backslash in the server name
server = r"MARUTHIREDDY\SQLEXPRESS"
database = "pycharmconnection"  # change later to your DB name

# Use your installed driver here
driver = "ODBC Driver 17 for SQL Server"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
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
