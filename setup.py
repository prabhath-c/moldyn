from setuptools import setup, find_packages

setup(
    name='my_molecular_dynamics',
    version='0.1.0',
    author='Prabhath Chilakalapudi',
    description='A basic molecular dynamics simulation package',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'run-md=run_simulation:main',  # Optional CLI entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
