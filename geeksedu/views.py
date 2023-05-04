from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feedback

class FeedbackView(APIView):
    def post(self, request):
        name = request.data.get('name')
        last_name = request.data.get('last_name')
        age = request.data.get('age')
       
