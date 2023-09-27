# Edit your configuration file to do as task 3 above, but this time using puppet

package {'nginx':
  ensure   => present,
  provider => 'apt',
}

exec { 'installation':
  command => 'sudo apt-get -y update; sudo apt-get install nginx',
}

exec { 'hello':
  command => 'echo "Hello World!" > /var/www/html/index.html'
}

exec { 'redirect_page':
  command => 'sudo sed -i "listen 80 default_server;\\n\t30i location/redirect_me / {\\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;} "/etc/nginx/sites-available/default'
}

exec { 'start_server':
  command => 'sudo service nginx start'
}
