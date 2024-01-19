from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Sala
from voluptuous.schema_builder import Required
from backend.utils import validate_data
from unidecode import unidecode

def capi(input_string):
    capitalized_string = input_string.capitalize()
    without_accents = unidecode(capitalized_string)
    return without_accents

@api_view(['GET'])
@permission_classes([AllowAny])
def get_room (request):
    rooms = Sala.objects.all()
    response = []
    for room in rooms:
        response.append({
            'id':room.id,
            'nombre':room.nombre,
            'tamano':room.tamano,
            'ubicacion':room.ubicacion,
            'aforo':room.aforo
        })
    return Response(response)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_room (request):
    data = validate_data({
        Required('nombre'):str,
        ('tamano'):int,
        ('ubicacion'):str,
        ('aforo'):int,
    },request.data)
    if 'tamano' not in data:
        data['tamano'] = None
    if 'ubicacion' not in data:
        data['ubicacion'] = None
    else:
        data['ubicacion']=capi(data['ubicacion'])
    if 'aforo' not in data:
        data['aforo']  = None
    data['nombre']=capi(data['nombre'])
    room = Sala.objects.create(nombre=data['nombre'],tamano=data['tamano'],ubicacion=data['ubicacion'],aforo=data['aforo'])
    room.save()
    return Response('Sala creada con exito')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_room (request):
    data = validate_data({
        Required('id'):int,
        ('nombre'):str,
        ('tamano'):int,
        ('ubicacion'):str,
        ('aforo'):int
    },request.data)
    try:
        room=Sala.objects.get(id=data['id'])
        if 'nombre' in data:
            room.nombre=capi(data['nombre'])
        if 'tamano' in data:
            room.tamano=data['tamano']
        if 'ubicacion' in data:
            room.ubicacion=capi(data['ubicacion'])
        if 'aforo' in data:
            room.aforo=data['aforo']
        room.save()
        return Response('Sala actualizada con exito')
    except: 
        return Response('La sala que deseas modificar no existe')
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_room(request):
    data = validate_data({
        Required('id'):int,
    }, request.data)
    try:
        room = Sala.objects.get(id=data['id'])
        room.delete()
        return Response('Sala eliminada exitosamente')
    except:
        return Response('La sala que deseas eliminar no existe')
