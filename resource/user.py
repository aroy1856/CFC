from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('FirstName',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('LastName',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('PhoneNumber',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('FirstLineOfAddress',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Street',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Area',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('District',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Pincode',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, email):
        user = UserModel.find_by_email(email)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self, email):
        if UserModel.find_by_email(email):
            return {'message': "An user with email '{}' already exists.".format(email)}, 400

        data = User.parser.parse_args()

        user = UserModel(email, **data)
        try:
            user.insert_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return user.json(), 201
