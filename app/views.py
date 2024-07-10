from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet,ModelViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrudView(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        MSPO=ProductMS(LPO,many=True)
        return Response(MSPO.data)

    def retrieve(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JO=ProductMS(PO)
        return Response(JO.data)
    def create(self,request):
        PO=request.data
        JO=ProductMS(data=PO)
        if JO.is_valid():
            JO.save()
        return Response({'create':'Data is inseted'})

    def update(self,request,pk):
        PO=Product.objects.get(pid=pk)
        jd=request.data
        MSPO=ProductMS(PO,data=jd)
        if MSPO.is_valid():
            MSPO.save()
            return Response({'update':'Updated succesfully'})
        else:
            return Response({'update':'Not updated'})


    def partial_update(self,request,pk):
        PO=Product.objects.get(pid=pk)
        jd=request.data
        MSPO=ProductMS(PO,data=jd,partial=True)
        if MSPO.is_valid():
            MSPO.save()
            return Response({'update':'Updated succesfully'})
        else:
            return Response({'update':'Not updated'})

    def destroy(self,request,pk):
        PO=Product.objects.get(pid=pk)
        PO.delete()
        return Response({'delete':'Deleted is done'})


class ProductCrudMVS(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductMS