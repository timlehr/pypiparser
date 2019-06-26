# PyPiParser

Simple PyPI Package Index parser for index servers without XML / JSON API.

_Note: It's still very much a prototype and missing a lot of potentially cool features, 
since I wrote it with a specific project need in mind._

# Installation

via PIP

```
pip install pypiparser
```

# Usage

    from pypiparser import PackageIndex
    
    # create an index object to work with
    index = PackageIndex("http://pypi.example.com")
    
    # get simple index url / base url
    print index.index_url
    """ Result: http://pypi.example.com/simple """ 
    
    # check if a package is available on the index
    print index.provides_package("pyside2")
    """ Result: True """
    
    # get all available package versions from index
    print index.get_all_versions("pyside2")
    """ Result: 
    [<'pyside2' (Wheel, v5.9.0a1.dev1527518830, '<PackageIndex, 'http://pypi.example.com'>')>, 
    <'pyside2' (Wheel, v5.9.0a1.dev1527519010, '<PackageIndex, 'http://pypi.example.com'>')>, 
    <'pyside2' (Wheel, v5.9.0a1.dev1527519532, '<PackageIndex, 'http://pypi.example.com'>')>, 
    <'pyside2' (Wheel, v5.9.0a1.dev1527520114, '<PackageIndex, 'http://pypi.example.com'>')>, 
    <'pyside2' (Wheel, v5.9.0a1.dev1527520119, '<PackageIndex, 'http://pypi.example.com'>')>, 
    <'pyside2' (Wheel, v5.9.0a1.dev1527520955, '<PackageIndex, 'http://pypi.example.com'>')>] """
    
    
    # get the newest compatible version with my setup (filter=True)
    pkg = index.get_newest_version("pyside2", filter=True)
    print pkg
    """ Result: <'pyside2' (Wheel, v5.9.0a1.dev1527518830, '<PackageIndex, 'http://pypi.example.com'>')> """ 
    
    # access metadata
    print pkg.distribution
    print pkg.version
    """ Result: 
    pyside2
    5.9.0a1.dev1527518830
    """ 
    
    # access metadata as dict
    print pkg.as_dict()
    """ Result: 
    {'platform': u'linux_x86_64', 
    'url': 'http://pypi.example.com/packages/PySide2-5.9.0a1.dev1527518830-5.9.6-cp27-cp27mu-linux_x86_64.whl#md5=d87921063a3701e16478b7e0c2b09012', 
    'abi': u'cp27mu', 'python': u'cp27', 
    'version': u'5.9.0a1.dev1527518830', 
    'build': u'5.9.6', 'distribution': 'pyside2'}
    """ 


# Requirements

- [beautifulsoup](https://pypi.org/project/beautifulsoup4/) (MIT license)
- [requests](https://pypi.org/project/requests/) (Apache 2.0 license)

# Todo

- tarball / egg support