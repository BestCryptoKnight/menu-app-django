from django.db.models import fields
from rest_framework import serializers
from .models import Section, Item, Modifier


class ModifierSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Modifier
		fields = ('id', 'description')

class ItemSerializer(serializers.ModelSerializer):
	modifiers = ModifierSerializer(many=True, read_only=True)
	
	def create(self, data):
		data["section"] = self.context["section"]
		return Item.objects.create(**data)
	
	class Meta:
		model = Item
		fields = ('id', 'name', 'description', 'price', 'modifiers')
	
class SectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Section 
		# fields = ('name', 'description', 'items')
		fields = '__all__'

class AllSerializer(serializers.ModelSerializer):
	items = ItemSerializer(many=True, read_only=True)

	class Meta:
		model = Section 
		# fields = ('name', 'description', 'items')
		fields = '__all__'
