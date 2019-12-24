# --.python3.6.--
# 2019年12月24日 星期二
import os
import sys
import cc

# 运行代码
cmd = None


class CmdList:
    @staticmethod
    def index():
        """
        空页面
        :return:
        """
        print(' 欢迎使用 styleGan Maker(sg_maker)')
        print(f' python {sys.version}')
        print(f' 版本信息: {cc.VERSION}/{cc.DATE}')

    @staticmethod
    def help():
        """
        帮助信息
        :return:
        """
        print(' run 运行模型，必须参数列表如下')
        print('   1.-M, --model-path  模型地址')
        print()
        print('   可选参数: ')
        print('     1. -O,--out-dir      输出地址')
        print('     1. -N,--num          本次生成数')
        print(' -v,--version 版本信息')
        print(' -h,--help 输出帮助信息')

    @staticmethod
    def version():
        print(f'{cc.VERSION}/{cc.DATE}')

    @staticmethod
    def run():
        """
        模型运行器
        :return:
        """
        app = cmd.app
        opt_list = ['model-path', 'M']
        if not app.check_opts(*opt_list):
            print(' --model-path 选项未设置，运行失败！')
            return

        model_path = app.getOpts(*opt_list)
        if model_path is None or model_path == "" or not os.path.exists(model_path):
            print(f' --model-path={model_path} 不是一个有效的地址！')
            return

        # 条件引入
        import run_model
        run_model.execute_model(model_path, **app.data())


if __name__ == "__main__":
    import cmd_bin

    cmd = cmd_bin.Command()
    cmd.empty_fn_register(CmdList.index)
    cmd.opt_fn_register(['h', 'help'], CmdList.help)
    cmd.opt_fn_register(['v', 'version'], CmdList.version)

    cmd.cmd_fn_register('run', CmdList.run)

    # 测试命令
    # cmd.args('run', '-M')

    cmd.run()
