import cv2 as cv

class Vision():
    
    def GetLocationFromPicture(self, needle, haystack, method=cv.TM_CCOEFF_NORMED):
        
        result = cv.matchTemplate(haystack, needle, method)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        clickPoint = (max_loc[0] + int(needle.shape[1] / 2), max_loc[1] + int(needle.shape[0] / 2))
        
        return clickPoint