
## 官方安装文档

[NewInstallFromSource](https://code.google.com/p/memcached/wiki/NewInstallFromSource)

## 我的源码编译过程

测试环境 Mac OS 10.6, Xcode 4.0 提供的 gcc4.2.1 。测试工程路径 `/Users/apple/APP_PRJ/m_memcached/`。

### libevent 源码编译

	$ cd /Users/apple/APP_PRJ/m_memcached/
	$ git clone https://github.com/nmathewson/Libevent.git libevent_git
    $ cd libevent_git/
    $ git checkout release-2.0.18-stable
    $ ./autogen.sh
    $ ./configure --prefix=/Users/apple/APP_PRJ/m_memcached/libevent_git/install
    $ make -j8 && make install

### memcached 源码编译

	$ cd /Users/apple/APP_PRJ/m_memcached/
	$ git clone https://github.com/memcached/memcached.git memcached_git
	$ cd memcached_git
	$ git checkout 1.4.15
	$ ./autogen.sh
	$ ./configure --with-libevent=../libevent_git/install
	$ make -j8

### memcached 运行

	$ cd /Users/apple/APP_PRJ/m_memcached/memcached_git
    $ export DYLD_LIBRARY_PATH=/Users/apple/APP_PRJ/m_memcached/libevent_git/install/lib/:$DYLD_LIBRARY_PATH
    $ ./memcached -h
    ```
		memcached 1.4.15
		... ...
	```
	$ make test

## REF

* [Macos动态库加载分析](http://liang8305.github.io/mac/ios/macos%E5%8A%A8%E6%80%81%E5%BA%93%E5%8A%A0%E8%BD%BD%E5%88%86%E6%9E%90/)


