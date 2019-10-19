from setuptools import setup, find_packages

setup(
    name="ft_turing",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['docopt>=0.6.2'],
    entry_points={
        'console_script': [
            'ft_turing = ft_turing:main'
        ]
    }
)
