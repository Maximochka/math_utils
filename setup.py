from setuptools import setup, find_packages

setup(
    name="math_utils_testing1488",
    version="0.0.1",
    author="Maximka052",
    author_email="plutomax3108@gmail.com",
    description="Простая библиотека для математических операций",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Maximochka/math_utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)