1. For Parser.py:
	imports : re, pickle
	-only this script needs input directory for the location of wsj.xml file
	-this can be provided on line 4. 

2. For Indexer.py:
	imports : defaultdict from collections, pickle, lmdb

3. For Search_Engine.py:
	imports : math, lmdb, pickle

4. Python 3.13 or above


->All files that will be generated such as .bin files and .txt file are hard coded to be generated on the same directory as the script is contained in.	