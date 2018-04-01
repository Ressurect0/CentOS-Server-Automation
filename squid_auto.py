import os
rules = ["ip","src","dst","srcdomain","dstdomain","url_regex","time"]
rule_line = ""
rule_set = raw_input("Enter the Rule set: ")
while(True):
	counter = 0
	print "0. Exit"
	for rule in rules:
		print str(counter+1)+". "+rules[counter]  
	if n == 0:
		break
	else:
		n = input("Select the Rule to append in /etc/squid/squid.conf")
		temp = raw_input("Enter the required parameter value: ")	
		file = open("/etc/squid/squid.conf","a")	
		rule_line = "acl " + rule_set + " src " + temp
		file.write(rule_line)
		file.write("http_access " + rule_set +" deny")

