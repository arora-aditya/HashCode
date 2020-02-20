from typing import List
from photo import Photo

class Slide:
    def __init__(self,
                 photos: List[Photo],
                 tags: set):
        self.photos = photos
        self.tags = set(tags)

    @property
    def valid(self):
        orients = set()
        for photo in self.photos:
            orients.add(photo.orient)
        assert len(orients) == 1
        return len(orients) == 1

    def transition_score(self, next_slide):
        transition_scores = (
            len(self.tags & next_slide.tags),
            len(self.tags - next_slide.tags),
            len(next_slide.tags - self.tags)
        )
        return min(transition_scores)

    def __str__(self):
        return (f'valid:{self.valid}\n'
              f'orients:{[a.orient for a in self.photos]}\n'
              f'tags:{self.tags}\n'
              )