from rest_framework import serializers
from .models import Company, Category, Quarter, Daily

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'ticker2',
            'category_name',
            'category_ticker',
        )
        model = Category