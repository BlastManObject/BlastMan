# -*- coding: utf-8 -*-

from BlastManFunction.ValueMode import DoubleValueModeJudge
from BlastManFunction.ValueMode import SingleValueModeJudge

def ValueJudge(value_dict):
	errors = {}
	errors["type_status"] = None
	errors["type_content"] = None
	errors["type_response"] = None

	if value_dict["request_file"] is None:
		print("Request file column cannot be empty,-f option")
		sys.exit()
	else:
		try:
			fopen = open(value_dict["request_file"], "r")
			fopen.close()
		except OSError:
			print("Request file error,-f option")
			sys.exit()	

	if value_dict["errors_content"] is None and value_dict["errors_status"] is None and value_dict["errors_response"] is None:
		print("No error mark,-e or -E option")
		sys.exit()
	else:
		if value_dict["errors_content"] is not None:
			errors["type_content"] = "errors_content"
			errors["value_content"] = value_dict["errors_content"]
		if value_dict["errors_status"] is not None:
			errors["type_status"] = "errors_status"
			errors["value_status"] = value_dict["errors_status"]
		if value_dict["errors_response"] is not None:
			errors["type_response"] = "errors_response"
			errors["value_response"] = value_dict["errors_response"]
	
	value_dict["errors_mark"] = errors

	if value_dict["single_variable"]:
		return SingleValueModeJudge.SingleValueModeJudge(value_dict)
	else:
		return DoubleValueModeJudge.DoubleValueModeJudge(value_dict)
	
