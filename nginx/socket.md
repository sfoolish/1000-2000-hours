## socket opt

### SO_RCVLOWAT和SO_SNDLOWAT 

	// nginx-0.2.6
    ngx_int_t
    ngx_send_lowat(ngx_connection_t *c, size_t lowat)
    {
        sndlowat = (int) lowat;
        if (setsockopt(c->fd, SOL_SOCKET, SO_SNDLOWAT,
                                      (const void *) &sndlowat, sizeof(int)) == -1)
    }

每个套接口有一个接收低潮限度和一个发送低潮限度，他们由函数select使用。SO_RCVLOWAT和SO_SNDLOWAT这两个选项可以修改他们。 

接收低潮限度是让select返回“可读”而在套接口接收缓冲区中必须有的数据量，对于一个TCP或UDP套接口，此值缺省为1。发送低潮限度是让select返回“可写”而在套接口发送缓冲区中必须有的可用空间，对于TCP套接口，此值常为2048。
