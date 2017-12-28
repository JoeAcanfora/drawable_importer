import json
from decimal import Decimal
import math

file_name = '/Users/joeacanfora/Desktop/oa-assets/oa-flair.json'


def getTint(color, alpha):

    unrounded = (1 - alpha) + ( color)

    tmp = int(math.floor(unrounded))
    if (tmp > 255):
        return 255
    return tmp


def rgba2hex(r, g, b, a):
    return '#%02x%02x%02x' % (getTint(r, a), getTint(g, a), getTint(b, a))

def makeItem(itemName, itemValue):
    printable = '\t<item name="' + itemName + '">' + itemValue + '</item>'
    return printable

with open (file_name) as json_data:
    data = json.load(json_data)
    fontStyles = data['styles']
    for styleName, styleValue in fontStyles.iteritems():
        print '<style name="' + styleName + '" parent="fontStyle">'
        for fontKey, fontValue in styleValue.iteritems():


            fontName = ""
            fontSize = ""
            lineHeightMultiplier = 0.0

            if (type(fontValue) is dict):
                fontName = fontValue["fontName"]
                fontSize = fontValue["size"]
                print makeItem("android:textSize", str(fontSize) + "sp")
                print makeItem("fontPath", "fonts/" + fontName + ".otf")

            if (type(fontValue) is float):
                lineHeightMultiplier = fontValue
                print makeItem("android:lineSpacingMultiplier", str(lineHeightMultiplier))

        print "</style>\n"
