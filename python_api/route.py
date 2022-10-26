from flask import render_template,redirect,url_for,request
from python_api import app
from python_api.newsRepository import get_sql_data,delete_sql_data,get_news_by_id,update_news_to_sql,search_news,create_news
from python_api.newsService import fda_all_data
from python_api.forms import EditNewsForm,SearchForm,AddNewsForm
import requests



@app.route('/',methods=['GET','POST'])
def home_page():
	form = SearchForm()
	if form.validate_on_submit():
		searched = form.searched.data.strip()
		get_data = search_news(searched)
		return render_template('home.html',get_data=get_data,form=form,searched=searched)

	get_data = get_sql_data()
	return render_template('home.html',get_data=get_data,form=form)

@app.route('/update_news')
def update_news():
	url = 'http://www.fda.gov.tw/DataAction'
	fda_req_data = requests.get(url)
	all_data = fda_req_data.json()
	fda_all_data(all_data)
	return redirect(url_for('home_page'))

@app.route('/delete_page/<delete_id>')
def delete_page(delete_id):
	delete_sql_data(delete_id)
	return redirect(url_for('home_page'))

@app.route('/edit_page/<edit_id>',methods=['GET','POST'])
def edit_page(edit_id):
	search_form = SearchForm()
	if search_form.validate_on_submit():
		searched = search_form.searched.data.strip()
		get_data = search_news(searched)
		return render_template('home.html',search_form=search_form,searched=searched,get_data=get_data)

	form = EditNewsForm()
	if request.method == 'GET':
		news_data = get_news_by_id(edit_id)
		form.edit_news_title.data = news_data['title']
		form.edit_news_content.data = news_data['content']
	if request.method == 'POST':
		title = form.edit_news_title.data
		content = form.edit_news_content.data
		update_news_to_sql(edit_id,title,content)
		return redirect(url_for('home_page'))
	return render_template('edit.html',form=form)

@app.route('/add_news',methods=['GET','POST'])
def add_news():
	form = SearchForm()
	if form.validate_on_submit():
		searched = form.searched.data.strip()
		get_data = search_news(searched)
		return render_template('home.html',form=form,searched=searched,get_data=get_data)

	form = AddNewsForm()
	if form.validate_on_submit():
		title = form.add_news_title.data
		content = form.add_news_content.data
		url = form.add_news_url.data
		create_news(title,content,url)
		return redirect(url_for('home_page'))
	return render_template('add_news.html',form=form)

@app.context_processor # 將內容傳遞到 navbar
def base():
	form=SearchForm()
	return dict(form=form)