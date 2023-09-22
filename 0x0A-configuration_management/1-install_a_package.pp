# Install flask package from pip3

package { 'openflask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
