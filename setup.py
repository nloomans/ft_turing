from setuptools import setup, find_packages

setup(
    name="ft_turing",
    version="0.1.0",
    packages=['ft_turing'],
    install_requires=['docopt>=0.6.2'],
    entry_points={
        'console_scripts': [
            'ft_turing = ft_turing.__main__:main',
        ]
    }
)
