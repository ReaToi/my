from django.urls import path
from . import views, consumers


urlpatterns = [
    path("test/", views.TestAPIView.as_view()),
    # path('ws/some_path/', consumers.MyConsumer.as_asgi()),
    # path('ws/test/', consumers.Test.as_asgi()),


]
