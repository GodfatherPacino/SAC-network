# !/usr/bin/python27
# coding: utf8

from sklearn import neighbors
import hocmidp
import warnings
import cPickle
warnings.filterwarnings("ignore")

seg1 = hocmidp.hocmidp('sac1.hoc')
seg2 = hocmidp.hocmidp('sac2.hoc')
seg3 = hocmidp.hocmidp('sac3.hoc')
seg4 = hocmidp.hocmidp('sac4.hoc')
seg5 = hocmidp.hocmidp('sac5.hoc')
seg6 = hocmidp.hocmidp('sac6.hoc')
seg7 = hocmidp.hocmidp('sac7.hoc')

tocels = {}


def segname(i):
    if i in range(29):
        name = 'dend[%d]' % i
    elif i in range(29, 96):
        name = 'apic[%d]' % (i-29)
    elif i in range(96, 262):
        name = 'axon[%d]' % (i-96)
    else: print 'error'
    return name


def bt2(seg, k):
    global seg1
    global tocels
    num = 0
    lst = []
    for ele in seg1:
        j = seg1.index(ele)
        tem = seg[:]        ## very important here if there is no [:],see the list definition for detail
        tem[0:0] = [ele]
        tree = neighbors.KDTree(tem)
        i = tree.query_radius(tem[0], r=8.2, count_only=True)
        # if i > 1:
        #     if not tocels.has_key(segname(j)):
        #         tocels[segname(j)] = 1
        #     else:
        #         tocels[segname(j)] = tocels[segname(j)] + 1
        num = i + num
        ind = tree.query_radius(tem[0], r=8.2)
        ind = ind[0].tolist()
        for i in range(len(ind)):
            ind[i] = int(ind[i])-1
        del ind[ind.index(-1)]      # usable for segname()
        for k in ind:
            x = (j, k)
            lst.append(x)

    return lst

# num12 = bt2(seg2[:], 2)
# num13 = bt2(seg3[:], 3)
# num14 = bt2(seg4[:], 4)
# num15 = bt2(seg5[:], 5)
# num16 = bt2(seg6[:], 6)
# num17 = bt2(seg7[:], 7)
# print num12, num13, num14, num15, num16, num17
# print num12+num13+num14+num15+num16+num17
lst12 = bt2(seg2[:], 2)
lst13 = bt2(seg3[:], 3)
lst14 = bt2(seg4[:], 4)
lst15 = bt2(seg5[:], 5)
lst16 = bt2(seg6[:], 6)
lst17 = bt2(seg7[:], 7)

cPickle.dump(lst12, open("E:\\test\\lst12.txt", "wb"))
cPickle.dump(lst13, open("E:\\test\\lst13.txt", "wb"))
cPickle.dump(lst14, open("E:\\test\\lst14.txt", "wb"))
cPickle.dump(lst15, open("E:\\test\\lst15.txt", "wb"))
cPickle.dump(lst16, open("E:\\test\\lst16.txt", "wb"))
cPickle.dump(lst17, open("E:\\test\\lst17.txt", "wb"))


# i = 0
# for k in tocels:
#     if tocels[k] > 3 :
#         i = i + 1
#         print tocels[k]
# print i
# print len(tocels)

if __name__ == "__main__":
    print ('This is main of module "countcon.py"')
    bt2(seg2[:], 2)

