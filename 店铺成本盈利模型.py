# -*- coding: cp936-*-
print '店铺成本/盈利模型'
print '请输入店铺面积,店铺租金（rmb/平米/每月），物业费预算（rmb/平米）'
a=raw_input()
a=int(a)
b=raw_input()
b=int(b)
c=raw_input()
c=int(c)
DZ=(a*b)+(a*c)
print '店租为'
print DZ

print '人力工资预算，请输入工人数量，月平均工资'
gs=raw_input()
gs=int(gs)
gz=raw_input()
gz=int(gz)
r=gs*gz
print '人力预算为'
print r

print '采购预算,请输入日均采购数量,平均价格'
a=raw_input()
a=int(a)
b=raw_input()
b=int(b)
s=a*b
print 'cp936'
print '请输入一次性装修费用'
zxf=raw_input()
zxf=int(zxf)

print zxf

print '请输入座位数，桌数，上座率，营业时间，人均消费'

a=raw_input()
a=int(a)
b=raw_input()
b=int(b)
c=raw_input()
c=float(c)
d=raw_input()
d=int(d)
e=raw_input()
e=int(e)
x=a*b*c*d*e

print '营业额为'
print x
sl=0.17
print'每月利润为'
sf=x*sl
lirun=(x-sf-s)*30-r-DZ
print lirun
print '回本时间为'#前期总投入/每月利润#装修费，转让费'
huiben=zxf/lirun
print huiben
print huiben

print '参考'



