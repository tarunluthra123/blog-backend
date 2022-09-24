from api.models import User, Article, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "bio", "profile_pic"]



class ArticleTagSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.name



class ArticleSerializer(serializers.ModelSerializer):
    tags = ArticleTagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
