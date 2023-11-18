# fix server failing under pressure
exec { 'limit':
  onlyif  => 'test -e /etc/default/nginx/',
  command => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx; sudo service nginx restart',
}
