#Operadores que permiten manipulas bits de datos individuales, de denominan operadores bit a bit
# &,|,~,^
a=1
b=0
a&b #and
~b #not
a|b  #or
a^b

# shifting esto se aplica solo a los valores de un numero entero
# Los operadores de cambio en Python son un par de digrafos
# << Es un valor entero cuyos bits se desplazan corresponde a multiplicacion por dos 
# >> Es un valor entero cuyos bits se desplazan corresponde a dividir entre dos
var=17
var_right = var >> 1
var_left = var << 2
print(var,var_left,var_right)

