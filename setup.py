from setuptools import setup

setup(
    name = "tokenROI",
    version = "0.1.1",
    author = "Lukasz Czerwinski",
    author_email = "mrowacz@gmail.com",
    description = ("Quick ROI calculator for your token balances base on"
                   " idex.market prices"),
    license = "MIT",
    keywords = "tokens cryptocurrencies idex roi",
    packages=['python', 'tests'],
    install_requires=['python-editor', 'pydrive']
)