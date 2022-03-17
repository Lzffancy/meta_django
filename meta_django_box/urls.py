"""meta_django_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from message_board.views import MessageBoardViewSet
from meta_django_box import views

# restful注册view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"message_borad",MessageBoardViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_api/',include(router.urls)),
    # query function page
    # todo test_query后面需不需要适应斜杠？
    path("test_query/", include("test_query.urls")),
    # home page

    # 兜底 无法匹配的路由全部导向首页
    # re_path(r'.*', TemplateView.as_view(template_name="index.html")),

]
