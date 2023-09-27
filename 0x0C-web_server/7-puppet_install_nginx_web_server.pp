# Edit your configuration file to do as task 3 above, but this time using puppet

include stdlib

package { 'nginx':
provider => 'apt',
}

exec { 'hello'
  command => '/usr/bin/sudo echo Hello World! /var/www/html/index.html'
}

exec { 'redirect_page':
  command => '/usr/bin/sudo /bin/sed/ -i "30i location/redirect_me / {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}"/etc/nginx/sites-available/default'
}

exec { 'start_server':
  command => '/usr/bin/sudo /usr/sbin/service nginx start'
}
