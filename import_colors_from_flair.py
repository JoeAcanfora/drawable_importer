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

with open (file_name) as json_data:
    data = json.load(json_data)
    colors = data['colors']
    for colorKey, colorValue in colors.iteritems():
        for styleKey, styleValue in colorValue.iteritems():

            rawColor = str(styleValue)
            rawColor = rawColor.replace('rgba(', '').replace(')', '')

            r = Decimal(rawColor.split(',')[0]) * 255
            g = Decimal(rawColor.split(',')[1]) * 255
            b = Decimal(rawColor.split(',')[2]) * 255
            a = Decimal(rawColor.split(',')[3])

            hexValue = rgba2hex(r, g, b, a)

            print '<color name="' + colorKey + "_" + styleKey + '">' + hexValue + '</color>'
