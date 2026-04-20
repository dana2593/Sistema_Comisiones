# Sistema de Ventas y Comisiones con Django (MTV)

Proyecto académico desarrollado con Django siguiendo el patrón de diseño **MTV (Modelo - Template - Vista)**, variante del clásico MVC.

## ¿Qué hace?
- Gestiona **Vendedores**, **Reglas de Comisión** y **Ventas**
- Filtra ventas por **rango de fechas**
- Calcula automáticamente la **comisión** de cada venta según las reglas configuradas

## Patrón MTV
| Capa | Archivo | Responsabilidad |
|------|---------|----------------|
| **Modelo** | `comisiones/models.py` | Define Vendedor, ReglaComision, Venta |
| **Template** | `comisiones/templates/` | HTML que muestra los datos al usuario |
| **Vista** | `comisiones/views.py` | Lógica: filtra ventas y calcula comisiones |

## Estructura del proyecto
```
sistema_comisiones/
├── comisiones/
│   ├── migrations/
│   ├── static/comisiones/css/
│   │   └── estilos.css
│   ├── templates/comisiones/
│   │   └── reporte.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── sistema_comisiones/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Cómo ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/sistema-comisiones.git
cd sistema-comisiones

# 2. Crear entorno virtual
python -m venv venv

# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (para el admin)
python manage.py createsuperuser

# 6. Correr el servidor
python manage.py runserver
```

- App principal: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

## Deploy
Desplegado en PythonAnywhere: http://TUUSUARIO.pythonanywhere.com/

## Información
- **Estudiante:** [Tu nombre]
- **Materia:** Ingeniería Web
- **Universidad:** UDLA
