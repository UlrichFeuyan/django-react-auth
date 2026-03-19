from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import UserSerializer
from api.models import Note
from api.serializers import NoteSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class NoteListCreate(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Une requête ne peut obtenir réponse positive de cette vue que si elle inclus des informations d'authentification correctes

    def get_queryset(self):
        """surcharge la méthode get_queryset de ListCreateAPIView
        Elles permet de limiter l'accès de cette fonction aux notes apartenant au User authentifier

        Returns:
            _type_: Note
        """
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """surcharge la méthode get_queryset de ListCreateAPIView
        Elles permet de limiter l'accès de cette fonction aux notes apartenant au User authentifier

        Returns:
            _type_: Note
        """
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
