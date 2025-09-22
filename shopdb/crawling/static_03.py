# Database 접속
# Insert 쿼리문을 이용해 수집한 데이터를 DB에 저장
import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )


import crawlingcoffee

for page_num in range(1, 47):

    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
                    insert into shop_base_tbl
                    values(null,%s,%s,%s,%s,%s)
                    '''
            # cur.execute(sql, (, , , ,))
            cur.executemany(sql, crawlingcoffee.get_data(page_num))
        conn.commit()

