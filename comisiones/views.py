from django.shortcuts import render
from .models import Venta, ReglaComision
from decimal import Decimal


# Función auxiliar: calcula la comisión según las reglas configuradas
def calcular_comision(monto, reglas):
    comision = Decimal('0')
    for regla in reglas:
        if monto >= regla.monto_minimo:
            comision = monto * (regla.porcentaje / Decimal('100'))
    return comision


# Vista principal: recibe fechas por GET, filtra ventas y calcula comisiones
def reporte_ventas(request):
    ventas          = []
    fecha_inicio    = request.GET.get('fecha_inicio', '')
    fecha_fin       = request.GET.get('fecha_fin', '')
    total_comisiones = Decimal('0')

    if fecha_inicio and fecha_fin:
        # Filtrar ventas en el rango de fechas
        ventas_qs = Venta.objects.filter(
            fecha__range=[fecha_inicio, fecha_fin]
        ).select_related('vendedor')

        # Obtener reglas ordenadas de menor a mayor monto
        reglas = ReglaComision.objects.all().order_by('monto_minimo')

        # Calcular comisión por cada venta
        for venta in ventas_qs:
            comision = calcular_comision(venta.monto, reglas)
            total_comisiones += comision
            ventas.append({
                'vendedor'   : venta.vendedor.nombre,
                'descripcion': venta.descripcion,
                'monto'      : venta.monto,
                'fecha'      : venta.fecha,
                'comision'   : comision,
            })

    context = {
        'ventas'          : ventas,
        'fecha_inicio'    : fecha_inicio,
        'fecha_fin'       : fecha_fin,
        'total_comisiones': total_comisiones,
    }
    return render(request, 'comisiones/reporte.html', context)
