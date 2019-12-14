+++
date = "2017-06-12T12:00:00"
draft = true 
image = ""
tags = ["events"]
title = "4th HBP Summer School" 
math = true
summary = """
Test
"""
banner = "/img/hbp-summer-school/view.jpg"
+++

The 4th HBP Summer School took place from June 12 to June 18 at the Obergurgl University Center in Austria.
The diverse program includes introductions to High Performance Computin, Principles of Brain Computation,
workshop sessions and programming tutorials as well as student talks and poster presentations.

## High Performance Computing

In two talks on Tuesday and Wednesday, [Erwin Laure](todo) from KTH Stockholm gave an introduction to concepts in High Performance Computing (HPC).

![SpiNNaker Board for simulating spiking neural network with up to 16.000 neurons](/img/hbp-summer-school/spinnaker.jpg)

Types of Computing Infrastructure:

- SISD (Single Instruction Single Data)
- SIMD (Single Instruction Multiple Data)
- MISD (Multiple Instruction Single Data)
- MIMD (Multiple Instruction Multiple Data)

As a general boundary to what is achievable by parallizable HPC, Amdahl's Law is frequently considered, stating that the fraction of time spend on the execution of *not serializable* code effectively provides an upper bound on the total execution time.
The maximum speedup $S$ of a program is therefore limited by two rates:
The fraction of parallizable code $r\_p$ and the fraction of not parallizable coe $r\_s$, yielding

$$
S = \frac{1}{r\_s + \frac{r\_p}{n}},
$$

where $n$ denotes the number of parallel processes used for speeding up the computation.
It is easily inferrable that the maximum speedup for $n \to \infty$ is given as $S = 1 / r\_s$.

But even with this bound in mind, writing parallizable code is crucial for application development in HPC.

We discussed different programming schemes for HPC, with a special focus on memory access.
Roughly, three main fields of application can be considered, with different programming tools available:

- Shared Memory
    - pThreads: Rather low level programming model
    - OpenMP: Higher level library allowing for easy use of Fork-Join Models (execute serial code, create parallel processes in some points, e.g. for loop execution, joining all processes after completion of the task)
- Distributed Memory
    - Massage Passing (MPI) using the SPMD scheme
    - Partitional global address space (PGAS)
- GPU Programming (Separate Memory)
    - CUDA (propritrary, Nvidia)
    - OpenCL

In general, Erwin Laure proposed that in the future, there is no single programming paradigm to follow: Instead, both main modalities, Latency Optimized Cores (LOC) as well has Throughput Optimized Cores (TOC) have to be used in conjunction in order to build successful programs.
Surprisingly, in current HPC systems, the cost for moving data remains constant over successive processor generations while the cost for floating point operations (FLOPs) is constantly reduced.
This results in the curious situation that no longer steps of execution, but favouring mostly local memory access schemes with low rate of data movement is preferred, requiring to rethink how we design our algorithms.

## Principles of stochastic computation

In a second series of two talks and a tutorial session, Dr. [Mihai Petrovici]() gave an introduction to Principles of Brain Computation, focusing on stochastic computation.
In this PhD thesis [TODO](), he extensively worked on this topic and during two sessions gave a detailed overview on key concepts of stochastic computation.
The main points will be highlighted in the article section below.

### Background on Graphical Models and Factor Graphs

![Mihai Petrovici gave an introduction to probabilistic graphical models and spiking networks based on boltzman machines](/img/hbp-summer-school/talk-computing.jpg)

![Discussion](/img/hbp-summer-school/discuss.jpg)

![](/img/hbp-summer-school/outside.jpg)

We started with discussing factor graphs and decomposition of probability distributions into their respective parts.
Given any system with multiple random variables depending upon one another, a probability distribution can usually be decomposed into a-priori and posterior distributions.
Considering a simple Bayesian network with $c \to b \to a$ and $c \to a$, we have

$$
p(a,b,c) = p(a|b,c) p(b|c) p(c).
$$

More general, this can be done in any graphical model using the techique of factorizing the distribution of the maximum clique within the network.


### Derivation of the membrane potential 
From membrane potential to probability distributions

Since we have

$$
u\_k = \log \frac{p(z\_k = 1 | z\_{\backslash k})}{p(z\_k = 0 | z\_{\backslash k})}
$$

and after some derivations arrive at 

$$
u\_k = \log \frac{\sum\_{i} z\_i z\_k w\_{i,k} + b\_k z\_k |\_{z\_k = 1}}{\sum\_{i} z\_i z\_k w\_{i,k} + b\_k z\_k |\_{z\_k = 0}}
$$

where the denominator can be reduced to zero, yielding

$$
u\_k = \sum\_i z\_i w\_{i,k} + b\_k.
$$

Note that the initial equation for $u\_k$ implicitely assumed binary neurons with a sigmoid activation function, i.e.,

$$
p(z\_k = 1 | z\_{\backslash k}) = \frac{1}{1 + e^{-u\_k}}.
$$

### Neural Sampling


## Tutorial Sessions

During the week, several introductions to techniques relevant for neuromorphic computing and computational neuroscience where introduced

![](/img/hbp-summer-school/lecture.jpg)

### Introduction to Python

Eric Mülller, University of Heidelberg

### Theory of Computational Neuroscience

Mihai Petrovici, University of Bern

### BrainScaleS

Sebastian Billaudelle, University of Heidelberg
Korbinian Schreiber, University of Heidelberg

### SpiNNaker

David Lester, Alan Stokes, Oliver Rhodes, University of Manchester

## Student Talks and Poster Sessions

![During the two poster sessions, the attending Master's and PhD students presented their recent work in neuroscience, neuromorphic computing and machine learning](/img/hbp-summer-school/poster.jpg)

![Each of the over 50 attendees had a three minutes timeslots for presenting recent work](/img/hbp-summer-school/presentation.jpg)

*Steffen Schneider*



## References

[1] Petrovici, M. A. (2015). Form vs. Function: Theory and Models for Neuronal Substrates. Universität Heidelberg.

[2] Petrovici, M. A., Leng, L., Stöckel, D., Breitwieser, O., Bytschok, I., Jordan, J., … Meier, K. (n.d.). Stochastic inference with deterministic spiking neurons. Retrieved from http://neuroscience.berkeley.edu/wp-content/uploads/2016/05/Mihai_Petrovici_talk.pdf

[3] O ’connor, P., & Welling, M. (n.d.). Deep Spiking Networks. Retrieved from https://arxiv.org/pdf/1602.08323.pdf

[4] Indiveri, G., Corradi, F., & Qiao, N. (n.d.). Neuromorphic Architectures for Spiking Deep Neural Networks. Retrieved from http://ncs.ethz.ch/pubs/pdf/Indiveri_etal15.pdf

[5] Brüderle, D., Petrovici, M. A., Vogginger, B., Ehrlich, M., Pfeil, T., Millner, S., … Potjans, T. C. (2011). A comprehensive workflow for general-purpose neural modeling with highly configurable neuromorphic hardware systems. Biol Cybern, 104(104). https://doi.org/10.1007/s00422-011-0435-9

[6] Leng, L., Petrovici, M., Martel, R., Bytschok, I., Breitwieser, O., Bill, J., … Meier, K. (2015). Spiking neural networks as superior generative and discriminative models. Retrieved from http://www.kip.uni-heidelberg.de/Veroeffentlichungen/download.php/5684/temp/3279.pdf

[7] Starkweather, C. K., Babayan, B. M., Uchida, N., & Gershman, S. J. (2017). Dopamine reward prediction errors reflect hidden-state inference across time. Nature Neuroscience. https://doi.org/10.1038/nn.4520
