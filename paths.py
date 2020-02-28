#!/usr/bin/env python
from pathlib import Path
class CONST(object):
	__slots__ = ()
	#FOO = 1234
	TWITTER_DATA = Path("../dataset/twitter.csv")
	TWITTER_DATA_2 = Path("../dataset/twitter2.csv")
	RAW_DATA = Path("../dataset/raw_data.csv")
	TRAIN_DATA = Path("../dataset/train_data.csv")
	TEST_DATA = Path("../dataset/test_data.csv")

	#def __setattr__(self, *_):
		#raise TypeError

#CONST = CONST()
#CONST.FOO = 4321
#CONST.__dict__['FOO'] = 4321 
#CONST.BAR = 5678

#print(CONST.FOO)       

#print(CONST.FOO)