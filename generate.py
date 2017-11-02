# !/usr/bin/python27
# coding: utf8

import cPickle
from countcon import segname

lst12 = cPickle.load(open("E:\\test\\lst12.txt", "rb"))
lst13 = cPickle.load(open("E:\\test\\lst13.txt", "rb"))
lst14 = cPickle.load(open("E:\\test\\lst14.txt", "rb"))
lst15 = cPickle.load(open("E:\\test\\lst15.txt", "rb"))
lst16 = cPickle.load(open("E:\\test\\lst16.txt", "rb"))
lst17 = cPickle.load(open("E:\\test\\lst17.txt", "rb"))

# f = open("E:\\test\\result12.txt", "w+")
# for k in lst12:
#     print >> f, "\tSAC[2].%s syn = new Exp2Syn(0.5)" % segname(k[1])
#     print >> f, "\tsyn.e = -70"
#     print >> f, "\tSAC[1].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
#     print >> f, "\tnetcon.weight = 16e-5"
#     print >> f, "\tnclist1.append(netcon)"

f = open("E:\\test\\result13.txt", "w+")
for k in lst13:
    print >> f, "\tSAC[3].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[1].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist1.append(netcon)"

f = open("E:\\test\\result14.txt", "w+")
for k in lst14:
    print >> f, "\tSAC[4].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[1].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist1.append(netcon)"

f = open("E:\\test\\result15.txt", "w+")
for k in lst15:
    print >> f, "\tSAC[5].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[1].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist1.append(netcon)"

f = open("E:\\test\\result16.txt", "w+")
for k in lst16:
    print >> f, "\tSAC[6].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[1].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist1.append(netcon)"

f = open("E:\\test\\result17.txt", "w+")
for k in lst17:
    print >> f, "\tSAC[7].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[1].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist1.append(netcon)"

f = open("E:\\test\\result21.txt", "w+")
for k in lst15:
    print >> f, "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[2].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 8e-5"
    print >> f, "\tnclist2.append(netcon)"

f = open("E:\\test\\result23.txt", "w+")
for k in lst14:
    print >> f, "\tSAC[3].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[2].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist2.append(netcon)"

f = open("E:\\test\\result27.txt", "w+")
for k in lst16:
    print >> f, "\tSAC[7].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[2].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist2.append(netcon)"

f = open("E:\\test\\result31.txt", "w+")
for k in lst16:
    print >> f, "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[3].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 8e-5"
    print >> f, "\tnclist3.append(netcon)"

f = open("E:\\test\\result32.txt", "w+")
for k in lst17:
    print >> f, "\tSAC[2].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[3].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist3.append(netcon)"

f = open("E:\\test\\result34.txt", "w+")
for k in lst15:
    print >> f, "\tSAC[4].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[3].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist3.append(netcon)"

f = open("E:\\test\\result41.txt", "w+")
for k in lst17:
    print >> f, "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[4].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 8e-5"
    print >> f, "\tnclist4.append(netcon)"

f = open("E:\\test\\result43.txt", "w+")
for k in lst12:
    print >> f, "\tSAC[3].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[4].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist4.append(netcon)"

f = open("E:\\test\\result45.txt", "w+")
for k in lst16:
    print >> f, "\tSAC[5].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[4].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist4.append(netcon)"

f = open("E:\\test\\result51.txt", "w+")
for k in lst12:
    print >> f, "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[5].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 8e-5"
    print >> f, "\tnclist5.append(netcon)"

f = open("E:\\test\\result54.txt", "w+")
for k in lst13:
    print >> f, "\tSAC[4].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[5].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist5.append(netcon)"

f = open("E:\\test\\result56.txt", "w+")
for k in lst17:
    print >> f, "\tSAC[6].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[5].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist5.append(netcon)"

f = open("E:\\test\\result61.txt", "w+")
for k in lst13:
    print >> f, "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[6].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 8e-5"
    print >> f, "\tnclist6.append(netcon)"

f = open("E:\\test\\result65.txt", "w+")
for k in lst14:
    print >> f, "\tSAC[5].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[6].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist6.append(netcon)"

f = open("E:\\test\\result67.txt", "w+")
for k in lst12:
    print >> f, "\tSAC[7].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[6].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist6.append(netcon)"

f = open("E:\\test\\result71.txt", "w+")
for k in lst14:
    print >> f, "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[7].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 8e-5"
    print >> f, "\tnclist7.append(netcon)"

f = open("E:\\test\\result76.txt", "w+")
for k in lst15:
    print >> f, "\tSAC[6].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[7].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist7.append(netcon)"

f = open("E:\\test\\result72.txt", "w+")
for k in lst13:
    print >> f, "\tSAC[2].%s syn = new Exp2Syn(0.5)" % segname(k[1])
    print >> f, "\tsyn.e = -70"
    print >> f, "\tSAC[7].%s netcon = new NetCon (&v(.5), syn)" % segname(k[0])
    print >> f, "\tnetcon.weight = 16e-5"
    print >> f, "\tnclist7.append(netcon)"