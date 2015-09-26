__version__ = '0.0.5'


def find_emoticon_data_files():
    import os
    import glob
    abs_file_dir = os.path.abspath(__file__)
    base_dir = os.path.dirname(abs_file_dir)
    yaml_files = glob.glob(base_dir + '/*.yaml')
    return yaml_files

EMOTION_DATA_FILES = find_emoticon_data_files()

