from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category
from users.models import User
from users.serializers import UserSerializer


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        exclude = ("description",)
        model = Ad


class AdAuthorSerializer(ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, obj):
        return obj.ad_set.count()

    class Meta:
        exclude = ("password", "role")
        model = User


class AdDetailSerializer(ModelSerializer):
    author = UserSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"
