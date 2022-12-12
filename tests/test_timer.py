import time
import pytest
from src.timer.Timer import Timer

class TestTimer:
    
    def test_instance(self):
        timer = Timer(1)
        assert isinstance(timer, Timer)
    
    def test_infinite(self):
        timer = Timer(-1)
        assert timer.duration == -1
        assert timer.not_expired is True
        
    def test_expired(self):
        timer = Timer(1)
        timer.explode()
        assert timer.expired is True
    
    def test_not_expired(self):
        timer = Timer(1)
        assert timer.not_expired is True
    
    def test_integer_timer(self):
        timer = Timer(10)
        assert timer.duration == 10
    
    def test_float_timer(self):
        timer = Timer(0.1)
        assert timer.duration == 0.1
    
    def test_add_duration_int(self):
        timer = Timer(5)
        timer.increment(5)
        assert timer.duration == 10
    
    def test_add_duration_float(self):
        timer = Timer(5)
        timer.increment(2.5)
        assert timer.duration == 7.5
    
    def test_reset(self):
        timer = Timer(5)
        time.sleep(1)
        timer.reset()
        assert int(timer.at) == 0
        
        
    def test_normal_usage_expired(self):
        timer = Timer(1)
        while timer.not_expired:
            time.sleep(.2)
            print('timer running...')
        assert timer.expired == True
        
    def test_normal_usage_not_expired(self):
        timer = Timer(1)
        while timer.not_expired:
            time.sleep(.2)
            break
        assert timer.not_expired == True