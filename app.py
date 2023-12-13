from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.movie import MovieListResource, MovieResource, MovieSearchResource
from resources.review import ReviewResource


from resources.user import UserLogoutResource, jwt_blocklist
from resources.user import LoginRegisterResource, UserRegisterResource


app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in jwt_blocklist
api = Api(app)

api.add_resource( UserRegisterResource,'/user/register')
api.add_resource( LoginRegisterResource,'/user/login')
api.add_resource( UserLogoutResource,'/user/logout')
api.add_resource( ReviewResource,'/review')
api.add_resource( MovieResource,'/movie/<int:movie_id>')
api.add_resource( MovieListResource,'/movie')
api.add_resource( MovieSearchResource,'/movie/search')










if __name__ == '__main__' :
    app.run()