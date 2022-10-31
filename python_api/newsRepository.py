import psycopg2
from datetime import datetime,timedelta

def get_conn():
	conn = psycopg2.connect(
		host='host',
		database='database',
		user='user',
		password='password',
		port=5432
	)
	return conn

def add_news_list_to_sql(data):
	conn = None
	cur = None

	try:
		conn = get_conn()
		cur = conn.cursor()

		for i in data:
			title = i['title']
			content = i['content']
			url = i['url']
			create_date = i['create_date']
			modified_date = i['modified_date']
			status = i['status']

			sql = f"INSERT INTO news (title,content,url,create_date,modified_date,status) VALUES ('{title}','{content}','{url}','{create_date}','{modified_date}','{status}') WHERE EXISTS (select * from news where title='{title}') do instead nothing ;"
			try:
				cur.execute(sql)
				conn.commit()
			except:
				continue

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()

def get_sql_data():
	conn = None
	cur = None

	try:
		conn = get_conn()
		cur = conn.cursor()
		sql = "SELECT id,title,content,url,create_date,modified_date,status from news WHERE status=1 order by modified_date desc,create_date desc;"
		cur.execute(sql)
		
		records = cur.fetchall()
		conn.commit()

		get_info_list = []
		for i in records:
			id = i[0]
			title = i[1]
			content = i[2]
			url = i[3]
			create_date = i[4]
			modified_date = i[5]
			
			get_data_dic = {
				'id':id,
				'title':title,
				'content':content,
				'url':url.split(",",1),
				'create_date':create_date,
				'modified_date':modified_date
			}
			get_info_list.append(get_data_dic)
		return get_info_list

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()


def delete_sql_data(delete_id):
	conn = None
	cur = None

	try:
		conn = get_conn()
		cur = conn.cursor()
		sql = f"UPDATE news SET status=0 WHERE id={delete_id}"
		cur.execute(sql)
		conn.commit()

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()

def get_news_by_id(id):
	conn = None
	cur = None

	try:
		conn = get_conn()
		cur = conn.cursor()
		sql = f"SELECT * FROM news WHERE id={id}"
		cur.execute(sql)
		records = cur.fetchone()
		get_news_dic = {
				'id':records[0],
				'title':records[1],
				'content':records[2],
				'url':records[3],
				'create_date':records[4],
				'modified_date':records[5]
			}
		conn.commit()
		return get_news_dic

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()

def update_news_to_sql(id,title,content):
	conn = None
	cur = None

	datetime_dt = datetime.today() #獲得現在時間
	time_delta = timedelta(hours=8) #時差
	new_dt = datetime_dt + time_delta
	time = new_dt.strftime('%Y/%m/%d %H:%M:%S')

	try:
		conn = get_conn()
		cur = conn.cursor()
		sql = f"UPDATE news SET title='{title}',content='{content}',modified_date='{time}' WHERE id={id}"
		cur.execute(sql)
		conn.commit()

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()

def search_news(searched):
	conn = None
	cur = None

	try:
		conn = get_conn()
		cur = conn.cursor()
		sql = f"SELECT * FROM news WHERE status=1 AND (content LIKE '%{searched}%' OR title LIKE '%{searched}%')"
		cur.execute(sql)

		records = cur.fetchall()
		conn.commit()
		
		get_search_list = []
		for i in records:
			id = i[0]
			title = i[1]
			content = i[2]
			url = i[3]
			create_date = i[4]
			modified_date = i[5]

			get_data_dic = {
				'id':id,
				'title':title,
				'content':content,
				'url':url,
				'create_date':create_date,
				'modified_date':modified_date
			}
			get_search_list.append(get_data_dic)
		return get_search_list

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()

def create_news(title,content,url):
	conn = None
	cur = None

	datetime_dt = datetime.today() #獲得現在時間
	time_delta = timedelta(hours=8) #時差
	new_dt = datetime_dt + time_delta
	time = new_dt.strftime('%Y/%m/%d %H:%M:%S')

	try:
		conn = get_conn()
		cur = conn.cursor()
		sql = f"INSERT INTO news (title,content,url,create_date,modified_date) VALUES ('{title}','{content}','{url}','{time}','{time}')"
		cur.execute(sql)
		conn.commit()

	except Exception as error:
		print(error)

	finally:
		if cur is not None:
			cur.close()
		if conn is not None:
			conn.close()