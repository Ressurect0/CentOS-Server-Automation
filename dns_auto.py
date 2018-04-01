# The current program 1. Adds a new zone in the dns server which can be accessed by Host2 by making changes in its nameserver[/etc/resolv.conf]
import os, datetime
os.system("yum install -y bind bind-utils")
os.system("systemctl start named")
while(True):
	user_input = input("1. Add a new zone\n2.Exit\n")
	if user_input == 1:
		domain = raw_input("Enter the domain: ")
		zone_filename = domain + "-zone"
		#host2 = raw_input("Enter the IP of host: ");
		os.system("touch /var/named/" + zone_filename)
		file2 = open("/etc/named.conf","a")
		file2.write('zone "'+domain+'" IN {\n'+'\ttype master;\n'+'\tfile "'+zone_filename+'";\n')
		file2.close()
		
		# Necessary values for zone files.
		# These values will be stored in a temporary config before getting 
		# properly formatted.
		temp_conf = []
		ask = raw_input("TTL value: 2D OK(Enter)?\n")
		if ask == "":
			temp_conf.append("2D")
		else:
			temp_conf.append(ask)
		#nameserver temp_conf[1]
		temp = "ns." + domain + "."
		ask = raw_input("nameserver: "+temp+" OK(Enter)?\n")
		if ask == "":
			temp_conf.append(temp)
		else:
			temp_conf.append(ask)
		temp = "root." + domain + "."
		ask = raw_input("root user Email ID: "+temp+" OK(Enter)?\n")
		if ask == "":
			temp_conf.append(temp)
		else:
			temp_conf.append(ask)
		now = datetime.datetime.now()
		temp = str(now.year) + str(now.month) + str(now.date) + "01"
		temp_conf.append(temp)
		ask = raw_input("refresh: 1D OK(Enter)?\n")
		if ask == "":
			temp_conf.append("1D")
		else:
			temp_conf.append(ask)
		ask = raw_input("retry: 1H OK(Enter)?\n")
		if ask == "":
			temp_conf.append("1H")
		else:
			temp_conf.append(ask)
		ask = raw_input("expire: 1W OK(Enter)?\n")
		if ask == "":
			temp_conf.append("1W")
		else:
			temp_conf.append(ask)
		ask = raw_input("minimum: 3H OK(Enter)?\n")
		if ask == "":
			temp_conf.append("3H")
		else:
			temp_conf.append(ask)
		# mail server = temp_conf[8]
		temp = "mail." + domain + "."
		ask = raw_input("mail server: "+ temp +"OK(Enter)?\n")
		if ask == "":
			temp_conf.append(temp)
		else:
			temp_conf.append(ask)
		# mail server priority = temp_conf[9]
		ask = raw_input("mail server priority: 10 OK(Enter)?\n")
		if ask == "":
			temp_conf.append("10")
		else:
			temp_conf.append(ask)
		#temp_conf[9,10,11] = [NS,MX,www]
		temp_conf.append(raw_input("Enter nameservers IP: "))
		temp_conf.append(raw_input("Enter mail servers IP: "))
		temp_conf.append(raw_input("ENter web servers IP: "))
		
		# Proper formatting for zone files
		zone_conf = []
		zone_conf.append("$TTL " + temp_conf[0])
		zone_conf.append("@\tIN\tSOA\t" + temp_conf[1] + "\t" + temp_conf[2] + "(")
		zone_conf.append("\t\t\t\t"+temp_conf[3])
		zone_conf.append("\t\t\t\t"+temp_conf[4])
		zone_conf.append("\t\t\t\t"+temp_conf[5])
		zone_conf.append("\t\t\t\t"+temp_conf[6])
		zone_conf.append("\t\t\t\t"+temp_conf[7] + ")")
		zone_conf.append("@\tIN\tNS\t" + temp_conf[1])
		zone_conf.append("@\tIN\tMX\t" + temp_conf[9] + "\t" + temp_conf[8])
		zone_conf.append("ns\tA\t"+temp_conf[9])
		zone_conf.append("mx\tA\t"+temp_conf[10])
		zone_conf.append("www\tA\t"+temp_conf[11])		
		
		
		# Writing to the zone file		
		file3 = open("/var/named/"+zone_filename,"w")
		for line in zone_conf:
			file3.write(line)
		os.system("systemctl restart named")
	if user_input == 2:
		exit(0)

#file1 = open("a.txt","r")
#filedata_list = file.read().split("\n")
#filedata_list = filedata_list[:-1]

