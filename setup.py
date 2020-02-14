from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='V0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/mbonokennedy/Predict_Analysis',
    author='Kennedy Mbono',
    author_email='mbonokennedy@gmail.com'
)