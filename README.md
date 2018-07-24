# Project
正好这段时间对日语感兴趣，想看看日语常用的字有哪些，下载了一部夏目漱石的《我是猫》，统计一下常用字，应该只要学会最常用的1000个日语汉字也就够日常交流了吧，顺便学了python练练手
- text/chinese.txt是中文版，统计结果如下
![chinese](https://github.com/fanjingdan012/foreign-lan-learn/blob/master/doc/chinese.png)
- text/japanese.txt是中文版，统计结果如下
![japanese](https://github.com/fanjingdan012/foreign-lan-learn/blob/master/doc/japanese.png)
平假名最常用，还有一些事云出见之类的
# Code
- 用了`collections.Counter`进行统计
- `mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']`可以防止中文和日文产生乱码