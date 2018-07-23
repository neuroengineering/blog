import pandas as pd

import os
import os.path as osp

head = u"""
+++
date = "2010-01-01T12:00:00"
draft = false
tags = ["events","tum"]
title = "MSNE Students"
menu = "main"
math = true
+++

<style>

.card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.4);
    width:50%;
    height: 350px;
    max-width:200px;
    margin: 10px 5px;
    text-align: center;
    background-color: #f5f5f5;
    padding: 5px 5px 5px 5px;
    float: left;
}

card.col1 {
    float: left;
    width: 20%;
}
card.col2 {
    float: left;
    width: 70%;
}
card.title {
    font-size: 100pt;
}

a.link {
    text-decoration: none;
    font-size: 18px;
}

.image-cropper {
    width: 100px;
    height: 100px;
    margin: 10px auto;
    position: relative;
    overflow: hidden;
    border-radius: 50%;
}

img {
    display: inline;
    margin-left: auto;
    margin-right: auto;
    height: 100%;
    width: 100%;
    margin: 0 auto;.
    align: center;
}

.linklist {
height:100%;
}

</style>
"""

tmpl = u"""
<div class="card">
    <div class="image-cropper">
    <img src="{file}" >
    </div>
    <p><b>{first} {last}</b>
    </br>
    {text}
    </p>
    <div id="linklist">
    {links}
    </div>
</div>
"""

linktypes = [   'envelope',
                'link',
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
    
    return s.lower().replace('í', 'i')

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
    'E-Mail'               : 'envelope',
    'LinkedIn Profile URL' : 'linkedin',
    'Github Profile URL'   : 'github',
    'Twitter Profile URL'  : 'twitter',
    'Facebook Profile URL' : 'facebook',
    'Google Scholar URL'   : 'scholar',
    'Website URL'          : 'link',
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

link_tmpl = u"""<a href="{value}" class="link"><i class="fa fa-{key}"></i></a>"""

for i in range(len(df)):
    
    my_dict = tgt.loc[i].to_dict()
    
    d = {k: my_dict[k] for k in my_dict if not str(my_dict[k]) == '#'}
    
    #print(d)
    
    links = []
    for l in linktypes:
        if l in d:
            links.append(link_tmpl.format(key = l, value=d[l]))
            del(d[l])
            
    d['links'] = '\n'.join(links)

    html += tmpl.format(**d)
    
from IPython.core.display import HTML

with open('content/post/static.md', 'w') as fp:
    fp.write(html)