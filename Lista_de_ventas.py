# Lista de ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 800.00},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.50},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 790.00},
    {"fecha": "2024-01-02", "producto": "Monitor", "cantidad": 3, "precio": 220.00},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 4, "precio": 26.00},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 2, "precio": 45.00},
    {"fecha": "2024-01-04", "producto": "Monitor", "cantidad": 1, "precio": 210.00}
]

# Cálculo de ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# Análisis del producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]
    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0, 0)
    suma_precio, total_cantidad = precios_por_producto[producto]
    precios_por_producto[producto] = (suma_precio + ingreso, total_cantidad + cantidad)

precios_promedio = {}
for producto, (total_ingresos, total_cantidad) in precios_por_producto.items():
    precios_promedio[producto] = round(total_ingresos / total_cantidad, 2)

# Ventas por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# Resumen de ventas
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio = precios_promedio[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": round(ingresos_totales_producto, 2),
        "precio_promedio": precio_promedio
    }

# Resultados
print("Lista original de ventas:")
for venta in ventas:
    print(venta)

print(f"\nIngresos totales: ${round(ingresos_totales, 2)}")
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")

print("\nPrecio promedio por producto:")
for producto, promedio in precios_promedio.items():
    print(f"{producto}: ${promedio}")

print("\nIngresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${round(ingreso, 2)}")

print("\nResumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"{producto}: {resumen}")
