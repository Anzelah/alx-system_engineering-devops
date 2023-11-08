# change the extension from .phpp to php
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => 'file',
  source => '/var/www/html/wp-includes/class-wp-locale.php',
}
