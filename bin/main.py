#!/usr/bin/env python3

import click
from distributions import *

@click.group()
@click.argument('p', type=float)
def bernoulli():
    pass

@bernoulli.command()
def bernoulli(p):
    """ compute the bernoulli distribution """
    d = Bernoulli(p)
    click.echo('Mean: %f' % d.mean())
    click.echo('Variance: %f' % d.variance())
    click.echo('Standard deviation: %f' % d.std())
    click.echo('Probability mass function: %f' % d.pmf())
    click.echo('Cumulative distribution function: %f' % d.cdf())
    pmfs = d.pmfs()
    click.echo('P(X=1): %f' % pmfs[0])
    click.echo('P(X=0): %f' % pmfs[1])

# @click.group()
# def binomial():
#     pass
#
# @binomial.command()
# @click.argument('-p', help="Probability number", type=float)
# @click.argument('-n', help="Number of tirals", type=int)
# @click.argument('-r', help="Number of successes among n trials", type=int)
# def binomial(r, n, p):
#     """ compute the binomial distribution """
#     d = Binomial(r, n, p)
#     click.echo('Mean: %f' % d.mean())
#     click.echo('Variance: %f' % d.variance())
#     click.echo('Standard deviation: %f' % d.std())
#     click.echo('Probability mass function: %f' % d.pmf())
#     click.echo('Cumulative distribution function: %f' % d.cdf())
#     pmfs = d.pmfs()
#     click.echo('{}'.format(pmfs))
#
if __name__ == "__main__":
    bernoulli()
