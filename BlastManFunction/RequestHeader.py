# -*- coding: utf-8 -*-

def RequestHeader(request_file, ssl_variable):
	request_dict = {}
	head_dict = {}
	#data_dict = {}
	request_dict["header"] = head_dict
	#request_dict["data_dict"] = data_dict

	head_list = request_file.splitlines()

	ls1 = head_list[1].split(" ")
	ls2 = head_list[0].split(" ")

	request_dict["success_logname"] = ls1[1] +"_success.txt"
	request_dict["error_logname"] = ls1[1] + "_error.txt"
	request_dict["error_dict"] = ls1[1] + "_error_dict.txt"

	if ssl_variable:
		request_dict["url"] = "https://"+ls1[1]+ls2[1]
	else:
		request_dict["url"] = "http://"+ls1[1]+ls2[1]

	if ls2[0] == "GET":
		request_dict["method"] = "GET"
		for line in head_list[1:]:
			if not line.isspace() and len(line) > 0 and not line.startswith("Content-Length"):
				ls = line.split(':',1)
				head_dict[str(ls[0].strip())] = str(ls[1].strip())

	if ls2[0] == "POST":
		request_dict["method"] = "POST"
		bo = False
		for line in head_list[1:]:
			if not line.isspace() and not bo and len(line) > 0:
				if not line.startswith("Content-Length"):
					ls = line.split(':',1)
					head_dict[str(ls[0].strip())] = str(ls[1].strip())
			elif bo and not line.isspace() and len(line) > 0:
				'''if line.find("&") != -1:
					line_list = line.split("&")
				for line_line in line_list:
					line_line_list = line_line.split("=")
					data_dict[str(line_line_list[0])] = str(line_line_list[1])'''
				request_dict["data"] = line
			else:
				bo = True
				continue
		
	return request_dict
