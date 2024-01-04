class Colours:
    darkGrey = (26, 31, 40)    
    darkBlue = (44, 44, 107)
    lightGrey = (36, 44, 59)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    @classmethod
    def get_cell_colours(cls):
        return [cls.lightGrey, cls.red, cls.orange, cls.yellow, cls.green, cls.blue, cls.purple]    #Assign indexes to each colour
    
    @classmethod
    def get_keypeg_colours(cls):
        return [cls.lightGrey, cls.orange, cls.green]