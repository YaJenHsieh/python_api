from python_api.newsRepository import add_news_list_to_sql
from datetime import datetime

def fda_all_data(all_data):
	data_list = []
	for i in all_data:
		title = i['標題']
		content = i['內容']
		url = i['附檔連結']
		create_date = i['發布日期'] + " " + datetime.now().strftime('%H:%M:%S')
		modified_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
		status = 1
		
		data_dict = {
			'title':title,
			'content':content,
			'url':url,
			'create_date':create_date,
			'modified_date':modified_date,
			'status':status
		}
		data_list.append(data_dict)
	add_news_list_to_sql(data_list)