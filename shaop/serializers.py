from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        for symbol in '!@#$%^&*':
            if symbol in value:
                raise serializers.ValidationError(f'name should not contain {symbol}')
        return value


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    # def validate(self, data):
    #     qr = str(data['category'])+'C'+str(data['price'])+'P'+str(data['id'])+'I'
    #     if str(data['QR']) != qr:
    #         raise serializers.ValidationError("QR is incorrect")
    #     return data
