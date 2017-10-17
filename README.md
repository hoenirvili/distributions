# distributions

[![Build Status](https://travis-ci.org/hoenirvili/distributions.svg?branch=master)](https://travis-ci.org/hoenirvili/distributions)

Simple package for computing different distributions

## Installation
```
    python setup.py install
```

## Run

```
$ distributions bernoulli 0.85

[[Distibutions]]
Mean: 0.85
Variance: 0.1275
Standard deviation: 0.3570714214271425
Cumulative distribution: 1.0
Probability mass function: 0.0
PMFS: [ 0.15  0.85]
```

## Plot the results

```bash
$ distribution --plot bernoulli 0.85
```

![bernoulli](doc/bernoulli.png)

