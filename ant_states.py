from state import State

class Home(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Home")
        return super().update(object)
    
class Search(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Searching for food/water")
        return super().update(object)
    
class CarringFood(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Carring Food")
        return super().update(object)

class CarringWater(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Carring Water")
        return super().update(object)
    
class GoingHome(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        
    def update(self, object):
        print("Going Home")
        return super().update(object)
    