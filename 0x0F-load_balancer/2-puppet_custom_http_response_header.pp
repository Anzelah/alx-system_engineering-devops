# Edit your configuration file to do as task 2 above, but this time using puppet

include stdlib
file_line { 'Custom http header':
  path    => '/etc/haproxy/haproxy.cfg',
  line    => 'frontend http
        bind *:80
        mode http
        default_backend web-backend

	backend web-backend
        balance roundrobin
        server web-01 54.210.88.27:80 check
        server web-02 52.91.117.155:80 check',
  replace => true
}
