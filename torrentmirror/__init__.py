#!/usr/bin/env python3.5
"""Torrentmirror python interface."""
import warnings
from collections import defaultdict
from docopt import docopt
import robobrowser
from tabulate import tabulate
warnings.filterwarnings("ignore")


def get_proxies(url="https://www.torrentmirror.net/", filter_offline=True):
    """Manage complete search for specified pages."""
    page = robobrowser.RoboBrowser()
    page.open(url)
    proxies = defaultdict(list)

    # pylint: disable=not-callable
    for link in page.find_all(class_='mirror-links'):
        name = link.find('thead').find('th').text.split('\n')[1]
        for row in link.find_all('tr'):
            entry = [a.text.strip() for a in row.find_all('td')][:2]
            if len(entry) > 1 and '.' in entry[0]:
                if not filter_offline or 'OFFLINE' not in entry[1]:
                    proxies[name.replace(' Links', '')].append(entry)
    return dict(proxies)


def main():
    """TorrentMirror.

    Usage: torrentmirror [<torrent_mirror_url>]
    """
    opt = docopt(main.__doc__, version="0.0.1")
    proxies = get_proxies(
        opt.get('<torrent_mirror_url', "https://www.torrentmirror.net/"))
    for name, proxies in proxies.items():
        print("\n{}".format(name))
        print(tabulate(proxies))
