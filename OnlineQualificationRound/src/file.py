from photo import Photo
from typing import List, Dict

class File:
    def __init__(self,
                 num_photos: int,
                 photos: dict,
                 global_tags: dict):
        self.num_photos = num_photos
        self.photos = photos
        self.global_tags = global_tags

def read_input_file(filename: str) -> File:
    """Reads the input of a Pizza problem.

    returns:

    R: number of Rows of pizza grid
    C: number of Cols of pizza grid
    L: Lowest number of each ingredients per slice
    H: Highest number of cells per slice
    pizza: the pizza grid (1 == tomato, 0 == mushroom)
    """
    lines = open(filename).readlines()
    total_photos = int(lines[0])
    photos = {}
    global_tags = {}
    for i in range(total_photos):
        params = lines[1+i].split()
        orient, num_tags, tags = params[0], int(params[1]), params[2:]
        mapped_tags = []
        for tag in tags:
            if tag in global_tags:
                mapped_tags.append(global_tags[tag])
            else:
                global_tags[tag] = len(global_tags)
        assert len(tags) == num_tags
        photos[i] = Photo(id=i, orient=orient, tags=tags)
    # print(photos)
    print(f'{filename} read file, total tags: {len(global_tags)}, total photos: {total_photos}')
    return File(num_photos=total_photos, photos=photos, global_tags=global_tags)

