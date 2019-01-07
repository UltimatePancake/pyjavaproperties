# pyjavaproperties

This is a "fork" of https://pypi.org/project/pyjavaproperties/. I haven't located the original source and made some changes so that this would work on py3.

# usage

```py
from pyjavaproperties import Properties
p = Properties()
p.load(open('test2.properties'))
p.list()
print p
print p.items()
print p['name3']
p['name3'] = 'changed = value'
print p['name3']
p['new key'] = 'new value'
p.store(open('test2.properties','w'))
```
