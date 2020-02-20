from typing import List

class Photo:
    def __init__(self,
                 id: int,
                 tags: List[int],
                 orient: str):
        self.id = id
        self.tags = set(tags)
        self.orient = orient

    def __str__(self):
        return (f'id:{self.id}\n'
              f'orient:{self.orient}\n'
              f'tags:{self.tags}\n'
              )