from django.db import models


# MODELO 1: Vendedor
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    email  = models.EmailField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name        = 'Vendedor'
        verbose_name_plural = 'Vendedores'


# MODELO 2: Regla de Comisión
# Define el porcentaje que se aplica según el monto mínimo de la venta
class ReglaComision(models.Model):
    descripcion   = models.CharField(max_length=200)
    monto_minimo  = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje    = models.DecimalField(max_digits=5,  decimal_places=2)  # ej: 10.00 = 10%

    def __str__(self):
        return f"{self.descripcion} — {self.porcentaje}%"

    class Meta:
        verbose_name        = 'Regla de Comisión'
        verbose_name_plural = 'Reglas de Comisión'


# MODELO 3: Venta
class Venta(models.Model):
    vendedor    = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, blank=True)
    monto       = models.DecimalField(max_digits=10, decimal_places=2)
    fecha       = models.DateField()

    def __str__(self):
        return f"{self.vendedor.nombre} — ${self.monto} ({self.fecha})"

    class Meta:
        verbose_name        = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering            = ['-fecha']
