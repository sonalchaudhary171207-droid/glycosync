from django.urls import path
from .views import GlucoseListCreateView, DietEngineView

urlpatterns = [
    path('glucose/', GlucoseListCreateView.as_view(), name='glucose-list-create'),
    path('diet-engine/', DietEngineView.as_view(), name='diet-engine'),
]