import setuptools
setuptools.setup(
    name='phddsf22m001scraper',
    version='0.1',
    author='Muhammad Husnain',
    author_email='m.husnain8721@gmail.com',
    description='A web scraper that returns parsed response for a given taget',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
)
