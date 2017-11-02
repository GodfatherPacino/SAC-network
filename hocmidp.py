# !/usr/bin/python27
# coding: utf8

import re
from midpoint import midp


# f = open('E:\\test\\sac2.hoc', 'r')
# axon = ['0' for n in range(166)]
# dend = ['0' for n in range(29)]
# apic = ['0' for n in range(67)]


def compute_mid():
    lst1 = []
    global f
    #global filepoint
    #f.seek(filepoint, 0)
    charl = f.readline()
    chars = ''.join(charl)
    charspattern1 = re.compile(r'.*\}')  # charspattern1: }
    m1 = re.match(charspattern1, chars)
    while not m1:
        p3dadd = re.compile('.*pt3dadd.*')
        if re.search(p3dadd, chars):
            m = re.match(r'.+pt3dadd\((.+)\)', chars)
            lst = m.group(1).split(', ')
            lst = lst[:3]
            lst1.append(lst)
        charl = f.readline()
        chars = ''.join(charl)
        m1 = re.match(charspattern1, chars)
    #filepoint = f.tell()
    return midp(lst1[:])


def hocmidp(filename):
    global f
    global dend
    global axon
    global apic
    axon = ['0' for n in range(166)]
    dend = ['0' for n in range(29)]
    apic = ['0' for n in range(67)]
    fn = 'E:\\test\\%s' % filename
    print fn
    f = open(fn, 'r')
    try:
        while True :
            #global filepoint
            charl = f.readline()
            if '' == charl:
                break
            chars = ''.join(charl)
            chars = chars.replace(' ', '')
            charspattern = re.compile(r'''
                        (dend|axon|apic)
                        (\[.+\])?  #[count]
                        \{pt3dclear\(\)
                        ''', re.VERBOSE)
            s = re.search(charspattern, chars)
            if s :
                # print "found it!"
                # print '%-40s # %i' % (chars. num)
                m = re.match(charspattern,chars)
                if m.group(1) == 'dend':
                    s = re.compile(r'\[.+\]')
                    try:
                        if re.match(s, m.group(2)):
                            i = m.group(2).lstrip('\[')
                            i = i.rstrip('\]')
                            i = int(i)
                            #print i
                            dend[i] = compute_mid()
                    except TypeError:
                        dend[0] = compute_mid()
                        # lst1 = []
                        # charl = f.readline()
                        # chars = ''.join(charl)
                        # charspattern1 = re.compile(r'\.\}')     #charspattern1: }
                        # m1 = re.match(charspattern1,chars)
                        # while not m1:
                        #     p3dadd = re.compile('pt3dadd')
                        #     if re.search(p3dadd,chars):
                        #         m = re.match(r'/.+pt3dadd\((\.+)\)')
                        #         lst = m.group(1).split(', ').pop()
                        #         lst1.append(lst)
                        #     charl = f.readline()
                        #     chars = ''.join(charl)
                        #     m1 = re.match(charspattern1, chars)
                        # dend[i] = midp(lst1)
                elif m.group(1) == 'axon':
                    s = re.compile(r'\[.+\]')
                    try:
                        if re.match(s, m.group(2)):
                            i = m.group(2).lstrip('\[')
                            i = i.rstrip('\]')
                            i = int(i)
                            axon[i] = compute_mid()
                    except TypeError:
                        axon[0] = compute_mid()
                elif m.group(1) == 'apic':
                    s = re.compile(r'\[.+\]')
                    try:
                        if re.match(s, m.group(2)):
                            i = m.group(2).lstrip('\[')
                            i = i.rstrip('\]')
                            i = int(i)
                            apic[i] = compute_mid()
                    except TypeError:
                        apic[0] = compute_mid()
    finally:
        f.close()
    for i in range(len(dend)):
        dend[i] = dend[i].tolist()
    for i in range(len(axon)):
        axon[i] = axon[i].tolist()
    for i in range(len(apic)):
        apic[i] = apic[i].tolist()
    ret = dend[:]
    ret.extend(apic)
    ret.extend(axon)
    # print dend
    # print apic
    return ret

if __name__ == "__main__":
    print ('This is main of module "hocmidp.py"')
    print hocmidp('sac1.hoc')









