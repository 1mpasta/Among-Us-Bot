import cv2 as cv


class Vision():

    def GetLocationFromPicture(self, needle, haystack, method=cv.TM_CCOEFF_NORMED):

        result = cv.matchTemplate(haystack, needle, method)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        clickPoint = (max_loc[0] + int(needle.shape[1] / 2), max_loc[1] + int(needle.shape[0] / 2))

        return clickPoint

    def PixelMatchesColor(self, pixel, rgb):
        redOk = True if pixel[0] >= rgb[0] else False
        g = max(int(round(rgb[1] * 0.62162162162162)), 0)
        greenOk = True if pixel[1] == rgb[1] or pixel[1] in range(g - 1, g + 2) else False
        b = max(int(round(rgb[2] * 0.62162162162162)), 0)
        blueOk = True if pixel[2] == rgb[2] or pixel[2] in range(b - 1, b + 2) else False
        allOk = True if redOk == greenOk == blueOk == True else False
        if allOk:
            return True
        return False

    def ResizeToScreen(self, src, screenSize, percentage):
        size = (int(round(screenSize[0] * percentage[0])), int(round(screenSize[1] * percentage[1])))
        resized = cv.resize(src, size, cv.INTER_LINEAR)
        return resized
