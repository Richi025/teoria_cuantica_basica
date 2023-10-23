import Lib_Complex_Vec_y_Mat as lc
import unittest
import numpy as np

class Test_operations_complex_matriz_vector(unittest.TestCase):

    def test_sum_complex_Vector(self):
        suma = lc.sum_complex_Vector([complex(-1,5), complex(3,6)],[complex(-5,3),complex(-1,3)])
        self.assertAlmostEqual(suma[0], complex(-6,8))
        self.assertAlmostEqual(suma[1], complex(2,9))

    def test_sum_complex_Vector2(self):
        suma = lc.sum_complex_Vector([complex(-3, 5), complex(1, 6)],[complex(-3, 3), complex(-5, 3)])
        self.assertAlmostEqual(suma[0], complex(-6,8))
        self.assertAlmostEqual(suma[1], complex(-4,9))

    def test_inver_complex_Vector(self):
        inver = lc.inver_complex_Vector([complex(-5, 4), complex(-6, 7)])
        self.assertAlmostEqual(inver[0], complex(5, -4))
        self.assertAlmostEqual(inver[1], complex(6,-7))

    def test_inver_complex_Vector2(self):
        inver = lc.inver_complex_Vector([complex(-2, 4), complex(-5, 7)])
        self.assertAlmostEqual(inver[0], complex(2, -4))
        self.assertAlmostEqual(inver[1], complex(5, -7))

    def test_mult_escalar_complex_Vector(self):
        mult = lc.mult_escalar_complex_Vector(5,[complex(-5, 4), complex(-6, 7)])
        self.assertAlmostEqual(mult[0], complex(-25, 20))
        self.assertAlmostEqual(mult[1], complex(-30, 35))

    def test_mult_escalar_complex_Vector2(self):
        mult = lc.mult_escalar_complex_Vector(6,[complex(-1, 4), complex(-6, 3)])
        self.assertAlmostEqual(mult[0], complex(-6, 24))
        self.assertAlmostEqual(mult[1], complex(-36, 18))

    def test_add_complex_matriz(self):
        suma = lc.add_complex_matriz([[complex(3,6),complex(-3,3)],[complex(-1,5),complex(3,6)]],[[complex(2,6),complex(-3,7)],[complex(-1,8),complex(5,6)]])
        self.assertAlmostEqual(suma[0][0], complex(5,12))
        self.assertAlmostEqual(suma[0][1], complex(-6,10))
        self.assertAlmostEqual(suma[1][0], complex(-2,13))
        self.assertAlmostEqual(suma[1][1], complex(8,12))

    def test_add_complex_matriz2(self):
        suma = lc.add_complex_matriz([[complex(3,8),complex(-3,8)],[complex(-1,8),complex(3,8)]],[[complex(2,6),complex(-3,7)],[complex(-1,8),complex(5,6)]])
        self.assertAlmostEqual(suma[0][0], complex(5, 14))
        self.assertAlmostEqual(suma[0][1], complex(-6, 15))
        self.assertAlmostEqual(suma[1][0], complex(-2, 16))
        self.assertAlmostEqual(suma[1][1], complex(8, 14))

    def test_inv_add_complex_matriz(self):
        inver = lc.inv_add_complex_matriz([[complex(3, 6), complex(-3, 3)],
                                            [complex(-1, 5), complex(3, 6)]])
        self.assertAlmostEqual(inver[0][0], complex(-3, -6))
        self.assertAlmostEqual(inver[0][1], complex(3, -3))
        self.assertAlmostEqual(inver[1][0], complex(1, -5))
        self.assertAlmostEqual(inver[1][1], complex(-3, -6))

    def test_inv_add_complex_matriz2(self):
        inver = lc.inv_add_complex_matriz([[complex(8, 6), complex(-8, 3)],
                                            [complex(-8, 5), complex(8, 6)]])
        self.assertAlmostEqual(inver[0][0], complex(-8, -6))
        self.assertAlmostEqual(inver[0][1], complex(8, -3))
        self.assertAlmostEqual(inver[1][0], complex(8, -5))
        self.assertAlmostEqual(inver[1][1], complex(-8, -6))

    def test_mult_complex_num_matriz(self):
        mult = lc.mult_complex_num_matriz(5, [[complex(2, 2), complex(2, -1)],[complex(2, 4), complex(-4, 5)]])
        self.assertAlmostEqual(mult[0][0], complex(10, 10))
        self.assertAlmostEqual(mult[0][1], complex(10, -5))
        self.assertAlmostEqual(mult[1][0], complex(10, 20))
        self.assertAlmostEqual(mult[1][1], complex(-20, 25))

    def test_mult_complex_num_matriz2(self):
        mult = lc.mult_complex_num_matriz(4, [[complex(3, 2), complex(3, -1)],[complex(3, 4), complex(-3, 5)]])
        self.assertAlmostEqual(mult[0][0], complex(12, 8))
        self.assertAlmostEqual(mult[0][1], complex(12, -4))
        self.assertAlmostEqual(mult[1][0], complex(12, 16))
        self.assertAlmostEqual(mult[1][1], complex(-12, 20))

    def test_transp_complex_matriz_vector(self):
        transp = lc.transp_complex_matriz_vector([complex(3, 2), complex(3, -1)])
        self.assertAlmostEqual(transp[0][0], complex(3, 2))
        self.assertAlmostEqual(transp[1][0], complex(3, -1))

    def test_transp_complex_matriz_vector2(self):
        transp = lc.transp_complex_matriz_vector([[complex(3, 2), complex(3, -1)],[complex(3, 4), complex(-3, 5)]])
        self.assertAlmostEqual(transp[0][0], complex(3, 2))
        self.assertAlmostEqual(transp[0][1], complex(3, 4))
        self.assertAlmostEqual(transp[1][0], complex(3, -1))
        self.assertAlmostEqual(transp[1][1], complex(-3, 5))

    def test_conjugada_matriz(self):
        conjugada = lc.conjugada_matriz([complex(3, 2), complex(3, -1)])
        self.assertAlmostEqual(conjugada[0], complex(3, -2))
        self.assertAlmostEqual(conjugada[1], complex(3, 1))

    def test_conjugada_matriz2(self):
        conjugada = lc.conjugada_matriz([[complex(3, 2), complex(3, -1)],[complex(3, 4), complex(-3, 5)]])
        self.assertAlmostEqual(conjugada[0][0], complex(3, -2))
        self.assertAlmostEqual(conjugada[0][1], complex(3, 1))
        self.assertAlmostEqual(conjugada[1][0], complex(3, -4))
        self.assertAlmostEqual(conjugada[1][1], complex(-3, -5))

    def test_adjunta_matriz(self):
        adjunta = lc.adjunta_matriz([complex(3, 2), complex(3, -5)])
        self.assertAlmostEqual(adjunta[0][0], complex(3, -2))
        self.assertAlmostEqual(adjunta[1][0], complex(3, 5))

    def test_adjunta_matriz2(self):
        adjunta = lc.adjunta_matriz([[complex(3, 2), complex(3, -5)], [complex(2, 4), complex(-2, 6)]])
        self.assertAlmostEqual(adjunta[0][0], complex(3, -2))
        self.assertAlmostEqual(adjunta[0][1], complex(2, -4))
        self.assertAlmostEqual(adjunta[1][0], complex(3, 5))
        self.assertAlmostEqual(adjunta[1][1], complex(-2, -6))

    def test_mult_matriz_compatibles(self):
        mult = lc.mult_matriz_compatibles([[complex(6,6),complex(-6,3)],[complex(-6,5),complex(6,6)]],[[complex(6,6),complex(-6,7)],[complex(-6,8),complex(6,6)]])
        self.assertAlmostEqual(mult[0][0], complex(12, 6))
        self.assertAlmostEqual(mult[0][1], complex(-132, -12))
        self.assertAlmostEqual(mult[1][0], complex(-150, 6))
        self.assertAlmostEqual(mult[1][1], complex(1, 0))

    def test_mult_matriz_compatibles2(self):
        multi = lc.mult_matriz_compatibles([[complex(6,2),complex(-6,2)],[complex(-6,2),complex(6,2)]],[[complex(6,2),complex(-6,2)],[complex(-6,2),complex(6,2)]])
        self.assertAlmostEqual(multi[0][0], complex(64, 0))
        self.assertAlmostEqual(multi[0][1], complex(-80, 0))
        self.assertAlmostEqual(multi[1][0], complex(-80, 0))
        self.assertAlmostEqual(multi[1][1], complex(64, 0))

    def test_accion_matriz_vector(self):
        accion = lc.accion_matriz_vector([[complex(6, 2), complex(5, 4)],
                                     [complex(5, 4), complex(-5, 5)]],
                                    [complex(-5, 1), complex(1, 3)])
        self.assertAlmostEqual(accion[0], complex(-39, 15))
        self.assertAlmostEqual(accion[1], complex(-49, -25))

    def test_accion_matriz_vector2(self):
        accion = lc.accion_matriz_vector([[complex(5, 2), complex(5, 4)],
                                     [complex(5, 4), complex(-5, 5)]],
                                    [complex(-5, 1), complex(5, 3)])
        self.assertAlmostEqual(accion[0], complex(-14, 30))
        self.assertAlmostEqual(accion[1], complex(-69, -5))


    def test_produc_intern_cplx(self):
        vec_a = [3-8j, 7, 1, 4+3j]
        vec_b = [2j, 5-4j, 7j, 3j]
        respm = 28-3j
        respc = lc.produc_intern_cplx(vec_a, vec_b)
        self.assertAlmostEqual(respc, respm)

    def test_produc_intern_cplx2(self):
        vec_a = [3 + 4j, 8, 0, 1 + 3j]
        vec_b = [1j, 5 - 4j, 7j, 3j]
        respm = 53 - 26j
        respc = lc.produc_intern_cplx(vec_a, vec_b)
        self.assertAlmostEqual(respc, respm)

    def test_norma_vec_cplx(self):
        vec_a = [1 + 2j, 3 - 4j, -3j]
        respm = 6.24
        respc = lc.norma_vec_cplx(vec_a)
        self.assertAlmostEqual(respc, respm)

    def test_norma_vec_cplx2(self):
        vec_a = [3+2j,4-4j,-2j]
        respm = 7.0
        respc = lc.norma_vec_cplx(vec_a)
        self.assertAlmostEqual(respc, respm)
    def test_dist_vec_cplx(self):
        vec_a = [2,2-1j,4+4j]
        vec_b = [5-3j,-1j,4j]
        respm = 6.16
        respc = lc.dist_vec_cplx(vec_a, vec_b)
        self.assertAlmostEqual(respc, respm)

    def test_dist_vec_cplx2(self):
        vec_a = [4, 2 - 1j, 2 + 4j]
        vec_b = [4 - 3j, -1j, 2j]
        respm = 4.58
        respc = lc.dist_vec_cplx(vec_a, vec_b)
        self.assertAlmostEqual(respc, respm)

    def test_vec_propios(self):
        matr_a = np.array([[-1, -1j], [1j, 1]])
        respm = np.array([0.92 + 0.j, -0. - 0.38j])
        respc = lc.vec_propios(matr_a)
        np.testing.assert_allclose(respc, respm)

    def test_val_propios(self):
        matr_a = np.array([[-6,-1j],[6j,1]])
        respm = np.array([-6.77, 1.77])
        respc = lc.val_propios(matr_a)
        np.testing.assert_allclose(respc, respm)


    def test_val_propios2(self):
        matr_a = np.array([[-1, -1j], [1j, 1]])
        respm = np.array([-1.41+0.j, 1.41+0.j])
        respc = lc.val_propios(matr_a)
        np.testing.assert_allclose(respc, respm)
    def test_matriz_unitaria(self):
        u = [[2 / 3, (-2 + 1j) / 3], [(2 + 1j) / 3, 2 / 3]]
        respm = "La matriz ingresada es unitaria"
        respc = lc.matriz_unitaria(u)
        self.assertEqual(respc, respm)

    def test_matriz_unitaria2(self):
        u = [[2 / 3, (-8 + 1j) / 3], [(2 + 1j) / 3, 2 / 3]]
        respm = "La matriz ingresada NO es unitaria"
        respc = lc.matriz_unitaria(u)
        self.assertEqual(respc, respm)

    def test_matriz_hermitiana(self):
        u = [[3, 2 - 1j, -5j], [2 + 1j, 0, 9 - 5j], [5j, 9 + 5j, 6]]
        respm = "La matriz ingresada es hermitiana"
        respc = lc.matriz_hermitiana(u)
        self.assertEqual(respc, respm)

    def test_matriz_hermitiana2(self):
        u = [[9, 2 - 8j, -5j], [2 + 1j, 0, 9 - 5j], [5j, 9 + 5j, 6]]
        respm = "La matriz ingresada NO es hermitiana"
        respc = lc.matriz_hermitiana(u)
        self.assertEqual(respc, respm)


    def test_produc_tensor_matriz_vector(self):
        u = [[5, 3], [5, 4]]
        v = [[1, 3, 2], [6, 0, 2], [-9, 5, 6]]
        respm = [[5, 15, 10, 3, 9, 6], [30, 0, 10, 18, 0, 6], [-45, 25, 30, -27, 15, 18], [5, 15, 10, 4, 12, 8], [30, 0, 10, 24, 0, 8], [-45, 25, 30, -36, 20, 24]]
        respc = lc.produc_tensor_matriz_vec(u, v)
        self.assertAlmostEqual(respc, respm)

    def test_produc_tensor_matriz_vector2(self):
        u = [[2, 3], [1, 4]]
        v = [[5, 3, 2], [1, 0, 2], [-2, 5, 6]]
        respm = [[10, 6, 4, 15, 9, 6], [2, 0, 4, 3, 0, 6], [-4, 10, 12, -6, 15, 18], [5, 3, 2, 20, 12, 8],
                 [1, 0, 2, 4, 0, 8], [-2, 5, 6, -8, 20, 24]]
        respc = lc.produc_tensor_matriz_vec(u, v)
        self.assertAlmostEqual(respc, respm)


if __name__ == '__main__':
    unittest.main()