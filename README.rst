
##############################################
PartNLP Project
##############################################


Overview
#############

    `documentation <www.google.com>`_

    This documentation is all about *PartNLP* package. PartNLP designes to help developers to perprocessing their text automatically! Also it has many useful features that makes perprocessing more fun! However, This is not an exhaustive description but it should show you how use the package effortlessly.


Introduction
#############
PartNLP is an integrated package uses many famous packages. Moreover, PartNLP supports multi languages.
In the below table you can see all valid operations accomplishing by PartNLP and their corresponder packages.


==============        ==============      ================================== 
Operations               Keyword                   Packages
==============        ==============      ==================================
normalize               NORMALIZE                 HAZM, PARSIVAR 
sent tokenize           S_TOKENIZE                HAZM, PARSIVAR, STANZA 
word tokenize           W_TOKENIZE                HAZM, PARSIVAR, STANZA  
lemmatize               LEMMATIZE                 HAZM,           STANZA
stem                    STEM                      HAZM, PARSIVAR, STANZA
==============        ==============      ==================================


Installation
#############
for installing, you can simpley use pip to install the package.  

>>> pip install -i https://test.pypi.org/simple/PartNLP

Usage
#############

In this section we are going to see the simple usage of PartNLP package.

.. image:: https://gitlab.com/mostafarahgouy/pparser/-/raw/mostafa-dev/images/demo.gif



Examples
#############

Simple example:

>>> from PartNLP import Pipeline


.. image:: https://gitlab.com/mostafarahgouy/pparser/-/raw/mostafa-dev/images/usage_example_scale.png


#############


.. image:: https://gitlab.com/mostafarahgouy/pparser/-/raw/mostafa-dev/images/validation_example_scale.png

