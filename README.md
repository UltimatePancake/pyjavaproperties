# pyjavaproperties

This is a "fork" of https://pypi.org/project/pyjavaproperties/. I haven't located the original source and made some changes so that this would work on py3.

As per the pypi project the was hosted here: <http://bitbucket.org/jnoller/pyjavaproperties/>

# Installation

```
pip install git+https://github.com/UltimatePancake/pyjavaproperties
```

# Usage

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

# About

This is a “fork” of the “python replacement for java.util.Properties” recipe on ASPN: <http://code.activestate.com/recipes/496795/> and uploaded by Anand Balachandran Pillai.

The project is maintained by Jesse Noller <jnoller@gmail.com>, Anand Pilla <abpillai@gmail.com>.

# License

As with all ASPN recipes not otherwise licensed prior to July 15, 2008 on aspn.activestate.com, the original recipe is under PSF License. For more information, see the ASPN terms of service here:

<http://code.activestate.com/help/terms/>

While the licensing under the PSF license is sub-optimal, it is what it is. See <http://docs.python.org/license.html> for more information about the PSF license.
