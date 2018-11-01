# NumPy 简介

**NumPy** 是 *Numerical Python* 的简称，它是 Python 中的科学计算基本软件包。NumPy 为 Python 提供了大量数学库，使我们能够高效地进行数字计算。

(之前一直有个问题，它们功能的底层是什么？介绍清楚了，它们的底层语言是C语言，这回也是计算机的底层代码。)

- 如何导入 NumPy
- 如何使用各种方法创建多维 NumPy ndarray
- 如何访问和更改 ndarray 中的元素
- 如何加载和保存 ndarray
- 如何使用切片选择或更改 ndarray 的子集
- 了解 ndarray 视图和副本之间的区别
- 如何使用布尔型索引并设置操作以选择或更改 ndarray 的子集
- 如何对 ndarray 排序
- 如何对 ndarray 执行元素级操作
- 了解 NumPy 如何使用广播对不同大小的 ndarray 执行操作。

虽然 Python 列表本身很强大，但是 NumPy 具有很多关键功能，从而比 Python 列表更具优势。其中一个优势便是速度。在对大型数组执行操作时，NumPy 的速度比 Python 列表的速度快了好几百倍。这是因为 NumPy 数组本身能节省内存，并且 NumPy 在执行算术、统计和线性代数运算时采用了优化算法。**Pandas 等很多 Python 软件包都是在 NumPy 的基础上构建而成。**

NumPy 的核心是 **ndarray**，其中 *nd* 表示 n 维。ndarray 是一个多维数组，其中的所有元素类型都一样。换句话说，ndarray 是一个形状可以多样，并且可以存储数字或字符串的网格。在很多机器学习问题中，你通常都会发现需要以多种不同的方式使用 ndarray。例如，你可能会使用 ndarray 存储一个图像的像素值，然后将该图像馈送到神经网络中以进行图像分类。

Numpy数组中数值类型都是一致的。请务必注意，Python 列表和 ndarray 之间的最大区别是：与 Python 列表不同的是，ndarray 的所有元素都必须类型相同。因此，虽然我们可以同时使用整数和字符串创建 Python 列表，但是无法在 ndarray 中同时使用这两种类型。如果向 `np.array()` 函数提供同时具有整数和字符串的 Python 列表，NumPy 会将所有元素解析为字符串（比如U21）。我们可以在下面的示例中见到这种情况：

