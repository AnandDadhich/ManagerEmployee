from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserInfoSerializer, ManagerSerializer, EmployeeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from Assignment import settings
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
import jwt
from rest_framework_jwt.settings import api_settings
from .models import UserInfo, Manager, Employee
from allauth.account.signals import user_logged_in
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import IsManager

# Create your views here.


# class UserLoginView(RetrieveAPIView):
#     lookup_field = 'pk'
#     queryset = ManagerInfo.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code' : status.HTTP_200_OK,
#             'message': 'User logged in  successfully',
#             'token' : serializer.data['token'],
#             }
#         status_code = status.HTTP_200_OK
#
#         return Response(response, status=status_code)


class RegisterManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self):
        return Manager.objects.get(pk=self.request.get("pk"))

    def partial_update(self, request, *args, **kwargs):
        contact_object = self.get_object()
        x = Manager.objects.filter(id=self.kwargs.get("pk")).values_list('user__id', flat=True).last()
        user_object = UserInfo.objects.get(id=x)

        u_serializer = UserInfoSerializer(user_object, data=request.data, partial=True)
        m_serializer = ManagerSerializer(contact_object, data=request.data, partial=True)

        if m_serializer.is_valid(raise_exception=True) and u_serializer.is_valid(raise_exception=True):
            self.perform_update(u_serializer)
            self.perform_update(m_serializer)
            u_serializer.save()
            m_serializer.save()

            return Response({"data": [m_serializer.data], 'status': 200}, status=status.HTTP_200_OK)
        return Response({"message": "Wrong Parameters", "status": 400}, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == "retrieve":
            return [AllowAny(), ]
        return super(RegisterManagerView, self).get_permissions()


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsManager,)
    authentication_classes = (JSONWebTokenAuthentication,)

class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsManager,)
    authentication_classes = (JSONWebTokenAuthentication,)


class EmployeeDetailAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsManager,)
    authentication_classes = (JSONWebTokenAuthentication,)


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsManager,)
    authentication_classes = (JSONWebTokenAuthentication,)
