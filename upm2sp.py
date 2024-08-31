
def upm2sp(upm):
    return upm/250

def point2sp(x_upm, y_upm):
    return (upm2sp(x_upm), upm2sp(y_upm))

def generate_bBox_JSON(glyph, ne_upm, sw_upm):
    ne_sp = point2sp(*ne_upm)
    sw_sp = point2sp(*sw_upm)
    print(f'"{glyph}": {{\n    "bBoxNE": [\n        {ne_sp[0]},\n        {ne_sp[1]}\n    ],\n    "bBoxSW": [\n        {sw_sp[0]},\n        {sw_sp[1]}\n    ]\n}},')

if __name__=="__main__":
    generate_bBox_JSON('glyph', (1000, 500), (0.0, 0.0))