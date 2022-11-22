class State:
    def __init__(self, name) -> None:
        self.name = name
        
    def enter(self):
        print(f'Entering {self.name}')
        
    def update(self, object):
        pass
    
    def exit(self):
        pass
    
class Transition:
    def __init__(self, _from, _to) -> None:
        self._from = _from
        self._to = _to
