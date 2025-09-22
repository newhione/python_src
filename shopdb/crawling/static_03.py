import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('127.0.0.1'),
        user = os.getenv('root'),
        password = os.getenv('1234'),
        database=os.getenv('shopinfo')
    )
with get_connection() as conn:
   with conn.cursor() as cur:
       sql = '''
            insert into shop_base_tbl
                values(null,'?','?','?','?','?')'''
       # cur.execute(sql, (, , , ,))