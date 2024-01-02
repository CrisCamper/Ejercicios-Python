ventas = [
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoC", 8, 120),
    ("ProductoD", 12, 80),
    ("ProductoE", 3, 210),
    ("ProductoF", 15, 130),
    ("ProductoG", 7, 85),
]

# Inicializar variables para el total de ventas y la ganancia total
total_ventas = 0
producto_mayor_10 = set()
ganancia_total = 0

# Iterar sobre la lista de ventas
for producto, cantidad, precio_unitario in ventas:
    # Calcular el total de ventas por producto
    total_producto = cantidad * precio_unitario
    # Calcular ganancia total
    ganancia_total += total_producto
    # Encontrar producos con más de 10 ventas
    if cantidad >= 10:
       producto_mayor_10.add(producto)
    

print((producto,total_producto))
print('Productos con más de 10 ventas:', producto_mayor_10)
print('Ganancia total:',ganancia_total)
