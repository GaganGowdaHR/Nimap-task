from django.urls import path,include
from blog.views import ClientListCreateAPIView,ClientRetrieveUpdateDestroyAPIView,ProjectListCreateAPIView,ProjectRetrieveUpdateDestroyAPIView  

urlpatterns = [
    # path('categories',CategoryAPIView.as_view()),
    path('clients',ClientListCreateAPIView.as_view()),
    path('clients/<int:pk>',ClientRetrieveUpdateDestroyAPIView.as_view()),
    path('project',ProjectListCreateAPIView.as_view()),
    path('project/<int:pk>',ProjectRetrieveUpdateDestroyAPIView.as_view()),
]