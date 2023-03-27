from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                last_name= validated_data['last_name'],
                first_name=validated_data['first_name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     password = validated_data.get('password', None)
    #     if password:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
