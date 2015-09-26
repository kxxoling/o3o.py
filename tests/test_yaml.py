# coding:utf-8
import yaml
import unittest
from emoticon import find_emoticon_data_files


class YAMLFileTest(unittest.TestCase):
    def test_yaml_files(self):
        yaml_files = find_emoticon_data_files()
        for f in yaml_files:
            yaml.load(f)

    def test_find_emoticon_data_files(self):
        yaml_files = find_emoticon_data_files()
        self.assertEqual(1, len(yaml_files))
        for f in yaml_files:
            assert f.endswith('.yaml')

