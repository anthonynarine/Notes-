from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from api.serializers import NotesSerializer

from api.models import Notes
from api.serializers import NoteSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view( [ "GET", "POST" ])
def notess_list(request):
    if request.method == "GET":
        note = Notes.objects.all()
    
        title = request.GET.get("title", None)
        if title is not None:
            notes = notes.filter(name__icontsins=title)  #this django filter is explained below.  
        
        notes_serializer = NotesSerializer(notes, many=True)
        return Response(notes_serializer.data)
        # "SAFE=FALSE" FOR OBJECTS SERIALIZATION
    elif request.method == "POST":
        notes_data = JSONParser().parse(request)
        notes_serializer = NotesSerializer(data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return Response(notes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(notes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    # LINE 17-19 EXPLAINED
    # Django filter allows users to filter down a queryset based on a model's fields.
    # The "icontains" checks if either the title of the description field contains the value of the 
    # search_terms.
