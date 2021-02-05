from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("register", RegisterManagerView, basename="RegisterManager")

urlpatterns = [
    # path('login/', UserLoginView.as_view(), name="login"),
    path('employee/create/', EmployeeCreateAPIView.as_view(), name="EmployeeCreate"),
    path('employee/list/', EmployeeListAPIView.as_view(), name="EmployeeList"),
    path('employee/detail/<int:pk>', EmployeeDetailAPIView.as_view(), name="EmployeeDetail"),
    path('employee/update/<int:pk>', EmployeeUpdateAPIView.as_view(), name="EmployeeUpdate"),
    path('', include(router.urls)),
]
