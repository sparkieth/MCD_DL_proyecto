import math
import os
from PIL import Image
import numpy as np
import pandas as pd
import re
import seaborn as sns
import sys
sys.path.append('MCD_DL_proyecto2')
import funciones
import re


def decontracted(phrase):
  phrase = re.sub(r"won't", "will not", phrase)
  phrase = re.sub(r"can\'t", "can not", phrase)
  phrase = re.sub(r"n\'t", " not", phrase)
  phrase = re.sub(r"\'re", " are", phrase)
  phrase = re.sub(r"\'s", " is", phrase)
  phrase = re.sub(r"\'d", " would", phrase)
  phrase = re.sub(r"\'ll", " will", phrase)
  phrase = re.sub(r"\'t", " not", phrase)
  phrase = re.sub(r"\'ve", " have", phrase)
  phrase = re.sub(r"\'m", " am", phrase)
  return phrase

  SYNS = []
  for sentance in dataframe:
    sentance = re.sub(r"http\S+", "", sentance)
    sentance = decontracted(sentance)
    sentance = re.sub("\S*\d\S*", "", sentance).strip()
    sentance = re.sub('[^A-Za-z]+', ' ', sentance)
    sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in stopwords)
    sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in STOPWORDS)
    SYNS.append(sentance.strip())
  return SYNS

# Cleaning
TAG_RE = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)")
def preprocess_text(sen):
  """
  """
  sentence = TAG_RE.sub('', sen) # html tags
  sentence = re.sub('[^a-zA-Z]', ' ', sentence) # punctuations and numbers
  sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence) # single character
  sentence = re.sub(r'\s+', ' ', sentence) # multiple spaces
  return sentence

    
