from api.models import User, Article, Comment, Like
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
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return Like.objects.filter(article=obj).values_list("user__id", flat=True)

    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
