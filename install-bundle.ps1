# window 打包分发
echo '*************************************'
echo '*****                         *******'
echo '***** bundleIntoSingleExeFile *******'
echo '*****                         *******'
echo '*************************************'

$path = './runtime/bundle'
if(-not (Test-Path -Path $path )){
    mkdir $path
}

# 启用 python venv 环境
./py36-tf1.10/Scripts/Activate.ps1

cd $path

# -w 不显示输出的调试信息
# 编译
pyinstaller -i ../../docs/sg_maker.ico -F ../../sg_maker.py

# 返回项目根目录
cd ../../