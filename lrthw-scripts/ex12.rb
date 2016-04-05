print "Give me a number: "
number = gets.chomp.to_i

bigger = number * 100
puts "A bigger number is #{bigger}."

print "Give me another number: "
another = gets.chomp
number = another.to_f

smaller = number / 100
puts "A smaller number is #{smaller}."

# puts adds a new line to the end, print doesn't

puts "Give me some money"
print "> £"
money = gets.chomp.to_f
change = money * 0.1
puts "Here's your change £#{change}"
