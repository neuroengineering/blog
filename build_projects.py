import pandas as pd

columns = [
    "time",
    "first",
    "last",
    "batch",
    "type",
    "start",
    "project",
    "affiliation",
    "laburl",
    "supervisor",
    "description",
    "puburl",
    "codeurl",
    "nan",
    "nan"
]

header = """\
+++
date = "2019-04-27T12:00:00"
draft = false
tags = ["events","research","about"]
title = "Research"
menu = ""
math = true

banner = "/img/hbp-entrepreneurship/ChristophExplaining.jpg"
+++

## Retreats

- [1st MSNE Retreat 2017](/2017/05/14/spring-2017-msne-retreat/). Invited Speakers: Matthias Bethge, Heiko Neumann, Dmitry Kireev 
- [2nd MSNE Retreat 2018](/2018/06/01/2nd-msne-retreat/). Invited Speakers: Jakob Macke, Benjamin Grewe, Thomas Euler
- [3rd MSNE Retreat 2019](/2019/05/30/3rd-msne-retreat/). Invited Speakers: Nora Heinzelmann, Tobias Reichenbach, Albert Compte, Emily King
- *Soon: 4th MSNE Retreat 2020*

## Conference Visits

### 2019
- Computational and Systems Neuroscience 2019 ([cosyne.org](http://www.cosyne.org/c/index.php?title=Cosyne_19))

### 2018
- [13th Bernstein Conference Göttingen](/2017/07/14/13th-bernstein-conference-g%C3%B6ttingen/)
- [2nd HBP Student Conference](2nd-hbp-student-conference-transdisciplinary-research-linking-neuroscience-brain-medicine-and-computer-science/)
- [Interdisciplinary College](http://localhost:1313/2018/03/13/interdisciplinary-college-2018/)
- [CoC Neuroengineering Workshop Munich](/2018/04/19/coc-neuro-engineering-networking-workshop/)
- [Conference on Clinical Neurotechnologies and Healthy Aging](/2018/06/27/conference-on-clinical-neurotechnologies-and-healthy-aging/)
- Neuroscience 2018, San Diego ([sfn.org](https://www.sfn.org/Meetings/Neuroscience-2018))
- Thirty-second Conference on Neural Information Processing Systems ([neurips.cc](https://neurips.cc/Conferences/2018))

### 2017
- [1st HBP Student Conference](2017/02/10/1st-human-brain-project-student-conference-in-vienna/)

## Events (Co-) Organized by MSNE Students

- [RoboCare - Future of Care between Human and Machine](/2018/07/02/robotcare-future-of-care-between-human-and-machine/)
- [Workshop on Learning in Brains and Machines](https://stes.io/learning-in-brains-and-machines)

## Research Projects

Besides their final thesis project, MSNE students spend 15 weeks on additional two research projects over the course of their studies.
[In our blog post](/2018/11/16/msne-research-internships/), Pranshul, Annika and Vanessa write about their experiences at UC Davis, the Max Planck Institute for Intelligent Systems and MIT. 



"""

fmt = """\
- **{project}**
  {first} {last}, {supervisor}
  [{affiliation}]({laburl})
  {description}
  {puburl}
  {codeurl}
  *Time scope: {type}, beginning on {start:%B %d, %Y}*
"""

remap_keys = {
    "project" : lambda x: x.strip(),
    "supervisor" : lambda x : ", ".join(reversed(x.split("\n"))),
    "puburl" :  "Publication: {}</br>".format,
    "codeurl" : "Code: {}".format,
    "start" : lambda x : pd.to_datetime(x, dayfirst=True, format='%d.%m.%Y').date()
}

def generate_markdown(inp):
    
    md = fmt.format(**inp.to_dict())
    md = '\n'.join(map(lambda x: x+"{{< break >}}", filter(lambda x : len(x.strip()), md.split('\n'))))
    print(md)
    return md

if __name__ == "__main__":

    print("Writing project list")

    df = pd.read_csv("projects.csv", parse_dates=True, infer_datetime_format=True, dayfirst=True)
    df.columns = columns
    for key, mapping in remap_keys.items():
        idc = ~df[key].isna()
        df.loc[idc,key] = df.loc[idc,key].apply(mapping)
    df = df.fillna("")
    df = df.sort_values("start")

    md = header + "\n\n".join(df.T.apply(generate_markdown))
    with open("content/about/research.md", "w") as fp:
        fp.write(md)
    
    print("Done.")