from contextvars import Token
from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoCompleteSerializer
from todo.models import Todo
from django.db import IntegrityError
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from rest_framework.parsers import JSONParser

from django.http import JsonResponse

@csrf_exempt
def signup(request):
    if request.method == 'POST':
            try:
                data = JSONParser().parse(request)
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                user.save()
                login(request, user)
                return JsonResponse({'token':'gafgdsghhsh'},status=201)
            except IntegrityError:
                return JsonResponse({'error':'That username alredy been taken choose another one plz!'},status=400)
            

#login view
@csrf_exempt
def login(request):
    if request.method == 'POST':
                data = JSONParser().parse(request)
                user = authenticate(request, username=data['username'], password=data['password'])
                user.save()
                if user is None:
                    return JsonResponse({'error':'Username and password did not match'},status=400)
                else:
                    try:
                        token=Token.objects.get(user=user)
                        return JsonResponse({'token':str(token)},status=200)
                    except Token.DoesNotExist:
                        return JsonResponse({'error':'Token not found'},status=400)
            

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')


class TodoListCreate(generics.ListCreateAPIView):   # fixed base class
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()   # fixed spelling
        serializer.save()
