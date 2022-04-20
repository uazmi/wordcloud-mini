# Wordcloud Mini

# Membuat wordcloud sederhana dari hasil survei PC IMM BSKM (.txt)

# Melengkapi library/module yang ingin digunakan
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
from os import path

# Kode untuk generate wordcloud
if __name__ == '__main__':
    stopwords = set(STOPWORDS)
    stopwords.update(["yang", "saya", "dan", "jika", "akan", "dengan", "kamu", ".", ","])

    file = open("kepemimpinan.txt")
    line = file.read()
    words = line.split()
    for r in words:
        if not r in stopwords:
            appendFile = open("filteredtext.txt", "a")
            appendFile.write(" " + r)
            appendFile.close()
    with open("filteredtext.txt", "r") as txt_file:
        filteredtext = txt_file.read()

# Pengaturan Wordcloudnya

wordcloud = WordCloud(width=3000, height=2000, background_color="white", stopwords=stopwords).generate(filteredtext)

# Menampilkan WordCloud
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Menyimpan gambarnya
wordcloud.to_file("namagambar.png")

# Done
