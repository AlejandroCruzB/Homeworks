precios = {
    "banana": 4,
    "manzana": 2,
    "naranja": 1.5,
    "pera": 3,
}
compras = {
    "banana": 1,
    "naranja": 2,
    "manzana": 2
}


inventario = {
    "banana": 6,
    "manzana": 0,
    "naranja": 32,
    "pera": 15
}



def calcular_factura(comida):
    total = 0
    for item in comida:
        if inventario[item] > 0:
            total += precios[item] * comida[item]
            inventario[item] -= precios[item] * comida[item]
    return total
print calcular_factura(compras)

#preguntar a enrique sobre inventario, otra manera de hacerlo? poner solo -1?
#con el inventario podemos jugar haciéndolo diccionario y eligiendo "":""