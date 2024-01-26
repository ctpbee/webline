import click
import sqlalchemy
import shutil

from ctpbee_webline.model import Admin
from ctpbee_webline.util import encrypt
from ctpbee_webline.env import SQLALCHEMY_DATABASE_URI


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    """
    初始化数据库
    """
    from ctpbee_webline import create_app, model
    app = create_app()
    with app.app_context():
        init = False
        try:
            admin = Admin.query.filter().all()
            if len(admin) == 0:
                init = True
        except sqlalchemy.exc.OperationalError:
            file_path = SQLALCHEMY_DATABASE_URI.split("///")[1]
            click.echo(f'ctpbee: 未发现数据库文件, 开始创建/instance/{file_path}')
            model.create_all()
            init = True
        if init:
            click.echo('ctpbee: 尚未创建admin用户, 开始创建')
            admin = Admin(username="admin", pwd=encrypt("123456"))
            model.session.add(admin)
            model.session.commit()
            click.echo('ctpbee: admin用户创建成功, 默认密码为123456')
        else:
            click.echo('ctpbee: 忽略操作')
        click.echo('ctpbee: 数据库初始化操作完成')


@cli.command()
def dropdb():
    """
    删除数据库
    """
    import os
    file_list = os.listdir(".")
    if "instance" not in file_list:
        click.echo('ctpbee: 未发现数据库文件 操作忽略')
    else:
        click.echo("ctpbee: 删除数据库是危险操作, 下次小心一点")
        shutil.rmtree("./instance")


if __name__ == '__main__':
    cli()
