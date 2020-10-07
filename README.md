# FuckWormKingTweetGen
一个池沼项目，用于帮助您生成冲🐍皇用的推特文本。

## 如何使用

`git clone 项目地址`

`pip install pyperclip`

`python main.py`

如果你看不懂以上内容，请参阅：[详细帮助](./How_To.md)

参数：
    - `-t`：设置 tags，将把你接下来输入的 tags 加入配置文件的 tags 列表
    - `-n`：后面跟一个数字，为你需要附带的 tags 数目，将修改配置文件中的相应值
    - `-p`：输出当前配置信息

## 能做什么

将你输入的文字加上从 tags 列表中随机选取的指定数量 tags，然后输出并放入你的剪贴板。

如果你的文本加上 tags 后会超长，则将会把文字切片，返回加上 tags（差不多）凑满字数限制的内容；接着按下 Enter，则会继续往下切片，直到你的文本被用完。

## License

[LICENSE](./LICENSE)