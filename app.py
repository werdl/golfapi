N,M,L,H,G,B='POST','uuid','GET','r','w',open
from flask import request as J,jsonify as E,Flask
import json as A,os,requests
from uuid import uuid4 as K
F=Flask(__name__)
C='i'
D='c'
if not os.path.exists(C):
	with B(C,G)as I:A.dump([],I)
if not os.path.exists(D):
	with B(D,G)as I:A.dump([],I)
@F.route('/i',methods=[L])
def O():
	with B(C,H)as D:F=A.load(D)
	return E(F)
@F.route('/i',methods=[N])
def P():
	D=J.json;D[M]=str(K())
	with B(C,H)as F:I=A.load(F)
	I.append(D)
	with B(C,G)as F:A.dump(I,F)
	return E(D)
@F.route('/c',methods=[L])
def Q():
	with B(D,H)as C:F=A.load(C)
	return E(F)
@F.route('/c',methods=[N])
def R():
	C=J.json;C[M]=str(K())
	with B(D,H)as F:I=A.load(F);I.append(C)
	with B(D,G)as F:A.dump(I,F)
	return E(C)
from flask import request as J,jsonify as E,Flask
import json as A,os,requests
from uuid import uuid4 as K