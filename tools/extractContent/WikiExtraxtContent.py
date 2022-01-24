#!/usr/bin/env python
# coding: utf-8
# =============================================================================
#  Version: 1.0 (Jan 22, 2022)
#  Author: Marouane Nadir (marouane.nadir@outlook.it)
#
# =============================================================================


import os
import bz2
import pandas as pd
import re
import sys
from tqdm import tqdm


# In[104]:


path = sys.argv[1]



##creare decompressed folder
def decompressedFile(dirpath,directory):
    files =  [f for f in os.listdir(dirpath) if "bz2" in f]
    endpath = dirpath + '\\decompressed'
    
    if not os.path.isdir(endpath):
        os.mkdir(endpath)
    
    print("Start decomppress for ", directory )

    for filename in tqdm(files):
        filepath = os.path.join(dirpath, filename)
        newfilepath = os.path.join(endpath,filename + '.decompressed')
        with open(newfilepath, 'wb') as new_file, open(filepath, 'rb') as file:
            decompressor = bz2.BZ2Decompressor()
            for data in iter(lambda : file.read(100 * 1024), b''):
                new_file.write(decompressor.decompress(data))
    
    print("Terminated decomppress for ", directory )


# In[107]:


def createDataframe(dirpath,pathOutput,nameDf):
    df = pd.DataFrame(columns=('title', 'Descr'))
    endpath = dirpath + '\\decompressed'
    files =  [f for f in os.listdir(endpath) if "bz2" in f]
    print("Start creating of dataframe for",nameDf )
    for file in tqdm(files):
        filePath = endpath + '\\' + file
        f = open(filePath, "r", encoding='UTF-8')
        a = f.read()
        listOfItWord = [s.strip() for s in re.split("</doc>", a)]
        df = sliptWorld(listOfItWord,df)

    
    namexls = pathOutput + '\\DataFrame_' + nameDf + '.xlsx'
    print("Created the dataframe for",nameDf )

    df.to_excel(namexls, index=False)
    print("Saved the dataframe for",nameDf )


# In[108]:


def sliptWorld(listOfItWord,df):
    for itWord in listOfItWord:
        if len(itWord) > 0: 
            title = re.findall(r'title="(.+?)">', itWord)[0]
            n = re.findall(r'(.+?)>\n', itWord)[0]+'>\n'
            descr = itWord.replace(n, "")
            regex = title + '\n\n'
            descrFinal = descr.replace(regex, "")
            df = df.append({'title' : title, 'Descr' : descrFinal}, 
                        ignore_index = True)
    return df


# In[109]:


os.chdir(path)
path_output = path +  '\\output'

if not os.path.isdir(path_output):
    os.mkdir(path_output)

subdirectory = [f for f in os.listdir('.') if "output" not in f]



for directory in subdirectory:
    newPath = path + '\\'+ directory
    os.chdir(newPath)
    decompressedFile(newPath, directory )
    createDataframe(newPath,path_output,directory)


# In[ ]:




