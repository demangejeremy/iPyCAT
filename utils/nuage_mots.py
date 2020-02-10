import os
from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
def nuagesMots(link_txt, width, height, max_words, background_color):
    text = open(path.join(d, link_txt)).read()

    # Generate a word cloud image
    wordcloud = WordCloud(font_path=None, width=width, height=height, margin=2, ranks_only=None, prefer_horizontal=.9, mask=None, scale=1, color_func=None, max_words=max_words, min_font_size=4, stopwords=None, random_state=None, background_color=background_color, max_font_size=None, font_step=1, mode="RGB", relative_scaling='auto', regexp=None, collocations=True, colormap=None, normalize_plurals=True, contour_width=0, contour_color='black', repeat=False, include_numbers=False, min_word_length=0).generate(text)

    # The pil way (if you don't have matplotlib)
    image = wordcloud.to_image()
    image.show() 