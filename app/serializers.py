#app/serializers.py
from rest_framework import serializers
from .models import SwapEvent, MintEvent, BurnEvent, CollectEvent, TokenPairs

class SwapEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwapEvent
        fields = '__all__'

class MintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MintEvent
        fields = '__all__'

class BurnEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BurnEvent
        fields = '__all__'

class CollectEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectEvent
        fields = '__all__'

class TokenPairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenPairs
        fields = '__all__'
    