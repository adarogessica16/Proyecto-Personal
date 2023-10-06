from django.db import models
from registro.models import Usuario  # Importa el modelo Usuario de la aplicación "registro"
from menu.models import Menu  # Importa el modelo Menu de la aplicación "menu"

class Pedido(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    menus = models.ManyToManyField(Menu, through='DetallePedido')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nombre

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pedido.cliente.nombre


