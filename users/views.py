from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from users.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class =  UserSerializer

class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class =  UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
   
class CreateTokenView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })