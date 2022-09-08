from app.models import List
from app.api.serializers import ListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ListAV(APIView):

    def get(self, request):
        movies = List.objects.all()
        serializer = ListSerializer(movies, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ListSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = List.objects.get(pk=pk)
        except List.DoesNotExist:
            return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ListSerializer(movie)
        return Response(serializer.data)

    
    def put(self,request, pk):
        movie = List.objects.get(pk=pk)
        serializer = ListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk):
        movie = List.objects.get(pk=pk)
        movie.delete()
        return