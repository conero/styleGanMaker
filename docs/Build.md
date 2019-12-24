# 环境搭建

> 2019年12月24日 星期二
>
> Joshua Conero





## 环境

### 硬件信息

*运行命令: `nvcc --version`*

```shell
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2017 NVIDIA Corporation
Built on Fri_Sep__1_21:08:32_Central_Daylight_Time_2017
Cuda compilation tools, release 9.0, V9.0.176
```



- **cudnn**  *v7.4.1.5*



### 软件包信息

- **python**             *3.6*
- **tensorflow**      *tensorflow 1.10.0   含`tensorflow -gpu`*
- **Pillow**                图像处理库
- **requests**           网络请求库



## 搭建

**使用 python venv 环境**

```powershell
# 创建虚拟环境
python -m venv py36-tf1.10

# 启动环境
./py36-tf1.10/Scripts/Activate.ps1

# pip 更新
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
# pip 依赖安装
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==1.10.0 tensorflow-gpu==1.10.0 pillow requests

# 可选的，单文件打包工具实现
# python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

