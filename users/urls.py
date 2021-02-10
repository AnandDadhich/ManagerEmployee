from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title="Swagger Docs")

router = DefaultRouter()
router.register("register", RegisterManagerView, basename="RegisterManager")

urlpatterns = [
    # path('login/', UserLoginView.as_view(), name="login"),
    path('docs/', schema_view),
    path('employee/create/', EmployeeCreateAPIView.as_view(), name="EmployeeCreate"),
    path('employee/list/', EmployeeListAPIView.as_view(), name="EmployeeList"),
    path('employee/detail/<int:pk>', EmployeeDetailAPIView.as_view(), name="EmployeeDetail"),
    path('employee/update/<int:pk>', EmployeeUpdateAPIView.as_view(), name="EmployeeUpdate"),
    path('', include(router.urls)),
]
