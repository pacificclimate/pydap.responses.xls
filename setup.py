from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

install_requires = [
    'xlwt',
    'coards',
    'numpy',
    'pydap >=3.2.1'
]

setup(name='pydap.responses.xls',
    version=version,
    description="Pydap response that returns the dataset as a XLS file",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='xls pydap opendap dods',
    author='Roberto De Almeida',
    author_email='roberto@dealmeida.net',
    url='http://pydap.org/responses.html#xls',
    dependency_links = ['https://github.com/pacificclimate/pydap-pdp/tarball/master#egg=Pydap-3.2.2'],
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['pydap', 'pydap.responses'],
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
        [pydap.response]
        xls = pydap.responses.xls:XLSResponse
    """,
)
