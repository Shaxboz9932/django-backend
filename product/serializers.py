from django.db.models import Avg, Count
from rest_framework import serializers
from rest_framework.permissions import BasePermission

from product.models import Product, ProductImage, Category, Brand
from review.models import Review


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(source="rating_awg", read_only=True)
    rating_count = serializers.IntegerField(source="reviews_count", read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    # category = serializers.SerializerMethodField()
    # brand = serializers.SerializerMethodField()

    images = ProductImageSerializer(many=True, read_only=True)
    upload_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000),
        write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'


    def create(self, validated_data):
        upload_images = validated_data.pop('upload_images')
        product = Product.objects.create(**validated_data)

        for img in upload_images:
            ProductImage.objects.create(product=product, image=img)
        return product

    def get_category(self, obj):
        return obj.category.title

    def get_brand(self, obj):
        return obj.brand.title

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']



