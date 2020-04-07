# -*- coding: utf-8 -*-

from BlastManCore import SingleBlast

class DoubleBlast(object):
	def __init__(self,value_dict):
		self.request_file = value_dict["request_file"]
		self.mark_username = value_dict["mark_username"]
		self.username_dic_file = value_dict["value_username"]
		self.verbose = value_dict["verbose"]
		value_dict["mark_single_variable"] = value_dict["mark_password"]
		value_dict["single_variable_file"] = value_dict["value_password"]

		fopen = open(self.request_file)
		self.request_content = fopen.read().strip().strip("\r").strip("\n")
		fopen.close()

		with open(self.username_dic_file, "rb") as f:
			for line in f:
				line = line.decode(encoding = "utf-8").strip()
				new_request_content = self.request_content.replace(self.mark_username, line)
				value_dict["new_request_content"] = new_request_content
				value_dict["username_variable"] = line
				if self.verbose:
					print("%s%s" % ("\r\n\r\nStart blasting, Username: ",line))
				SingleBlast.SingleBlast(value_dict)


