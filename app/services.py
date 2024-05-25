from django.core.exceptions import ValidationError
from .models import Vehiculo, Chofer, RegistroContabilidad

# crear_vehiculo
# crear_chofer
# crear_registro_contable
# deshabilitar_chofer
# deshabilitar_vehiculo
# habilitar_chofer
# habilitar_vehiculo
# obtener_vehiculo
# obtener_chofer
# asignar_chofer_a_vehiculo
# imprimir_datos_vehiculos

#Funcion para crear vehiculos
def crear_vehiculo(nuevaPatente, nuevaMarca,nuevoModelo,nuevoYear,estadoActivo):
    #Creo el objeto de vehoculo
    vehiculo = Vehiculo(
        patente = nuevaPatente,
        marca = nuevaMarca,
        modelo = nuevoModelo,
        year = nuevoYear,
        activo = estadoActivo
        )
    
    #Validacion previa a guardar el vehiculo
    try:
        vehiculo.full_clean()  # Esto ejecutará todas las validaciones
    except ValidationError as e:
        return {'error': str(e)}  # Manejo los errores de validación, saldra de la funcion mostrando un mensaje de error

    #Se guarda despues de validar si esta todo correcto
    vehiculo.save()
    print('Vehiculo creado correctamente')
    return vehiculo


def obtener_vehiculo(patente_a_buscar):
    vehiculo = Vehiculo.objects.get(patente = patente_a_buscar)
    return vehiculo


def crear_chofer(nuevoRut, nuevoNombre, nuevoApellido, estadoActivo, patente_vehiculo):
    #Busco el vehiculo a registrar
    vehiculo_obtenido = obtener_vehiculo(patente_vehiculo)
    #Creo el objeto de chofer
    chofer = Chofer(
        rut = nuevoRut,
        nombre = nuevoNombre,
        apellido = nuevoApellido,
        activo = estadoActivo,
        vehiculo = vehiculo_obtenido
    )

    #Validacion previa a guardar el chofer
    try:
        chofer.full_clean()  # Esto ejecutará todas las validaciones
    except ValidationError as e:
        return {'error': str(e)}  # Manejo los errores de validación, saldra de la funcion mostrando un mensaje de error
    
    #Se guarda despues de validar si esta todo correcto
    chofer.save()
    print('Chofer creado correctamente')
    return chofer


def obtener_chofer(rut_a_buscar):
    chofer = Chofer.objects.get(rut = rut_a_buscar)
    return chofer


#Funcion para crear un nuevo registro contable
def crear_registro_contable(nuevaFecha_compra, nuevoValor, patente_ingresada):
    #Busco el vehiculo a registrar
    vehiculo_obtenido = Vehiculo.objects.get(patente = patente_ingresada)
    #Creo el objeto de registro
    registro = RegistroContabilidad(
        fecha_compra = nuevaFecha_compra,
        valor = nuevoValor,
        vehiculo = vehiculo_obtenido
    )
    
    #Validacion previa a guardar el registro contable
    try:
        registro.full_clean()  # Esto ejecutará todas las validaciones
    except ValidationError as e:
        return {'error': str(e)}  # Manejo los errores de validación, saldra de la funcion mostrando un mensaje de error

    #Se guarda despues de validar si esta todo correcto
    registro.save()
    print('Registro Contable creado correctamente')
    return registro


#Funcion que cambia el valor del chofer, activo a false
def deshabilitar_chofer(rut_chofer):
    chofer = Chofer.objects.get(rut = rut_chofer)

    #Valido que exista el chofer
    if not chofer:
        return print('Chofer Inexistente')
    
    chofer.activo = False
    chofer.save()
    print('Chofer deshabilitado')
    return chofer


#Funcion que cambia el valor del chofer, activo a true
def habilitar_chofer(rut_chofer):
    chofer = Chofer.objects.get(rut = rut_chofer)

    #Valido que exista el chofer
    if not chofer:
        return print('Chofer Inexistente')
    
    chofer.activo = True
    chofer.save()
    print('Chofer habilitado')
    return chofer


#Funcion que cambia el valor del vehiculo, activo a False
def deshabilitar_vehiculo(patente_a_buscar):
    vehiculo = Vehiculo.objects.get(patente = patente_a_buscar)

    #Valido que exista el vehiculo
    if not vehiculo:
        return print('Vehiculo Inexistente')
    
    vehiculo.activo = False
    vehiculo.save()
    print('Vehiculo deshabilitado')
    return vehiculo


#Funcion que cambia el valor del vehiculo, activo a true
def habilitar_vehiculo(patente_a_buscar):
    vehiculo = Vehiculo.objects.get(patente = patente_a_buscar)

    #Valido que exista el vehiculo
    if not vehiculo:
        return print('Vehiculo Inexistente')
    
    vehiculo.activo = True
    vehiculo.save()
    print('Vehiculo habilitado')
    return vehiculo


#Imprime toda la informacion de los vehiculos existentes
def imprimir_vehiculos():
    #Creo una lista con todos los vehiculos existentes
    vehiculos = Vehiculo.objects.all()

    for vehiculo in vehiculos:
        #Por cada vehiculo contenido en la lista, imprime:
        print(f"""Vehiculo:
- Patente: {vehiculo.patente}
- Marca: {vehiculo.marca}
- Modelo: {vehiculo.modelo}
- Año: {vehiculo.year}
- Activo: {vehiculo.activo}""")
        
        #Si existe el atributo chofer en el vehiculo:
        if hasattr(vehiculo, 'chofer'):
            #Imprime sus valores ordenados en pantalla
            print(f"""- Chofer:
-- Rut: {vehiculo.chofer.rut}
-- Nombre: {vehiculo.chofer.nombre} {vehiculo.chofer.apellido}
-- Activo: {vehiculo.chofer.activo}""")
        
        #Si existe el atributo contabilidad en el vehiculo:
        if hasattr(vehiculo,'contabilidad'):
            #Imprime sus valores ordenados en pantalla
            print(f"""- Contabilidad:
-- ID: {vehiculo.contabilidad.id}
-- Fecha de compra: {vehiculo.contabilidad.fecha_compra}
-- Valor:{vehiculo.contabilidad.valor}""")
        print("---------------------------------------------------------------------------------")