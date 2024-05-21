import os

from os import path
from wordcloud import WordCloud
#%%
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'research.txt')).read()
print(text)
#%%
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(18, 3), dpi=300)
wordcloud = WordCloud(background_color='white',margin=0, max_words=50, width=1800, height=256, min_font_size=20, max_font_size=80).generate(text)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.savefig('images/about2.png')

