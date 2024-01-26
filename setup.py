from setuptools import setup, find_packages

setup(
    name='SDAT',
    version='0.1.0',
    description='Description of your package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/val-iisc/SDAT',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        # e.g., 'numpy>=1.18.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)