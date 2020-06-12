from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


setup(
    name="craqt api",
    ext_modules=cythonize("*.pyx"),
)