
nginx 的 command 是如何被执行的，在哪些阶段执行
nginx 的模块机制是基于什么原理


static ngx_command_t ngx_http_uwsgi_commands[] = {
    { ngx_string("uwsgi_pass"),
      NGX_HTTP_LOC_CONF|NGX_HTTP_LIF_CONF|NGX_CONF_TAKE1,
      ngx_http_uwsgi_pass,
      NGX_HTTP_LOC_CONF_OFFSET,
      0,
      NULL },
}

static char *
ngx_http_uwsgi_pass(ngx_conf_t *cf, ngx_command_t *cmd, void *conf)
{
    clcf->handler = ngx_http_uwsgi_handler;
}
ngx_http_uwsgi_merge_loc_conf(ngx_conf_t *cf, void *parent, void *child)
{
    clcf->handler = ngx_http_uwsgi_handler;
}

ngx_http_uwsgi_handler
    -> ngx_http_upstream_create
    -> ngx_http_upstream_init
