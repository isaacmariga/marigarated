from django.shortcuts import redirect, render
from .models import Test2, Test3, Test1
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import Test1Serializer, Test2Serializer, Test3Serializer



class Test1List(APIView):
		def get(self, request, format=None):
				text = Test1.get_all()
				serializers = Test1Serializer(text, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = Test1Serializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




class Test2List(APIView):
		def get(self, request, format=None):
				text = Test2.get_all()
				serializers = Test2Serializer(text, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = Test2Serializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class Test3List(APIView):
		def get(self, request, format=None):
				text = Test3.get_all()
				serializers = Test3Serializer(text, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = Test3Serializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)