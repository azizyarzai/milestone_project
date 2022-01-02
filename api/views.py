from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView, permission_classes

from products.models import Product

from .serializers import ProductSerilizer, TestSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# APIView == View

# Create your views here.


@api_view(['GET', 'POST'])
def say_hi(request):

    serailizer = TestSerializer(data=request.data)

    if serailizer.is_valid():
        return Response({"id": 25, **serailizer.validated_data}, status=201)
    else:
        return Response(serailizer.errors, status=400)

    # if len(request.data["name"]) < 5:
    #     return Response({'name': "should have more than 5 characters."})
    # return Response({'value': 'Hi There.'})


class SayHiApiView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'value': 'Hi There.'})


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerilizer(products, many=True)
    return Response(serializer.data, status=200)


class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    # queryset = Product.objects.filter(is_availible=True)
    serializer_class = ProductSerilizer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        return Product.objects.filter(is_availible=True)
