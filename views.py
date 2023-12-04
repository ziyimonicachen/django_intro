from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AppDevClubReviewsView(APIView):
    def __init__(self):
        self.reviews = ['app dev is great']

    def get(self, request):
        return Response({'reviews': self.reviews})
    
    def post(self, review):
        self.reviews.append(review)
        return Response({'message':'Review added successfully'})