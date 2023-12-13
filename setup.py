from setuptools import setup

setup(
    name='sales_tax',
    version='1.0',
    description='Calculate sales tax for a given price and state',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Bella288/SalesTax',
    author='Bella288',
    author_email='bella288@gmail.com',
    license='MIT',
    keywords='sales tax calculator',
    packages=['sales_tax'],
    install_requires=['numpy', 'pandas'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
        
    ],
)
