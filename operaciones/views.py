
from django.http import HttpResponse

def sumar(request, a, b):
    resultado = a + b
    return HttpResponse(f"La suma de {a} + {b} = {resultado}")

def restar(request, a, b):
    resultado = a - b
    return HttpResponse(f"La resta de {a} - {b} = {resultado}")

def multiplicar(request, a, b):
    resultado = a * b
    return HttpResponse(f"La multiplicación de {a} * {b} = {resultado}")
