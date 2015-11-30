from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("_example_cython",
                  sources=["_example_cython.pyx"],
                  libraries=["functions"],
                  extra_link_args=["-L."],
                  )
    ]
)
