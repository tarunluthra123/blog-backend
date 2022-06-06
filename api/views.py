from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from api.models import User
from api.serializers import UserSerializer, ProfileSerializer
from utils.codec import Codec
from utils.jwt import generate_token


class PingPongView(APIView):
    def get(self, request):
        return Response({"message": "pingpong"})


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "username"


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.filter(username=username).first()

        if user and Codec.compare(password, user.password):
            # Check if the user password matches with the given password in the request
            # Generate an auth token and return it.
            payload = {
                "id": user.id,
                "username": user.username,
            }
            token = generate_token(payload)

            serializer = UserSerializer(user)

            return Response({"token": token, **serializer.data})

        return Response({"message": "Invalid credentials"}, status=401)
