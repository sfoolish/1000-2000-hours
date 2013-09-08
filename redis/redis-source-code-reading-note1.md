## redis 代码阅读笔记

### 阅读版本 2.6.9
	$ git clone git@github.com:antirez/redis.git
	$ cd redis
	$ git checkout 2.6.9

	$ cd src && make -j8
	$ make test

#### 测试代码的进一步说明

redis 的绝大多少的测试代码在代码树的 `tests` 目录下用 tcl 脚步实现，一小部分单元测试代码直接内嵌在 `.c` 文件中，如 `ziplist.c`， `zipmap.c` 等。

`runtest` 脚本的简单使用记录：

    $ ./runtest --help
    ```
        /usr/bin/tclsh8.5
        --valgrind         Run the test over valgrind.
        --accurate         Run slow randomized tests for more iterations.
        --quiet            Don't show individual tests.
        --single <unit>    Just execute the specified unit (see next option).
        --list-tests       List all the available test units.
        --clients <num>    Number of test clients (16).
        --force-failure    Force the execution of a test that always fails.
        --help             Print this help screen.
    ```
    $ ./runtest --list-tests
    ```
        /usr/bin/tclsh8.5
        unit/printver
        ... ...
    ```
    $ ./runtest --single unit/printver
    ```
        /usr/bin/tclsh8.5
        Cleanup: may take some time... OK
        Starting test server at port 11111
        
        Testing unit/printver
        
        ... ...
        
        Execution time of different units:
          0 seconds - unit/printver
        
        \o/ All tests passed without errors!
        
        Cleanup: may take some time... OK
    ```

ziplist.c 单元测试代码运行

	$ git diff
	```
        diff --git a/src/redis.c b/src/redis.c
        index 23083fb..d86e173 100644
        --- a/src/redis.c
        +++ b/src/redis.c
        @@ -2528,7 +2528,7 @@ void redisOutOfMemoryHandler(size_t allocation_size) {
             redisPanic("OOM");
         }
         
        -int main(int argc, char **argv) {
        +int __main(int argc, char **argv) {
             struct timeval tv;
         
             /* We need to initialize our libraries, and the server configuration. */
        diff --git a/src/ziplist.c b/src/ziplist.c
        index d4ac4f9..e439f5d 100644
        --- a/src/ziplist.c
        +++ b/src/ziplist.c
        @@ -951,6 +951,7 @@ void ziplistRepr(unsigned char *zl) {
             printf("{end}\n\n");
         }
         
        +#define ZIPLIST_TEST_MAIN
         #ifdef ZIPLIST_TEST_MAIN
         #include <sys/time.h>
         #include "adlist.h"
    ```
    $ make -j8
    $ ./redis-server
    ```
        {total bytes 75} {length 6}
        {tail offset 44}
        
        ... ...
        
        List size:    15872, bytes:    95243, 100000x push+pop (TAIL): 439907 usec
        List size:    16128, bytes:    96779, 100000x push+pop (TAIL): 425798 usec
    ```
