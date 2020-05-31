from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ['id', 'name', 'description', 'price', 'image_url', 'slug']

	def get_image_url(self, product):
		request = self.context.get('request')
		image_url = product.image.url
		return request.build_absolute_uri(image_url)


class ProductDetailSerializer(serializers.ModelSerializer):
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Product
		exclude = ('image',)

	def get_image_url(self, product):
		request = self.context.get('request')
		image_url = product.image.url
		return request.build_absolute_uri(image_url)