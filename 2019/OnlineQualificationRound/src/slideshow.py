from file import File
from slide import Slide
from photo import Photo
from typing import List

from random import shuffle

from datetime import datetime

import os

class ArguementUndefinedError(Exception):
    pass

class Slideshow:
    def __init__(self,
                 file: File,
                 output_file_name:str):
        self.directory_name = f"output/output_{str(datetime.now()).replace(' ', '_')[:-7]}"
        # print(file.global_tags)
        try:
            os.mkdir(self.directory_name)
        except OSError:
            # Dir already exists
            pass
        print(f'zip -r {self.directory_name}/archive.zip __init__.py photo.py slide.py file.py slideshow.py main.py')
        self.num_photos = file.num_photos
        self.tag_to_id_map = file.tag_to_id_map
        self.photos_ids = file.photos.keys()
        self.photos = file.photos
        self.horizontal_photos = [self.photos[photo_id].id for photo_id in self.photos if self.photos[photo_id].orient == 'H']
        self.vertical_photos = [self.photos[photo_id].id for photo_id in self.photos if self.photos[photo_id].orient == 'V']
        self.sort_h = sorted(self.horizontal_photos)
        self.sort_v = sorted(self.vertical_photos)
        self.slides:List[Slide] = []
        self.filename = output_file_name

    @property
    def num_slides(self):
        return len(self.slides)

    @staticmethod
    def _score_helper(slides):
        if len(slides) <= 1:
            return 0
        else:
            score = 0
            for i in range(len(slides)-1):
                score += slides[i].transition_score(slides[i+1])
            return score

    def score(self):
        if len(self.slides) <= 1:
            return 0
        else:
            score = 0
            for i in range(len(self.slides) - 1):
                transition_scores = (len(self.slides[i].tags & self.slides[i + 1].tags),
                                     len(self.slides[i].tags - self.slides[i + 1].tags),
                                     len(self.slides[i + 1].tags - self.slides[i].tags)
                                     )
                score += min(transition_scores)
            return score

    def _construct_slide(self, photos):
        if isinstance(photos, Photo):
            return Slide([photos])
        elif isinstance(photos, list):
            return Slide(photos)
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

    def arrange2(self):
        d = self.tag_to_id_map
        # print(d)
        sorted_keys = sorted(d, key=lambda k: len(d[k]), reverse=True)
        # print(sorted_keys)
        hz, vt = set(), set()
        used = set()
        slide_temp = []
        vt_temp = []
        for key in sorted_keys:
            # print(key, d[key])
            for id in d[key]:
                if id not in used:
                    used.add(id)
                    # print(used)
                    if self.photos[id].orient == 'H':
                        slide_temp.append(Slide(photos = [self.photos[id]], tags=self.photos[id].tags))
                        assert id not in hz
                        hz.add(id)
                    else:
                        if len(vt) < 2:
                            vt_temp.append(id)
                        if len(vt) == 2:
                            photos = [self.photos[vt_temp[0]], self.photos[vt_temp[1]]]
                            slide_temp.append(
                                Slide(
                                    photos=photos,
                                    tags=photos[0].tags | photos[1].tags
                                )
                            )
                        assert id not in vt
                        vt.add(id)
        assert len(used) == len(self.vertical_photos) + len(self.horizontal_photos)
        assert len(vt) == len(self.vertical_photos)
        assert len(hz) == len(self.horizontal_photos)
        # print(hz, vt)
        self.horizontal_photos = list(hz)
        self.vertical_photos = list(vt)
        self.slides = slide_temp

    def arrange3(self):
        self.slides, optimal = self._bubble_sort()
        return optimal


    def _bubble_sort(self):
        slide_temp = self.slides
        optimal = True
        for i in range(len(slide_temp) - 1):
            orig_score, swap_score = 0, 0
            if (i > 0):
                orig_score += slide_temp[i-1].transition_score(slide_temp[i])
                swap_score += slide_temp[i-1].transition_score(slide_temp[i+1])
            if (i + 2 < len(slide_temp)):
                orig_score += slide_temp[i].transition_score(slide_temp[i+1])
                swap_score += slide_temp[i].transition_score(slide_temp[i+1])
            if swap_score > orig_score:
                slide_temp[i], slide_temp[i + 1] = slide_temp[i + 1], slide_temp[i]
                optimal = False
        return slide_temp, optimal

    def shuffle(self):
        shuffle(self.horizontal_photos), shuffle(self.vertical_photos)
        assert sorted(self.horizontal_photos) == self.sort_h
        assert sorted(self.vertical_photos) == self.sort_v

    def check(self):
        return True

    def to_file(self, approach: int):
        used_ids = {}
        line_no = 1
        with open(f'{self.directory_name}/{approach}__{self.filename}.txt', 'w+') as file:
            file.write(str(self.num_slides) + '\n')
            line_no += 1
            for slide in self.slides:
                for photo in slide.photos:
                    if photo.id in used_ids:
                        print(f'{photo.id} used on lines {used_ids[photo.id]} and {line_no}')
                    else:
                        used_ids[photo.id] = line_no
                st = ' '.join([str(photo.id) for photo in slide.photos]) + '\n'
                file.write(st)
                line_no += 1

#