from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

extensions = cythonize([
    Extension("fairino.Robot", ["fairino/Robot.py"])
])

setup(
    name="fairino",
    version="0.1",
    packages=["fairino"],
    ext_modules=extensions,
)
