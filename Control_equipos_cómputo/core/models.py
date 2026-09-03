from django.db import models


class Equipo(models.Model):
    TIPO_EQUIPO_CHOICES = [
        ('desktop', 'Desktop'),
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('impresora', 'Impresora'),
        ('servidor', 'Servidor'),
        ('otro', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('en_uso', 'En uso'),
        ('en_reparacion', 'En reparación'),
        ('dado_de_baja', 'Dado de baja'),
    ]

    codigo_interno = models.CharField(max_length=50, unique=True)
    tipo_equipo = models.CharField(max_length=20, choices=TIPO_EQUIPO_CHOICES)
    marca = models.CharField(max_length=100)
    serial = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.codigo_interno} - {self.marca} ({self.get_tipo_equipo_display()})"
