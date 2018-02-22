from setuptools import setup

setup(
    name='pylovepdf',
    version='1.3.0',
    packages=['pylovepdf', 'pylovepdf.tools'],
    url='http://www.github.com/AndyBTuttofare',
    license='LICENSE.md',
    author='Andrea.Bruschi',
    author_email='moonx2006@gmail.com',
    description='ilovepdf.com python API library',
    long_description=open('README.md').read(),
    install_requires=['requests==2.18.4', 'urllib3==1.22']
)
