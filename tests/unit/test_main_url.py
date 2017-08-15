def test_returns_dict():
    import torrentmirror
    result = torrentmirror.get_proxies()
    assert isinstance(result, dict)
