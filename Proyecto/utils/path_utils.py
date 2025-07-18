import os

def get_asset_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
    return os.path.join(base_dir, "..", "assets", filename)
