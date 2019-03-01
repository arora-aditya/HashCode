from sys import argv
from file import read_input_file
from slideshow import Slideshow

slides_list = {}
# for filename in ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']:

filename = argv[1]
file_object = read_input_file(f'../files/{filename}.txt')

slides = Slideshow(file_object, output_file_name=filename)
print(slides.directory_name)
slides.arrange2()
slides.to_file(approach=2)
print(f'Arrange 2 score: {slides.score()}')


try:
    tries = int(argv[2])
except:
    tries = 100

max_score = 0
slides_list[filename] = (slides, max_score)
for tr in range(tries):
    print(f'Progress: {round(tr/tries * 100, 2)}% - {max_score}' + ' '*80, end='\r')
    slides.arrange()
    score = slides.score()
    if score > max_score:
        max_score = score
        slides.to_file(approach=1)
        slides_list[filename] = (slides, max_score)
    slides.shuffle()
print(f'Arrange 1 score: {max_score}'+ ' '*80)

max_score = 0
tries = 10000
count = 0
for tr in range(tries):
    print(f'Progress: {round(tr/tries * 100, 2)}% - {max_score}' + ' '*80, end='\r')
    optimal = slides.arrange3()
    score = slides.score()
    if score > max_score:
        max_score = score
        slides.to_file(approach=3)
    if optimal:
        count += 1
        if count == 2:
            break
        else:
            slides.arrange2()
print(f'Arrange 3 score: {max_score}' + ' '*80)
