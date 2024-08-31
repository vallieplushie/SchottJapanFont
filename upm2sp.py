
def upm2sp(upm):
    return upm/250

def point2sp(x_upm, y_upm):
    return (upm2sp(x_upm), upm2sp(y_upm))

"""
Prints the glyphbBoxes record for a glyph.
- glyph: string of the glyphname as defined by smufl
- ne_upm: float tuple, the coordinates in upm for the north east corner
- sw_upm: float tuple, the coordinates in upm for the north east corner
"""
def generate_bBox_JSON(glyph, ne_upm, sw_upm):
    ne_sp = point2sp(*ne_upm)
    sw_sp = point2sp(*sw_upm)
    print(f'"{glyph}": {{\n    "bBoxNE": [\n        {ne_sp[0]},\n        {ne_sp[1]}\n    ],\n    "bBoxSW": [\n        {sw_sp[0]},\n        {sw_sp[1]}\n    ]\n}},')

if __name__=="__main__":
    generate_bBox_JSON('glyph', (1000, 500), (0.0, 0.0))