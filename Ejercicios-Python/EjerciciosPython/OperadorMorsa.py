# El operador morsa permite unificar sentencias de asignacion dentro de expresiones. Su nombre proviene de la forma que tiene :=
# A continuación un ejemplo en el que computamos el perímetro de una circunferencia, indicando al usuario que debe incrementarlo
# siempre y cuando no llegue a un minimo establecido:

# Versión normal:

radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimun perimeter')
    print('Actual perimeter:', perimeter)

# Versión con operador morsa :=
    
radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimun perimeter')
    print('Actual perimeter:', perimeter)