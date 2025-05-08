import numpy as np
import pytest
from disk import final_disk_speed

def test_height_negative():
    height = -1.0
    with pytest.raises(ValueError, match="Height cannot be negative"):
        final_disk_speed(height)

def test_height_zero(): 
    height = 0
    result = final_disk_speed(height)
    assert result == 0

def test_height_large():
    height = 100000.0
    expected = np.sqrt((4.0/3.0) * 9.81 * height)
    result = final_disk_speed(height)
    assert result == expected

def test_height_random():
    height = 7.0
    expected = np.sqrt((4.0/3.0) * 9.81 * height)
    result = final_disk_speed(height)
    assert result == expected

