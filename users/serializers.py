from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validate_data):

        return get_user_model().objects.create_user(**validate_data)
    
    def update(self,instance,validated_data):
        
        password = validated_data.pop('password', None)
        user = super().update(instance,validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
       
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type':'password'})

    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )

        if not user:
            raise serializers.ValidationError('No se pudo autenticar', code='authorization')
        
        data['user'] = user
        return data
        