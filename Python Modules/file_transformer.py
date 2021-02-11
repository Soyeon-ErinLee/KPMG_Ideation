#!/usr/bin/python --> 이거 민찬이가 환경에 적합한 형태로 변경해주세요
# -*- coding: utf-8 -*-

# Written by Ju Yeon Lee. justforher12344@gmail.com
# Co-worker: Min Chan Kim.

import re
import pandas as pd
import json
import requests
import pymysql
from datetime import date, timedelta


class STT_transformer(object):

    '''To parse json file data from STT processing

    Example
    -------
    >>> import sys
    >>> sys.path.append('/home/hoheon/Packages/')
    >>> ## 사용방법

    >>> json_path = ## AWS에서 해당 위치 지정
    >>> 구체적 사용법 제시
    '''

    def __init__(self, json):
        assert type(json) is str, print('json path must be str.')

        self.path = json
        self.data = self._load_json()


    def _load_json(self):
        with open(self.path) as jsonfile:
            data = json.load(jsonfile)
        return data


    def _html_adapter(self, string, tag):

        assert type(string) is str, print("text input must be string.")
        assert type(string) is str, print("tag input must be string.")

        ''' 

        tag information

        1. start : we add "<strong>" at the front part of input, which contains start time and speaker information
        2. middle : we add "</strong><br>" at the front part of the input, which is usually real script.
        3. end : we add "<br><br>" at the last part of the input, which is usually real script.

        '''

        if tag == 'start':
            new_string = "<strong>" + string
            return new_string

        elif tag == 'middle':
            new_string = "</strong><br>" + string
            return new_string

        elif tag == 'end':
            new_string = string + " <br><br>"
            return new_string

        else:
            print("there is no such {} tag").format(tag)


    def _segmentation(self, data):

        level0 = list(self.data.values())
        level1 = list(level0[2].values())
        level2 = level1[1]
        level2 = level1[1]
        level3 = level2['segments']

        df = pd.DataFrame()
        for script in level3:
            s = script['start_time']
            e = script['end_time']
            l = script['speaker_label']
            print(s, e, l)
            df = df.append([(l, s, e)], ignore_index=False)
        df.columns = ['speaker', 'start_time', 'end_time']

        information = dict()
        information['full_transcript'] = list(level1[0][0].values())[0]
        information['speaker_num'] = level2['speakers']

        return df, information


    def _parsing(self, data):
        base_df = self._segmentation()[0]

        return


    def to_frontend(self):

        return


    def to_model(self):

        return


    def file_export(self):

        # text 파일이나 excel 등으로 볼 수 있게 내보내는 과정

        return
