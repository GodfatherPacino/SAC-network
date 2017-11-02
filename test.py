# !/usr/bin/python27
# coding: utf8

# ****************for bc stim con to sac
import hocmidp
import warnings
import numpy as np
from countcon import segname
warnings.filterwarnings("ignore")
lst1 = []
lst2 = []
lst3 = []
seg1 = hocmidp.hocmidp('sac1.hoc')
for node in seg1:
    if node[0] > 70 and node[0] < 75:
        lst1.append(seg1.index(node))
    elif node[0] < 70:
        lst2.append(seg1.index(node))
    elif node[0] < 170:
        lst3.append(seg1.index(node))

print segname(172)
# for i in lst1:
#     print "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(i)
#     print "\tsyn.e = 0"
#     print "\tsoma netcon = new NetCon (&v(.5), syn)"
#     print "\tnetcon.weight = 23e-5"
#     print "\tbslist.append(netcon)"

# for i in lst2:
#     print "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(i)
#     print "\tsyn.e = 0"
#     print "\tsoma1 netcon = new NetCon (&v(.5), syn)"
#     print "\tnetcon.weight = 23e-5"
#     print "\tbslist1.append(netcon)"
#
# for i in lst3:
#     print "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(i)
#     print "\tsyn.e = 0"
#     print "\tsoma2 netcon = new NetCon (&v(.5), syn)"
#     print "\tnetcon.weight = 23e-5"
#     print "\tbslist2.append(netcon)"






# origin = np.array([20, 0, 0])
# num = 0
# lst1 = []
# lst2 = []
# for node in seg1:
#     i = seg1.index(node)
#     node = np.array(node)
#     if np.sqrt(np.sum((node - origin)**2)) < 50 :
#         lst1.append(segname(i))
#     elif np.sqrt(np.sum((node - origin)**2)) < 100 :
#         lst2.append(segname(i))
    # print node - origin
    # print (node - origin)**2
    # print np.sum((node - origin)**2)
    # print np.sqrt(np.sum((node - origin)**2))

# print len(lst1), len(lst2)
    #     print segname(i)
    #     print "\tSAC[1].%s syn = new Exp2Syn(0.5)" % segname(i)
    #     print "\tsyn.e = 0"
    #     print "\tsoma netcon = new NetCon (&v(.5), syn)"
    #     print "\tbslist.append(netcon)"
# ****************************************************




