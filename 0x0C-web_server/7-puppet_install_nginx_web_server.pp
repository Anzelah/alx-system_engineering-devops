# Edit your configuration file to do as task 3 above, but this time using puppet


package {'nginx':
  ensure   => installed,
  provider => 'apt',
}

#exec { 'installation':
#  command => 'sudo apt-get -y update; sudo apt-get install nginx',


exec { 'hello':
  command => '/usr/bin/sudo echo "Hello World!" > /var/www/html/index.html'
}

exec { 'redirect_page':
  command => '/usr/bin/sudo /bin/sed/ -i "listen 80 default_server;\\n\t30i location/redirect_me / {\\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;} "/etc/nginx/sites-available/default'
}

exec { 'start_server':
  command => '/usr/bin/sudo /usr/bin/ service nginx start'
}
