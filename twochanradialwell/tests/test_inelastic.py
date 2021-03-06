import os
import sys
basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,basedir+'/../..')

import twochanradialwell as radwell
import channelutil as chanutil
import unittest

class test_elastic(unittest.TestCase):
    def runTest(self):
        asymcalc = chanutil.AsymCalc(chanutil.hartrees, thresholds=[0.,2.])
        fun = radwell.get_Smat_fun(1., 2., 2., asymcalc, 1.)

        expect_mat = radwell.nw.matrix([[1., 0.],[0., -13.56891277]])
        got_mat = fun(0.)
        self.assertTrue(radwell.nw.np.allclose(got_mat,expect_mat))

        expect_mat = radwell.nw.matrix(\
          [[-0.92934972-0.36920061j, 3.95429415+5.82581759j],
           [3.95429415+5.82581759j, -22.30580611-24.7882964j]])
        got_mat = fun(1.8)
        self.assertTrue(radwell.nw.np.allclose(got_mat,expect_mat))

        expect_mat = radwell.nw.matrix(\
          [[0.17030364+0.94186257j, -0.26879527-0.10789196j],
           [-0.26879527-0.10789196j, -0.77423472+0.56273353j]])
        got_mat = fun(3.0)
        self.assertTrue(radwell.nw.np.allclose(got_mat,expect_mat))



if __name__ == "__main__":
    #Just for debug
    b = test_elastic()
    b.runTest()
