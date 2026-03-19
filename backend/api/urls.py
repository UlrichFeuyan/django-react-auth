from django.urls import path
from api.views import CreateUserView, NoteListCreate, NoteDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name="api"
urlpatterns = [
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresdh"),
    
    path("notes/", NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>", NoteDelete.as_view(), name="note-delete")
]
