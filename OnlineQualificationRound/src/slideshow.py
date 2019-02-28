from file import read_input_file, File
from slide import Slide
from photo import Photo
from typing import List

from random import shuffle
from sys import argv

from datetime import datetime

import os

class ArguementUndefinedError(Exception):
    pass

class Slideshow:
    def __init__(self,
                 file: File,
                 output_file_name:str):
        self.directory_name = f"output_{str(datetime.now()).replace(' ', '_')[:-7]}"
        try:
            os.mkdir(self.directory_name)
        except OSError:
            # Dir already exists
            pass
        print(f'zip -r {self.directory_name}/archive.zip __init__.py photo.py slide.py file.py slideshow.py')
        self.num_photos = file.num_photos
        self.photos_ids = file.photos.keys()
        self.photos = file.photos
        print(file.photos[0], type(file.photos[0]), file.photos[0].orient)
        print()
        self.horizontal_photos = [photo.id for photo in self.photos if photo.orient == 'H']
        self.vertical_photos = [photo.id for photo in self.photos if photo.orient == 'V']
        self.slides:List[Slide] = []
        self.filename = output_file_name

    @property
    def num_slides(self):
        return len(self.slides)


    def score(self):
        if len(self.slides) <= 1:
            return 0
        else:
            score = 0
            for i in range(len(self.slides)-1):
                transition_scores = (len(self.slides[i].tags & self.slides[i+1].tags),
                                        len(self.slides[i].tags - self.slides[i+1].tags),
                                        len(self.slides[i+1].tags - self.slides[i].tags)
                                    )
                score += min(transition_scores)
            return score

    def _construct_slide(self, photos):
        if isinstance(photos, Photo):
            return Slide([photos])
        elif isinstance(photos, list):
            return Slide[photos]
        else:
            raise ArguementUndefinedError

    def arrange(self):
        # print(f'{filename} reached arrange')
        shuffle_horizontal, shuffle_vertical= self.horizontal_photos, self.vertical_photos
        slide_temp = []
        for photo_id in shuffle_horizontal:
            photo = self.photos[photo_id]
            slide_temp.append(Slide(photos = [photo], tags=photo.tags))
        for ix in range(0, len(shuffle_vertical), 2):
            photos = [self.photos[ix], self.photos[ix+1]]
            slide_temp.append(
                Slide(
                    photos = photos,
                    tags=photos[0].tags | photos[1].tags
                )
            )
        self.slides = slide_temp

    def shuffle(self):
        shuffle(self.horizontal_photos), shuffle(self.vertical_photos)


    def to_file(self):
        with open(f'{self.directory_name}/{self.filename}.txt', 'w') as file:
            file.write(str(self.num_slides) + '\n')
            for slide in self.slides:
                st = ' '.join([str(photo.id) for photo in slide.photos]) + '\n'
                file.write(st)

slides_list = {}
# for filename in ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']:

filename = argv[1]
file_object = read_input_file(f'../files/{filename}.txt')

slides = Slideshow(file_object, output_file_name=filename)
try:
    tries = int(argv[2])
except:
    tries = 10000
max_score = 0
print(slides.directory_name)
for tr in range(tries):
    print(f'current try {tr} - {max_score}', end='\r')
    slides.arrange()
    score = slides.score()
    if score > max_score:
        max_score = score
        slides.to_file()
        slides_list[filename] = (slides, score)
    slides.shuffle()
print(f'{filename} {slides_list[filename][1]}')

#