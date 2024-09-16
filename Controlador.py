from Modelo import *

global tarjetas
tarjetas = []

def nueva_tarjeta(x,y,z):
    for i in range (len(tarjetas)):
        if x == tarjetas[i].id:
            mensaje = 1
            break
    else:
        tarjeta = Tarjeta(x,y,z)
        mensaje = 3
        tarjetas.append(tarjeta)
    return mensaje

def consultar_saldo(x,y,z):
    for i in range (len(tarjetas)):
        if x == tarjetas[i].id:
            if y == tarjetas[i].clave:
                mensaje = 4
                break
            else:
                mensaje = 5
                break
    else:
        mensaje = 2
    return mensaje,tarjetas[i].monto

def abonar_saldo(x,y,z):
    for i in range (len(tarjetas)):
        if x == tarjetas[i].id:
            if y == tarjetas[i].clave:
                saldo_antiguo = int(tarjetas[i].monto)
                tarjetas[i].monto = saldo_antiguo + int(z)
                mensaje = 8
                break
            else:
                mensaje = 5
                break
    else:
        mensaje = 2
    return mensaje,tarjetas[i].monto

def retirar_saldo(x,y,z):
    for i in range (len(tarjetas)):
        if x == tarjetas[i].id:
            if y == tarjetas[i].clave:
                saldo_antiguo = int(tarjetas[i].monto)
                if saldo_antiguo < int(z):
                    mensaje = 7
                    break
                else:
                    tarjetas[i].monto = saldo_antiguo - int(z)
                    mensaje = 6
                    break
            else:
                mensaje = 5
                break
    else:
        mensaje = 2
    return mensaje,tarjetas[i].monto
