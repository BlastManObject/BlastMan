# -*- coding: utf-8 -*-

import threading
import time

from BlastManCore import BlastRequest
from BlastManFunction import RequestHeader

class Single_ThreadBlast(threading.Thread):
	def __init__(self, request_content, errors_mark_dict, verbose, blast_dict, thread_id, timeout, number_of_times, mark_single_variable, mark_single_Greater_than_0, mark_single_variable_Greater_than_0, ssl_variable, username_variable, find_stop, break_time):
		threading.Thread.__init__(self)
		self.request_content = request_content
		self.errors_mark_dict = errors_mark_dict
		self.verbose = verbose
		self.blast_dict = tuple(blast_dict)
		self.thread_id = thread_id
		self.timeout = timeout
		self.number_of_times = number_of_times
		self.mark_single_variable = mark_single_variable
		self.mark_single_Greater_than_0 =  mark_single_Greater_than_0
		self.mark_single_variable_Greater_than_0 = mark_single_variable_Greater_than_0
		self.ssl_variable = ssl_variable
		self.username_variable = username_variable
		self.find_stop = find_stop
		self.break_time = break_time

	def run(self):
		bo = False
		send = BlastRequest.BlastRequest(self.errors_mark_dict, self.verbose, self.timeout, self.number_of_times, self.break_time)

		for dic in self.blast_dict:
			new_request_content = ""
			try:
				dic = dic.decode(encoding = "utf-8").strip()
				if not self. mark_single_Greater_than_0:
					new_request_content = self.request_content.replace(self.mark_single_variable, dic)
				else:
					lists = self.mark_single_variable_Greater_than_0.split(self.mark_single_variable)
					num = 1
					for line in lists:
						num += 1
						if num < len(lists):
							new_request_content = new_request_content + line + self.mark_single_variable
						elif num == len(lists):
							new_request_content = new_request_content + line + dic
					request_content_list = self.request_content.split(self.mark_single_variable_Greater_than_0)
					new_request_content = new_request_content + request_content_list[1]
			except:
				print("%s %s" % ("Data exception: ", dic))

			new_request_content = new_request_content.strip().strip("\r").strip("\n")
			request_content_dict = RequestHeader.RequestHeader(new_request_content, self.ssl_variable)
			bo = send.sendrequest(request_content_dict, dic, new_request_content)
			send.recording(bo, new_request_content, request_content_dict,dic, self.username_variable, self.find_stop)
			time.sleep(self.break_time)













