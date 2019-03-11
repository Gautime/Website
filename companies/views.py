# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

# Create your views here.


#List all the stocks and also create new ones
class StockList(APIView):


	def get(self, request):
		#this is getting all the stocks from database and storing in stocks
		stocks = Stock.objects.all()
		#this is serializing the stocks in json format and telling django that the "stocks" contains many values, not just one
		serializer = StockSerializer(stocks, many=True)

		#serializer.data just represents the json data
		return Response(serializer.data)