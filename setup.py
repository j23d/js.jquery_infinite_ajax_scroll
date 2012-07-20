from setuptools import setup, find_packages
import os

version = '0.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_infinite_ajax_scroll', 'test_jquery_infinite_ajax_scroll.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_infinite_ajax_scroll',
    version=version,
    description="fanstatic jquery infinite ajax scroll",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic infinit-ajax-scroll',
    author='Marco Scheidhuber',
    author_email='j23d@jusid.de',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'jquery.jquery_infinite_ajax_scroll = js.jquery_infinite_ajax_scroll:library',
            ],
        },
    )
