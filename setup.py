from setuptools import setup, find_packages

setup(
    name='moldyn',
    version='0.1.0',
    author='Prabhath Chilakalapudi',
    description='A basic molecular dynamics simulation package',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pathlib',
        'time'
    ],
    entry_points={
        'console_scripts': [
            'run-md=run_simulation:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
