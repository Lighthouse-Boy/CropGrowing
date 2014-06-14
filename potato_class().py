

from CropGrow import *

class Potato(Crop):
    """A potato crop"""

    def __init__(self):
        #call the parent class
        super().__init__(1,3,6)
        self._type = "Potato"

    #overriding grow
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water >self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._growth == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing +=1
        self._update_status()
def main():
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow (potato_crop)
    print(potato_crop.report())

if __name__ == "__main__":
    main()
