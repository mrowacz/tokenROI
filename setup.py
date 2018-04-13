from setuptools import setup, find_packages

setup(
    name = "tokenROI",
    version = "0.6.1",
    author = "Lukasz Czerwinski",
    author_email = "mrowacz@gmail.com",
    description = ("Quick ROI calculator for your token balances base on"
                   " idex.market prices"),
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
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
