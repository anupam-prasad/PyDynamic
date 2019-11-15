"""
Perform test for uncertainty.propagate_DWT
"""

import matplotlib.pyplot as plt
import numpy as np

from PyDynamic.uncertainty.propagate_DWT import dwt, wave_dec, idwt, wave_rec, filter_design

import pywt


def test_filter_design():

    for filter_name in ["db3", "db4", "rbio3.3"]:

        ld, hd, lr, hr = filter_design(filter_name)

        assert isinstance(ld, np.ndarray)
        assert isinstance(hd, np.ndarray)
        assert isinstance(lr, np.ndarray)
        assert isinstance(hr, np.ndarray)


def test_dwt():
    
    for filter_name in ["db3", "db4"]:

        for nx in [20,21,22,23]:

            x = np.random.randn(nx)
            Ux = 0.1 * (1 + np.random.random(nx))

            ld, hd, lr, hr = filter_design(filter_name)

            # execute single level DWT
            y1, Uy1, y2, Uy2 = dwt(x, Ux, ld, hd, kind="diag")

            # all output has same length
            assert y1.size == y2.size
            assert y1.size == Uy1.size
            assert Uy1.size == Uy2.size

            # output is half the length of (input + filter - 1)
            assert (x.size + ld.size - 1) // 2 == y1.size

            # compare to pywt
            ca, cd = pywt.dwt(x, filter_name, mode="zero")
            assert ca.size == y1.size
            assert cd.size == y2.size
            assert np.allclose(ca, y1)
            assert np.allclose(cd, y2)


def test_idwt():

    for filter_name in ["db3", "db4"]:

        for nc in [10,11,12,13]:

            c_approx = np.random.randn(nc)
            Uc_approx = 0.1 * (1 + np.random.random(nc))
            c_detail = np.random.randn(nc)
            Uc_detail = 0.1 * (1 + np.random.random(nc))

            ld, hd, lr, hr = filter_design(filter_name)

            # execute single level DWT
            x, Ux = idwt(c_approx, Uc_approx, c_detail, Uc_detail, lr, hr, kind="diag")

            # all output has same length
            assert x.size == Ux.size

            # output double the size of input minus filter
            assert 2*c_approx.size - lr.size + 2 == x.size

            # compare to pywt
            r = pywt.idwt(c_approx, c_detail, filter_name, mode="zero")
            assert np.allclose(x, r)


def test_identity(make_plots=False):

    for filter_name in ["db3", "db4"]:

        for nx in [20, 21, 22, 23]:

            x = np.linspace(1,nx,nx)  # np.random.randn(nx)
            Ux = 0.1 * (1 + np.random.random(nx))

            ld, hd, lr, hr = filter_design(filter_name)

            # single decomposition
            y_approx, U_approx, y_detail, U_detail = dwt(x, Ux, ld, hd, kind="diag")

            # single reconstruction
            xr, Uxr = idwt(y_approx, U_approx, y_detail, U_detail, lr, hr, kind="diag")

            if x.size % 2 == 0:
                assert x.size == xr.size
                assert Ux.size == Uxr.size
                assert np.allclose(x, xr)
            else:
                assert x.size + 1 == xr.size
                assert Ux.size + 1 == Uxr.size
                assert np.allclose(x, xr[:-1])
            
            if make_plots:
                plt.plot(x)
                plt.plot(xr)
                plt.show()

                plt.plot(Ux)
                plt.plot(Uxr)
                plt.show()


def test_decomposition():
    pass


def test_reconstruction():
    pass