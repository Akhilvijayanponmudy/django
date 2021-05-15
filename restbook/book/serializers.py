from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerializer(serializers.Serializer):
    book_name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()

    def create(self, validated_data):

        return Book.objects.create(**validated_data)

 #                   book         data
    def update(self, instance, validated_data):
        #        model name                    seeializer name
        instance.book_name=validated_data.get("book_name")
        instance.author=validated_data.get("author")
        instance.price=validated_data.get("price")
        instance.save()
        return instance




class BookModelSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
