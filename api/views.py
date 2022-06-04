from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from api.models import User
from api.serializers import UserSerializer


class PingPongView(APIView):
    def get(self, request):
        return Response({"message": "pingpong"})


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
