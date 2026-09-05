from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import viewsets

from .models import Equipo
from .serializers import EquipoSerializer
from .forms import EquipoForm


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoListView(ListView):
    model = Equipo
    template_name = 'core/equipo_list.html'
    ordering = ['-fecha_registro']


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'core/equipo_detail.html'


class EquipoCreateView(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'core/equipo_form.html'
    success_url = reverse_lazy('equipo_list')

    def form_valid(self, form):
        messages.success(self.request, f'Equipo "{form.cleaned_data["codigo_interno"]}" creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el equipo. Revisa los campos marcados.')
        return super().form_invalid(form)


class EquipoUpdateView(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'core/equipo_form.html'
    success_url = reverse_lazy('equipo_list')

    def form_valid(self, form):
        messages.success(self.request, f'Equipo "{form.cleaned_data["codigo_interno"]}" actualizado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el equipo. Revisa los campos marcados.')
        return super().form_invalid(form)


class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'core/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo_list')

    def delete(self, request, *args, **kwargs):
        equipo = self.get_object()
        messages.success(request, f'Equipo "{equipo.codigo_interno}" eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)