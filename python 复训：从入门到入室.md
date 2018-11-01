# python 复训：从入门到入室

学习目标：建立较为完善python知识体系；定位重难点并在文档和论坛中寻找答案；**新增：易错问题集**

## 目录

### 第 2 节课：数据类型和运算符

- 数据类型：整型、浮点型、布尔型、字符串、列表、元组、集合、字典
- 运算符：算术、赋值、比较、逻辑、成员、恒等运算符
- 内置函数、复合数据结构、类型转换
- 空格和样式指南

### 第 3 节课：控制流

- 条件语句
- 布尔表达式
- For 和 While 循环
- break 和 continue
- zip 和 enumerate
- 列表推导式

### 第 4 节课：函数

- 定义函数
- 变量作用域
- 文档
- Lambda 表达式
- 迭代器和生成器

### 第 5 节课：脚本

- Python 安装和环境设置
- 运行和编辑 Python 脚本
- 与用户输入交互
- 处理异常
- 读写文件
- 导入本地、标准和第三方模块
- 在解析器中进行实验

---

###初次见面：这些东西是什么？

在python中处理数据的三种方式：运算符、函数、方法

前两者都很清楚。方法与特定数据类型对象有关，也即是属于特定对象的函数。感觉上的一个区别是函数在头，方法往往跟在点号后面（）

