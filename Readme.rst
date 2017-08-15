\:tv\: TorrentMirror CLI and python library
=================================================

Python library to expose torrentmirror as a command and python library.

.. contents:: :local:


\:tv\: torrentmirror - TorrentMirror CLI Interface
------------------------------------------------------

katcr comes with a simple but powerful command line interface, able to
return either magnets or torrents.


.. image:: http://i.imgur.com/HdY0NIl.png


Usage
+++++

::

    TorrentMirror.

        Usage: torrentmirror [<torrent_mirror_url>]



\:notebook\: Library Usage
---------------------------

TorrentMirror exposes a simple get_proxies method::

        def get_proxies(url="https://www.torrentmirror.net/",
                        filter_offline=True)


It returns a dict in the form::

        {"site_name": [["proxy_1", "status"], ["proxy_2", "status]]

Where status can be "ONLINE" or anything that starts with "OFFLINE".



\:star\: Installation
---------------------

This is a python package available on pypi.

On windows and mac `you can download python3.5 here <https://www.python.org/downloads/release/python-352/>`_.
On linux distros, python3.5 is already on most package managers :smile:

With python3.5 installed just execute::

    pip3.5 install torrentmirror


If it asks about permissions and you don't know what to do, you should
probably read `Jamie Matthews's article about virtualenvs <https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/>`_
