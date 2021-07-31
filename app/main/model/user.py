from .. import db, flask_bcrypt
import datetime
from ..config import key, algorithm
import jwt

class User(db.Model):
    """ User Model for storing user related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    major = db.Column(db.String(120), nullable=True)
    public_id = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(120))
    registered_on = db.Column(db.DateTime, nullable=False)
    verify_on = db.Column(db.Boolean, default = False, nullable = False)
    verify_code = db.Column(db.String(20), nullable=True)
    
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True} 
    
    @property
    def password(self):
      raise AttributeError('password: write-only field')
    
    @password.setter
    def password(self, password):
      self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
      return flask_bcrypt.check_password_hash(self.password_hash, password)
    
    def encode_auth_token(self, user):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10),
                'iat': datetime.datetime.utcnow(),
                'email': user.email,
            }
            return jwt.encode(
                payload,
                key,
                algorithm
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
          temp = jwt.decode(auth_token,key,algorithm)
        except jwt.ExpiredSignatureError:
          return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
          return 'Invalid token. Please log in again.'
        else:
          return temp

    def __repr__(self):
        return '<User %r>' % self.username