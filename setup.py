import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Python-Alexandria",
    version="1.2.5",
    author="Antonio Lopez Rivera",
    author_email="antonlopezr99@gmail.com",
    description="General utilities for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonlopezr/alexandria",
    packages=setuptools.find_packages(),
    install_requires=[
        "termcolor",
        "scipy",
        "numpy",
        "coverage",
        "coverage-badge"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
