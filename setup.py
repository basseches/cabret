from setuptools import setup, find_packages

setup(
    include_package_data=True,
    package_data={'': ['templates/template.tex']},
    packages=find_packages()
)
