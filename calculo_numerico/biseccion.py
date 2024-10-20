#!/usr/bin/env python3
import math


def biseccion(f, a, b, er, n):
    """Algoritmo de Bisección.

    Args:
        f (function): función a calcularle la raíz.
        a (float): límite inferior del intervalo.
        b (float): límite superior del intervalo.
        er (float): cota máxima del error.
        n (int): número máximo de iteraciones.

    Returns:
        tuple: retorna una tupla con la raíz y el último error calculado.
    """
    ei = 1.00           # Error iterativo.
    i = 0               # Contador de iteraciones.
    m_anterior = False  # Punto medio anterior.

    while (ei > er) and (i < n):
        m_actual = (a + b)/2

        if m_anterior:
            ei = math.fabs((m_actual - m_anterior)/m_actual)

        if f(a)*f(m_actual) < 0:
            b = m_actual
        elif f(m_actual)*f(b) < 0:
            a = m_actual
        else:
            return m_actual, ei

        m_anterior = m_actual

        i = i + 1

    return m_actual, ei


if __name__ == "__main__":

    # Testing...

    f = lambda x: math.exp(-x) - math.log(x)
    a = 1
    b = 1.5
    er = 0.01
    n = 100
    result = biseccion(f, a, b, er, n)
    print(result)
    print(f"Raiz: {result[0]:0.7f}\nError: {result[1]:0.4f}")