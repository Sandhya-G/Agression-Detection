#!/usr/bin/env python
from pathlib import Path
import os
class CONST(object):
	__slots__ = ()
	#FOO = 1234
	PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
	TWITTER_DATA = Path(PROJECT_ROOT_DIR,"dataset/twitter.csv")
	TWITTER_DATA_2 = Path(PROJECT_ROOT_DIR,"dataset/twitter2.csv")
	RAW_DATA = Path(PROJECT_ROOT_DIR,"dataset/raw_data.csv")
	TRAIN_DATA = Path(PROJECT_ROOT_DIR,"dataset/train_data.csv")
	TEST_DATA = Path(PROJECT_ROOT_DIR,"dataset/test_data.csv")

	#def __setattr__(self, *_):
		#raise TypeError

#CONST = CONST()
#CONST.FOO = 4321
#CONST.__dict__['FOO'] = 4321 
#CONST.BAR = 5678

#print(CONST.FOO)       

#print(CONST.FOO)