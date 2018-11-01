# Pandas学习笔记

**Pandas** 是 Python 中的数据操纵和分析软件包。名称“Pandas”得名自计量经济学 *Panel Data*（面板数据）一词。Pandas 为 Python 带来了两个新的数据结构，即 **Pandas Series**和 **Pandas DataFrame**。借助这两个数据结构，我们能够轻松直观地处理*带标签*数据和*关系*数据。

- 如何导入 Pandas
- 如何使用各种方法创建 Pandas Series 和 DataFrame
- 如何访问及更改 Series 和 DataFrame 中的元素
- 如何对 Series 执行算术运算
- 如何向 DataFrame 中加载数据
- 如何处理非数 (NaN) 值

### 为何要使用 Pandas？

因此，机器学习的重要一步是首先检查数据，通过进行一些基本的数据分析，确保数据很适合你的训练算法。这时候，Pandas 就派上用场了。Pandas Series 和 DataFrame 专门用于快速进行数据分析和操纵，并且使用起来灵活简单。

- 允许为行和列设定标签
- 可以针对时间序列数据计算滚动统计学指标
- 轻松地处理 NaN 值
- 能够将不同格式的数据加载到 DataFrame 中
- 可以将不同的数据集合并到一起
- 与 NumPy 和 Matplotlib 集成

Pandas Series 和 NumPy ndarrays 之间的另一个明显区别是 Pandas Series 可以存储不同类型的数据。和 NumPy ndarray 一样，Pandas Series 也是可变的，也就是说，创建好 Pandas Series 后，我们可以更改其中的元素。

访问和删除：

访问的多种方法：

Pandas Series 提供了两个属性 `.loc` 和 `.iloc`，帮助我们清晰地表明指代哪种情况。属性 `.loc` 表示 *位置*，用于明确表明我们使用的是标签索引。同样，属性 `.iloc` 表示*整型位置*，用于明确表明我们使用的是数字索引。

我们可以通过在 `.drop()` 方法中将关键字 `inplace` 设为 `True`，原地地从 Pandas Series 中删除条目。我们来看一个示例：

```python
groceries.drop('apples', inplace = True)
```

对 Pandas Series 执行算术运算

```python
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

fruits + 2
```

```python
print('EXP(X) = \n', np.exp(fruits))
print() 
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of fruits to the power of 2
```

仅对 fruits 购物清单中的部分条目应用算术运算。

```python
fruits['bananas'] + 2
fruits.iloc[0] - 2
fruits[['apples', 'oranges']] * 2
fruits.loc[['apples', 'oranges']] / 2
```

```python
groceries * 2 #会使每个条目翻倍
```

### 创建Datas Frame 

开始学习如何手动地通过字典创建 Pandas DataFrame，稍后，我们将学习如何将数据文件中的数据加载到 DataFrame 中。

```python
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

shopping_carts = pd.DataFrame(items)
```

