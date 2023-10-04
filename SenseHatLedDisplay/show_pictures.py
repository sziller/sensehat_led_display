def picture(**kwargs):
    coldict = kwargs['coldict']
    title = kwargs['title']
    image = IMAGES[title]
    return [coldict[_] for _ in image]


IMAGES = {
    "snail":
        [0, 0, 7, 7, 7, 7, 0, 0,
         0, 7, 0, 0, 0, 0, 7, 0,
         7, 0, 0, 7, 7, 0, 0, 7,
         7, 0, 7, 0, 0, 7, 0, 7,
         7, 0, 7, 0, 0, 7, 0, 7,
         7, 0, 7, 0, 7, 0, 0, 7,
         7, 0, 7, 0, 0, 0, 7, 0,
         7, 0, 0, 7, 7, 7, 0, 0],
    "heart":
        [0, 0, 7, 0, 0, 7, 0, 0,
         0, 7, 0, 7, 7, 0, 7, 0,
         7, 0, 0, 0, 0, 0, 0, 7,
         7, 0, 0, 0, 0, 0, 0, 7,
         7, 0, 0, 0, 0, 0, 0, 7,
         0, 7, 0, 0, 0, 0, 7, 0,
         0, 0, 7, 0, 0, 7, 0, 0,
         0, 0, 0, 7, 7, 0, 0, 0],
    "smiley":
        [0, 0, 7, 7, 7, 7, 0, 0,
         0, 7, 0, 0, 0, 0, 7, 0,
         7, 0, 0, 0, 0, 0, 0, 7,
         7, 0, 7, 0, 0, 7, 0, 7,
         7, 0, 0, 0, 0, 0, 0, 7,
         7, 0, 7, 7, 7, 7, 0, 7,
         0, 7, 0, 0, 0, 0, 7, 0,
         0, 0, 7, 7, 7, 7, 0, 0],
    "target":
        [0, 0, 7, 7, 7, 7, 0, 0,
         0, 7, 4, 4, 4, 4, 7, 0,
         7, 4, 4, 7, 7, 4, 4, 7,
         7, 4, 7, 4, 4, 7, 4, 7,
         7, 4, 7, 4, 4, 7, 4, 7,
         7, 4, 4, 7, 7, 4, 4, 7,
         0, 7, 4, 4, 4, 4, 7, 0,
         0, 0, 7, 7, 7, 7, 0, 0],
    "sun":
        [7, 0, 0, 0, 7, 0, 0, 7,
         0, 7, 0, 0, 4, 0, 7, 0,
         0, 0, 4, 7, 7, 4, 0, 0,
         7, 4, 7, 0, 0, 7, 0, 0,
         0, 0, 7, 0, 0, 7, 4, 7,
         0, 0, 4, 7, 7, 4, 0, 0,
         0, 7, 0, 4, 0, 0, 7, 0,
         7, 0, 0, 7, 0, 0, 0, 7]
    
}