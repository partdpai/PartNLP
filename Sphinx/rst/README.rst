##############################################
PParser Project
##############################################


Overview
#############

documentation <www.google.com>_

This documentation is all about PParser package. PParser designes to help developers to perprocessing their text automatically! Also it has many useful features that makes perprocessing more fun! However, This is not an exhaustive description but it should show you how use the package effortlessly.


Introduction
#############
PParser is an integrated package uses many famous packages. Moreover, PParser supports multi languages.
In the below table you can see all valid operations accomplishing by PParser and their corresponder packages.


============== ============== ==================================
Operations Keyword Packages
============== ============== ==================================
normalize NORMALIZE HAZM, PARSIVAR
sent tokenize S_TOKENIZE HAZM, PARSIVAR
word tokenize W_TOKENIZE HAZM, PARSIVAR
lemmatize LEMMATIZE HAZM
stem STEM HAZM, PARSIVAR
============== ============== ==================================


Features
#############
This section provides a list of possible features supported by PParser. It able to:

* Use GPU
* Use multi thread
* Add custom stopwords
* Use multi processors
* Separate files for using GPU
* Remove specify range of characters
* Remove digits and Non-Persian letters
* Convert fnglish letters to persian letters

Installation
#############
for installing, you can simpley use pip to install the package.
>> pip install -i https://test.pypi.org/simple/ mPPars.
Usage
#############

In this section we are going to see the simple usage of PParser package.

.. image:: https://gitlab.com/mostafarahgouy/pparser/-/raw/mostafa-dev/images/guideline.gif

Example
--------
>>> from mPPars.models.core1 import Pipeline:
>>> Pipeline(package= 'hazm', lang='persian', processors=['STEM'],
text='برای بدست آوردن نتایج بهتر میتوان. از پیش پردازش بهره برد'' )
test.pypi.org
Simple index

