from data import db_session
from data.news import News
from data.users import User
from flask_restful import abort, Resource
from flask import jsonify
from .reqparse import parser


def abort_if_news_not_found(news_id):
    sess = db_session.create_session()
    news = sess.query(User).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class NewsRecource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        sess = db_session.create_session()
        users = sess.query(User).get(news_id)
        user_news: News = sess.query(News).filter(News.user_id == news_id).all()
        return jsonify(
            {
                'user': users.to_dict(only=(
                    'name', 'about', 'email', 'created_date')),
                'news': [news.to_dict(only=(
                    'title', 'content', 'is_private', 'user_id', 'created_date')) for news in user_news]
            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        sess = db_session.create_session()
        news = sess.query(News).get(news_id)
        sess.delete(news)
        sess.commit()
        return jsonify({'success': 'OK'})


class NewsListResource(Resource):
    def get(self):
        sess = db_session.create_session()
        news = sess.query(News).all()
        return jsonify(
            {
                'news': [item.to_dict(only=(
                    'title', 'content', 'user.name')) for item in news]
            }
        )

    def post(self):
        args = parser.parse_args()
        sess = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_private=args['is_private']
        )
        sess.add(news)
        sess.commit()
        return jsonify({'success': 'OK'})

