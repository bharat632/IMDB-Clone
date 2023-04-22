from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from stream.models import Stream, Show, Review
from .serializer import StreamSerializer, ShowSerializer, ReviewSerializer

# Create your views here.

class StreamAV(APIView):
    def get(self, request):
        streams = Stream.objects.all()
        serializer = StreamSerializer(streams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StreamDetailsAV(APIView):
    def get(self, request, pk):
        msg = {'errors':'Stream not found!'}
        try:
            stream = Stream.objects.get(pk=pk)
        except Stream.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamSerializer(stream)
        return Response(serializer.data)
        
    def put(self, request, pk):
        stream = Stream.objects.get(pk=pk)
        serializer = StreamSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stream = Stream.objects.get(pk=pk)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShowsAV(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShowDetailsAV(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ShowReviewsAV(APIView):
    def get(self, request, pk):
        msg = {'error':'Review Not Found!'}
        try:
            reviews = Review.objects.filter(shows = pk)
            print(reviews)
        except Review.DoesNotExist:
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
        serializer = ReviewSerializer(reviews, many =True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request,pk):

        show = Show.objects.get(pk= pk)
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(shows = show)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


class ReviewsVS(viewsets.ViewSet):

    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        queryset = Review.objects.all()
        show = get_object_or_404(queryset, pk= pk)
        serializer = ReviewSerializer(show)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        review = get_object_or_404(Review, pk= pk)
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        review = get_object_or_404(Review, pk= pk)
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# class ReviewDetailsAV(APIView):
#     def get(self, request, pk):
#         msg = {'error':'Review Not Found!'}
#         try:
#             review = Review.objects.get(pk = pk)
#         except Review.DoesNotExist:
#             return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
#         serializer = ReviewSerializer(review, context={'request': request})
#         return Response(serializer.data , status = status.HTTP_200_OK)
