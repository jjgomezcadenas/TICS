import numpy as np
import pandas as pd
import os, sys

from scipy.linalg import norm

from  . system_of_units import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from typing import Tuple, List


def set_fonts(ax, fontsize=20):
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(fontsize)


def plot_hits3d(hits,
                autorange = True,
                weight    = 'energy',
                xrange    = (-500,500),
                yrange    = (-500,500),
                zrange    = (0,1000),
                figsize   = (7,5)):
    """
    Draw hits in a 3D graphics.
    (requires a structure --eg, DF-- with fields (x,y,z,energy))

    """
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    set_fonts(ax)
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_zlabel('Z (mm)')

    if not autorange:
        ax.set_xlim3d(*xrange)
        ax.set_ylim3d(*yrange)
        ax.set_zlim3d(*zrange)
    if weight == 'energy':
        p = ax.scatter(hits.x, hits.y, hits.z, cmap='coolwarm',
        c=(hits.energy / keV))
        cb = fig.colorbar(p, ax=ax)
        cb.set_label('Energy (keV)')
    elif weight == 'nhits':
        p = ax.scatter(hits.x, hits.y, hits.z, cmap='coolwarm',
        c=(hits.nhits))
        cb = fig.colorbar(p, ax=ax)
        cb.set_label('nhits in  voxel')
    else:
        print(f'option {weight} not implemented ')
        sys.exit(1)
    plt.show()


def sphere(r, x0, y0, z0):
    """
    defines a sphere with center (x0,y0,z0) and radius r
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    x[:] = x[:] + np.ones(x.shape[0]) * x0
    y[:] = y[:] + np.ones(y.shape[0]) * y0
    z[:] = z[:] + np.ones(z.shape[0]) * z0
    #y = y + np.ones(np.size(x)) * y0
    #z = z + np.ones(np.size(x)) * z0
    return x,y,z



def plot_gtrack(gt,
                rblob     = 5,
                autorange = True,
                weight    = 'energy',
                xrange    = (-500,500),
                yrange    = (-500,500),
                zrange    = (0,1000),
                figsize   = (14,10),
                fontsize  =10):
    """
    Draw a gtrack

    """

    def plot_extrema():
        ax.scatter(e1[0], e1[1], e1[2], marker="d", s=250, color='black')
        ax.scatter(e2[0], e2[1], e2[2], marker="d", s=250, color='black')

    def plot_blobs():
        ax.plot_surface(x1, y1, z1, color='g', alpha=0.1, linewidth=0, antialiased=False)
        ax.plot_surface(x2, y2, z2, color='g', alpha=0.1, linewidth=0, antialiased=False)

    hits = gt.voxels
    e1 = gt.extrema['e1']
    e2 = gt.extrema['e2']

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    set_fonts(ax, fontsize)
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_zlabel('Z (mm)')

    x1,y1,z1 = sphere(rblob, e1[0], e1[1], e1[2])
    x2,y2,z2 = sphere(rblob, e2[0], e2[1], e2[2])

    if not autorange:
        ax.set_xlim3d(*xrange)
        ax.set_ylim3d(*yrange)
        ax.set_zlim3d(*zrange)

    if weight == 'energy':
        p = ax.scatter(gt.voxels_df.x, gt.voxels_df.y, gt.voxels_df.z,
                       cmap='coolwarm', c=(gt.voxels_df.energy / keV))
        cb = fig.colorbar(p, ax=ax)
        cb.set_label('Energy (keV)')
        plot_extrema()
        plot_blobs()
    elif weight == 'nhits':
        p = ax.scatter(hits.x, hits.y, hits.z, cmap='coolwarm', c=(hits.nhits))
        cb = fig.colorbar(p, ax=ax)
        cb.set_label('nhits in  voxel')
        plot_extrema()
        plot_blobs()
    else:
        print(f'option {weight} not implemented ')
        sys.exit(1)

    #ax.xaxis.set_major_locator(LinearLocator(5))
    #ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))

    plt.show()


def plot_gtracks(gtrks, figsize   = (14,10), fontsize=10):
    """
    Draws several tracks each in a different color

    """
    def plot():
        ax.set_xlabel('X (mm)')
        ax.set_ylabel('Y (mm)')
        ax.set_zlabel('Z (mm)')
        p = ax.scatter(gt.voxels_df.x, gt.voxels_df.y, gt.voxels_df.z)

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    set_fonts(ax, fontsize)
    
    for gt in gtrks:
        if trackList == None:
            plot()
        else:
            print(gt.event_id)
            if gt.event_id in trackList:
                print("Plot!")
                plot()


    plt.show()
