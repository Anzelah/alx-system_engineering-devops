# Edit your configuration file to do as task 2 above, but this time using puppet

include stdlib
file_line { 'Remove password':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true
}

file_line { 'Change source file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true
}
