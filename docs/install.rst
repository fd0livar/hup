Installation
============

**Hup** requires Python 3.7 or later. If you do not already have a Python
environment configured on your computer, please see the instructions for
installing the full `scientific Python stack`_.

.. note::
   If you are using the Windows platform and want to install optional packages
   (e.g., `scipy`), then it may be useful to install a Python distribution such
   as: `Anaconda`_, `Enthought Canopy`_, `Python(x,y)`_, `WinPython`_, or
   `Pyzo`_. If you already use one of these Python distributions, please refer
   to their online documentation.

Below it is assumed, that you have the default Python environment configured on
your computer and you intend to install Hup inside of it.  If you want to create
and work with Python virtual environments, please follow instructions on `venv`_
and `virtual environments`_.

Install the latest distributed package
--------------------------------------

You can install the latest distributed package of Hup by using ``pip``::

    $ pip install hup

Install the development branch
------------------------------

The installation requires that you have `Git`_ installed
on your system. Under this prerequisite the first step is to clone the github
repository of Hup::

    $ git clone https://github.com/frootlab/hup.git

Thereupon the development branch can locally be installed by using `pip`::

    $ cd hup
    $ pip install -e .

The ``pip install`` command allows you to follow the development branch as
it changes by creating links in the right places and installing the command
line scripts to the appropriate locations.

Update the development branch
-----------------------------

Once you have cloned the GitHub repository onto a local directory, you can
update it anytime by running a ``git pull`` in this directory::

    $ git pull

Testing the development branch
------------------------------

Hup uses the Python builtin module :module:`unittest` for testing. Since the
tests are not included in the distributed package at you are required to install
the development branch, as described above. Thereupon you have to switch to the
repository directory and run::

    $ python3 tests

.. References:
.. _scientific Python stack: https://scipy.org/install.html
.. _Anaconda: https://www.anaconda.com/download/
.. _Enthought Canopy: https://www.enthought.com/product/canopy
.. _Python(x,y): http://python-xy.github.io/
.. _WinPython: https://winpython.github.io/
.. _Pyzo: http://www.pyzo.org/
.. _venv: https://docs.python.org/3/library/venv.html
.. _virtual environments:
    http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _Git: https://git-scm.com/
