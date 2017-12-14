from distutils.core import setup
from Cython.Build import cythonize


setup(
  name = 'Hello world app',
  ext_modules = cythonize("source_file/*.pyx")
)

'''
  a_modules = cythonize("time_input.pyx"),
  b_modules = cythonize("newton.pyx"),
  c_modules = cythonize("draw.pyx"),
  d_modules = cythonize("syield.pyx"),
  e_modules = cythonize("rdata.pyx"),
  f_modules = cythonize("integration.pyx"),
  ext_modules = cythonize("LargeDataCalc.pyx"),
 '''