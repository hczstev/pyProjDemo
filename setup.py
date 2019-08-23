from setuptools import setup, find_packages

setup(
    name="PyProjDemo",
    version="0.1.0",
    description="Python project demo",
    long_description="It is a python project demo",

    packages=find_packages(exclude=("tests",)),
    # packages=["PyProjDemo"],
    package_data={"": ["*.json"]},

    install_description=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],

    entry_points={
        "console_scripts": [
            "demo = PyProjDemo.__main__:main",
        ],
    },
    # Other useful parameters: py_modules, cmdclass...
)
