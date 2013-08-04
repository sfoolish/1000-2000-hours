---
* [你真的会python嘛?](http://www.dongwm.com/archives/ni-zhen-de-hui-pythonma/)
写的很在理，好好梳理一下 python 还没入门呐。

---
## tornado 源码阅读
* python 的一些经典处理方法
    - (ioloop.py)try ... except 实现兼容性处理；
    - (iostream.py)经典的对象继承，重载关系 BaseIOStream -> IOStream -> SSLIOStream；

* 异步 IO 的实现机制；

    iostream.py 要点：
        - callback 与 stack_context.wrap；
        - ioloop 驱动 callback ；

    ioloop.py 要点：

* 对 WebSocket 的支持；
