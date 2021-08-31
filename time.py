#Given that days = 17, hours = 23, minutes = 17, seconds = 45. Display the total number of seconds in the above duration.

#Solution

#Given that 60seconds = 1minutes, 3600seconds = 1hr, 86400seconds = 1 day

days = 17 * 86400
hours = 23 * 3600
minutes = 17 * 60
seconds = 45
total_number_of_seconds = days + hours + minutes + seconds
print(total_number_of_seconds)

