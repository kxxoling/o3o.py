# coding:utf-8
from __future__ import unicode_literals
import yaml
import unittest
from emoticon.main import gen_emoticon_map, get_random_emoticon
from emoticon.main import emoticon_map, emo_yaml_dir
from six import text_type as u, binary_type as s
from six import PY2


class MainTest(unittest.TestCase):
    def test_get_random_emoticon(self):
        if PY2:
            text_fixture = ['happy', u('happy'), '高兴', '\u9ad8\u5174']
        else:
            text_fixture = [s('happy'), 'happy', s('高兴'), '高兴']
        for e in text_fixture:
            emo = get_random_emoticon(e, emoticon_map)
            self.assertIsNotNone(emo)

    def test_emoticon_map(self):
        self.assertIn('高兴', emoticon_map.keys())
        self.assertIn('生气', emoticon_map.keys())

    def test_get_emoticon_map(self):
        with open(emo_yaml_dir) as f:
            emo_yaml = yaml.load(f)
            emoticon_map = gen_emoticon_map(emo_yaml)
            for v in emoticon_map.values():
                self.assertIsInstance(v, list)
                self.assertNotEqual(0, len(v))


@unittest.SkipTest
class CLITest(unittest.TestCase):
    def test_cli(self):
        pass
