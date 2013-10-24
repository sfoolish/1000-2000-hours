## 源码编译 nginx + lua(luajit)
    
    $ cd nginx_lua_sf
    $ tar xvf LuaJIT-2.0.2.tar.gz 
    $ mkdir -p ../install/luajit
    $ vim Makefile 
    ```
    - export PREFIX= /usr/local
    + export PREFIX= /Users/apple/APP_PRJ/c_nginx/nginx_lua_sf/install/luajit
    ```
    $ make -j8
    $ make install
    $ export LUAJIT_LIB=/Users/apple/APP_PRJ/c_nginx/nginx_lua_sf/install/luajit/lib
    $ export LUAJIT_INC=/Users/apple/APP_PRJ/c_nginx/nginx_lua_sf/install/luajit/include/luajit-2.0/
    
    $ tar xvf lua-nginx-module-0.9.0.tar.gz 
    $ tar xvf ngx_devel_kit-0.2.19.tar.gz 
    
    $ cd nginx-1.5.6
    $ ./configure \
        --add-module=../lua-nginx-module-0.9.0 \
        --add-module=../ngx_devel_kit-0.2.19 \
        --with-pcre=/Users/apple/APP_PRJ/c_nginx/pcre-8.30 \
        --with-debug \
        --prefix=/Users/apple/APP_PRJ/c_nginx/nginx_lua_sf/install/nginx
    
    $ make -j8
    $ make install

## REF

* [lua-nginx-module](https://github.com/chaoslawful/lua-nginx-module)
* [lua-nginx-module installation](https://github.com/chaoslawful/lua-nginx-module#installation)
* [Nginx与Lua](http://huoding.com/2012/08/31/156)

## OpenResty

### openresty-1.0.6.22

./configure --with-debug --with-pcre=/Users/apple/APP_PRJ/c_nginx/pcre-8.30 --with-luajit --with-http_iconv_module --prefix=/Users/apple/APP_PRJ/c_nginx/ngx_openresty-1.0.6.22/install_sf
make -j8
make install

[【开源访谈】OpenResty 作者章亦春访谈实录](http://www.oschina.net/question/28_60461)