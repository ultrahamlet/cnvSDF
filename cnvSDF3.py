import json
import numpy as np
# rotation matrix
def rotate_x(deg):
    # degree to radian
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
    # rotate x
    R_x = np.matrix((
        (1, 0, 0),
        (0, C, -S),
        (0, S, C)
    ))
    return R_x

def rotate_y(deg):
    # degree to radian
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
    # rotate y
    R_y = np.matrix((
        (C, 0, S),
        (0, 1, 0),
        (-S, 0, 1)
    ))
    return R_y

def rotate_z(deg):
     # degree to radian
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
     # rotate z
    R_z = np.matrix((
        (C, -S, 0),
        (S, C, 0),
        (0, 0, 1)
    ))
    return R_z

def total(mf):
    #print(">>>> ",mf)
    global gcount
    global pcount
    #print('>>>> ',len(mf),mf)
    #
    prm = []
    if len(mf) > 1:
         #print('===> ', mf,len(mf))
         if not isinstance(mf[0], list):
            if mf[0] == 'ref':
                #print('>>>>  ',prim[mf[1]],' refnum = ', mf[1])
                prHead = prim[mf[1]][0]
                #prVal  = prim[mf[1]][0]
                prVal  = prim[mf[1]][1]

                if(prHead == 'pEllipsoid'):
                    spos = prVal.replace('Vector3','vec3')
                    prm.append('vec3 ElRa_' + str(gcount) + ' = ' + spos + ';')
                    gcount += 1
                if prHead == 'pBox':
                    spos = prVal.replace('Vector3','vec3')
                    prm.append('vec3 BoSi_' + str(gcount) + ' = ' + spos + ';')
                    gcount += 1
                if prHead == 'pCylinder':
                    val0 = str(float(prVal))
                    prm.append('float CyRa_' + str(gcount) + ' = ' + val0 + ';')
                    gcount += 1
                    #val1 = str(float(prim[1][2]))
                    val1  = str(float(prim[mf[1]][2]))
                    prm.append('float CyHe_' + str(gcount) + ' = ' + val1 + ';')
                    gcount += 1
                if prHead == 'pCone':
                    val0 = str(float(prVal))
                    #val1 = str(float(prVal))
                    prm.append('vec2 CoGe_' + str(gcount)  + ' = vec2(' + val0 + ' ,' + val0 +');')
                    gcount += 1
                    #val2 = str(float(prim[1][2]))
                    val1 = str(float(prim[mf[1]][2]))
                    prm.append('float CoHe_' + str(gcount) + ' = ' + val1 + ';')
                    gcount += 1
                for pm in prm:
                    print(pm)
                    #gcount += 

            #val1 = str(float(prim[1][2]))
            #prm.append('float CyHe_' + str(gcount) + ' = ' + val1 + ';')
            #gcount += 1
            if mf[0] == 'mTranslation':
            # get vector float value
                spos = mf[len(mf)-1].replace('Vector3(','') 
                spos = spos.replace(')','')
                u = spos.split(',')
                v0 = -float(u[0])
                v1 = -float(u[1])
                v2 = -float(u[2])
                # make vec3 TrIn_?? = .... format
                rt = 'vec3 TrIn_'+str(gcount) #header
                rt = rt + ' = vec3(' + str(v0) +' ,'+ str(v1) + ' ,'  + str(v2) + ');'
                print(rt)
                gcount += 1
            if mf[0] == 'mRotation':
                rv = mf[2]     #totatuon value
                rt = 'mat3 RoIn_'+str(gcount)
                #
                t = rv.replace('Vector3(','')
                t = t.replace(')','')
                u = t.split(',')
                # get float rotation value
                v0 = -float(u[0])
                v1 = -float(u[1])
                v2 = -float(u[2])
                #rot = rotate_x(v0)*rotate_z(v2)
                rot = rotate_x(v0)*rotate_y(v1)*rotate_z(v2)
                e = np.linalg.inv(rot) #inverse matrix
                # for output mat3
                strm = str(e)
                strm = strm.replace('[[' ,'mat3(')
                strm = strm.replace(']]' ,');')
                strm = strm.replace(' ' ,'_')
                strm = strm.replace('\n' ,'')
                strm = strm.replace(']_[' ,'_')
                strm = strm.replace('_' ,',')
                strm = strm.replace('(,' ,'( ')
        #
                while  ',,' in strm:
                    strm = strm.replace(',,' ,',')
                strm = strm.replace(',)' ,')')
                # print mat3
                print(rt,'=', strm)
                gcount += 1
            for mem in mf:
                if isinstance(mem, list):
                    for mm in mem:
                        #print('---> ',mm,len(mm))
                        total(mm)
            return
    else:
        return
    #print('here ---> ',mf)
    
    

    
# analyze operator_tree
def total2(mf):
    global gcount
    if len(mf) > 1:
        #print(len(mf[0]),len(mf), mf)
        if not isinstance(mf[0], list):
                #print(mf[0])
                if(mf[0] == 'oThicken'):
                    print('float ThTh_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                if(mf[0] == 'oSmoothUnion'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                if(mf[0] == 'oSmoothSubtraction'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1

        for mem in mf:
            if isinstance(mem, list):
                total2(mem)

global gcount
global pcount
gcount = 1
pcount = 0
#
#  main    
# read json file
f = open('sample.json', 'r')
json_dict = json.load(f)
prim = json_dict['primitives']
#j = 0
modi = json_dict['modifiers']
print('//----------------------------------------------------------------')
for md in  modi:
    total(md)
    #j += 1
opt = json_dict['operator_tree']
###    total2(a[0])
for op in  opt:
    total2(op)
print('//----------------------------------------------------------------')





