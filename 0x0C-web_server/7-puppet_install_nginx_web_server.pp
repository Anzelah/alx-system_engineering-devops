# Edit your configuration file to do as task 3 above, but this time using puppet

package { 'nginx':
  ensure => 'installed',
}

file {'/var/www/html/index.html':
  ensure  => file,
  path    => '/var/www/html/index.html'
  content => 'Hello World!'
  require => File['/var/www/html/index.html']
}

file { 'redirect_me':
  ensure  => file,
  path    => '/etc/nginx/sites-available/default'
  content => '30i location/redirect_me / {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4:}'
  require => File['/etc/nginx/sites-available/default']
}
