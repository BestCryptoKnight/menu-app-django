from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Section, Item, Modifier
from .serializers import SectionSerializer, ItemSerializer, ModifierSerializer, AllSerializer


############### Section ##################

class AllSections(APIView):

	def get(self, request, id=None):
		if id:
			section = get_object_or_404(Section, id=id)
			serializer = SectionSerializer(section)
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
			
		sections = Section.objects.all()
		serializer = SectionSerializer(sections, many=True)
		return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
	
	def post(self, request):
		serializer = SectionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
		
		return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
	def put(self, request, id=None):
		section = get_object_or_404(Section, id=id)
		serializer = SectionSerializer(section, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "success", "data": serializer.data})
		
		return Response({"status": "error", "data": serializer.errors})

	def delete(self, request, id=None):
		section = get_object_or_404(Section, id=id)
		section.delete()
		return Response({"status": "success", "data": "Section Deleted"})


############### Item ##################

class AllItems(APIView):

	def get(self, request, id=None):
		if id:
			item = get_object_or_404(Item, id=id)
			serializer = ItemSerializer(item)
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
			
		items = Item.objects.all()
		serializer = ItemSerializer(items, many=True)
		return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
	
	def post(self, request, section_id=None):
		if section_id:
			section = get_object_or_404(Section, id=section_id)
			serializer = ItemSerializer(data=request.data, context={"section": section})

			if serializer.is_valid():
				serializer.save()
				return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
			
			return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
		
		return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
	
	def put(self, request, id=None):
		item = get_object_or_404(Item, id=id)
		serializer = ItemSerializer(item, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "success", "data": serializer.data})
		
		return Response({"status": "error", "data": serializer.errors})
	
	def delete(self, request, id=None):
		item = get_object_or_404(Item, id=id)
		item.delete()
		return Response({"status": "success", "data": "Item Deleted"})


################## Modifier ####################


class AllModifiers(APIView):

	def get_object(self, id):
		try:
			return Modifier.objects.get(id=id)
		except Modifier.DoesNotExist:
			return Response({"status":"failure", "message": "Modifier Does Not Exist."}, status=status.HTTP_404_NOT_FOUND)

	def get(self, request, id=None):
		if id:
			modifier = get_object_or_404(Modifier, id=id)
			serializer = ModifierSerializer(modifier)
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
			
		modifiers = Modifier.objects.all()
		serializer = ModifierSerializer(modifiers, many=True)
		return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
	
	def post(self, request):
		serializer = ModifierSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
		
		return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
	def put(self, request, id=None):
		modifier = get_object_or_404(Modifier, id=id)
		serializer = ModifierSerializer(modifier, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "success", "data": serializer.data})
		
		return Response({"status": "error", "data": serializer.errors})
	
	def delete(self, request, id=None):
		modifier = get_object_or_404(Modifier, id=id)
		modifier.delete()
		return Response({"status": "success", "data": "Modifier Deleted"})

########### Item -> Modifier ################

@api_view(['POST'])
def add_modifier(request, item_id, modifier_id):
	if request.method == "POST":
		item = get_object_or_404(Item, id=item_id)
		modifier = get_object_or_404(Modifier, id=modifier_id)
		modifier.items.add(item)
		return Response({"status":"success"}, status=status.HTTP_200_OK)

########### All sections, items, modifiers ##########

@api_view(['GET'])
def all_values(request):
	sections = Section.objects.all()
	serializer = AllSerializer(sections, many=True)
	return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


		
		

