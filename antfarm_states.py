from state import State

class Empty(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Formigueiro Empty")
        return super().update(object)
    
class HasFood(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Has Food")
        return super().update(object)

class HasWater(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Has Water")
        return super().update(object)
    
class Spawn(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Spawning ant")
        return super().update(object)
    