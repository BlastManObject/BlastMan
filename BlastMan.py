#!/usr/bin/python3
# -*- coding: utf-8 -*-
import optparse
import sys
import time

from BlastManFunction import ValueJudge
from BlastManCore import SingleBlast
from BlastManCore import DoubleBlast

def main():
	
	value_dict = {}
	apiparser = optparse.OptionParser()
	group_Single = optparse.OptionGroup(apiparser, "Single variable mode","Use this mode when only one parameter needs to be tested")
	group_Double = optparse.OptionGroup(apiparser, "Double variable mode","Account password mode")
 
	apiparser.add_option("-f","--file",type="string",action="store",dest="request_file",help="File containing request header content")
	apiparser.add_option("-t","--thread",type="int",action="store",dest="thread",default="5",help="Number of concurrent threads,5 threads by default")
	apiparser.add_option("-n","--number_of_times",type="int",action="store",dest="number_of_times",default="3",help="Maximum number of requests,3 times by default")
	apiparser.add_option("-b","--break_time",type="int",action="store",dest="break_time",default="0",help="Time difference between requests,default is 0,Unit:second")
	apiparser.add_option("-e","--errors_content",type="string",action="store",dest="errors_content",help="Mark the error symbol in the returned content to determine if the content is correct. Note that newlines are not equal to spaces")
	apiparser.add_option("-E","--errors_status",type="int",action="store",dest="errors_status",help="Mark errors based on status code to determine if content is correct")
	apiparser.add_option("-R","--errors_response",type="string",action="store",dest="errors_response",help="Mark error symbols in returned response headers to determine if the content is correct")
	apiparser.add_option("-T","--timeout",type="int",action="store",dest="timeout",default="5",help="Response waiting time,5 seconds by default")
	apiparser.add_option("-S","--ssl_variable",action="store_true",dest="ssl_variable",default=False,help="Https switch,default False,")
	apiparser.add_option("-X","--stop",action="store_true",dest="find_stop",default=False,help="Stop immediately after success")
	apiparser.add_option("-v","--verbose",action="store_true",dest="verbose",default=False,help="Show details")

	group_Double.add_option("-u","--markusername",type="string",action="store",dest="mark_username",help="Mark username variable burst location")
	group_Double.add_option("-U","--username_file",type="string",action="store",dest="username_file",help="Username list,The default file is dict/Users.txt",default="dict/Users.txt")	
	group_Double.add_option("-p","--markpassword",type="string",action="store",dest="mark_password",help="Mark password variable burst location")
	group_Double.add_option("-P","--password_file",type="string",action="store",dest="password_file",help="Password list,The default file is dict/Password.txt",default="dict/Password.txt")
	apiparser.add_option_group(group_Double)

	group_Single.add_option("-C","--single_variable",action="store_true",dest="single_variable",default=False,help="Single variable mode,Only one test variable interface,Shared with -c option")
	group_Single.add_option("-c","--single_variable_file",type="string",action="store",dest="single_variable_file",help="Single variable mode,Only one test variable interface,Shared with -C option")
	group_Single.add_option("-M","--mark_single_variable",type="string",action="store",dest="mark_single_variable",help="Mark the burst location of a single variable,Shared with -C option")	
	apiparser.add_option_group(group_Single)

	(options, args) = apiparser.parse_args()

	value_dict["request_file"] = options.request_file
	value_dict["ssl_variable"] = options.ssl_variable
	value_dict["single_variable"] = options.single_variable
	value_dict["single_variable_file"] = options.single_variable_file
	value_dict["errors_content"] = options.errors_content
	value_dict["errors_status"] = options.errors_status
	value_dict["errors_response"] = options.errors_response
	value_dict["mark_single_variable"] = options.mark_single_variable
	value_dict["mark_username"] = options.mark_username
	value_dict["mark_password"] = options.mark_password
	value_dict["thread"] = options.thread
	value_dict["username_file"] = options.username_file
	value_dict["password_file"] = options.password_file
	value_dict["verbose"] = options.verbose
	value_dict["timeout"] = options.timeout
	value_dict["number_of_times"] = options.number_of_times
	value_dict["find_stop"] = options.find_stop
	value_dict["break_time"] = options.break_time

	value_dict = ValueJudge.ValueJudge(value_dict)

	print("\r\nThe program is about to start.If successful, it will be recorded in the log: BlastMan/log/")
	print("Error log: BlastMan/log/\r\n\r\n")
	print("The program will start in 10 seconds...\r\n")

	time.sleep(10)

	print("Program started,please wait...")

	if options.single_variable:
		SingleBlast.SingleBlast(value_dict)
	else:
		DoubleBlast.DoubleBlast(value_dict)
try:
	main()
except:
    	print("EXIT")
