---

# Redis 突击强化笔记 [2013.09.04 21:00]

之前对 Redis 的了解是，她是非常不错的 key-value nosql 类数据库。Redis 支持的数据结构比较丰富。知道的东西都比较的笼统模糊。使用方面也只是停留在源码编译，然后通过 `redis-cli` 做过简单的操作。简单的浏览过 `redis-py` 和 `tornado-redis` 的代码。

翻出之前读过的一篇文章[如何熟悉一个开源项目？](http://www.blogjava.net/killme2008/archive/2012/05/22/378885.html)。觉得写的非常不错打算照着实践一下。

上面 Redis REF 中的链接都是非常不错的资料，之前都没有细看。

* 浏览一遍 [Redis documentation](http://redis.io/documentation)，基本知道后续看那些文章。
* 阅读 [Data types](http://redis.io/topics/data-types)
* 阅读 [15 minutes introduction to Redis data types](http://redis.io/topics/data-types-intro)
* 阅读 [Writing a simple Twitter clone with PHP and Redis](http://redis.io/topics/twitter-clone)
* https://code.google.com/p/redis/downloads/list 下载早期代码(github 中的代码库包含早期版本)及 retwis-0.3.tar.gz 实例代码。      测试代码的运行[TODO]。

* 源码下载，编译，单元测试
	$ git clone git@github.com:antirez/redis.git
	$ cd redis
	$ git checkout v2.0.4-stable
	$ find ./ | grep '\.c$' | xargs wc -l | grep total
	    ``` 17474 total ```
	$ make -j8
	$ make test

* 阅读 [The Little Redis Book](http://openmymind.net/2012/1/23/The-Little-Redis-Book/)
* 阅读 [Redis 设计与实现](http://www.redisbook.com/en/latest/index.html) 浏览完毕，原计划晚上看完的，到十二点的时候还有最后几个小节没看，实在太困，眯了一会儿后，被外面的敲门声吵醒，起来继续看。
看完之后对 Redis 的内部实现有了大致的了解。图文并貌，条理清晰，很不错的一份文档。

* 阅读 [Connections Handling](http://redis.io/topics/clients)
* 阅读 [Signals Handling](http://redis.io/topics/signals)
* 阅读 [Redis Administration](http://redis.io/topics/admin)
* 阅读 [Redis Persistence](http://redis.io/topics/persistence)
    * TO READ [Redis persistence demystified](http://oldblog.antirez.com/post/redis-persistence-demystified.html)
* 阅读 [Replication](http://redis.io/topics/replication)
* 阅读 [Redis Internals documentation](http://redis.io/topics/internals)
	* 阅读 [Hacking Strings the Redis String implementation](http://redis.io/topics/internals-sds): 巧妙的指针处理，使得 `sds *` 兼容 `char *`
	* 阅读 [virtual memory implementation details](http://redis.io/topics/internals-vm)
	* 阅读 [Event Library](http://redis.io/topics/internals-eventlib)
		* TO READ [why Redis uses its own event library](https://groups.google.com/forum/#!topic/redis-db/tSgU6e8VuNA)
	* 阅读 [Redis Event Library](http://redis.io/topics/internals-rediseventlib)
