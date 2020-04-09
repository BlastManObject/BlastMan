#!/usr/bin/python3
# -*- coding: utf-8 -*-
import optparse
import sys
import time

from BlastManFunction import ValueJudge
from BlastManCore import SingleBlast
from BlastManCore import DoubleBlast

def main():
	
	apiparser = optparse.OptionParser()
	apiparser.add_option("-f","--file",type="string",action="store",dest="request_file",help="File containing request header content")
	apiparser.add_option("-S","--ssl_variable",action="store_true",dest="ssl_variable",default=False,help="Https switch,default False,")
	apiparser.add_option("-C","--single_variable",action="store_true",dest="single_variable",default=False,help="Single variable mode,Only one test variable interface,Shared with -c option")
	apiparser.add_option("-c","--single_variable_file",type="string",action="store",dest="single_variable_file",help="Single variable mode,Only one test variable interface,Shared with -C option")
	apiparser.add_option("-e","--errors_content",type="string",action="store",dest="errors_content",help="Mark the error symbol in the returned content to determine if the content is correct. Note that newlines are not equal to spaces")
	apiparser.add_option("-E","--errors_status",type="int",action="store",dest="errors_status",help="Mark errors based on status code to determine if content is correct")
	apiparser.add_option("-R","--errors_response",type="string",action="store",dest="errors_response",help="Mark error symbols in returned response headers to determine if the content is correct")
	apiparser.add_option("-M","--mark_single_variable",type="string",action="store",dest="mark_single_variable",help="Mark the burst location of a single variable,Shared with -C option")	
	apiparser.add_option("-u","--markusername",type="string",action="store",dest="mark_username",help="Mark username variable burst location")
	apiparser.add_option("-U","--username_file",type="string",action="store",dest="username_file",help="Username list")	
	apiparser.add_option("-p","--markpassword",type="string",action="store",dest="mark_password",help="Mark password variable burst location")
	apiparser.add_option("-P","--password_file",type="string",action="store",dest="password_file",help="Password list")
	apiparser.add_option("-t","--thread",type="int",action="store",dest="thread",default="5",help="Number of concurrent threads,5 threads by default")
	apiparser.add_option("-T","--timeout",type="int",action="store",dest="timeout",default="5",help="Response waiting time,5 seconds by default")
	apiparser.add_option("-n","--number_of_times",type="int",action="store",dest="number_of_times",default="3",help="Maximum number of requests,3 times by default")
	apiparser.add_option("-X","--stop",action="store_true",dest="find_stop",default=False,help="Stop immediately after success")
	apiparser.add_option("-v","--verbose",action="store_true",dest="verbose",default=False,help="Show details")
	(options, args) = apiparser.parse_args()

	value_dict = ValueJudge.ValueJudge(options.request_file, options.ssl_variable, options.single_variable, options.single_variable_file, options.errors_content, options.errors_status, options.errors_response, options.mark_single_variable, options.mark_username, options.mark_password, options.thread, options.username_file, options.password_file, options.verbose, options.timeout, options.number_of_times, options.find_stop)

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
