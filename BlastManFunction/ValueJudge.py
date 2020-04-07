# -*- coding: utf-8 -*-

from BlastManFunction.ValueMode import DoubleValueModeJudge
from BlastManFunction.ValueMode import SingleValueModeJudge

def ValueJudge(request_file, ssl_variable, single_variable, single_variable_file, errors_content, errors_status, errors_response, mark_single_variable, mark_username, mark_password, thread, username_file, password_file, verbose, timeout, number_of_times, find_stop):

	value_dict = {}
	errors = {}
	errors["type_status"] = None
	errors["type_content"] = None
	errors["type_response"] = None

	if request_file is None:
		print("Request file column cannot be empty,-f option")
		sys.exit()
	else:
		try:
			fopen = open(request_file, "r")
			fopen.close()
		except OSError:
			print("Request file error,-f option")
			sys.exit()	

	if errors_content is None and errors_status is None and errors_response is None:
		print("No error mark,-e or -E option")
		sys.exit()
	else:
		if errors_content is not None:
			errors["type_content"] = "errors_content"
			errors["value_content"] = errors_content
		if errors_status is not None:
			errors["type_status"] = "errors_status"
			errors["value_status"] = errors_status
		if errors_response is not None:
			errors["type_response"] = "errors_response"
			errors["value_response"] = errors_response
	
	value_dict["request_file"] = request_file
	value_dict["errors_mark"] = errors
	value_dict["thread"] = thread
	value_dict["verbose"] = verbose
	value_dict["ssl_variable"] = ssl_variable
	value_dict["timeout"] = timeout
	value_dict["number_of_times"] = number_of_times
	value_dict["single_variable"] = single_variable
	value_dict["find_stop"] = find_stop

	if single_variable:
		return SingleValueModeJudge.SingleValueModeJudge(request_file, mark_single_variable, single_variable_file, value_dict)
	else:
		return DoubleValueModeJudge.DoubleValueModeJudge(request_file, mark_username, mark_password, username_file, password_file, value_dict)

	
