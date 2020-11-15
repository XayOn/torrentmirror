\:tv\: TorrentMirror CLI and python library
=================================================

Python library to expose torrentmirror as a command and python library.

.. contents:: :local:


\:tv\: torrentmirror - TorrentMirror CLI Interface
------------------------------------------------------

You can invoke torrentmirror command to have a nice tabulated list of mirrors
in your terminal

.. image:: http://i.imgur.com/HdY0NIl.png


\:star\: Usage
++++++++++++++++

::

    TorrentMirror.

        Usage: torrentmirror [<torrent_mirror_url>]


\:star\: Installation
---------------------

This is a python package available on pypi.

With python3.8 installed just execute

.. code:: sh

    pip3.8 install torrentmirror


If it asks about permissions and you don't know what to do, you should
probably read `Jamie Matthews's article about virtualenvs <https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/>`_



\:notebook\: Library Usage
---------------------------

TorrentMirror exposes a simple get_proxies method


.. code:: python

        get_proxies(url="https://www.torrentmirror.net/", renew=False)

It returns a dict in the form

.. code:: python 

        {
          "site_name": [
            {
              "link": "http://foo.com",
              "status": "ONLINE",
              "percentage": 40
            },
            {
              "link": "http://foo.com",
              "status": "ONLINE",
              "percentage": 40
            }
          ]
        }
