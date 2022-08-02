==============
zeeklog2pandas
==============


.. image:: https://img.shields.io/pypi/v/zeeklog2pandas.svg
        :target: https://pypi.python.org/pypi/zeeklog2pandas

.. image:: https://img.shields.io/travis/stratosphereips/zeeklog2pandas.svg
        :target: https://travis-ci.com/stratosphereips/zeeklog2pandas

.. image:: https://readthedocs.org/projects/zeeklog2pandas/badge/?version=latest
        :target: https://zeeklog2pandas.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Read Zeeek/Bro log and log.gz (even broken ones) into a Pandas DataFrame.


* Free software: MIT license
* Documentation: https://zeeklog2pandas.readthedocs.io.


Features
--------

* zeeklog2pandas allows to read Zeek/Bro .log files or compressed .log.gz files, transparently into a Pandas DataFrames. 
  
* Best effort reading of corrupted or incomplete compressed .log.gz files.

* Columns filtering.

* Interface compatible with Pandas `read_csv()` function.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
