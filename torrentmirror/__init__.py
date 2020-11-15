#!/usr/bin/env python3
"""Torrentmirror python CLI interface and API."""
import pickle
import warnings
from contextlib import suppress
from collections import defaultdict
from docopt import docopt
import robobrowser
from tabulate import tabulate
import xdg

warnings.filterwarnings("ignore")
CACHE_FILE = xdg.XDG_CACHE_HOME / 'torrentmirror.pickle'


def get_proxies(url="https://www.torrentmirror.net", renew=False):
    """Return complete torrent proxy list from torrentmirror.net

    This library acts as a quick torrentmirror list by scraping torrentmirror.net.
    To prevent overusing the torrentmirror service, by default it stores mirrors on
    disk, you can renew them by deleting torrentmirror.pickle file in your cache
    dir, or by passing renew=True to get_proxies method.
    """

    if not renew and CACHE_FILE.exists():
        with suppress(Exception):
            return pickle.load(CACHE_FILE.open('rb'))

    page = robobrowser.RoboBrowser()
    page.open(url)
    proxies = defaultdict(list)

    # pylint: disable=not-callable
    for link in page.find_all(class_='proxy-item'):
        page.open(f'{url}{link.attrs["href"]}')

        for row in page.find_all(class_='proxy-table'):
            name_ = row.find(class_='proxy-name')
            if not name_:
                continue

            status = row.find(class_='proxy-statues')
            percentage = row.find(class_='proxy-like').find(class_='counts')
            proxies[link.find('span').text].append(
                dict(link=name_.find('a').attrs['href'],
                     percentage=int(percentage.text.replace('%', '')),
                     status=status.text.strip()))

    proxies = dict(proxies)
    pickle.dump(proxies, CACHE_FILE.open('wb'))
    return proxies


def main():
    """TorrentMirror.

    Usage: torrentmirror [<torrent_mirror_url>]
    """
    opt = docopt(main.__doc__, version="0.0.1")
    proxies = get_proxies(
        opt.get('<torrent_mirror_url', "https://www.torrentmirror.net"))
    for name, proxies in proxies.items():
        print(f"\n{name}\n{tabulate(proxies)}")
