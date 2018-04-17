import io
import os
from setuptools import setup, find_packages

package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, 'README.md')
with io.open(readme_filename, encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name = "tokenROI",
    version = "0.6.7",
    author = "Lukasz Czerwinski",
    author_email = "mrowacz@gmail.com",
    url = "https://github.com/mrowacz/tokenROI",
    description = ("Quick ROI calculator for your token balances base on"
                   " idex.market prices"),
    long_description=readme,
    entry_points={
        'console_scripts': [
            'token_roi = token_roi:main',
        ]
    },
    license = "MIT",
    keywords = "tokens cryptocurrencies idex roi",
    packages=find_packages(),
    install_requires=['python-editor', 'dropbox', 'requests>=2.16.2'],
    classifiers=(
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ),
)
