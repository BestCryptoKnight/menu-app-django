from django.urls import include, path
from . import views
  
urlpatterns = [
    path('sections', views.AllSections.as_view()),
    path('sections/<int:id>', views.AllSections.as_view()),
    path('sections/<int:section_id>/items', views.AllItems.as_view()),
    path('items', views.AllItems.as_view()),
    path('items/<int:id>', views.AllItems.as_view()),
    path('modifiers', views.AllModifiers.as_view()),
    path('modifiers/<int:id>', views.AllModifiers.as_view()),
    path('items/<int:item_id>/modifiers/<int:modifier_id>/', views.add_modifier),
    path('all/', views.all_values)
]

