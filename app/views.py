from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import TokenPairs, SwapEvent, MintEvent, BurnEvent, CollectEvent
from .serializers import TokenPairsSerializer, SwapEventSerializer, MintEventSerializer, BurnEventSerializer, CollectEventSerializer
from django.conf import settings
from pool_data_fetcher import BlockchainClient
from datetime import datetime
from .utils import normalize_datetime
class TokenPairsDetail(generics.GenericAPIView):
    serializer_class = TokenPairsSerializer
    def __init__(self) -> None:
        super().__init__()
        self.blockchainclient = BlockchainClient(settings.ETHEREUM_RPC_NODE_URL)
    
    def post(self, request, *args, **kwargs):
        token0 = request.data.get("token0", None)
        token1 = request.data.get("token1", None)
        fee = request.data.get("fee", None)
        start_datetime = request.data.get("start_datetime", None)
        end_datetime = request.data.get("end_datetime", None)
        start_datetime = normalize_datetime(start_datetime)
        end_datetime = normalize_datetime(end_datetime)
        start_block_number, end_block_number = self.blockchainclient.get_block_number_range(start_datetime, end_datetime)
        if not token0 or not token1:
            return Response({"error": "Please provide exactly two token pairs"}, status=status.HTTP_400_BAD_REQUEST)
        if not fee:
            token_pairs = TokenPairs.objects.filter(token0=token0, token1=token1)
        else:
            token_pairs = TokenPairs.objects.filter(token0=token0, token1=token1, fee=fee)
        if not token_pairs.exists():
            return Response({"error": "Token pair not found."}, status=status.HTTP_404_NOT_FOUND)
        
        response_data = []
        for token_pair in token_pairs:
            swap_events = SwapEvent.objects.filter(pool_address=token_pair.pool, block_number__gte=start_block_number, block_number__lte=end_block_number)
            mint_events = MintEvent.objects.filter(pool_address=token_pair.pool, block_number__gte=start_block_number, block_number__lte=end_block_number)
            burn_events = BurnEvent.objects.filter(pool_address=token_pair.pool, block_number__gte=start_block_number, block_number__lte=end_block_number)
            collect_events = CollectEvent.objects.filter(pool_address=token_pair.pool, block_number__gte=start_block_number, block_number__lte=end_block_number)
            swap_events_data = SwapEventSerializer(swap_events, many=True).data
            mint_events_data = MintEventSerializer(mint_events, many=True).data
            burn_events_data = BurnEventSerializer(burn_events, many=True).data
            collect_events_data = CollectEventSerializer(collect_events, many=True).data
            
            response_data.append({
                "token_pair": TokenPairsSerializer(token_pair).data,
                "swap_events": swap_events_data,
                "mint_events": mint_events_data,
                "burn_events": burn_events_data,
                "collect_events": collect_events_data
            })
        
        return Response(response_data)
            
        
        
        
        