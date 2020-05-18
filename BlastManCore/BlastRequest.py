# -*- coding: utf-8 -*-

import requests
import os

class BlastRequest(object):
	def __init__(self, errors_mark_dict, verbose, timeout, number_of_times):
		try:
			self.errors_mark_dict = errors_mark_dict
			self.verbose = verbose
			self.timeout = timeout
			self.number_of_times = number_of_times
			self.logPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/log/"
			self.bo = ("out_time","success","failure")
			
		except:
			print("Data exception")

	def sendrequest(self, request_content_dict, dic, new_request_content):
		method_this = request_content_dict["method"]
		header_this = request_content_dict["header"]
		url_this = request_content_dict["url"]
		data_this = request_content_dict["data"].encode("utf-8")

		try:
			i = 0
			while i < self.number_of_times:
				try:
					if method_this == "POST":
						req = requests.post(url_this, data=data_this, headers=header_this, timeout=self.timeout, allow_redirects=False)
					if method_this == "GET":
						req = requests.get(url_this, headers=header_this, timeout=self.timeout , allow_redirects=False)					
					break
				except requests.exceptions.RequestException as e:
					i += 1
					if i == self.number_of_times:
						return self.bo[0]
			if self.verbose:
				print("%s %s%s" % (dic,"--Response status code:",req.status_code))

			if self.errors_mark_dict["type_status"] == None and self.errors_mark_dict["type_response"] == None and self.errors_mark_dict["type_content"] != None:
				if req.text.find(self.errors_mark_dict["value_content"]) == -1:
					return self.success(dic,req.status_code)

			elif self.errors_mark_dict["type_status"] != None and self.errors_mark_dict["type_response"] == None and self.errors_mark_dict["type_content"] == None:		
				if req.status_code != self.errors_mark_dict["value_status"]:
					return self.success(dic,req.status_code)

			elif self.errors_mark_dict["type_status"] == None and self.errors_mark_dict["type_response"] != None and self.errors_mark_dict["type_content"] == None:
				header_content = ""
				for dic in req.headers:
					header_content = header_content + dic + ":" + req.headers[dic] + "\n"
				if header_content.find(self.errors_mark_dict["value_response"]) == -1:
					return self.success(dic,req.status_code)

			elif self.errors_mark_dict["type_status"] != None and self.errors_mark_dict["type_content"] != None and self.errors_mark_dict["type_response"] == None:
				if req.text.find(self.errors_mark_dict["value_content"]) == -1 and req.status_code != self.errors_mark_dict["value_status"]:
					return self.success(dic,req.status_code)

			elif self.errors_mark_dict["type_status"] == None and self.errors_mark_dict["type_content"] != None and self.errors_mark_dict["type_response"] != None:
				header_content = ""
				for dic in req.headers:
					header_content = header_content + dic + ":" + req.headers[dic] + "\n"
				if header_content.find(self.errors_mark_dict["value_response"]) == -1 and req.text.find(self.errors_mark_dict["value_content"]) == -1:
					return self.success(dic,req.status_code)

			elif self.errors_mark_dict["type_status"] != None and self.errors_mark_dict["type_content"] == None and self.errors_mark_dict["type_response"] != None:
				header_content = ""
				for dic in req.headers:
					header_content = header_content + dic + ":" + req.headers[dic] + "\n"
				if header_content.find(self.errors_mark_dict["value_response"]) == -1 and req.status_code != self.errors_mark_dict["value_status"]:
					return self.success(dic,req.status_code)

			elif self.errors_mark_dict["type_status"] != None and self.errors_mark_dict["type_content"] != None and self.errors_mark_dict["type_response"] != None:
				header_content = ""
				for dic in req.headers:
					header_content = header_content + dic + ":" + req.headers[dic] + "\n"
				if header_content.find(self.errors_mark_dict["value_response"]) == -1 and req.status_code != self.errors_mark_dict["value_status"] and req.text.find(self.errors_mark_dict["value_content"]) == -1:
					return self.success(dic,req.status_code)

			else:
				if self.verbose:
					print("%s %s%s %s" % (dic,"--Response status code:",req.status_code,"--FAILURE"))
				return self.bo[2]

		except:
				filename = self.logPath + request_content_dict["error_logname"]
				fopen = open(filename,"a")
				fopen.write("%s %s%s" % ("I did not detect it successfully:",dic,"\r\n\r\n\r\n"))
				fopen.write(new_request_content)
				fopen.close()
				print("Request except,Please check your configuration. Program error location is at 'BlastRequest'")

	def recording(self, bo, new_request_content, request_content_dict, dic, username_variable, find_stop):
		if bo == "success":
			filename = self.logPath + request_content_dict["success_logname"]
			fopen = open(filename,"a")
			fopen.write(new_request_content+"\r\n\r\n\r\n")
			fopen.close()
			if find_stop:
				os._exit(1)
		elif bo == "out_time":
			filename = self.logPath + request_content_dict["error_logname"]
			fopen = open(filename,"a")
			fopen.write("out time: \r\n")
			fopen.write(new_request_content+"\r\n\r\n\r\n")
			fopen.close()
			if username_variable != None:
				dic = username_variable + "\t" + dic
			filename = self.logPath + request_content_dict["error_dict"]
			fopen = open(filename,"a")
			fopen.write(dic+"\r\n")
			fopen.close()
			print("%s%s" % (dic,"--Existence timeout,please check the log."))

	def success(self, dic, status_code):
		print("\033[1;32;40m\tThere are new findings, please check the log.\033[0m")
		print("%s %s%s %s" % (dic," --Response status code:",status_code,"--SUCCESS"))
		return self.bo[1]