![](https://i.imgur.com/kQk46Sm.jpg)

比如print是实用的内置函数。

### 变量命名避开

python[保留字符](https://pentangle.net/python/handbook/node52.html)：

- 数据类型：整型、浮点型、布尔型、字符串、列表、元组、集合、字典
- 运算符：算术、赋值、比较、逻辑、成员、恒等运算符
- 内置函数、复合数据结构、类型转换
- 空格和样式指南

###字符串、列表、元组、字典的玩法

列表、字符串和可变性

与 `string`、`float` 和 `int` 一样，`list` 也是一种类型。在我们看到的所有类型中，列表与字符串最为相似：这两种类型都支持索引、切片、`len` 函数和 `in` 运算符。表示对象可否修改的术语是**可变性**（Mutability）。列表是可变的，而字符串不可变。

##### Python 中 [format](https://blog.csdn.net/a359680405/article/details/42844443) 方法所做的事情便是将每个参数值替换至格式所在的位置。

字符串索引：first_word[0]

`len` 仅适用于“序列（例如字符串、字节、元组、列表或范围）或集合（例如字典、集合或冻结集合）

执行一个[字符串格式化](https://www.jianshu.com/p/0fd45ef0b040)操作。待被格式化的字符串中含有文本字符串个和用大括号{}中的将被替换的部分（replacement fields ）。每一个将被替换的部分都有一个在索引或者关键字参数。

1. 不需要理会数据类型的问题，在%方法中%s只能替代字符串类型

2. 单个参数可以多次输出，参数顺序可以不相同

3. 填充方式十分灵活，对齐方式十分强大

4. 官方推荐用的方式，%方式将会在后面的版本被淘汰

   ```python
   str1 = "I love beijing Tian'anmen"
   print(str1.split())
   print(str1.center(50,'*'))
   print(str1.count("love", 0,15))
   print(str1.encode(encoding='utf-8',errors='strict'))
   print("Hello {0},I am {1}".format("Tom","Kevin"))
   print(str1.replace("beijing","shanghai",1))
   ```

   [List to string](https://blog.csdn.net/kangkanglou/article/details/78836660):print("".join(a_list))

   ​	隐含知识点：[**map()** 函数](http://www.runoob.com/python/python-func-map.html)

   会根据提供的函数对指定序列做映射。

   `sentence1` 是一个字符串，因此是不可变对象。意味着虽然你可以引用 `sentence1` 中的单个对象（例如，可以写为 `sentence1[5]`），但是无法为它们赋值。


实用的列表函数

```python
# join是一个字符串方法，将字符串列表作为参数，并返回一个由列表元素组成并由分隔符字符串分隔的字符串。
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
#会将元素添加到列表末尾。
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
```

元组是另一个实用容器。它是一种不可变有序元素数据类型。通常用来存储相关的信息。请看看下面这个关于纬度和经度的示例：

```
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
```

元组还可以用来以紧凑的方式为多个变量赋值。

```
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
```

在文档里看到很多次iterable迭代，以及相关的概念iterator迭代器，专门查询一下，希望能弄清楚。Python中iterable被认为是一个对象，这个对象可以一次返回它的一个成员（也就是对象里面的元素），[由此可知](https://blog.csdn.net/asialee_bird/article/details/79574727)，Python中的string，list，tuple，dict，file，xrange都是可迭代的，都属于iterable对象，可迭代的对象都是可以遍历的，实际上Python中有很多iterable类型是使用iter()函数来生成的。

**集合**

**集合**是一个包含唯一元素的可变无序集合数据类型。集合的一个用途是快速删除列表中的重复项。

```
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

{1, 2, 3, 6}
```

另外和列表一样支持in运算符还有add\pop 增删方法。区别是集合是无序的。

**字典**

**字典**是可变数据类型，其中存储的是唯一键到值的映射。下面是存储元素和相应原子序数的字典。

```
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
```

```
print("carbon" in elements)
print(elements.get("dilithium"))
```

练习暴露对于字典的item不够熟悉。[文档](https://docs.python.org/3/library/stdtypes.html#lists)

```python
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
```

in和get在字典中查询值；另外恒等运算符is/is not

```
n = elements.get("dilithium")
print(n is None)
print(n is not None)
```

**字符串、列表、[元组](https://www.cnblogs.com/spiritman/p/5141824.html)、字典辨析**

字符串除了不能修改序列之外，可以视同列表处理。支持[下标索引](https://blog.csdn.net/tichimi3375/article/details/79638373)处理。

列表是可变的，里面的元素可以是字符串、整数、数组等等。之前对于列表元素的取出并不娴熟：比如cargo[0]

字典中的每项都包含两部分（键和值），字典中的项目是无序的，我们在这节课见到了嵌套字典示例。可以嵌套，不能用append增加。不可排序。 

集合是无序的，因此项目的出现顺序可能不一致，你可以使用 `.add` 向集合中添加项目。和字典及列表一样，集合是可变的。集合中不能有重复项，不能对集合排序。对于这两个属性，更适合使用列表。不可排序。

元组：有序不可变。以紧凑的方式为多个变量赋值。

切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。切片的语法：[起始:结束:步长]

![](https://ws2.sinaimg.cn/large/006tNc79ly1fvpi836tatj30ou0o8gms.jpg)

### 控制流：函数与循环

- 条件语句
- 布尔表达式
- For 和 While 循环
- Break 和 Continue
- Zip 和 Enumerate
- 列表推导式

**条件语句**：if 

**布尔表达式**：如果我们在`if` 语句中使用非布尔对象代替布尔表达式，Python 将检查其真假值，判断是否运行缩进代码。默认情况下，Python 中对象的真假值被视为 True，除非在文档中被指定为 False。

****

**For 和 While 循环**：Python 有两种类型的循环：`for` 循环和 `while` 循环。`for` 循环用来遍历**可迭代**对象。

**可迭代对象（iterable）**是每次可以返回其中一个元素的对象，包括字符串、列表和元组等序列类型，以及字典和文件等非序列类型。你还可以使用[迭代器和生成器](https://anandology.com/python-practice-book/iterators.html)定义可迭代对象。比如city in cities，这里city就是循环的迭代变量。

**比较生疏的点**：可以使用 `range` 函数为 `cities` 列表中的每个值生成索引。这样我们便可以使用 `cities[index]` 访问列表中的元素，以便直接修改 `cities` 列表中的值。

```python
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index]=usernames[index].lower().replace(" ","_")

print(usernames)
```

可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。可以使用isinstance()判断一个对象是否是Iterable对象

在 Python 中，我们可以使用列表来存储数据序列，并使用 for 循环来遍历列表。

1. 关键字 `for` 表示这是一个 for 循环。
2. 该行的其余部分表示正在迭代的内容。`names` 是这个 for 循环迭代的列表。`name` 是该循环的迭代变量。针对 `names` 中的每个元素， for 循环的主体都会被执行一次，迭代变量 `name` 可用于循环体，从而指代循环当前处理的元素。
3. for 循环的主体部分需要缩进四个空格，并针对列表中的每个元素执行一次。\

**薄弱环节**：字符串索引

```python
tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
```

For 循环是 "定迭代" 的一种，循环次数已经指定好：列表的 for 循环针对列表中的每个元素执行一次主体。使用 `range` 函数的 for 循环，其执行次数将由 range 函数调用指定。 

而"不定迭代" 不同，后者指循环重复未知次数，直到**满足**某些条件时循环才会结束。下面这个示例将模拟二十一点发牌，使用 while 循环将卡片牌堆拖到手牌中，在手牌的值大于或等于 17 时停止。

1. 关键字 `While` 表示这是一个 while 循环

2. 接下来是一个测试表达式，在该示例中表达式为 `sum(hand) <= 21`。如果表达式为真，将执行循环主体，之后将再次判断该表达式是否为真。这一过程重复判断测试表达式的真假，并运行循环主体，直到表达式变为 false。

3. 循环主体前需要缩进四个空格。循环主体应该以某种方式修改测试表达式中的变量。如果测试表达式的值没有改变，这将导致一个无限循环！在上面的示例中，循环主体将数字追加到了 `hand` 列表中，因此增加了 `sum(hand)` 的值。

   比如：最接近的平方数

   ```python
   limit = 40
   
   num = 0
   while (num+1)**2 < limit:
       num += 1
   nearest_square = num**2
   
   print(nearest_square)
   ```

`break` 停止：精确控制

For 循环迭代序列中的每个元素，而 while 循环在满足条件时停止迭代。在大多数情况下，这两种用法就已经足够了，但我们有时候需要更精确地控制循环何时结束。这时我们就需要使用关键字 `break` 了。

`continue` 跳过循环的一次迭代

`zip` 返回一个将多个可迭代对象组合成一个元组序列的迭代器。每个元组都包含所有可迭代对象中该位置的元素。例如，

`list(zip(['a', 'b', 'c'], [1, 2, 3]))` 将输出 `[('a', 1), ('b', 2), ('c', 3)]`.

正如 `range()` 一样，我们需要将其转换为列表或使用循环进行遍历以查看其中的元素。

你可以如下所示地用 `for` 循环拆封每个元组。

```python
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
```

除了可以将两个列表组合到一起之外，还可以使用星号拆封列表。

```
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
```

用zip进行转置实例：

```python
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
```

`enumerate` 是一个会返回元组迭代器的内置函数，这些元组包含列表的索引和值。当你需要在循环中获取可迭代对象的每个元素及其索引时，将经常用到该函数。

```
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
```

在 Python 中，你可以使用列表推导式快速简练地创建列表。借助列表推导式，我们可以使用 `for` 循环用一步创建一个列表。

我们使用方括号 `[]` 创建列表推导式，括号里包含要对可迭代对象中的每个元素进行评估的条件。上述列表推导式对 `cities` 中的每个元素 `city` 调用 `city.title()`，以为新列表 `capitalized_cities` 创建每个元素。

```python
capitalized_cities = [city.title() for city in cities]
```

```python
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```

### 函数

- 函数定义
- 变量作用域
- 文档
- Lambda 表达式
- 迭代器和生成器

Lambda 表达式

你可以使用 Lambda 表达式创建匿名函数，即没有名称的函数。lambda 表达式非常适合快速创建在代码中以后不会用到的函数。尤其对高阶函数或将其他函数作为参数的函数来说，非常实用。

我们可以使用 lambda 表达式将以下函数

```
def multiply(x, y):
    return x * y
```

简写为：

```
double = lambda x, y: x * y
```

```python
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)
```

`map()` 是一个高阶内置函数，接受函数和可迭代对象作为输入，并返回一个将该函数应用到可迭代对象的每个元素的迭代器。

`filter()` 是一个高阶内置函数，接受函数和可迭代对象作为输入，并返回一个由可迭代对象中的特定元素（该函数针对该元素会返回 True）组成的迭代器。

```python
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
```

**调用文件**

Python 提供了一个特殊的语法（with），该语法会在你使用完文件后自动关闭该文件。

```python
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
```

该 `with` 关键字使你能够打开文件，对文件执行操作，并在缩进代码（在此示例中是读取文件）执行之后自动关闭文件。现在，我们不需要调用 f.close() 了！你只能在此缩进块中访问文件对象 f。

**导入本地脚本**

在导入本地脚本的时候有个 `if main` 块，也就是说只导入主程序模块，而不是所有的代码。

为了避免运行从其他脚本中作为模块导入的脚本中的可执行语句，将这些行包含在 `if __name__ == "__main__"` 块中。或者，将它们包含在函数 main() 中并在 `if main`块中调用该函数。

但是很多时候并不需要自己造模块导入，因为python有一个强大的标准库。

###不用重复造轮子：标准库和扩展库

学过函数与循环之后。

程序员可以自己编写代码，而我们也有一些现成的代码可以解决常见的问题。我们将这些“现成的代码”称为 Python 标准库。Python 标准库是大量强大编程工具的集合，可为你在 Python 中编程提供帮助。从网络到数学统计，Python 标准库为一系列常见的专业任务提供新的对象类型和函数。其他程序员编写好的代码被放入有用的“模块”（module）中，以供你在自己的代码中访问和使用。

所以标准库就是大型公共函数集？import

为了使用 `factorial` 函数，我们需调用它，以模块名称 `math` 开始，然后是一个点符号 (`.`)，最后是函数名 `factorial()`

**推荐模块**

Python 标准库包含大量模块！为了帮助你熟悉那些实用的模块，我们在下面筛选了一些我们推荐的 Python 标准库模块并解释为何我们喜欢使用它们！

- [`csv`](https://docs.python.org/3/library/csv.html)：对于读取 csv 文件来说非常便利
- [`collections`](https://docs.python.org/3/library/collections.html)：常见数据类型的实用扩展，包括 `OrderedDict`、`defaultdict` 和 `namedtuple`
- [`random`](https://docs.python.org/3/library/random.html)：生成假随机数字，随机打乱序列并选择随机项
- [`string`](https://docs.python.org/3/library/string.html)：关于字符串的更多函数。此模块还包括实用的字母集合，例如 `string.digits`（包含所有字符都是有效数字的字符串）。
- [`re`](https://docs.python.org/3/library/re.html)：通过正则表达式在字符串中进行模式匹配：[正则表达式](http://www.runoob.com/regexp/regexp-syntax.html)(regular expression)描述了一种字符串匹配的模式（pattern），可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。感觉在搜索中常用。
- [`math`](https://docs.python.org/3/library/math.html)：一些标准数学函数
- [`os`](https://docs.python.org/3/library/os.html)：与操作系统交互
- [`os.path`](https://docs.python.org/3/library/os.path.html)：`os` 的子模块，用于操纵路径名称
- [`sys`](https://docs.python.org/3/library/sys.html)：直接使用 Python 解释器
- [`json`](https://docs.python.org/3/library/json.html)：适用于读写 json 文件（面向网络开发）

**模块、软件包和名称**

为了更好地管理代码，Standard 标准库中的模块被拆分成了子模块并包含在软件包中。**软件包**是一个包含子模块的模块。子模块使用普通的点记法指定。

子模块的指定方式是软件包名称、点，然后是子模块名称。你可以如下所示地导入子模块。

```python
import package_name.submodule_name
```

但标准库并不具有你想要的一切，它不支持某些太专业化的任务。但好在独立开发人员编写了成千上万个第三方库。有的程序员会把调用的库放在需求文件中，需要的话调用 pip install -r requirments.txt

# 实用的第三方软件包

能够安装并导入第三方库很有用，但是要成为优秀的程序员，还需要知道有哪些库可以使用。大家通常通过在线推荐或同事介绍了解实用的新库。如果你是一名 Python 编程新手，可能没有很多同事，因此为了帮助你了解入门信息，下面是优达学城工程师很喜欢使用的软件包列表。（可能部分网站在国内网络中无法打开）

- [IPython](https://ipython.org/) - 更好的交互式 Python 解释器
- [requests](http://docs.python-requests.org/) - 提供易于使用的方法来发出网络请求。适用于访问网络 API。
- [Flask](http://flask.pocoo.org/) - 一个小型框架，用于构建网络应用和 API。
- [Django](https://www.djangoproject.com/) - 一个功能更丰富的网络应用构建框架。Django 尤其适合设计复杂、内容丰富的网络应用。
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - 用于解析 HTML 并从中提取信息。适合网页数据抽取。
- [pytest](http://doc.pytest.org/) - 扩展了 Python 的内置断言，并且是最具单元性的模块。
- [PyYAML](http://pyyaml.org/wiki/PyYAML) - 用于读写 [YAML](https://en.wikipedia.org/wiki/YAML) 文件。
- [NumPy](http://www.numpy.org/) - 用于使用 Python 进行科学计算的最基本软件包。它包含一个强大的 N 维数组对象和实用的线性代数功能等。
- [pandas](http://pandas.pydata.org/) - 包含高性能、数据结构和数据分析工具的库。尤其是，pandas 提供 dataframe！
- [matplotlib](http://matplotlib.org/) - 二维绘制库，会生成达到发布标准的高品质图片，并且采用各种硬拷贝格式和交互式环境。
- [ggplot](http://ggplot.yhathq.com/) - 另一种二维绘制库，基于 R's ggplot2 库。
- [Pillow](https://python-pillow.org/) - Python 图片库可以向你的 Python 解释器添加图片处理功能。
- [pyglet](http://www.pyglet.org/) - 专门面向游戏开发的跨平台应用框架。
- [Pygame](http://www.pygame.org/) - 用于编写游戏的一系列 Python 模块。
- [pytz](http://pytz.sourceforge.net/) - Python 的世界时区定义。

---

###   错误集：

- [Python初学者错误](https://www.aliyun.com/jiaocheng/442683.html)：TypeError: unsupported operand type(s) for +: 'int' and 'str' 
- 对join不熟。前面应该加引号''.join(random.sample(word_list,3))

不熟悉的部分：

![](https://i.imgur.com/DxRzdMH.jpg)

诊断问题：

- 关于basemap升级引发的框架排雷

https://blog.csdn.net/sinat_18665801/article/details/82356988

- 关于导入csv文件的技法：

https://stackoverflow.com/questions/42165000/python-cannot-see-csv-file

- 没有登记agent去查原始的开发文档

https://github.com/geopy/geopy/blob/master/geopy/geocoders/osm.py

- 从字典里选出列表里的所有值

https://jingyan.baidu.com/article/0eb457e508b6d303f0a90572.html

- 以及basemap的x,y只接收list变量。https://blog.csdn.net/zm714981790/article/details/51224650/。

另外，此处进阶：如何调用API获取所有的坐标

- 读代码：center()方法语法。str.center(width[, fillchar])]

这样的写法其实并不复杂，要认识到方括号里是可以选择量的而已，可选可不选。

- 关于编码的疑惑。

```python
str.encode(encoding="utf-8", errors="strict")

这个看上去非常陌生，但实质上encode就是把字符串变为计算机可以识别但编码。相应但，decode就是把编码转换为字符串。binarys是二进制
```

```python
String.format(*args, **kwargs)
```

- 分割列表并取前半部

```python
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)
```

- 按照指定数字[分割列表](https://www.jb51.net/article/113149.htm)

我们可以使用内置函数 `input` 获取用户的原始输入，该函数接受一个可选字符串参数，用于指定在要求用户输入时向用户显示的消息。

```python
name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))
```

批量处理程序：

下面是实现该程序的一种方式！

```python
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
```

[异常和语法错误](https://docs.python.org/3/tutorial/errors.html)：**异常**是代码运行时发生的问题，而语法错误是 Python 在运行代码之前检查代码时发现的问题。

- 当 Python 无法解析代码时，就会发生**语法错误**，因为我们没有遵守正确的 Python 语法。当你出现拼写错误或第一次开始学习 Python 时，可能会遇到这些错误。
- 当在程序执行期间出现意外情况时，就会发生**异常**，即使代码在语法上正确无误。Python 有不同类型的内置异常，你可以在错误消息中查看系统抛出了什么异常。
- 如果你没有使用正确的语法，并且 Python 不知道如何运行你的代码，会发生语法错误。如果 Python 在执行代码时遇到意外情形，会发生异常，即使你采用了正确的语法，也可能会发生异常。

我们实际上可以指定要在 `except` 块中处理哪个错误，如下所示：

```python
try:
    # some code
except ValueError:
    # some code
```

现在它会捕获 ValueError 异常，但是不会捕获其他异常。如果我们希望该处理程序处理多种异常，我们可以在 `except` 后面添加异常元组。

```python
try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code
```

```python
def create_groups(items, num_groups):
    try:
        size = len(items) // num_groups
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(num_groups))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
```

如果没有要处理的具体错误，依然可以如下所示地访问消息：

```python
try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
```

问题：[np.random.choice](https://blog.csdn.net/qfpkzheng/article/details/79061601)的用法和random.choice()有何不同

