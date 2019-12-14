import pandas as pd

import os
import os.path as osp
import datetime

head = u"""
+++
title = "MSNE List of Students"
date = "{}"
type = "people"
layout="single"
menu=""
banner="img/180419-coc-summit.jpeg"

""".format(datetime.date.today().strftime("%Y-%m-%d"))

foot = u"""

+++

This is a list of students enrolled in the MSNE program since program start in 2016.

"""

tmpl = u"""
[[students]]
    image = "{file}"
    name = "{first} {last}"
    description = "{text}"

    {links}
"""

link_tmpl = '{key} = "{value}"'

linktypes = [   'email',
                'web',
                'linkedin',
                'github',
                'twitter',
                'facebook',
                'scholar']

root = 'static/img/student-list'
pageroot = '/img/student-list'
files = [osp.join(pageroot, f) for f in os.listdir(root)]

df = pd.read_csv('student-listing.csv')

names = ['{}'.format(j) for i,j in df[['First Name', 'Last Name']].values]

def normalize(s):
    
    return s.lower().replace('í', 'i').replace(" ", "")

def match(names, files):
    m = []
    for n in names:
        for f in files:
            if normalize(n) in normalize(f):
                m.append(f)
                break
        else:
            print('Missing {}'.format(n))
            m.append(None)
    return m

df['File'] = match(names, files)

df['E-Mail'] = 'mailto:' + df['E-Mail']

df['first'] = df['First Name']

remap = {
    'First Name'           : 'first',
    'Last Name'            : 'last',
    'Description'          : 'text',
    'E-Mail'               : 'email',
    'LinkedIn Profile URL' : 'linkedin',
    'Github Profile URL'   : 'github',
    'Twitter Profile URL'  : 'twitter',
    'Facebook Profile URL' : 'facebook',
    'Google Scholar URL'   : 'scholar',
    'Website URL'          : 'web',
    'File'                 : 'file'
}

fillna = {
    'First Name'           : '',
    'Last Name'            : '',
    'Description'          : '',
    'E-Mail'               : '#',
    'LinkedIn Profile URL' : '#',
    'Github Profile URL'   : '#',
    'Twitter Profile URL'  : '#',
    'Facebook Profile URL' : '#',
    'Google Scholar URL'   : '#',
    'Website URL'          : '#',
    'Profile Picture'      : 'placeholder.png'
}

tgt = pd.DataFrame()
df = df.fillna(value=fillna)

for k, v in remap.items():
    
    tgt[v] = df[k]
    
    
tgt = tgt.sort_values('last').reset_index(drop=True)

from math import isnan

html = head


for i in range(len(df)):
    
    my_dict = tgt.loc[i].to_dict()
    
    d = {k: my_dict[k] for k in my_dict if not str(my_dict[k]) == '#'}
    
    #print(d)
    
    links = []
    for l in linktypes:
        if l in d:
            links.append(link_tmpl.format(key = l, value=d[l]))
            del(d[l])
            
    d['links'] = '\n    '.join(links)

    html += tmpl.format(**d)

html += foot
    
from IPython.core.display import HTML

with open('content/people/index.md', 'w') as fp:
    fp.write(html)