![](https://i.imgur.com/oC9UUMu.jpg)

DataFrame 的行标签根据构建字典所用的两个 Pandas Series 的索引标签创建而成。DataFrame 的列标签来自字典的*键*。

另一个注意事项是，列按照字母顺序排序，而不是字典中的顺序。

最后要注意的是，我们发现该 DataFrame 中出现了一些 `NaN` 值。Pandas 通过这种方式表示该行和列索引没有值。

如果我们不向 Pandas Series 提供索引标签，Pandas 在创建 DataFrame 时将使用数字行索引。Pandas DataFrame 的行索引从 0 开始，就像 NumPy ndarray 的索引一样。

```python
# We create a dictionary of Pandas Series without indexes
data = {'Bob' : pd.Series([245, 25, 55]),
        'Alice' : pd.Series([40, 110, 500, 45])}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
df
```

- [pandas.DataFrame.index](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.index.html)
- [pandas.DataFrame.columns](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.columns.html)
- [pandas.DataFrame.dtypes](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dtypes.html)
- [pandas.DataFrame.ftypes](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ftypes.html)
- [pandas.DataFrame.get_dtype_counts](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.get_dtype_counts.html)
- [pandas.DataFrame.get_ftype_counts](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.get_ftype_counts.html)
- [pandas.DataFrame.select_dtypes](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.select_dtypes.html)
- [pandas.DataFrame.values](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.values.html)
- [pandas.DataFrame.get_values](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.get_values.html)
- [pandas.DataFrame.axes](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.axes.html)
- [pandas.DataFrame.ndim](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ndim.html)
- [pandas.DataFrame.size](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.size.html)
- [pandas.DataFrame.shape](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.shape.html)
- [pandas.DataFrame.memory_usage](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.memory_usage.html)
- [pandas.DataFrame.empty](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.empty.html)
- [pandas.DataFrame.is_copy](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.is_copy.html)

也可以选择只将部分数据放入DataFrame

```python
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])
```

为字典添加索引：

```python
# We create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame and provide the row index
df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])
```

手动创建 Pandas DataFrame 的最后一种方式是使用 Python 字典列表。流程和之前一样，我们先创建字典，然后将该字典传递给 `pd.DataFrame()` 函数。

```python
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

# We display the DataFrame
store_items
```

#### 访问 Pandas DataFrame 中的元素

```python
# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
```

请注意，在访问 DataFrame 中的单个元素时，就像上个示例一样，必须始终提供标签，并且列标签在前，格式为 `dataframe[column][row]`

添加新列：

```python
store_items['shirts'] = [15,2]
store_items['suits'] = store_items['pants'] + store_items['shirts']
#仅使用特定列的特定行中的数据向 DataFrame 添加新的列。并且新手表的数量与这些商店原有手表的库存一样
store_items['new watches'] = store_items['watches'][1:]
```

添加新行，我们首先需要创建新的 Dataframe，然后将其附加到原始 DataFrame 上。

```python
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]
new_store = pd.DataFrame(new_items, index = ['store 3'])
store_items = store_items.append(new_store)
```

`dataframe.insert(loc,label,data)` 方法使我们能够将新列（具有给定列`标签`和给定`数据`）插入 `dataframe` 的 `loc` 位置。我们将名称为 **shoes** 的新列插入 **suits** 列前面。因为 **suits** 的数字索引值为 4，我们将此值作为 `loc`。我们来看看代码编写方式：

```python
store_items.insert(4, 'shoes', [8,5,0])
```

要删除 DataFrame 中的行和列，我们将使用 `.pop()` 和 `.drop()` 方法。`.pop()` 方法仅允许我们删除列，而 `.drop()` 方法可以同时用于删除行和列，只需使用关键字 `axis` 即可。

```python
store_items.pop('new watches')
store_items = store_items.drop(['watches', 'shoes'], axis = 1)
store_items = store_items.drop(['store 2', 'store 1'], axis = 0)
```

有时候，我们可能需要更改行和列标签。我们使用 `.rename()` 方法将 **bikes** 列标签改为 **hats**

```python
store_items = store_items.rename(columns = {'bikes': 'hats'})
store_items = store_items.rename(index = {'store 3': 'last store'})
```

你还可以将索引改为 DataFrame 中的某个列。

```
store_items = store_items.set_index('pants')
```

![](https://i.imgur.com/tpYFXbf.jpg)

#### 处理 NaN

虽然任何给定数据集可能会出现各种糟糕的数据，例如离群值或不正确的值，但是我们几乎始终会遇到的糟糕数据类型是缺少值。正如之前看到的，Pandas 会为缺少的值分配 `NaN` 值。

如果我们向 DataFrame 中加载非常庞大的数据集，可能有数百万条数据，那么就不太容易直观地发现 `NaN` 值的数量。对于这些情形，我们结合使用多种方法来计算数据中的 `NaN` 值的数量。以下示例同时使用了 `.isnull()` 和 `sum()` 方法来计算我们的 DataFrame 中的 `NaN` 值的数量。

![](https://i.imgur.com/xtAaIpl.jpg)

```python
x =  store_items.isnull().sum().sum()
```

在上述示例中，`.isnull()` 方法返回一个大小和 `store_items` 一样的*布尔型*DataFrame，并用 `True` 表示具有 `NaN` 值的元素，用 `False` 表示非 NaN 值的元素。在 Pandas 中，逻辑值 `True` 的数字值是 1，逻辑值 `False` 的数字值是 0。

因此，我们可以通过数逻辑值 `True` 的数量数出 `NaN` 值的数量。为了数逻辑值 `True` 的总数，我们使用 `.sum()` 方法两次。要使用该方法两次，是因为第一个 sum() 返回一个 Pandas Series，其中存储了列上的逻辑值 `True` 的总数。

判断非 NaN* 值的数量。为此，我们可以使用 `.count()` 方法。

```python
store_items.count()
```

处理这些 NaN 值。通常可以*删除*或*替换* `NaN` 值。

首先，我们将学习如何从 DataFrame 中删除包含任何 `NaN` 值的行或列。如果 `axis = 0`，`.dropna(axis)` 方法将删除包含 `NaN` 值的任何*行*，如果 `axis = 1`，`.dropna(axis)` 方法将删除包含 `NaN` 值的任何*列*。我们来看一些示例：

```python
store_items.dropna(axis = 0)
```

注意，`.dropna()` 方法不在原地地删除具有 `NaN` 值的行或列。也就是说，原始 DataFrame 不会改变。你始终可以在 `dropna()` 方法中将关键字 `inplace 设为 True`，在原地删除目标行或列。

其次是替换。我们可以选择将所有 `NaN` 值替换为 0。为此，我们可以使用 `.fillna()` 方法，如下所示。

```python
store_items.fillna(0)
```

还可以使用 `.fillna()` 方法将 `NaN` 值替换为 DataFrame 中的上个值，称之为*前向填充*。在通过前向填充替换 `NaN` 值时，我们可以使用列或行中的上个值。`.fillna(method = 'ffill', axis)` 将通过前向填充 (`ffill`) 方法沿着给定 `axis` 使用上个已知值替换 `NaN` 值。

```python
#所有 NaN 值都被替换成了之前的行值
store_items.fillna(method = 'ffill', axis = 1)
#相似的，后向填充
store_items.fillna(method = 'backfill', axis = 0)
```

注意，`.fillna()` 方法不在原地地替换（填充）`NaN` 值。也就是说，原始 DataFrame 不会改变。你始终可以在 `fillna()` 函数中将关键字 `inplace 设为 True`，在原地替换 `NaN` 值。

还可以选择使用不同的[插值方法](https://jingyan.baidu.com/article/a501d80cf7c9c3ec620f5e5a.html)(根据两点估计中间点的值)替换 `NaN` 值。例如，`.interpolate(method = 'linear', axis)` 方法将通过 `linear` 插值使用沿着给定 `axis` 的值替换 `NaN` 值。

```python
store_items.interpolate(method = 'linear', axis = 0)
```

和我们看到的其他方法一样，`.interpolate()` 方法不在原地地替换 `NaN` 值。

####  将数据加载到 Pandas DataFrame 中

Pandas 使我们能够将不同格式的数据库加载到 DataFrame 中。用于存储数据库的最热门数据格式是 csv。CSV 是指*逗号分隔值*，是一种简单的数据存储格式。我们可以使用 `pd.read_csv()` 函数将 CSV 文件加载到 Pandas DataFrame 中。

```python
Google_stock = pd.read_csv('./GOOG.csv')

# 我们输出关于 Google_stock 的一些信息
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)
#查看前五行数据
Google_stock.head()
#后5行
Google_stock.tail()
```

我们还可以选择使用 `.head(N)` 或 `.tail(N)` 分别显示前 `N` 行和后 `N` 行数据。

我们快速检查下数据集中是否有任何 `NaN` 值。为此，我们将使用 `.isnull()` 方法，然后是 `.any()` 方法，检查是否有任何列包含 `NaN` 值。

```
Google_stock.isnull().any()
```

在处理大型数据集时，通常有必要获取关于数据集的统计信息。通过使用 Pandas 的 `.describe()` 方法，可以获取关于 DataFrame 每列的描述性统计信息。

另一个重要统计学衡量指标是数据相关性。数据相关性可以告诉我们不同列的数据是否有关联。我们可以使用 `.corr()` 方法获取不同列之间的关联性.

```python
Google_stock.corr()
```

![](https://i.imgur.com/YqZKZeE.jpg)

关联性值为 1 表明关联性很高，关联性值为 0 告诉我们数据根本不相关。

在这门“Pandas 入门”课程的最后，我们将讲解 `.groupby()` 方法。`.groupby()` 方法使我们能够以不同的方式对数据分组。我们来看看如何分组数据，以获得不同类型的信息。在下面的示例中，我们将加载关于虚拟公司的虚拟数据。

![](https://i.imgur.com/DZk3QEK.jpg)

我们来计算公司每年在员工薪资上花费的数额。为此，我们将使用 `.groupby()` 方法按*年份*对数据分组，然后使用 `.sum()` 方法将所有员工的薪资相加。

```python
data.groupby(['Year'])['Salary'].sum()
```

现在假设我们想知道每年的平均薪资是多少。为此，我们将使用 `.groupby()` 方法按*年份*对数据分组，就像之前一样，然后使用 `.mean()` 

现在我们来看看在这三年的时间内每位员工都收到多少薪资。在这种情况下，我们将使用`.groupby()`方法按照*Name*来对数据分组。之后，我们会把每年的薪资加起来。

```python
data.groupby(['Name'])['Salary'].sum()
```

现在让我们看看每年每个部门的薪资分配状况。在这种情况下，我们将使用`.groupby()`方法按照*Year*和*Department*对数据分组，之后我们会把每个部门的薪资加起来。

```
data.groupby(['Year', 'Department'])['Salary'].sum()
```

