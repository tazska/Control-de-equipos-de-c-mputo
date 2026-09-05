from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'equipos', views.EquipoViewSet)

urlpatterns = [
    # --- API REST (accesible en /api/) ---
    path('api/', include(router.urls)),

    # --- CRUD tradicional ---
    path('', views.EquipoListView.as_view(), name='inicio'),
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/nuevo/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('equipos/<int:pk>/editar/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('equipos/<int:pk>/eliminar/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
]