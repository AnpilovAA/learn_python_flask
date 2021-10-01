from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = 'Новости Learn python'
        weather = weather_by_city('Moscow,Russia')
        news_list = get_python_news()
        return render_template('index.html', weather=weather, page_title=title, news_list=news_list)
    return app
