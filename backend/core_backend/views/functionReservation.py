from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Reservacion
from core_backend.models import Sala
from core_backend.models import Usuario
from voluptuous.schema_builder import Required
from backend.utils import validate_data 
from datetime import datetime,date,time
from unidecode import unidecode

def capi(input_string):
    capitalized_string = input_string.capitalize()
    without_accents = unidecode(capitalized_string)
    return without_accents

@api_view(['GET'])
@permission_classes([AllowAny])
def get_reservation (request):
    reservations = Reservacion.objects.all()
    response = []
    for reservation in reservations:
        response.append({
            'id':reservation.id,
            'usuario':reservation.usuario.nombre,
            'sala':reservation.sala.nombre,
            'fecha':reservation.fecha,
            'hora_inicio':reservation.hora_inicio,
            'hora_fin':reservation.hora_fin,
        })
    return Response(response)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation (request):
    data = validate_data({
        Required('identificador'):int,
        Required('sala'):str,
        Required('fecha'):str,
        Required('hora_inicio'):str,
        Required('hora_fin'):str,
        Required('personas'):int,
    },request.data)
    data['sala'] = capi(data['sala'])
    data['fecha'] = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    data['hora_inicio'] = datetime.strptime(data['hora_inicio'], '%H:%M:%S').time()
    data['hora_fin'] = datetime.strptime(data['hora_fin'], '%H:%M:%S').time()
    try:
        sala=Sala.objects.get(nombre=data['sala'])
        usuario=Usuario.objects.get(identificador=data['identificador'])
        citas=Reservacion.objects.filter(fecha=data['fecha'],sala=sala.id)
        for cita in citas:
            if((data['hora_inicio']<cita.hora_fin and data['hora_fin']>cita.hora_inicio) or (data['hora_inicio']>cita.hora_inicio and data['hora_fin']<cita.hora_fin)):
                return Response("Error: Solapamiento de horarios")
        
        if(data['hora_inicio']>data['hora_fin']):
            return Response('Horario no elegible')
        
        if ((datetime.combine(datetime.min, data['hora_fin']) - datetime.combine(datetime.min, data['hora_inicio'])).total_seconds() / 3600) > 2:
            return Response('La nueva reservación supera el límite de tiempo')
        
        reservation=Reservacion.objects.create(usuario=usuario,sala=sala, fecha=data['fecha'], hora_inicio=data['hora_inicio'], hora_fin=data['hora_fin'],personas=data['personas'])
        reservation.save()
        return Response(f'Reservacion Creada, su id es :{reservation.id}')
    except Sala.DoesNotExist:
        return Response("Error: La sala no existe")
    except Usuario.DoesNotExist:
        return Response("Error: El usuario no existe")
    except Exception as e:
        return Response(f"Error: {str(e)}")
    
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_reservation (request):
    data = validate_data({
        Required('id'):int,
        ('sala'):str,
        ('fecha'):str,
        ('hora_inicio'):str,
        ('hora_fin'):str,
        ('personas'):int,
    },request.data)
    try:
        reservation=Reservacion.objects.get(id=data['id'])
        val=True
        if 'sala' in data:
            data['sala'] = capi(data['sala'])
            sala=Sala.objects.get(nombre=data['sala'])
            val=False
        else:
            sala=Sala.objects.get(nombre=reservation.sala.nombre)
        if 'fecha' in data:            
            fecha=data['fecha']
            val=False
        else:
            fecha=reservation.fecha
        if 'hora_inicio' in data:
            hora_inicio=data['hora_inicio']
            val=False
        else:
            hora_inicio= reservation.hora_inicio
        if 'hora_fin' in data:
            hora_fin=data['hora_fin']
            val=False
        else:
            hora_fin=reservation.hora_fin
        if 'personas' in data:
            personas=data['personas']
        else:
            personas=reservation.personas
        
        citas=Reservacion.objects.filter(fecha=fecha,sala=sala.id).exclude(id=data['id'])
        for cita in citas:
            if(((hora_inicio<cita.hora_fin and hora_fin>cita.hora_inicio) or (hora_inicio>cita.hora_inicio and hora_fin<cita.hora_fin)) and val):
                return Response("Error: Solapamiento de horarios")
        if(hora_inicio>hora_fin):
            return Response('Error: Horario no elegible')
        if ((datetime.combine(datetime.min, hora_fin) - datetime.combine(datetime.min, hora_inicio)).total_seconds() / 3600) > 2:
            return Response('Error: El nuevo horario supera el límite de tiempo')
        if(personas>sala.aforo):
            return Response('Error: Aforo maximo superado')
        reservation.sala=sala
        reservation.fecha=fecha
        reservation.hora_inicio=hora_inicio
        reservation.hora_fin=hora_fin
        reservation.personas=personas
        reservation.save()
        return Response('Reservacion actualizada con exito')
    except Sala.DoesNotExist:
        return Response("Error: La sala no existe")
    except Reservacion.DoesNotExist:
        return Response("Error: La reservacion no existe")
    except: 
        return Response('La sala no se pudo actualizar')


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_reservation(request):
    data = validate_data({
        Required('id'):int,
    }, request.data)
    try:
        reservation = Reservacion.objects.get(id=data['id'])
        reservation.delete()
        return Response('Reservacion eliminado exitosamente')
    except:
        return Response('La reservacion que deseas eliminar no existe')