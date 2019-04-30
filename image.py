#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fractions
import numpy as np
import matplotlib.pyplot as plt


def box(ax, x, y, w, h, *args, **kwargs):
    ax.plot([x, x+w, x+w, x, x], [y, y, y+h, y+h ,y], *args, **kwargs)

def draw2D():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for r in range(8):
        for c in range(2 ** r):
            x, y = c/2**r, 1/ 2**(r+1)
            w = 1/2**r
            h = w/2
            box(ax, x, y, w, h, color='k')

    # ax.set_axis_off()
    ax.set_frame_on(False)


    from matplotlib.ticker import FuncFormatter, MaxNLocator

    def format_x(tick_val, tick_pos):
        return str(fractions.Fraction(tick_val))


    ax.xaxis.set_major_formatter(FuncFormatter(format_x))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks([c/2**3 for c in range(2 ** 3+1)])

    def format_y(tick_val, tick_pos):
        return str(fractions.Fraction(tick_val))

    ax.yaxis.set_major_formatter(FuncFormatter(format_y))
    ax.yaxis.set_major_locator(MaxNLocator())

    ax.set_yticks([0] + [1/2**(3-r) for r in range(4)])
    plt.savefig('../images/semiring.jpg')


o=np.zeros(5)
def devide(a=0, b=1, y=0, n=0, ax=None):
    ax.plot(np.linspace(a,b,5), o+y, '-+k')
    h = (b-a)/4
    if (b-a)<=1/(4**n)+0.0001:
        m = n+1
        ax.text(a+h/2, y+0.05, r'$\frac{1}{%d}$' % (2**m))
        ax.text(a+h*5/2, y+0.05, r'$\frac{1}{%d}$' % (2**m))
        ax.text(a+h*3/2, y+0.05, '0')
        ax.text(a+h*7/2, y+0.05, '0')
    else:
        devide(a, a+h, y=y, n=n, ax=ax)
        devide(a+2*h, a+3*h, y=y, n=n, ax=ax)

def draw1D():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_axis_off()
    ax.set_frame_on(False)
    ax.plot(np.linspace(0,1,2), np.zeros(2)+0.6, '-+k')
    ax.text(0.5, .65, '1')
    devide(y=0.3,n=0,  ax=ax)
    devide(y=0, n=1, ax=ax)
    devide(y=-.3, n=2, ax=ax)

    ax.text(0.5, -.4, r'$\vdots$')
    plt.savefig('../images/semiring2.jpg')

draw1D()