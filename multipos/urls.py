"""multipos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view

from branches.viewsets.branch_viewset import BranchViewSet
from branches.viewsets.company_viewset import CompanyViewSet
from users.viewsets.user_viewset import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register("users", UserViewSet, basename="users")
router.register("companies", CompanyViewSet, basename="companies")
router.register("branches", BranchViewSet, basename="branches")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "openapi",
        get_schema_view(title="Your Project", description="API for multipos"),
        name="openapi-schema",
    ),
]
