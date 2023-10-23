

# Machine Learning




## 数据降维


### PCA




## SVM支持向量机

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231023/image.6dso0dq1h9w0.webp)

形式：
$$ min_{\omega, b} \frac{1}{2}||\omega||^2 \\
s.t.  y_i(\omega^Tx_i + b) >= 1, i = 1, 2, ... , m $$

### 对偶问题

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231023/image.70rgw36odjo0.webp)


带入并消去$\omega$和$b$，就可以得到对应的对偶问题：

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231023/image.4gd98nks5ze0.webp)

求解出来：
![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231023/image.layaw3s2ie8.webp)

KKT条件：

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231023/image.5zgpre1lkdk0.webp)

因此，$\alpha_i = 0$ or $y_if(x_i) = 0$
- $\alpha_i = 0$，对应着样本不会出现在求和中；
- $y_if(x_i) = 0$，样本再最大间隔的边界，是一个支持向量
  
支持向量机的一个重要性质:训练完成后?大部分的训练样本都不需
保留，最终模型仅与支持向量有关



### 软间隔与正则化

不一定存在超平面能够完全线性分割，引入soft margin




### 核方法

