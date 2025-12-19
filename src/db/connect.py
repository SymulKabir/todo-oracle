import oracledb

# Create a connection pool
# sqlplus APP_ONE/APP_ONE@localhost:1521/FREEPDB1
pool = oracledb.create_pool(
    user="APP_ONE",
    password="APP_ONE",
    dsn="localhost:1521/FREEPDB1",
    min=1,
    max=5,
    increment=1
)

def get_connection():
    return pool.acquire()