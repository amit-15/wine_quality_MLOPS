import pytest
class NotInRange(Exception):
    def __init__(self, massage = "value not in range"):
        self.massage = massage
        super().__init__(self.massage)


def test_generic():
    a= 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
    
