import math
import os
from PIL import Image

#función para xxx
def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group is not None, then we have captured a real comment string.
        if match.group(2) is not None:
            return "" 
        else: # otherwise, we will return the 1st group
            return match.group(1) 
    return regex.sub(_replacer, string)

#función para xxxxx
def get_lenghts(example):
    code = remove_comments(example['source_code'])
    example['sourcecode_len'] = len(code.split())
    example['bytecode_len'] = len(HexBytes(example['bytecode']))
    return example

#function for removing columns
def explode_map(df1,LABELS):
    df1=pd.DataFrame(df1)
    return df1['address','slither'].explode('slither').map(LABELS)

    
