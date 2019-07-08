from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        teacher = request.user.teacher.last_name
        response = {
            'username': teacher,
            "id": "id",
        }
        return Response(response)
