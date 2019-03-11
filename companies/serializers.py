from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock

		# Just add the attributes you wanna send, if not all
		fields= ('ticker', 'volume')

		#To send all the fields just write - fields= '__all__'