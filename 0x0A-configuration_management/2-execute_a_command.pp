# Kill a process

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pkill -f killmenow'
}
