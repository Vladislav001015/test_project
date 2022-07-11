from django.contrib.auth.models import User
from rest_framework import serializers

from applications.music.models import Music, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class UserS(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        # fields = ('title', 'category')
        fields = '__all__'
    def to_representation(self, instance):
        # print(instance)
        representation = super().to_representation(instance)
    # #     # уберем поле id, чтобы пользователь не видел
    #     representation.pop('id')
    #     print(representation)
    #     print(User.objects.filter(music=instance.id))
        category = UserS(User.objects.filter(music=instance.id), many=True).data
        # print(category[0]['username'])
        # print(category['fsadfa'])
        for i in category:
            representation['author'] = category[0]['username']
        # category = CategorySerializer(Category.objects.get(music=instance.id), many=False).data
    #     representation['category'] = category['title']
        return representation
