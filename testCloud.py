import jieba    # 分词
from wordcloud import WordCloud   # 形成词云
from matplotlib import pyplot     # 绘图，数据可视化，生成图片
from PIL import Image       # 图像处理
import numpy       # 矩阵运算
import sqlite3     # 数据库
import re

# 准备词云所需的文字
conn = sqlite3.connect("豆瓣电影Top250.db")
cur = conn.cursor()
sql = '''select details from movie'''
cur = cur.execute(sql)
text = ''
for item in cur:   # 返回一个元组
    text = text + (item[0])
# print(text)
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
text = re.sub(reg, '', text)  # 将特殊符号和标点符号替换
conn.close()

cut = jieba.cut(text)   # 将文本分词
words = ' '.join(cut)
# print(words)
img = Image.open(r'.\static\assets\img\tree.jpg')    # 打开一张遮罩的图片，背景色必须是白色
img_array = numpy.array(img)     # 将一张图片转化为一个图片数组
cloud = WordCloud(
    background_color='white',   # 词云背景颜色
    mask=img_array,     # 形成的遮罩数组
    font_path='STXINGKA.TTF'   # 使用的字体 字体位置C:\windows\fonts\
)
cloud.generate_from_text(words)   # 引入切割好的文本


# 绘制图片
# fig = pyplot.figure(1)
pyplot.imshow(cloud)  # 导入需要生成词云的文字
pyplot.axis('off')   # 是否显示坐标轴
# pyplot.show()  # 显示生成的词云图片
pyplot.savefig(r'.\static\assets\img\words.jpg', dpi=500)  # dpi:设置图片清晰度