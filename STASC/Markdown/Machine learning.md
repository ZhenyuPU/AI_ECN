# Machine learning
## 评估模型方法


## 线性模型
线性模型形式：$f(x) = \omega^Tx+b$, where $\omega = (\omega_1;...;\omega_d)$
### 线性回归(régression linéaire)
#### 多元线性回归(Régression linéaire multiple)
属性转换：
- 离散属性，若属性间存在order关系，连续化为连续值
- 不存在order关系，转化为k维向量
学习$f(x_i) = \omega^Tx_i+b$，使得$f(x_i) = y_i$，关键在于如何衡量这两者的差别，我们可以使用均方误差：
$$\begin{aligned} (\omega^*, b^*) &= arg min_{(\omega, b)} \sum_{i=0}^{m}(f(x_i) - y_i)^2 \\
&= arg min_{(\omega, b)} \sum_{i=0}^{m}(f(x_i) - \omega^Tx_i-b)^2 \end{aligned}$$

令 $E_{(\omega, b)} = \sum_{i=0}^{m}(f(x_i) - \omega^Tx_i-b)^2$，求导得到：
$$\begin{aligned}
\omega &= \frac{\sum_{i=1}^{m}y_i(x_i-\overline{x})}{\sum_{i=1}^{m}x_i^2 - \frac{1}{m}(\sum_{i=1}^{m}x_i)^2} \\
b &= \frac{1}{m}\sum_{i=1}^{m}(y_i - \omega x_i)\end{aligned}$$

以上称之为多元线性回归(Régression linéaire multiple)

$$
X =\left[
\begin{matrix}
 x_{11}      & x_{12}      & \cdots & x_{1d}  &    1    \\
 x_{21}      & x_{22}      & \cdots & x_{2d}    & 1  \\
 \vdots & \vdots & \ddots & \vdots \\
 x_{m1}      & x_{m2}      & \cdots & x_{md}   & 1   \\
\end{matrix}
\right]
$$

最后得到：
$$ f(\hat{x_i}) = \hat{x_i}^T(X^TX)^{-1}X^Ty$$
如果现实中$X^T$不是满秩矩阵，就引入正则化(Regularization)项。

#### 对数模型与对数几率回归(Logistic regression)

$$ lny = \omega^Tx+b$$
考虑一个单调可微函数g(·)，令
$$y = g^{-1}(\omega^Tx+b)$$

g(·)，此函数被称为“联系函数”。(Link Fucntion)，此模型称为“广义线性模型”。对数线性模型是$g(·) = ln(·)$ 的特例。 

用对数几率函数代替$g^{-1}(·)$，常见的有：
$$ y = \frac{1}{1+e^{-z}}$$
带入z， 对于这个模型的对数几率为：
$$ ln\frac{y}{1-y} =  \omega^Tx+b$$
实际上是用线性回归模型$\omega^Tx+b$去逼近对数几率，称之为“对数几率回归”。虽叫做回归，实际上是一种分类学习方法。
可以用极大似然法估计$\omega$和$b$：
$$\begin{aligned}
p_1 &= p(y=1|x) &= \frac{e^{\beta \hat{x}}}{1+e^{\beta \hat{x}}} \\
p_2 &= p(y=0|x) &= \frac{1}{1+e^{\beta \hat{x}}} \end{aligned}$$

极大似然估计：
$$\begin{aligned}
l(\beta) &= \sum_{i=1}^{m}lnp(y_i|x_i; \beta)\\
p &= p_1^{y_i}p_2^{1-y_i} \\
lnp &= y_ilnp_1+(1-y_i)lnp_2 \\
l(\beta) &= \sum_{i=1}^{m}(y_i\beta ^T\hat(x_i)-ln(1+e^{\beta ^T \hat(x_i)}))
\end{aligned}$$

利用梯度下降、牛顿法等，求得$\beta$使l最大



#### 线性判别分析(Linear Discrim inant Analysis-LDA)



