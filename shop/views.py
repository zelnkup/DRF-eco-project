from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductListView(APIView):
	def get(self, request):
		products = Product.objects.filter(available=True)
		serializer = ProductListSerializer(products, many=True, context={"request": request})
		return Response(serializer.data)


class ProductDetailView(APIView):
	def get(self, request, slug, id):
		product = get_object_or_404(Product, slug=slug, id=id, available=True)
		serializer = ProductDetailSerializer(product, context={"request": request})
		return Response(serializer.data)
