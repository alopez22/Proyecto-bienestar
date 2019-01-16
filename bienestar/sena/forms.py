#Importa este directorio forms para recoger todos nuestros formularios.
from django import forms
#Importamos desde el archivo models.py los siguientes modelos:
from .models import Categoria, Perfil, Centros, Eventos, Tips
#Importamos los ajustes para authentificar a lo Usuarios de nuestra aplicacion.
from django.contrib.auth.models import User 

#creamos una clase para nuestro inicio de sesión (formulario)
#Especificamos el tipo de dato que recogera cada variable.
class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
	contraseña  = forms.CharField(widget = forms.PasswordInput(render_value=False, attrs={"class":"form-control"}))

#Clase que nos creará un formulario para agregar datos de categoría.
class agregar_categoria_form(forms.ModelForm):
	class Meta:
		#Le indicamos que recoja los datos del modelo Categoría
		model = Categoria
		fields = '__all__'

class agregar_centro_form(forms.ModelForm):
	class Meta:
		#Le indicamos que recoja los datos del modelo Categoría
		model = Centros
		fields = '__all__'

class agregar_eventos_form(forms.ModelForm):
	class Meta:
		#Le indicamos que recoja los datos del modelo Categoría
		model = Eventos
		fields = '__all__'

class agregar_tips_form(forms.ModelForm):
	class Meta:
		#Le indicamos que recoja los datos del modelo Categoría
		model = Tips
		fields = '__all__'

#Clase que nos permite registrar a un usuario, para asignarle su perfil en la página.
class register_form(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	email = forms.EmailField(widget=forms.TextInput())
	password_1 = forms.CharField(label= 'Password',widget=forms.PasswordInput(render_value=False))
	password_2 = forms.CharField(label= 'Confirmar Password',widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ya Existe')

	def clean_password_2(self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']

		if password_1 == password_2:
			pass
		else:
			raise forms.ValidationError('Los password no coinciden')
# Clase que nos reccoge los datos del modelo Perfil
class perfil_form(forms.ModelForm):
	class Meta:
		model = Perfil
		#Le especificamos los campos que queremos extraer del modelo.
		fields = ['imagen', 'documento','edad']
		exclude = ['user']