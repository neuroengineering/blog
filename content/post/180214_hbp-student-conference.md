+++
date = "2018-02-14T12:00:00"
draft = false
banner = "/img/hbp-2nd-conference/hill.jpg"
tags = ["events"]
title = "2nd HBP Student Conference - Transdisciplinary Research Linking Neuroscience, Brain Medicine and Computer Science"
math = true
summary = """ """
+++

The [2nd HBP Student Conference](https://education.humanbrainproject.eu/web/2nd-hbp-student-conference) took place in Ljubljana, Slowenia, from 14 to 16 February 2018 and and offered a rich program covering different aspects of Neuroscience and Computational Methods within Neuroscience.

Apart from invited talks, MSc and PhD students got the opportunity to present both original and ongoing research in four oral and two poster sessions, comprised of the topics

1. Neurorobotics, Neuromorphic Computing, Theoretical Neuroscience
2. Medical Informatics
3. High Performance Computing, Brain Simulation
4. Human Brain/Mouse Brain Organisation, Systems and Cognitive Neuroscience

## Wednesday: Arrival, Neurorobotics and Kickoff

I particularly perceived the conference as an effort of bringing together scientists from neuroscience and computer science and as an effort to improve communication between the fields and enhance mutual understanding.
In this respect, the selection of speakers was quite diverse and consisted of senior scientists both from within and outside of the Human Brain Project.

On the first conference day, Marc-Oliver Gewaltig, investigator in the Blue Brain Project at the EPFL Lausanne, as well as coordinator of the Neurorobotics platform within the HBP, gave the opening talk on the HBP in general and his subproject in particular.

> "It is better to have a wrong model, than no model" -- *Marc-Oliver Gewaltig*

His work aims to target the intersection of sensory processing and emerging behaviors in robotics.
Herein, the main purpose of neurorobotics lies in the study of system behaviours that *emerge* from the simultaneous study of neural network simulations in connections with a robot body.
In this respect, the topic of *embodyment* in robotics played a central role in his talk.

Following the introduction to the conference, the first student session on Neurorobotics, Neuromorphic Computing and Theoretical Neuroscience took place.

![](/img/hbp-2nd-conference/city.jpg)

Personally, my highlights were the work by [Gabrial Urbain](https://twitter.com/gaburbain) on a Bio-Inspired Cat Robot and learning mechanisms for transferring behavior learned in simulated environments to the real system.

Also, [Pau Vilimelis Aceituno](https://scholar.google.com/citations?user=dahpSB8AAAAJ&hl=en) from the Max Planck Institute for Mathematics in Science gave an interesting theoretical account on the structure of complex networks and [how feedback connections in reservoir computing algorithms influence the performance of the derived feature embeddings](https://arxiv.org/abs/1707.02469).

The scientific program of the first day was closed by [Dr. Thomas Heinis](http://wp.doc.ic.ac.uk/theinis/) from Imperial College London, talking about a novel algorithm, FLAT, for organizing big sparse datasets to represent and quickly access neural data for simulations and analysis.

The following get-together and welcome reception concluded an insightful first day at the conference.

## Thursday: Medical Informatics, Deep Nets and Neuroethics

The second day was initiated by [Radoslaw Cichy](http://userpage.fu-berlin.de/rmcichy/) from the Bernstein Center for Computational Neuroscience in Berlin, who gave an interesting account on how multidimensional data from different sources can be integrated and analyzed.

At the core, his proposal is the use top-down models developed independently of biological brain function to fit behavioral data and derive explanations from that.
In particular, his work deals with the application of deep learning models to this and builds upon similarity analysis, which allows to integrate spatial resolution from fMRI data, temporal resolution from EEG as well algorithmic explicitness from fitted deep learning models.

Hereby, it is possible to gain novel understanding of the representations used by the brain, perform a new approach to brain mapping and providing a general framework for predicting brain and behavioral responses.

Following his talk, I presented my own work done in collaboration with the [Institute of Imaging and Computer Vision at RWTH Aachen](http://lfb.rwth-aachen.de) and the [MSNE faculty at the Institute for Cognitive Systems at TUM](https://www.ics.ei.tum.de/en/home/) on a novel approach to domain adaptation for medical datasets.
Other student talks in this session on Medical Informatics dealt with applications of machine learning algorithms to problems in clinical neuroscience, many related to the early detection of dementia.

Quite in contrast to the elsewise technical program, the morning program was concluded with a session on Neuroethics by [Dr. Arleen Salles](https://www.crb.uu.se/staff/arleen-salles/), [Dr. Michele Farisco](http://www.crb.uu.se/staff/michele-farisco/) and [Dr. Karen Rommelfanger](https://karenrommelfanger.com/).
In three talks, they investigated the effects and role of ethics research in the big brain initiatives world wide as well within the HBP.
Prof. Farisco gave an interesting philosophical account on ethics in conscious and unconscious subjects, and argued the also the unconscious receives ethical attentions, with several impacts on how interaction with patients should take place.


In the following third student session, the topic was on High Performance Computing for simulations of spiking neural networks.

The closing talk of the second day was delivered by [Prof. Anthony R. McIntosh](https://www.armcintosh.com/) from the [Virtual Brain](https://virtualbrain.org).
During his introduction, he motivated the need for models in neuroscience in a threefold way, namely as an explicit expression of intuitions, for considering multimodal data and to constrain possibilities in the interpretation of data.

At the Virtual Brain, quite contrary to Dr. Cichy's account from the first talk, a bottom-up modeling approach is performed in the application area of personalized medicine.
In several showcase examples, Prof. McIntosh demonstrated how brain simulations on the signal level helped to localize the origins and causes of elliptic seizures, even without completely imaging the brain, leveraging new methods for exploration and understanding of brain function and disfunction in clinical neuroscience.

The day was closed by the first poster session.
I got a lot of helpful feedback on my work, as well some further idea for real-world application cases for my machine learning work in the neuroscience.

![](/img/hbp-2nd-conference/castle.jpg)

## Friday: Imaging, Career Building and Biological Plausible Deep Nets

On the last conference day, the first talk by Prof. Isabel Fernaud from the University of Madrid gave some insights into work done in Neurology, as well as the role of information technology in her work.
Prof. Fernaud presented her work on the classification of functional types of neurons based on morphological features and the distribution of dendritic spines.

The fourth and final student session contained a couple of highly interesting talks.
Concerning data management techniques for dealing with large datasets, [Giacomo Mazzamuto](http://lens.unifi.it/bio/personal-page/mazzamuto/) presented interesting work on the use of video compression and image stiching algorithms in the handling of large 3D microscopy datasets.

Finally, the talk by [Andrew Morgan](http://muckli.psy.gla.ac.uk/index.php/people/postdocs/andrew-morgan) on the role of feedback and feedforward connections in V1 gave interesting new experimental insights about some intuitions I also used in my work on [Feature Aware Normalization](http://stes.io/fan).
Using occluded images as stimuli, Andrew investigated roles of predictive signals coming from higher cortical areas on the low-level processing done in V1, and concluded that while deeper layers are rather performing feed-forward computation, superficial cortical layers increasingly rely on high-level input when applying occlusion stimuli.

The final conference talk by [Prof. Gemma Roig](http://web.mit.edu/gemmar/www/) from MIT focused on aspects of using deep networks that are closer mimicking features of the human visual system.
During her first part, she proposed [Eccentricity as a criterion and Foveation as a mechanism for improving deep nets](https://arxiv.org/pdf/1511.06292.pdf) and enforcing scale invariance in object detection as well as overcoming the problem of crowding in images.
She concluded with presenting work done on defenses for adversarial examples, using similar, loosely brain-inspired mechanisms.

During the day, three parallel career sessions as well as the second poster session took place as well.


## Conclusions

Overall, the conference gave insights into both the general work of the HBP and the interactions with computer science, machine learning and machine intelligence.
In particular, I liked the focus on applications of deep learning models in neuroscience, but also the reverse mode of drawing inspiration, from behavioural observation in neuroscience research towards improving deep learning and machine learning models.
While many participants had a background in neuroscience, I had a lot of good interactions that pointed me to further useful work directions.

That being said, I am looking forward to further interdisciplinary conferences of this kind.

### Posters presented by MSNE students

- Schneider S, Ehrlich S, Bug D, Cheng G, Merhof D</br>
[Don't classify, generate: Dreaming up EEG Sequences for domain adaptation and data-efficient learning](#).
We thank the organizers for providing a Travel Grant.


{{< chip "profile-sq-800px - Steffen Schneider.jpg" "Steffen Schneider" >}}