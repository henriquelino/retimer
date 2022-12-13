# retimer

 > A simple package to make retry loops easier

[![PyPI version][pypi-image]][pypi-url]
[![Build status][build-image]][build-url]
[![GitHub stars][stars-image]][stars-url]
[![Support Python versions][versions-image]][versions-url]



## Getting started

You can [get `retimer` from PyPI](https://pypi.org/project/retimer),
which means it's easily installable with `pip`:

```bash
python -m pip install retimer
```




## Example usage
Think of a scenario where you need to keep trying to do something for a range of time, usually you can write this:

```python
from time import perfcounter

timeout = 10
begin = perfcounter()
while percounter() - begin < timeout:
     # do something for 10 seconds
     
     if retry_doing_something:
         time.sleep(.5)
         continue
         
     if something_bad:
         break
         
     # all good
     break
     
if perfcounter - begin >= timeout:
    print(f"Could not do something after {timeout} seconds")
else:
    print("Success!")
```


Rewriting using this package becomes:
```python
from retimer import Timer
import time

timer = Timer(10)
while timer.not_expired:
    # do something for 10 seconds
    
    if retry_doing_something:
        time.sleep(.5)
        continue
        
    if something_bad:
        timer.explode()
    
    # all good
    break
    
if timer.expired:
    print(f"Could not do something after {timer.duration} seconds")
else:
    print("Success!")
    
```

Although both codes accomplish the same result, I personally find the second one more readable and shines when I need two or more chained loops

## Changelog

Refer to the [CHANGELOG.md](https://github.com/henriquelino/retimer/blob/main/CHANGELOG.md) file.



<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/retimer
[pypi-url]: https://pypi.org/project/retimer/

[build-image]: https://github.com/henriquelino/retimer/actions/workflows/build.yaml/badge.svg
[build-url]: https://github.com/henriquelino/retimer/actions/workflows/build.yaml

[stars-image]: https://img.shields.io/github/stars/henriquelino/retimer
[stars-url]: https://github.com/henriquelino/retimer

[stars-image]: https://img.shields.io/github/stars/henriquelino/retimer
[stars-url]: https://github.com/henriquelino/retimer

[versions-image]: https://img.shields.io/pypi/pyversions/retimer
[versions-url]: https://pypi.org/project/retimer/

