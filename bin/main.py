#!/usr/bin/env python3

from distributions import Binomial


def main():
    d = Binomial(3, 5, 0.85)
    print("Mean {}".format(d.mean()))
    print("Variance {}".format(d.variance()))
    print("Standard deviation {}".format(d.std()))
    print("Probability mass function {}".format(d.pmf()))
    print("{}".format(d.pmfs()))
    d.plot()


if __name__ == "__main__":
    main()
