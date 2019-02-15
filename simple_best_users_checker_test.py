from unittest.case import TestCase

from simple_best_users_checker import id_best_users


class SimpleIpValidatorTest(TestCase):

    def test_id_best_users(self):
        a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
        a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
        a3 = ['A042', 'A025', 'B004']
        self.assertEqual(id_best_users(a1, a2, a3), [[5, ['A042']], [3, ['A025', 'B004']]])

        a1 = ['A043', 'B004', 'A025', 'A042', 'C025']
        a2 = ['B009', 'B040', 'B003', 'A042', 'A027', 'A044']
        a3 = ['A041', 'A026', 'B005']
        self.assertEqual(id_best_users(a1, a2, a3),  [])

        a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
        a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
        a3 = ['A042', 'B004', 'A025', 'A042', 'C025', 'B009', 'B040', 'B004', 'A042', 'A025', 'A042']
        a4 = ['A042', 'A025', 'B004']
        self.assertEqual(id_best_users(a1, a2, a3, a4), [[9, ['A042']], [5, ['A025', 'B004']]])
