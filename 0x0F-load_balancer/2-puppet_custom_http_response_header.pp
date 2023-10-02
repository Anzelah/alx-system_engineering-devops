# Edit your configuration file to do as task 2 above, but this time using puppet

exec { 'uppdate':
  command => '/usr/bin/apt-get update'
}

package {'nginx':
  ensure => present,
}

file_line { 'Custom header':
  path    => '/etc/nginx/sites-available/default'
  line    => '\\\tadd_header X-Served-By $HOSTNAME;'
  replace => true
}

exec { 'restart':
  command => '/usr/bin/service nginx restart'
}
