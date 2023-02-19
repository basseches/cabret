from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="texonomy",
    long_description=readme(),
    python_requires=">=3.8",
    include_package_data=True,
    package_data={'': ['templates/template.tex']},
    packages=find_packages()
)
