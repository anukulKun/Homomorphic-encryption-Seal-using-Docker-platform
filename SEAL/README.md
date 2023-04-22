## Microsoft SEAL Wrapper For Python and Health Score Predicting Model

Microsoft [**SEAL**](https://github.com/microsoft/SEAL) is an easy-to-use open-source ([MIT licensed](https://github.com/microsoft/SEAL/blob/master/LICENSE)) homomorphic encryption library developed by the Cryptography Research group at Microsoft.

[**pybind11**](https://github.com/pybind/pybind11) is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code.

This is a python binding for the Microsoft SEAL library.



## Contents

* [Build](https://github.com/Huelse/SEAL-Python#build)
* [Tests](https://github.com/Huelse/SEAL-Python#tests)
* [About](https://github.com/Huelse/SEAL-Python#about)
* [Contributing](https://github.com/ayosheisTHICC/Homomorphic-encryption-Seal-using-Docker-platform#contributing)



## Build
### Linux
CMake (>= 3.10), GNU G++ (>= 6.0) or Clang++ (>= 5.0), Python (>=3.6.8)

`sudo apt-get update && sudo apt-get install g++ make cmake git python3 python3-dev python3-pip`

`git clone https://github.com/Huelse/SEAL-Python.git`

```shell
cd SEAL/native/src
cmake .
make

pip3 install -r requirements.txt

# Check the path at first
# Setuptools (Recommend)
python3 setup.py build_ext -i
# or install
python3 setup.py install

### Windows

Visual Studio 2017 version 15.3 or newer is required to build Microsoft SEAL.

Open the `SEAL/SEAL.sln` in VS, config in `x64, Release, WinSDK(17763, etc)` mode and generate it.

```shell
python3 setup.py build_ext -i
# or install
python3 setup.py install
```

Microsoft official video [SEAL in windows](https://www.microsoft.com/en-us/research/video/installing-microsoft-seal-on-windows/).


## Future

* pickle
* microsoft gsl



## About

This project is still testing now, if any problems(bugs), [Issue](https://github.com/ayosheisTHICC/Homomorphic-encryption-Seal-using-Docker-platform/issues) please.

Email: [myemailaddressisdeku@gmail.com]


* [Contributors](https://github.com/Huelse/SEAL-Python/graphs/contributors)


