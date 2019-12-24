# python 环境使用
echo '*************************************'
echo '*****                         *******'
echo '***** build the python venv   *******'
echo '*****                         *******'
echo '*************************************'


# 创建
python -m venv py36-tf1.10

# 启用
./py36-tf1.10/Scripts/Activate.ps1

# pip 更新
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

# 安装依赖
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==1.10.0 tensorflow-gpu==1.10.0 pillow requests

# 可选的，单文件打包工具实现
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
