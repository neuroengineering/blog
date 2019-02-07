import pandas as pd

import os
import os.path as osp
import datetime

from math import isnan

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


# Start Data Section

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
    'File'                 : 'file',
    'page' : 'page'
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


class StudentListTemplate():
    
    head = u"""
    +++
    date = "{}"
    menu=""

    """.format(datetime.date.today().strftime("%Y-%m-%d"))

    head_list = u"""
    type = "people"
    title = "MSNE List of Students"
    banner="img/180419-coc-summit.jpeg"
    layout="single"
    """

    head_personal = u"""
    title = "{first} {last}"
    banner=""
    layout="personal"
    """

    foot = u"""

    +++

    This is a list of students enrolled in the MSNE program since program start in 2016.

    """

    tmpl = u"""
    [[students]]
        image = "{file}"
        name = "{first} {last}"
        description = "{text}"
        page = "/people/~{page}/"

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



class Student():

    def __init__():
        pass

class StudentList():

    def __init__(self,
            root = 'static/img/student-list',
            pageroot = '/img/student-list'
        ):
        files = [osp.join(pageroot, f) for f in os.listdir(root)]

        df = pd.read_csv('student-listing.csv')

        names = ['{}'.format(j) for i,j in df[['First Name', 'Last Name']].values]

        df['File'] = match(names, files)
        df['E-Mail'] = 'mailto:' + df['E-Mail']
        df['first'] = df['First Name']
        df['page'] = df['First Name'].apply(lambda x : x.lower().encode('ascii', 'replace').decode().replace("?", "").replace(" ", "") )

        tgt = pd.DataFrame()
        df = df.fillna(value=fillna)

        for k, v in remap.items():
            tgt[v] = df[k]
    
        tgt = tgt.sort_values('last').reset_index(drop=True)

    def html(self, tgt):

        html = head
        html += head_list
        for i in range(len(tgt)):
            my_dict = tgt.loc[i].to_dict()
            d = {k: my_dict[k] for k in my_dict if not str(my_dict[k]) == '#'}
            
            links = []
            for l in linktypes:
                if l in d:
                    links.append(link_tmpl.format(key = l, value=d[l]))
                    del(d[l])
                    
            d['links'] = '\n    '.join(links)
            html += tmpl.format(**d)
        html += foot
            
        with open('content/people/_index.md', 'w') as fp:
            fp.write(html)


    def profiles(self, tgt):
        for i in range(len(tgt)):
            html = head
            my_dict = tgt.loc[i].to_dict()
            d = {k: my_dict[k] for k in my_dict if not str(my_dict[k]) == '#'}
            
            html += head_personal.format(**d)
            
            name = "~{}/_index.md".format(d["page"])
            name = os.path.join('content/people/', name)
            os.makedirs(os.path.dirname(name), exist_ok = True)
            print(name)
            
            links = []
            for l in linktypes:
                if l in d:
                    links.append(link_tmpl.format(key = l, value=d[l]))
                    del(d[l])
                    
            d['links'] = '\n    '.join(links)
            html += tmpl.format(**d)
            html += foot
            print(html)
            with open(name, 'w') as fp:
                fp.write(html)


if __name__ == '__main__':

    pass