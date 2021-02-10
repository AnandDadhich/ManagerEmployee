from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from .models import UserInfo, Manager, Employee
from drf_writable_nested import WritableNestedModelSerializer, NestedCreateMixin, NestedUpdateMixin

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#
#
# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password is not found.'
#             )
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#         except ManagerInfo.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#         return {
#             'email': user.email,
#             'token': jwt_token
#         }


class UserInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = UserInfo
        exclude = ("groups","user_permissions")
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")


        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user


class ManagerSerializer(WritableNestedModelSerializer):
    user = UserInfoSerializer(many=False)

    class Meta:
        model = Manager
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data['user']['password']
        if len(password) < 6:
            raise ValidationError("Minimum password length is 6", code=400)
        else:
            a = dict(validated_data['user'])

            user = UserInfo(**a)
            user.is_active=True
            user.save()
            user.set_password(password)
            user.save()

            validated_data.pop("user")

            contact = Manager.objects.create(user=UserInfo.objects.get(email=user), **validated_data)
            if contact:
                return contact
            else:
                user.delete()


class EmployeeSerializer(WritableNestedModelSerializer):
    emp_user = UserInfoSerializer()

    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data['emp_user']['password']
        print(password)
        if len(password) < 6:
            raise ValidationError("Minimum password length is 6", code=400)
        else:
            a = dict(validated_data['emp_user'])
            user = UserInfo(**a)
            user.save()
            user.is_active=True
            user.set_password(password)
            user.save()

            validated_data.pop('emp_user')

            contact = Employee.objects.create(emp_user=UserInfo.objects.get(email=user), **validated_data)
            if contact:
                return contact
            else:
                user.delete()