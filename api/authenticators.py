from rest_framework import authentication
from utils.jwt import decode_token
from api.models import User
from jwt import DecodeError


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        jwt = request.headers.get("Authorization")

        if jwt:
            _, jwt = jwt.split(" ")

            try:
                payload = decode_token(jwt)
                user = User.objects.get(id=payload.get("id"))
                return user, jwt
            except (DecodeError, User.DoesNotExist):
                return None, None

        return None, None
