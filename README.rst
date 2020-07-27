.. image:: https://raw.githubusercontent.com/partdpai/PartNLP/master/images/PartAiLogo.png
    :align: center

##############################################
             PartNLP Project
##############################################


Overview
#############

    `documentation <https://partdpai.github.io/PartNLP/>`_

    This documentation is all about *PartNLP* package. PartNLP designs to help developers to perprocessing their text automatically! Also it has many useful features that makes perprocessing more fun! However, This is not an exhaustive description but it should show you how use the package effortlessly.


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
for installing, you can simply use pip to install the package.

>>> pip install PartNLP


Pipeline Usage Example
########################

.. code-block:: python

	>>> from PartNLP import Pipeline

	>>> Pipeline(lang='persian', package='hazm', processors=['W_TOKENIZE', 'LEMMATIZE'], text='این متن، جهت بررسی عملکرد بسته نوشته شده است')

        Output of Hazm word tokenizer:
        ['این', 'متن', '،', 'جهت', 'بررسی', 'عملکرد', 'بسته', 'نوشته_شده_است']
        Output of Hazm Lemmatizer :
        ['این', 'متن', '،', 'جهت', 'بررسی', 'عملکرد', 'بسته', 'نویس']


Pipeline also can handle missing required data in which should be passed by users. In the below example no `package`, `language` or `processors` entered but
Pipeline asks you to fill them out.

.. code-block:: python

   >>> Pipeline(text='این متن، جهت بررسی عملکرد بسته نوشته شده است')
  ‌Warning: no package selected. ‌List of supported packages:['HAZM', 'PARSIVAR', 'STANZA']
  please enter a valid value: 'hazm'
  ‌Warning: no language selected. ‌List of supported languages:['ENGLISH', 'PERSIAN']
  please enter a valid value: 'persian'
  ‌Warning: no operator selected. ‌List of supported operations for 'hazm' package :['NORMALIZE', 'S_TOKENIZE', 'STEM', 'W_TOKENIZE', 'LEMMATIZE']



Interface Usage Example
########################

In this section we are going to see the simple usage of PartNLP package.


.. image:: https://raw.githubusercontent.com/partdpai/PartNLP/master/images/Interface.gif
