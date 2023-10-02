# Edit your configuration file to do as task 2 above, but this time using puppet

exec { 'update':
  command => '/usr/bin/apt-get update'
}

package {'nginx':
  ensure => 'present',
}

file_line { 'Custom http header':
  path    => '/etc/nginx/sites-available/default',
  line    => "server {\n\tadd_header X-Served-By $hostname;}"
}

exec { 'restart':
  command => '/usr/sbin/service nginx restart'
}
