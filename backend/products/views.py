from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Retrieve title and content from the validated data
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # If no content is provided, use the title as the content
        if content is None:
            content = title
        # Save the product with the possibly updated content
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

        
product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        # super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

        
product_update_view = ProductUpdateAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not gonna use this method
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()


# --------------------- OR --------------------
## Using Function Based Views For Create Retrieve or List
@api_view(['GET','POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method # PUT --> update # DESTROY --> delete

    if method == "GET":
        # detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        # create an item

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data, status=201)
        return Response({"message": "Invalud data!"}, status=400)
