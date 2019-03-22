from setuptools import setup, find_packages

setup(
    name='workproject',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='recurtion and sort funtions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Rotondwatshipota1>/<workproject>',
    author='<Rotondwatshipota1>',
    author_email='<tshipotar@gmail.com>'
)
