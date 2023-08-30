# myproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
     path('repo/', include('repo.urls')),
    # path('repository/<int:pk>/', views.RepositoryDetailView.as_view(), name='repository_detail'),
    # Define other project URLs here
]