# zeeklog2pandas  
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/stratosphereips/zeeklog2pandas/main)
[![CI](https://github.com/stratosphereips/zeeklog2pandas/actions/workflows/publish-to-test.yml/badge.svg)](https://github.com/stratosphereips/zeeklog2pandas/actions/workflows/docker-image.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/zeeklog2pandas)

Read Zeeek/Bro log and log.gz (even broken ones) into a Pandas Dataframe.  

## Installation
### With pip
To install `zeeklog2pandas`, run this command in your terminal:  
  
```bash
$ pip install zeeklog2pandas 
```

This is the preferred method to install `zeeklog2pandas`, as it will always install the most recent stable release.  
  
If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide ](http://docs.python-guide.org/en/latest/starting/installation/)can guide you through the process.  

### From sources
The sources for `zeeklog2pandas` can be downloaded from the [Github repo](https://github.com/stratosphereips/zeeklog2pandas).  

You can either clone the public repository:  
```bash
$ git clone git://github.com/stratosphereips/zeeklog2pandas
```
Or download the `tarball`:  
  
```bash
$ curl -OJL https://github.com/stratosphereips/zeeklog2pandas/tarball/main
```  
  
Once you have a copy of the source, you can install it with:  
  
```bash
$ python setup.py install
```

## Usage
### Reading a zeek log into a pandas DataFrame
To read a file, simply import the library and use the `read_zeek` function. 
```python
import pandas as pd
from zeeklog2pandas import read_zeek

df = read_zeek('conn.log')  # or conn.log.gz, it will be handled transparently
```

### Mapping column types.
The `read_zeek` function only parses the zeek log files, without do any explicit conversion. You will get a warning if the zeek columns have mixed types. Also you will need to convert the ts column to datetimes. You can do that easily using pandas `to_datetime` help.

```python
In [1]: pd.to_datetime(df.ts, unit='s')  
Out[1]:    
0     2022-07-05 12:11:45.286374144  
1     2022-07-05 12:11:45.286611968  
2     2022-07-05 12:11:45.286622976  
3     2022-07-05 12:11:45.286629888  
4     2022-07-05 12:11:45.286637056  
                  ...                
195   2022-07-05 12:11:45.865832192  
196   2022-07-05 12:11:45.865839104  
197   2022-07-05 12:11:45.866068992  
198   2022-07-05 12:11:45.866075904  
199   2022-07-05 12:11:45.866082816  
Name: ts, Length: 200, dtype: datetime64[ns]
```

### Merging rotated logs
The `read_zeek` function does not merge the rotated log files. So if you have a bunch of hourly rotated zeek logs, you can easily merged into a single DataFrame doing something like

```python
from os import scandir

dfs = []
s = scandir('2022-07-05/')
for f in s:
	if f.name.startswith('ssh.'):
		dfs.append(read_zeek(f.path))
df = pd.concat(dfs)
```

This will merge all the ssh logs. You can replace `ssh.` for `conn.` in order to have one DataFrame with all the conn log of that day.

You need to be sure that the DataFrames have always the same columns. Otherwise you can use some other pandas method like merge or join, but you will need to take care of how the non existing values in some columns are handled.

