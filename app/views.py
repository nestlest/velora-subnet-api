from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from .models import TokenPairs, SwapEvent, MintEvent, BurnEvent, CollectEvent

from .utils import normalize_datetime
from pool_data_fetcher import BlockchainClient

import csv

def index(request):
    return render(request, 'app/index.html')
class PoolEventsDownload(generics.GenericAPIView):
    def __init__(self) -> None:
        super().__init__()
        self.blockchainclient = BlockchainClient(settings.ETHEREUM_RPC_NODE_URL)
    
    def get(self, request, *args, **kwargs):
        model_map = {
            'swap': (SwapEvent, ["transaction_hash", "pool_address", "block_number", "sender", "to", "amount0", "amount1", "sqrt_price_x96", "liquidity", "tick"]),
            'mint': (MintEvent, ["transaction_hash", "pool_address", "block_number", "sender", "owner", "tick_lower", "tick_upper", "amount", "amount0", "amount1"]),
            'burn': (BurnEvent, ["transaction_hash", "pool_address", "block_number", "owner", "tick_lower", "tick_upper", "amount", "amount0", "amount1"]),
            'collect': (CollectEvent, ["transaction_hash", "pool_address", "block_number", "owner", "recipient", "tick_lower", "tick_upper", "amount0", "amount1"]),
        
        }
        event_type = request.query_params.get("event_type", None)
        token0 = request.query_params.get("token0", None)
        token1 = request.query_params.get("token1", None)
        fee = request.query_params.get("fee", None)
        start_datetime = request.query_params.get("start_datetime", None)
        end_datetime = request.query_params.get("end_datetime", None)
        start_datetime = normalize_datetime(start_datetime)
        end_datetime = normalize_datetime(end_datetime)
        print(start_datetime, end_datetime)
        start_block_number, end_block_number = self.blockchainclient.get_block_number_range(start_datetime, end_datetime)
        if not token0 or not token1 or not fee:
            return Response({"error": "Please provide exactly two token pairs"}, status=status.HTTP_400_BAD_REQUEST)
        
        token_pair = TokenPairs.objects.filter(token0=token0, token1=token1, fee=fee).first()
        if not token_pair:
            return Response({"error": "Token pair not found."}, status=status.HTTP_404_NOT_FOUND)
        
        model, headers = model_map[event_type]
        events = model.objects.filter(pool_address=token_pair.pool, block_number__gte=start_block_number, block_number__lte=end_block_number)
        response = HttpResponse(content_type='text/csv')
        response["Content-Disposition"] = f'attachment; filename="{event_type}_events_{start_datetime}_{end_datetime}_{token0}_{token1}.csv"'
        
        writer = csv.writer(response)
        writer.writerow(headers)
        
        for event in events:
            row = [getattr(event, field, '') for field in headers]
            writer.writerow(row)
        return response
            
            
        
        
        
        