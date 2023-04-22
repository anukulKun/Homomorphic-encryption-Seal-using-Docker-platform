import os
import sys
import platform
from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc

incdir = os.path.join(get_python_inc())
cpp_args = ['-std=c++17']
include_dirs = [incdir, './pybind11/include', './SEAL/native/src']
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
    author='Deku',
    author_email='myemailaddressisdeku@gmail.com',
    description=' Design and implement a cloud service that uses homomorphic encryption to process sensitive healthcare data securely and efficientlyL',
    url='https://github.com/Huelse/SEAL-Python',
    license='MIT',
    ext_modules=ext_modules,
)
