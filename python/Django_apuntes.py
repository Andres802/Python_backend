Comparto aquí un resumen de la clase espero les sea útil:

Las opciones que Django propone para implementar Usuarios personalizados son:
- Usando el Modelo proxy
- Extendiendo la clase abstracta de Usuario existente

Para el presente proyecto debemos crear los campos de usuario:

    website
    biography
    phone_number
    profile picture
    created
    modified

Luego debemos crear la app que se llamará users

sudo python3 manage.py startapp

Crear el modelo
Se debe importar lo que necesitamos

from django.contrib.auth.models import User

Luego se crea los campos adicionales que se necesitan según el proyecto

class Profle (models.Model):
    """Profile Model."""
    """Proxy model that extends the base data with other information"""
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    website=models.URLField(max_length=200,blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)
    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return username."""
        return self.user.username

Posterior a eso dirigirse al archivo de settings.py y así como se instaló post se va a instalar users

Para que funcione el campo ImageField se debe instalar la librería Pillow y se lo hace de la siguiente manera

sudo pip install Pillow

Después ejecutar para que se hagan efecto las migraciones

python3 manage.py makemigrations
python3 manage.py migrate

Y para ingresar al administrador de django crear el super usuario

python3 manage.py createsuperuser
