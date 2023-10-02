# CM 1 Statistique

## Eléments de statistique descriptive

### 条件概率

定义：$P(A|B) = \frac {P(AB)}{P(A)}$

乘法公式：$P(AB) = {P(A)}{P(A|B)}$

全概率：$P(A) = \sum_{i=1}^nP(B_i)P(A|B_i)$, A发生的概率是全部原因引起A发生概率的总和，由原因推结果

贝叶斯: $P(B_i|A) = \frac {P(A|B_i)P(B_i)}{\sum^n_{j=1}P(A|B_i)P(B_j)}$, 在事件A发生的前提下，用贝叶斯公式寻找导致A发生的各种原因$B_i$的概率，由结果找原因


La moyenne (empirique) : $\overline{X} = \frac{1}{n}\sum_{i=1}^{n} {X_i} $
qui donne la tendance centrale des observations
La variance (empirique) : $\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n}{(X_i - \overline{X})^2}$
qui mesure la dispersion des observations.

期望

- 离散型：$E[X]=\sum_{k=1}^{+\infty}x_kp_k$, 二项分布np , 泊松$\lambda$
- 连续型：$E[X]=\int^{+\infty}_{-\infty}xf(x)dx$

方差：$D(X)=E[(X-E[X])^2] = E[X^2]-(E[X])^2$,标准差是他开根号

协方差: $Cov(X,Y)=E(XY)-E(X)E(Y)$

##  Loi de distribution et modèle de statistique

大数定理：设$X_1,X_2,..$是一个期望存在的随机变量序列，若对任意给定的正数

$\epsilon>0$有$lim_{n\rightarrow+\infty}P\{|\overline{X_n}-E[\overline{X_n}]|\geqslant\epsilon\}=0$，则称$\{X_n\}$服从大数定律 =>频率趋近于概率

中心极限定理：

<img src="https://cdn.staticaly.com/gh/nililili7876/blog_pic@main/20221120/ya709c291fba07eccdf119fd2b9844181.2yjkzw956ci0.jpg" alt="ya709c291fba07eccdf119fd2b9844181" style="zoom:50%;" />

总体：研究对象的全体

抽样：简单随机抽样、系统抽样、分层

样本：从总体X中随机抽取的n个个个体

常见统计量：极差，众数，均值，方差: $x^2=\frac1{n-1}\sum^n_{i=1}(x_i-\overline x)^2 = \frac1{n-1}(\sum^n_{i=1}{x_i}^2-n\overline x^2)$, 标准差$s$, 标准误差$s_{\overline x} = \frac s {\sqrt n}$,样本矩: k阶原点矩$S_n^k = \frac1n\sum^n_{i=1}X_i^k$，k阶中心矩$S_n^k = \frac1n\sum^n_{i=1}(X_i-\overline X)^k$

经验分布函数

<img src="https://cdn.staticaly.com/gh/nililili7876/blog_pic@main/20221120/yaf3274f32c38533d0a74b96d524cffa6.104q4sxtri4g.jpg" alt="yaf3274f32c38533d0a74b96d524cffa6" style="zoom:50%;" />


**<mark>直方图</mark>**: 设$x_1,x_2,..,x_n$是总体X的样本$X_1,X_2,..,X_n$的观察值，用直方图法求近似**概率密度函数**的作法步骤：

1. 从中找$x_1,x_2,..,x_n$出最小值M和最大值N；
2. 取适当的a,b使得$a＜M<N≤b$易于等分，即将[a,b]等分为m个小区间，分点为:$a=t_0<t_1<t_＜...<t_m=6$
3. 记录样本值$x_1,x_2,..,x_n$，正n落在小区间$(t_{i-1},t_i]$的个数，即频数$v_i$，则X落入$(t_{i-1},t_i]$的频率的近似值为$f_i=v_i/n$；
4. 在坐标平面上，自左向右在各个小区间$(t_{i-1},t_i],1≤i≤m$上画竖直的长方形，对第i个长方形，以x轴上的小区间$(t_{i-1},t_i]$的一段为底，以$y_i=f_i/(t_i-t_{i-1})$为高，画出图形既是所谓的直方图；
5. 用光滑曲线描出直方图的外廓曲线，即为总体 X 的近似密度函数曲线。

## Estimation et maximum de vraisemblance

点估计：用样本矩[$E[X],E[X^2]$]代替总体矩。

极大似然估计：1.似然函数：连乘；2.取对数；3.对$\theta$求导

估计量的评选标准：

- MSE[mean square error：均方误差]：$MSE(\widehat\theta)=E[\widehat\theta-\theta]^2$

- 无偏性[$E[\widehat{\theta}]=\theta$]，有效性[$\widehat{\theta_1}$与$\widehat{\theta_2}$是$\theta$的无偏估计量，若$D(\widehat{\theta_1}) < D(\widehat{\theta_2})$, 则$\widehat{\theta_1}$比$\widehat{\theta_2}$有效]，相合性$\widehat{\theta}$收敛到$\theta$.

区间估计：置信空间










# Model Performance

Penalized Empirical Risk Minimization:
penalization function: 正则化方法通常使用一个正则化项来控制模型的复杂性，以防止过拟合。正则化项包括一个惩罚函数（penalization function）以及一个平滑参数（smoothing parameter）或正则化参数，该参数决定了正则化的强度。平滑参数的作用是平衡模型的拟合能力和复杂性。

正则化的目的是==避免过拟合(overfitting)==的问题，过拟合是指模型在训练数据上表现很好，但在新数据上的泛化性能很差。正则化通过在模型的损失函数中添加一个正则项来实现，这个正则项通常是一个关于模型参数的函数，用于对参数进行约束，使其不能过于复杂。正则化的强度由正则化参数控制，该参数通常由模型训练过程中的交叉验证或其他技术来选择。

这个函数的形式可以根据具体的问题和模型而变化，但通常是一个关于模型参数的非负函数。这个函数的作用是惩罚模型参数的值，使得在训练过程中，模型更倾向于选择参数值较小或较简单的情况。

最常见的正则化函数之一是L2正则化，它使用模型参数的平方作为正则化项。L1正则化使用模型参数的绝对值作为正则化项。这些正则化函数都可以视为 "(positive) penalization function" 的示例，因为它们都是非负函数，并且在训练过程中对模型参数进行了正则化。

Smoothing parameter 作用：

1.   控制模型复杂性：平滑参数决定了正则化项对模型复杂性的影响程度。较大的平滑参数会导致更强的正则化，从而降低模型的复杂性，使模型更趋向于选择参数值较小或较简单的情况。这可以帮助防止过拟合，尤其是在训练数据相对较少或噪声较多时。

2.   调整拟合和泛化之间的权衡：平滑参数允许您在模型的拟合和泛化之间进行权衡。较小的平滑参数允许模型更好地拟合训练数据，但可能导致过拟合。较大的平滑参数会限制模型的拟合能力，但有助于更好地泛化到新数据。通过调整平滑参数，您可以控制这种权衡，以满足特定问题的需求。

3.   特征选择：平滑参数的变化可以影响正则化项对模型参数的稀疏性。较大的平滑参数通常会推动某些模型参数趋向于零，实现特征选择的效果。这对于自动选择重要特征或减少维度非常有用。

![image](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20231002/image.1dw3jse9mfy8.webp)



![image5](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20231002/image.fmu4oqcfu08.webp)