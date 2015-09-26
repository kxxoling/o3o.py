# coding:utf-8
import os
import random
import yaml
from emoticon import find_emoticon_data_files


abs_dir = os.path.dirname(__file__)
emo_yaml_dir = os.path.join(abs_dir, 'emo.yaml')


def gen_emoticon_map(emoticon_list, default=None):
    if default is None:
        emoticon_map = dict()
    else:
        emoticon_map = default
    for emoticon in emoticon_list:
        emotions = emoticon.get('tags', '').split(' ')
        for emotion in emotions:
            emoticon_map[emotion] = emoticon_map.get(emotion, []) + emoticon['emoticons']
    return emoticon_map


emoticon_map = None
for yaml_file in find_emoticon_data_files():
    with open(yaml_file) as f:
        emo_yaml = yaml.load(f)
        emoticon_map = gen_emoticon_map(emo_yaml, default=emoticon_map)


def get_random_emoticon(emotion, emoticon_map):
    emoticons = emoticon_map.get(emotion, [])
    return random.choice(emoticons)

