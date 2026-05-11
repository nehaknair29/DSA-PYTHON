student={"name":"Arul",'age':29}
print(student["name"])
print(student.get('age'))

dict={'Name':'Silpa','Age':19,'Section':'J'}
print(dict.keys())
print(dict.values())
print(dict['Name'])
print(dict['Age'])
print(dict['Section'])
print(dict.get('Section'))
dict['Mark']=99
dict['Age']=18
print(dict)
#deleting a key value results to deletion of that key value pair
del student['age']
print(student)

print(dict.items())
#dict.pop('a') - removes and returns vakue of a key
#dict.popitem() - removes the last inserted item
#dict.setdefault('<key>':'<value>') - returns value of a key,insert if missing
dict.setdefault('BG','A+')
print(dict)
dict.popitem()
print(dict)
d=dict.copy()
print(d)
d.clear()
print(d)
d=dict.copy()
print(d.pop('Mark'))
print("\n")

s={'Name':'Arun','Age':20,'Dept.':'CSE'}
print(s.get('Dept.'))
di={'Year':'2029'}
s.update(di)
print(s)
s.pop('Dept.')
print(s)
s.popitem()
print(s)
print(s.keys())
print(s.values())
print(s.items())
dic=s.copy()
print(dic)
s.clear()
print(s)
print('\n')        

p={'Pen':10,'Pencil':5,'Book':50}
p.setdefault('Eraser',7)
print(p)
a={'Book':55}
p.update(a)
print(p)
print(p.get('Pen'))
cp=p.copy()
print(p)
print(cp)

