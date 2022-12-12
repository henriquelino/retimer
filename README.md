
A simple package to make retry loops easier

### Usage:

```python
from retimer import Timer
import time

timer = Timer(10)
while timer.not_expired:
    # do something for 10 seconds
    
    if retry_doing_something:
                time.sleep(.5) # good if something is a request to a server or cpu intensive
        continue
    if something_bad:
        timer.explode()
    
    # all good so we break before timer expires
    break
    
if timer.expired:
    print("Could not do something after tried for 10 seconds")
else:
    print("Successfully did something after 10 seconds")
    
```
