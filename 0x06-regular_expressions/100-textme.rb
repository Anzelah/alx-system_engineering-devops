#!/usr/bin/env ruby
puts ARGV[0].scan(/[^+?\d+|(\w\.)*(^+\d$?)$],[^+?\d+|(\w\.)*(^+\d$?)$],[gim]/).join
