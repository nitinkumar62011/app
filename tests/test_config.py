import pytest
class NotINRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)
def test_generic():
    a=2
    with pytest.raises(NotINRange):
        if a<5:
            raise NotINRange