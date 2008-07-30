#! /usr/bin/env python
# -*- coding: utf-8 -*-
# filename: prova_leica.py
# Copyright 2008 Stefano Costa <steko@iosa.it>
# Under the GNU GPL 3 License

from output.dxf.sdxf import *
from models import tops

# read TS data

main = tops.LeicaTCR1205('/home/gqb/code/totalopenstation/models/leica_1205_1.txt')
main.parse_retrieve_data()
punti = main.points.list_to_tuple()


codici = set([ p[4] for p in punti ])

# create DXF

#Drawing
d=Drawing(layers=())
#tables
d.styles.append(Style())                #table styles
#d.styles.append(Style( name='GQB', height=0.04 ))
d.views.append(View('Normal'))          #table view
d.views.append(ViewByWindow('Window',leftBottom=(1,0),rightTop=(2,1)))  #idem

for n, i in enumerate(codici):
    name_p = "%s_PUNTI" % i
    name_q = "%s_QUOTE" % i
    name_n = "%s_NUMERI" % i
    d.append(Layer(name=name_p, color=n))
    d.append(Layer(name=name_q, color=n))
    d.append(Layer(name=name_n, color=n))

for p in punti:
    p_id, p_x, p_y, p_z, p_layer = p
    
    if p_layer < 1200:
        name_p = "%s_PUNTI" % p_layer
        name_q = "%s_QUOTE" % p_layer
        name_n = "%s_NUMERI" % p_layer
        
        # add point
        d.append(Point(points=[(p_x, p_y, 0)], layer=name_p, color=256))
        
        # add ID number
        d.append(Text(str(p_id),point=(p_x, p_y, 0), layer=name_n ))
        
        # add Z value
        d.append(Text(str(p_z), point=(p_x, p_y, 0), layer=name_q ))

d.saveas('leica.dxf')

