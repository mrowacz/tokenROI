tokenROI
========
Info: Console ethereum erc20 token portfolio.<br>
Author: Lukasz Czerwinski <mrowacz@gmail.com>

About
=====

tokenROI is an tool which eaisly presents your erc20 token collection
using data from idex stock.
It converts your token balances into ethereum and also shows current roi
of your investments. There is possibility to store your's configuration on
google drive.

Installation
============
download the project source and do::
```
  $ python setup.py install
```

Quick Start
============
Working token roi calculator needs list of erc20 tokens and your ethereum wallets.
Calculator allows easily edit configuration with:
```
$ token_roi --edit
```
It opens your system editor and starts edition of token_list.txt and
eth_wallets.txt. Config construction is easy and shouldn't make a problems.

Examples
========
Here's a basic usage examples
```
$ token_roi
```
console output should gives<br>
![screenshot from 2018-05-02 22-54-47_2](https://user-images.githubusercontent.com/11421787/39549323-be20f950-4e5d-11e8-8d3e-5122eec3e50b.png)
It shows only your ethereum erc20 token's balances. Showing with overall ethereum wallets
posession is made with:
```
$ token_roi --all
```
console output should gives<br>
![screenshot from 2018-05-02 22-54-47](https://user-images.githubusercontent.com/11421787/39549080-d9820492-4e5c-11e8-8bbd-a1d0873fda5b.png)

Contact
=======
All complains and suggestions sent through github issue system