from setuptools import setup, find_packages

setup(
    name='creativetext',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.8.3',
        'numpy==1.26.4',
        'pandas==2.2.1',
        'pytest==8.0.2',
        'scikit-learn==1.4.1.post1',
        'tqdm==4.66.2',
    ],
)