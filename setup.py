import os
import sys
import platform
from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc


# python include dir
incdir = os.path.join(get_python_inc())
# cpp flags
cpp_args = ['-std=c++17']
# include directories
include_dirs = [incdir, './pybind11/include', './SEAL/native/src']
# library path
extra_objects = ['./SEAL/native/lib/libseal-3.4.a']

if(platform.system() == "Windows"):
    cpp_args[0] = '/std:c++latest'
    extra_objects[0] = './SEAL/native/lib/x64/Release/seal.lib'

if not os.path.exists(extra_objects[0]):
    print('Can not find the seal lib')
    exit(1)

ext_modules = [
    Extension(
        name='seal',
        sources=['src/base64.cpp', 'src/wrapper.cpp'],
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=cpp_args,
        extra_objects=extra_objects,
    ),
]

setup(
    name='seal',
    version='3.4.5',
    author='Huelse',
    author_email='huelse@oini.top',
    description='Python wrapper for the Microsoft SEAL',
    url='https://github.com/Huelse/SEAL-Python',
    license='MIT',
    ext_modules=ext_modules,
)