（类与函数：类即class是一种高级抽象。[比较详细的介绍](https://www.cnblogs.com/hexige/p/7239695.html)）

#### 使用列表转换NumPy ndarray

```python
x = np.array([1, 2, 'World'])
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
```

当 NumPy 创建 ndarray 时，它会自动根据用于创建 ndarray 的元素的类型为其分配 *dtype*。

可以看出，当我们创建只有浮点数的 ndarray 时，NumPy 将元素当做 *64 位浮点数 (float64)* 存储在内存中。但是，当我们创建同时包含浮点数和整数的 ndarray 时，就像上面的 `z` ndarray，NumPy 也会为其元素分配 *float64* dtype。这叫做*向上转型*。因为 ndarray 的所有元素都必须类型相同，因此在这种情况下，NumPy 将 `z` 中的整数向上转型为浮点数，避免在进行数学计算时丢失精度。

虽然 NumPy 自动为 ndarray 选择 dtype，但是 NumPy 也允许你指定要为 ndarray 的元素分配的特定 dtype。当你在 `np.array()` 函数中创建 ndarray 时，可以使用关键字 `dtype` 指定 dtype。我们来看一个示例：

```python
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)
```

存储与读取：np.save("name",x)    np.load("*.npy")

#### 使用内置函数创建ndarray

`np.arange()` 和 `np.linspace()` 来创建秩为 1 的 ndarray

```python
x = np.arange(1,14,3)
x = np.linspace(0,25,10, endpoint = False)

print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
```

将这些函数与 `np.reshape()` 函数相结合，创建秩为 2 的任何形状 ndarray。`np.reshape(ndarray, new_shape)` 函数会将给定 `ndarray` 转换为指定的 `new_shape`。请务必注意：`new_shape` 应该与给定 `ndarray` 中的元素数量保持一致。

```python
x = np.arange(20)
x = np.reshape(x, (4,5))
print('Reshaped x = \n', x)

#当作方法实用的快捷方式
Y = np.arange(20).reshape(4, 5)
```

我们将创建的最后一种 ndarray 是*随机* ndarray。随机 ndarray 是包含随机数字的数组。在机器学习中，通常需要创建随机指标，例如，在初始化神经网络的权重时。NumPy 提供了各种随机函数来帮助我们创建任何形状的随机 ndarray。

```python
X = np.random.random((3,3))

#result:
X =
[[ 0.12379926 0.52943854 0.3443525 ]
 [ 0.11169547 0.82123909 0.52864397]
 [ 0.58244133 0.21980803 0.69026858]]
```

NumPy 还允许我们创建由特定区间内的随机整数构成的 ndarray。函数 `np.random.randint(start, stop, size = shape)` 会创建一个具有给定`形状`的 ndarray，其中包含在半开区间 `[start, stop)` 内的随机整数。

```python
X = np.random.randint(4,15,size=(3,2))
```

具有统计特征的ndarray：`np.random.normal(mean, standard deviation, size=shape)` 会创建一个具有给定`形状`的 ndarray，其中包含从`正态`高斯分布（具有给定`均值`和`标准差`）中抽样的随机数字。

```python
X = np.random.normal(0, 0.1, size=(1000,1000))
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')
```

### 访问、删除、插入、堆叠 ndarray中的元素

NumPy ndarray 是可变的，意味着 ndarray 中的元素在 ndarray 创建之后可以更改。NumPy ndarray 还可以切片，因此可以通过多种方式拆分 ndarray。例如，我们可以从 ndarray 中获取想要的任何子集。通常，在机器学习中，你需要使用切片拆分数据，例如将数据集拆分为训练集、交叉验证集和测试集。

访问、更改一维数组和列表相同。

要访问秩为 2 的 ndarray 中的元素，我们需要提供两个索引，格式为 `[row, column]`。比如：X[0,0]

向 ndarray 中添加元素及删除其中的元素。我们可以使用 `np.delete(ndarray, elements, axis)` 函数删除元素。此函数会沿着指定的`轴`从给定 `ndarray` 中`删除`给定的`元素`列表。对于秩为 1 的 ndarray，不需要使用关键字 `axis`。对于秩为 2 的 ndarray，`axis = 0` 表示选择*行*，`axis = 1` 表示选择*列*。我们来看一些示例：

```python
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We delete the first row of y
w = np.delete(Y, 0, axis=0)

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

Original x = [1 2 3 4 5]

Modified x = [2 3 4]

Original Y =
[[1 2 3]
 [4 5 6]
 [7 8 9]]

w =
[[4 5 6]
 [7 8 9]]

v =
[[2]
 [5]
 [8]]
```

向 ndarray 中附加值。我们可以使用 `np.append(ndarray, elements, axis)` 函数向 ndarray 中附加值。该函数会将给定的`元素`列表沿着指定的`轴`附加到 `ndarray` 中。

```python
# We append the integer 6 to x
x = np.append(x, 6)
x = np.append(x, [7,8])
# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)
# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)
```

插入：向 ndarray 中插入值。我们可以使用 `np.insert(ndarray, index, elements, axis)` 函数向 ndarray 中插入值。此函数会将给定的`元素`列表沿着指定的`轴`插入到 `ndarray` 中，并放在给定的`索引`**前面**。我们来看一些示例：

```python
# We insert the integer 3 and 4 between 2 and 5 in x. 
x = np.insert(x,2,[3,4])

# We insert a row between the first and last row of y
w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,5, axis=1)
```

NumPy 还允许我们将 ndarray 上下堆叠起来，或者左右堆叠。可以使用 `np.vstack()` 函数进行垂直堆叠，或使用 `np.hstack()` 函数进行水平堆叠。请务必注意，为了堆叠 ndarray，ndarray 的形状必须相符。

```python
# We create a rank 1 ndarray 
x = np.array([1,2])

# We create a rank 2 ndarray 
Y = np.array([[3,4],[5,6]])

z = np.vstack((x,Y))
w = np.hstack((Y,x.reshape(2,1)))
```

### ndarray 切片

```python
1. ndarray[start:end]
2. ndarray[start:]
3. ndarray[:end]

#在第一种方法和第三种方法中，结束索引不包括在内。此外注意，因为 ndarray 可以是多维数组，在进行切片时，通常需要为数组的每个维度指定一个切片。
```

```python
X =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [10 11 12 13 14]
 [15 16 17 18 19]]

Z = X[1:4,2:5]

Z =
[[ 7 8 9]
 [12 13 14]
 [17 18 19]]

q = X[:,2]
q = [ 2 7 12 17]

# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]
R =
[[ 2]
 [ 7]
 [12]
 [17]]

#注意，当我们选择第 3 列中的所有元素，即上述变量 q，切片返回一个秩为 1 的 ndarray，而不是秩为 2 的 ndarray。但是，如果以稍微不同的方式切片X，即上述变量 R，实际上可以获得秩为 2 的 ndarray。

```

但是，如果我们想创建一个新的 ndarray，其中包含切片中的值的副本，需要使用 `np.copy()` 函数。`np.copy(ndarray)` 函数会创建给定 `ndarray` 的一个副本。

使用一个 ndarray 对另一个 ndarray 进行切片

```python
indices = np.array([1,3])#实际上这里的array也是索引

# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices,:]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]
```

NumPy 还提供了从 ndarray 中选择特定元素的内置函数。例如，`np.diag(ndarray, k=N)` 函数会以 `N` 定义的`对角线`提取元素。默认情况下，`k=0`，表示主对角线。`k > 0` 的值用于选择在主对角线之上的对角线中的元素，`k < 0` 的值用于选择在主对角线之下的对角线中的元素。

```python
X =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

# We print the elements in the main diagonal of X
print('z =', np.diag(X))

# We print the elements above the main diagonal of X
print('y =', np.diag(X, k=1))

# We print the elements below the main diagonal of X
print('w = ', np.diag(X, k=-1))

z = [ 0 6 12 18 24]

y = [ 1 7 13 19]

w = [ 5 11 17 23]
```

从 ndarray 中提取唯一的元素。我们可以使用 `np.unique()` 函数查找 ndarray 中的唯一元素。`np.unique(ndarray)` 函数会返回给定 `ndarray` 中的 `唯一`元素，如以下示例所示：

```python
print('The unique elements in X are:',np.unique(X))

X =
[[1 2 3]
 [5 2 8]
 [1 2 3]]

The unique elements in X are: [1 2 3 5 8]
```

### 布尔型索引、集合运算和排序

借助逻辑而非序号进行索引：

例如，假设有一个 10,000 x 10,000 ndarray，其中包含从 1 到 15,000 的随机整数，我们只想选择小于 20 的整数。这时候就要用到*布尔型*索引，对于布尔型索引，我们将使用逻辑参数（而不是确切的索引）选择元素。也可以修改相应的值。

```python
# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that lees than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# We use Boolean indexing to assign the elements that are between 10 and 17 the value of -1
X[(X > 10) & (X < 17)] = -1
```

集合运算，比如找出两个数组的交集

```python
x = [1 2 3 4 5]
y = [6 7 2 8 4]

print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))
```

排序：还可以在 NumPy 中对 ndarray 进行排序。我们将了解如何使用 `np.sort()` 函数以不同的方式对秩为 1 和 2 的 ndarray 进行排序。和我们之前看到的其他函数一样，`sort` 函数也可以当做方法使用。但是，对于此函数来说，数据在内存中的存储方式有很大变化。当 `np.sort()` 当做函数使用时，它不会对ndarray进行就地排序，即不更改被排序的原始 ndarray。但是，如果将 `sort` 当做方法，`ndarray.sort()` 会就地排序 ndarray，即原始数组会变成排序后的数组。

```python
np.sort(x)
```

在对秩为 2 的 ndarray 进行排序时，我们需要在 `np.sort()` 函数中指定是按行排序，还是按列排序。为此，我们可以使用关键字 `axis`。

```python
# We sort the columns of X and print the sorted array
print()
print('X with sorted columns :\n', np.sort(X, axis = 0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))
```

### 算术运算和广播

对 ndarray 进行元素级运算

在进行元素级运算时，对其执行运算的 ndarray 必须具有相同的形状或者可以广播。

```python
print('x + y = ', x + y)
print('add(x,y) = ', np.add(x,y))
print()
print('x - y = ', x - y)
print('subtract(x,y) = ', np.subtract(x,y))
print()
print('x * y = ', x * y)
print('multiply(x,y) = ', np.multiply(x,y))
print()
print('x / y = ', x / y)
print('divide(x,y) = ', np.divide(x,y))
```

我们还可以同时对 ndarray 的所有元素应用数学函数，例如 `sqrt(x)`

```python
print('EXP(x) =', np.exp(x))
print()
print('SQRT(x) =',np.sqrt(x))
print()
print('POW(x,2) =',np.power(x,2)) 
```

NumPy 的另一个重要特性是具有大量不同的统计学函数。统计学函数为我们提供了关于 ndarray 中元素的统计学信息。

```python
# We create a 2 x 2 ndarray
X = np.array([[1,2], [3,4]])

# We print x
print()
print('X = \n', X)
print()

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))
print()
print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X,axis=0))
print('Median of all elements in the rows of X:', np.median(X,axis=1))
print()
print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))
print()
print('Maximum value of all elements in X:', X.min())
print('Maximum value of all elements in the columns of X:', X.min(axis=0))
print('Maximum value of all elements in the rows of X:', X.min(axis=1))
```

 NumPy 如何使 ndarray 中的所有元素与单个数字相加，而不使用复杂的循环——类似3 * X。

和之前一样，NumPy 能够通过沿着大的 ndarray 对更小的 ndarray 进行广播，将 1 x 3 和 3 x 1 ndarray 加到 3 x 3 ndarray 上。通常，NumPy 能够这么操作的前提是，更小的 ndarray（例如我们的示例中的 1 x 3 ndarray）可以扩展成更大的 ndarray 的形状，并且生成的广播很清晰明确。