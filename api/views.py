from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import json
import requests


@api_view(['GET'])
@permission_classes([AllowAny])
def get_with_parameters(request):
    if all(request.query_params.get(k) for k in ('from', 'to', 'value')):
        try:
            old_key = request.query_params['from'].upper()
            new_key = request.query_params['to'].upper()
            amount = float(request.query_params['value'].replace(',', '.'))
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={old_key}&tsyms={new_key}')
            rate = json.loads(r.content)[new_key]
            new_price = round(rate * amount, 3)
        except KeyError:
            return Response({'message': 'Use correct 3-letters currency abbreviation'},
                            status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'message': 'Parameter "value" should be a number'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Service unavailable'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': f'{new_price}'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'parameters of get-request should be "?from=CUR1&to=CUR2&value=AMOUNT" where '
                                    'CUR1 - converted currency, CUR2 - new currency, '
                                    'AMOUNT - amount of converted currency'},
                        status=status.HTTP_400_BAD_REQUEST)
