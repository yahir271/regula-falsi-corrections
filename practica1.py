import numpy as np
import matplotlib.pyplot as plt


# Definiremos la función
def funcion(x):
    #Los datos fueron modificados para cada interaccion
    A = 2272.741
    p = 0.2986
    C = 0
    Q = (0.9697) * (-0.9697)
    return ((-A/p) * np.exp(-(x/p))) - ((-6*C)/(x**7)) + ((-Q)/(x**2)) #Esta es la funcion para calcular los puntos criticos
# Definiremos los datos inciales que son los extremos (dos) en los cuales se calculará la raíz, en donde usaremos una variable float,
# pues permite representar datos positivos y negativos decimales.
a = 1
b = 4
t = 1.0e-6
# Inicializar variables
i = 0
fa = funcion(a)
fb = funcion(b)
c = b
d = a

# Crearemos nuestras listas para almacenar los valores utilizados.
a_list, b_list, c_list, fa_list, fb_list, fc_list = [a], [b], [], [fa], [fb], []  # Inicializar fc_list como una lista vacía

while (abs(d-c)) > t and i<1000 :
    d = c
    c = a - (fa * (b - a)) / (fb - fa)
    fc=funcion(c)

    fc = funcion(c)
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    fa_list.append(fa)
    fb_list.append(fb)
    fc_list.append(fc)

    if fb * fc < 0:
        a = b
        fa = fb

    else:
        fa = fa/2          # Illinois
        #fa = (fa*fb)/(fb + fc) # pegasus
        #fa = fa/(a + (fc/fb))**2

    i += 1
    b = c
    fb = fc


    # Luego, tabularemos nuestros resultados
print('n  a_n   b_n   c_n     f(a_n)    f(b_n)      f(c_n)')
for j in range(len(c_list)):
    print(f'{j+1:4d} {a_list[j]:11.10f} {b_list[j]:11.10f} {c_list[j]:11.10f} {fa_list[j]:11.10f} {fb_list[j]:11.10f} {fc_list[j]:11.10f}')

print(f'\nLa raíz que esta buscando es aproximadamente: {c:.6f}')



# Finalmente crearemos la elaboración de las gráficas.
z = np.linspace(a_list[0], b_list[0], 400)
plt.plot(z, funcion(z), 'r', label='Función')
plt.plot(c_list, fc_list, '+:b', label='Aproximación')
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Regula-falsi')
plt.legend()
#plt.show()
