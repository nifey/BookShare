from rest_framework import views
from .serializers import CreateUserSerializer
from rest_framework.response import Response
from .models import User


class CreateUserView(views.APIView):
    # this api creates the users
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # password has to be created separately. serializer.save() only creates the user

            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=500)

