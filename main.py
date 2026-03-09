import sys

def clean_value(value):
    ##Quitar espacios y solo permitir los digitos correctos
    value = value.strip()
    valid_chars= '.-0123456789'
    result=''
    ##Recorremos la cadena y si el digito es correcto lo guardamos
    for char in value:
        if char in valid_chars:
            result +=char
    return result
