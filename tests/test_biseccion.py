import math
import unittest

from calculo_numerico.biseccion import biseccion


class TestBiseccion(unittest.TestCase):

    def test_1(self):
        f = lambda x: math.exp(-x) - math.log(x)
        a = 1
        b = 1.5
        er = 0.01
        n = 100
        resultado = biseccion(f, a, b, er, n)
        self.assertEqual(resultado[0], 1.3046875)
        self.assertEqual(resultado[1], 0.005988023952095809)

    def test_2(self):
        f = lambda x: x**2 - 4
        a = 0
        b = 3
        er = 0.01
        n = 100
        resultado = biseccion(f, a, b, er, n)
        self.assertEqual(resultado[0], 2.00390625)
        self.assertEqual(resultado[1], 0.005847953216374269)