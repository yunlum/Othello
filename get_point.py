# Yunlu Ma ID: 28072206

class Point:
    
    # This Class contains the useful information for each clicked point on Canvas
    
    def __init__(self, frac_x: float, frac_y: float,color:str):
        # The __init__() fuction set the x and y fractional coordinates, the row number, the col number
        # And the color for the point
        self._frac_x = frac_x
        self._frac_y = frac_y
        self._color = color
        self._row = 0
        self._col = 0


    def frac(self) -> (float, float):

        # Return the fractional coordinates for the point
        
        return (self._frac_x, self._frac_y)


    def pixel(self, width: float, height: float) -> (float, float):

        # Return the pixel coordinates for the point

        return (self._frac_x * width, self._frac_y * height)

    def color(self) -> str:

        # Return the color for the point
        
        if self._color == 'B':
            return "black"
        elif self._color == 'W':
            return "white"

    def add_row(self,row:int):

        # Add the row number to the class
        
        self._row = row
        

    def add_col(self,col:int):

        # Add the col number to the class
        
        self._col = col
        
        
def from_frac(frac_x: float, frac_y: float,color:str) -> Point:

    # Add the fractional coordinates and color to the class
    
    return Point(frac_x, frac_y,color)


def from_pixel(pixel_x: float, pixel_y: float, width: float, height: float,color:str) -> Point:

    # Add the fractional coordinates from the pixel coordinates and color to the class
    
    return Point(pixel_x / width, pixel_y / height,color)



