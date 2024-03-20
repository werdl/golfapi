from flask import request as J,jsonify as E,Flask as Z;import json as A,os,requests;from uuid import uuid4 as K;F,C,D,N,M,L,H,G,B=Z(__name__),'i','c','POST','uuid','GET','r','w',open
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