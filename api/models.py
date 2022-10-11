from django.db import models

# Create your models here.


class Section(models.Model):
	name = models.CharField("name", max_length=255, blank=True, null=True)
	description = models.CharField("description", max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField("name", max_length=255, blank=True, null=True)
	description = models.CharField("description", max_length=255, blank=True, null=True)
	price = models.PositiveSmallIntegerField("price", blank=True, null=True)
	section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='items')

	def __str__(self):
		return self.name


class Modifier(models.Model):
	description = models.CharField("description", max_length=255, blank=True, null=True)
	items = models.ManyToManyField(Item, related_name="modifiers", blank=True)
	
	def __str__(self):
		return self.description
