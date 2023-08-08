from django.shortcuts import render
from .models import Label
from .serializers import labelSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class labelTable(APIView):
    def get(self,request,id=None):

        if id==None:
            data=Label.objects.all()
            seri=labelSerializers(data,many=True)
            response_data={
                "status": status.HTTP_200_OK,
                "data": seri.data
            }
            return Response(response_data)

        Label_data=self.gettingData(id)
        if Label_data:
            seri_data=labelSerializers(Label_data)
            response_data={
                "status" : status.HTTP_200_OK,
                "data" : seri_data.data
            }
            return Response(response_data)
        else :
            response_data={
                "status" : status.HTTP_204_NO_CONTENT,
                "message" : "Data does not exists"
            }
            return Response(response_data)
    
    def post(self,request):
        serializer_data=labelSerializers(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            response_data={
                "status": status.HTTP_201_CREATED,
                "data": serializer_data.data
            }
            return Response(response_data)
        return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer_data.errors})
    
    def gettingData(self,id):
        try:
            return Label.objects.get(id=id)
        except Label.DoesNotExist:
            return None
    
    def put(self,request,id):
        put_data=self.gettingData(id)
        if put_data:
            serializeput=labelSerializers(put_data,data=request.data)
            if serializeput.is_valid():
                serializeput.save()
                response_data={
                "status": status.HTTP_201_CREATED,
                "data": serializeput.data}
                return Response(response_data)
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializeput.errors})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message":"Data does not exists in database"})
    
    def delete(self,request,id):
        delete_data=self.gettingData(id)
        if delete_data:
            delete_data.delete()
            response_data={
                "status":status.HTTP_202_ACCEPTED,
                "message": "Data is deleted successfully"
            }
            return Response(response_data)
        return Response({"status":status.HTTP_204_NO_CONTENT,"message":"Data does not exists in the database"})


