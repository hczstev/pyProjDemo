from setuptools import setup, find_packages

setup(
    name="PyProjDemo",
    version="0.0.0",
    packages=find_packages(exclude=("tests",)),
    description="Python project demo",
    long_description="It is a python project demo",
    install_description=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    # Other useful parameters: py_modules, cmdclass, include_package_data...
)