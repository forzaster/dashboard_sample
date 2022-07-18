
_get_asset_func = None

def init(get_asset_func):
    global _get_asset_func
    _get_asset_func = get_asset_func

def get(name):
    if name:
        return _get_asset_func(name)
    return None