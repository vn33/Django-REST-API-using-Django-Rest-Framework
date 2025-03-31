from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        product_instance = serializer.save()
        serializer = ProductSerializer(product_instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"message":"Invalid data"}, status=400)

