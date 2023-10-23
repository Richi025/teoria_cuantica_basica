import unittest
import basic_quantum_theory as tc
import math
import numpy as np
from scipy.constants import hbar

class Test_basic_quantum_theory(unittest.TestCase):

    def test_prob_sist_Linea(self):
        prob = tc.probSisLinea([complex(-2, 1), complex(0, 2), complex(1, -1), complex(1, 0), complex(0, -2), complex(0, 2)], 3)
        self.assertAlmostEqual(prob, 0.05)

    def test_prob_sist_Linea2(self):
        prob = tc.probSisLinea([complex(-2, 1), complex(0, 2), complex(1, -1), complex(1, 0), complex(0, -2), complex(0, 2)], 0)
        self.assertAlmostEqual(prob, 0.25)

    def test_probabilityOfTransit(self):
        probaTransit = tc.probabilityOfTransit([complex(0, 1), complex(-1, 0)],[complex(1, 0), complex(0, -1)])
        self.assertAlmostEqual(probaTransit, 0)

    def test_probabilityOfTransit2(self):
        probaTransit = tc.probabilityOfTransit([complex(0, 4), complex(-2, 0)],[complex(2, 0), complex(0, -2)])
        self.assertAlmostEqual(probaTransit, 0.09999999999999996)

    def test_amplitudeOfTransit1(self):
        amplitudOfTransit = tc.amplitudeOfTransit([complex(0, 1), complex(-1, 0)], [complex(1, 0), complex(0, -1)])
        self.assertAlmostEqual(amplitudOfTransit, 0)

    def test_amplitudeOfTransit2(self):
        amplitudOfTransit = tc.amplitudeOfTransit([complex(2, 1), complex(-1, 3)], [complex(1, 1), complex(1, -1)])
        self.assertAlmostEqual(amplitudOfTransit, -0.12909944487358055-0.12909944487358055j)

    def test_mediaObservableKet(self):
        mediaObservableKet = tc.mediaObservableKet([[complex(3, 0), complex(1, 2)],
                               [complex(1, -2), complex(-1, 0)]],
                              [complex(math.sqrt(2)/2,0),complex(-math.sqrt(2)/2,0)])
        self.assertAlmostEqual(mediaObservableKet, 0.0)

    def test_mediaObservableKet2(self):
        mediaObservableKet = tc.mediaObservableKet([[complex(1, 0), complex(0, -1)],
                               [complex(0, 1), complex(2, 0)]],
                              [complex(math.sqrt(2) / 2, 0), complex(0, math.sqrt(2) / 2)])
        self.assertAlmostEqual(mediaObservableKet, 2.5)

    def test_variationObservableKet(self):
        mediaObservableKet = tc.variationObservableKet([[complex(3, 0), complex(1, 8)],
                              [complex(1, -8), complex(-1, 0)]],
                             [complex(math.sqrt(2) / 2, 0), complex(-math.sqrt(2) / 2, 0)])
        self.assertAlmostEqual(mediaObservableKet, 68)

    def test_variationObservableKet2(self):
        mediaObservableKet = tc.variationObservableKet([[complex(3, 3), complex(1, 5)],
                              [complex(1, -5), complex(-8, 0)]],
                             [complex(math.sqrt(2) / 2, 0), complex(-math.sqrt(2) / 2, 0)])
        self.assertAlmostEqual(mediaObservableKet, 'La matriz observable no es hermitania')


    def test_val_propios_and_probability_of_transition_to_vec_propios(self):
        result = tc.val_propios_and_probability_of_transition_to_vec_propios([complex(1, 0), complex(0, 0)],
                                                                           [[complex(0, 0), complex(hbar, 0)],
                                                                                    [complex(hbar, 0), complex(0, 0)]])
        val_propios = result[0]
        probabilities = result[1]
        self.assertAlmostEqual(val_propios[0], 1.0545718176461567e-34)
        self.assertAlmostEqual(val_propios[0], -1.0545718176461565e-34)
        self.assertAlmostEqual(probabilities[0], 0.5)
        self.assertAlmostEqual(probabilities[1], 0.5)

    def test_val_propios_and_probability_of_transition_to_vec_propios(self):
        results = tc.val_propios_and_probability_of_transition_to_vec_propios([complex(1, 0), complex(0, 0)],
                                                                           [[complex(0, 0), complex(hbar / 2, 0)],
                                                                            [complex(hbar / 2, 0), complex(0, 0)]])
        val_propios = results[0]
        probabilities = results[1]
        self.assertAlmostEqual(val_propios[0], 5.27285908823078e-35)
        self.assertAlmostEqual(val_propios[0], -5.27285908823078e-35)
        self.assertAlmostEqual(probabilities[0], 0.5)
        self.assertAlmostEqual(probabilities[1], 0.5)



    def test_sistem_dinamic(self):
        end_state = tc.sistem_dinamic([complex(-2, 0), complex(3, 1)],[[[complex(5, 1), complex(2, 4)],
                                                            [complex(4, 2), complex(-2, 6)]],
                                                            [[complex(3, 3), complex(2, 4)],
                                                            [complex(2, 4), complex(-2, 3)]]])
        self.assertAlmostEqual(end_state[0], -148-44j)
        self.assertAlmostEqual(end_state[1], -60-92j)

    def test_sistem_dinamic2(self):
        end_state =tc.sistem_dinamic([complex(-1, -1), complex(1, 1)],[[[complex(3, 2), complex(2, 4)],
                                                            [complex(3, 4), complex(-2, 6)]],
                                                            [[complex(3, 2), complex(2, 4)],
                                                            [complex(3, 4), complex(-2, 3)]]])
        self.assertAlmostEqual(end_state[0], -13-37j)
        self.assertAlmostEqual(end_state[1], 10-24j)
if __name__ == '__main__':
    unittest.main()