from django.shortcuts import render
from django.http import HttpResponse
from mongoengine import connection,DoesNotExist
from .models import Event,User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer,UserSerializer

@api_view(['POST'])
def create_todo(request):
    if request.method == 'POST':
        searializer = TodoItemSerializer(data=request.data)
        if searializer.is_valid():
            todo = searializer.save()
            return Response(searializer.data, status=status.HTTP_201_CREATED)
        return Response(searializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def get_todo(request):
    todos = TodoItem.objects()
    searializer = TodoItemSerializer(todos, many=True)
    return Response(searializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_todo(request, pk):
    try:
        todo = TodoItem.objects.get(id=pk)
    except TodoItem.DoesNotExist:
        return Response({'error': 'Todo not found'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    searializer = TodoItemSerializer(todo,data=request.data)
    if searializer.is_valid():
            todo = searializer.save()
            return Response(searializer.data, status=status.HTTP_201_CREATED)
    return Response(searializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo(request, pk):
    try:
        todo = TodoItem.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except TodoItem.DoesNotExist:
        return Response({'error': 'Todo not found'},
                        status=status.HTTP_404_NOT_FOUND
                        )

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer =UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # {'message': 'User registered successfully!'}, 


@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

    try:
        user = User.objects.get(username = username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            return Response({"refresh": str(refresh), "access": access}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    except DoesNotExist:
            return Response({'error": "Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def test_mongodb_connection(request):
    # Check if MongoDB is connected
    try:
        # List all MongoDB connections
        connections = connection._connections
        if connections:
            # Test creating and retrieving a document
            event = Event(title="Test Event", date="2024-09-30", description="Testing MongoDB connection")
            event.save()  # Save the event to MongoDB
            
            # Check if document was saved successfully
            saved_event = Event.objects(title="Test Event").first()
            if saved_event:
                return HttpResponse("MongoDB is connected and working. Event created: " + saved_event.title)
            else:
                return HttpResponse("MongoDB is connected, but could not save the event.")
        else:
            return HttpResponse("MongoDB is not connected.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
