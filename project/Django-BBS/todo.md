
## Django-BBS 开发要点及注意事项

考虑到用户量激增的可能性，将这个 BBS 切分成几个服务，配置Nginx将请求转发到不同服务。通过使⽤ Redis 为可能成为性能瓶颈的数据做缓存。

### Django

    - 要熟悉 Django 框架结构，及其使用；
    - Django 搭配数据库，数据对象模型设置。

### Nginx

    - uWSGI 对接 Django ；
    - 静态文件服务器，BootStrap 相关的 js, css 文件，网站相关图片直接走 nginx 。

### Redis

    - Django 内部已经实现缓存中间层，需要进行配置和安装redis python 驱动；
    - 服务代码中，使用 Django 提供的 decorator 进行 decrate 实现缓存功能;
    - 性能瓶颈的判断，测试是个难点。

### BootStrap
    
    - 主要是其提供一些组建的使用；

### BBS 参考网站

    - [dinette 1.4e](https://pypi.python.org/pypi/dinette/1.4e): Dinette is a forum application in the spirit of PunBB.
    - [github Dinette is fully featured Django forum app](https://github.com/agiliq/Dinette)
    - [DjangoBB-bitbucket](https://bitbucket.org/slav0nic/djangobb/overview)
    - [Django Bulletin Board  DjangoBB](http://djangobb.org/)
