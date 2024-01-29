from setuptools import setup, find_packages

pkg = find_packages()
install_requires = ["ctpbee", "flask", "click", "flask-jwt-extended", "redis", "sqlalchemy", "flask-socketio",
                    "gevent-websocket"]
setup(
    name='ctpbee_webline',
    version='0.1',
    description='ctpbee的web控制台',
    author='somewheve',
    author_email='somewheve@gmail.com',
    url='https://www.github.com/ctpbee/webline',
    install_requires=install_requires,
    packages=pkg,
    entry_points={
        'console_scripts': ['ctpbee_webline = ctpbee_webline.cmd:cli']
    }
)
