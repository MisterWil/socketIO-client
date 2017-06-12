import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))


def LOAD_TEXT(name): return io.open(join(HERE, name), encoding='UTF-8').read()


DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst',
    'CHANGES.rst',
])
setup(
    name='socketIO-client3',
    version='0.8.0',
    description='A socket.io client library',
    long_description=DESCRIPTION,
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
    ],
    keywords='socket.io node.js',
    author='Wil Schrader',
    author_email='wilrader@gmail.com',
    url='https://github.com/MisterWil/socketIO-client3',
    install_requires=[
        'requests>=2.7.0',
        'six',
        'websocket-client',
    ],
    tests_require=[
        'nose',
        'coverage',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False)
