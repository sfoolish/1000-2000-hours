---
## [你真的会python嘛?](http://www.dongwm.com/archives/ni-zhen-de-hui-pythonma/)
写的很在理，好好梳理一下 python 的基础知识。

---
## tornado 源码阅读
* python 的一些典型处理方法；
    - (ioloop.py)try ... except 实现兼容性处理；
    - (iostream.py)经典的对象继承，重载关系 BaseIOStream -> IOStream -> SSLIOStream；
    - decorator 标准库提供的，自己实现的；

* 异步 IO 的实现机制；
    - iostream.py 要点：
        - callback 与 stack_context.wrap；
        - ioloop 驱动 callback ；

    - ioloop.py 要点：
        - global IOLoop instance 实现原理；

* 对 WebSocket 的支持；

### REF
* [Tornado源码分析之http服务器篇](http://kenby.iteye.com/blog/1159621)

---
## 函数式编程
* [Functional Programming with Python -- PyCon US 2013](http://pyvideo.org/video/1799/functional-programming-with-python)