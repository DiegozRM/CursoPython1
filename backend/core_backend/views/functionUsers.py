from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Usuario
from voluptuous.schema_builder import Required
from backend.utils import validate_data
from unidecode import unidecode

def capi(input_string):
    capitalized_string = input_string.capitalize()
    without_accents = unidecode(capitalized_string)
    return without_accents

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user (request):
    users = Usuario.objects.all()
    response = []
    for user in users:
        response.append({
            'id':user.id,
            'nombre':user.nombre,
            'apellido':user.apellido,
            'identificador':user.identificador,
        })
    return Response(response)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_id (request):
    response = []
    data = validate_data({
        Required('identificador'):int,
    },request.data)
    try:
        user=Usuario.objects.get(identificador=data['identificador'])
        response.append({
            'id':user.id,
            'nombre':user.nombre,
            'apellido':user.apellido,
            'identificador':user.identificador,
        })
        return Response(response)
    except:
        return Response('Usuario no encontrado')

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user (request):
    data = validate_data({
        Required('nombre'):str,
        ('apellido'):str,
        #('identificador'):int,
    },request.data)
    if 'apellido' not in data:
        data['apellido'] = None
    else:
        data['apellido']=capi(data['apellido'])
    data['nombre']=capi(data['nombre'])
    # Obtener el último id de Usuario
    last_user_id = Usuario.objects.latest('id').id if Usuario.objects.exists() else 0
    # Calcular el nuevo identificador sumándole 1000
    new_identifier = last_user_id + 1000
    # Crear la instancia de Usuario con el nuevo identificador
    user = Usuario.objects.create(nombre=data['nombre'], apellido=data['apellido'], identificador=new_identifier)

    #user = Usuario.objects.create(nombre=data['nombre'],apellido=data['apellido'],identificador=id+1000)
    user.save()
    return Response('Usuario creado con exito')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user (request):
    data = validate_data({
        Required('identificador'):int,
        ('nombre'):str,
        ('apellido'):int,
    },request.data)
    try:
        user=Usuario.objects.get(identificador=data['identificador'])
        if 'nombre' in data:
            
            user.nombre=capi(data['nombre'])
        if 'apellido' in data:
            user.apellido=capi(data['apellido'])
        user.save()
        return Response('Usuario actualizado con exito')
    except: 
        return Response('El usuario que deseas modificar no existe')

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request):
    data = validate_data({
        Required('identificador'):int,
    }, request.data)
    try:
        user = Usuario.objects.get(identificador=data['identificador'])
        user.delete()
        return Response('Usuario eliminado exitosamente')
    except:
        return Response('El usuario que deseas eliminar no existe')