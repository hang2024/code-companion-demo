from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        return get_tutorials(request)
    elif request.method == 'POST':
        return create_tutorial(request)
    elif request.method == 'DELETE':
        return delete_all_tutorials()

def get_tutorials(request):
    title = request.GET.get('title', None)
    tutorials = Tutorial.objects.filter(title__icontains=title) if title else Tutorial.objects.all()
    tutorials_serializer = TutorialSerializer(tutorials, many=True)
    return JsonResponse(tutorials_serializer.data, safe=False)

def create_tutorial(request):
    tutorial_data = JSONParser().parse(request)
    tutorial_serializer = TutorialSerializer(data=tutorial_data)
    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_all_tutorials():
    count, _ = Tutorial.objects.all().delete()
    return JsonResponse({'message': f'{count} Tutorials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_tutorial(tutorial)
    elif request.method == 'PUT':
        return update_tutorial(request, tutorial)
    elif request.method == 'DELETE':
        return delete_tutorial(tutorial)

def get_tutorial(tutorial):
    tutorial_serializer = TutorialSerializer(tutorial)
    return JsonResponse(tutorial_serializer.data)

def update_tutorial(request, tutorial):
    tutorial_data = JSONParser().parse(request)
    tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data)
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_tutorial(tutorial):
    tutorial.delete()
    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
    tutorials_serializer = TutorialSerializer(tutorials, many=True)
    return JsonResponse(tutorials_serializer.data, safe=False)
