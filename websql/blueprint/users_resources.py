from data import db_session
from data.users import User
from data.news import News
from flask_restful import abort, Resource
from flask import jsonify
from .reqparse_user import parser


def abort_if_user_not_found(user_id):
    sess = db_session.create_session()
    users = sess.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


class UsersRecource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        sess = db_session.create_session()
        users = sess.query(User).get(user_id)
        user_news: News = sess.query(News).filter(News.user_id == user_id).all()
        return jsonify(
            {
                'user': users.to_dict(only=(
                    'name', 'about', 'email', 'created_date')),
                'news': [news.to_dict(only=(
                    'title', 'content', 'is_private', 'user_id', 'created_date')) for news in user_news]
            }
        )

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        sess = db_session.create_session()
        users = sess.query(User).get(user_id)
        user_news: News = sess.query(News).filter(News.user_id == user_id).all()
        for news in user_news:
            sess.delete(news)
            sess.commit()
        sess.delete(users)
        sess.commit()
        return jsonify({'success': 'OK'})


class UsersListRecource(Resource):
    def get(self):
        sess = db_session.create_session()
        users = sess.query(User).all()
        return jsonify(
            {
                'user': [item.to_dict(only=(
                    'name', 'about', 'email', 'created_date')) for item in users]
            }
        )

    def post(self):
        args = parser.parse_args()
        sess = db_session.create_session()
        users = User(
            name=args['name'],
            about=args['about'],
            hashed_password=args['hashed_password'],
            email=args['email']
        )
        sess.add(users)
        sess.commit()
        return jsonify({'success': 'OK'})




