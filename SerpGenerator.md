#使用方法
###1.将待处理的serp html文件与python文件放置到同一文件夹下
###2.python SerpGenerator.py [name] [mode]

#参数说明
###name: html文件的文件名（不要带上'.html'）
###model:0到3， 奇数表明 保留原有的question ; 偶数表明去除原question ,(1x)2表明serp为good quality, (0x)2表明serp为bad quality ,二进制首位仅用于新serp的命名。