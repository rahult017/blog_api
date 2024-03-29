from django.urls import path
from .views import (
    BlogListCreateView,
    BlogRetrieveUpdateDeleteView,
    UserRegistrationView,
)
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="login"),
    path("blogs/", BlogListCreateView.as_view(), name="blog-list-create"),
    path(
        "blogs/<int:pk>/",
        BlogRetrieveUpdateDeleteView.as_view(),
        name="blog-retrieve-update-delete",
    ),
]
