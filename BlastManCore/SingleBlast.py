# -*- coding: utf-8 -*-

from BlastManCore.SingleBlastCore import Single_ThreadBlast

class SingleBlast(object):
	def __init__(self,value_dict):
		self.request_file = value_dict["request_file"]
		self.errors_mark_dict = value_dict["errors_mark"]
		self.thread = value_dict["thread"]
		self.verbose = value_dict["verbose"]
		self.mark_single_variable = value_dict["mark_single_variable"]
		self.single_variable_file = value_dict["single_variable_file"]
		self.ssl_variable = value_dict["ssl_variable"]
		self.timeout = value_dict["timeout"]
		self.number_of_times = value_dict["number_of_times"]
		self.mark_single_Greater_than_0 = value_dict["mark_single_Greater_than_0"]
		self.mark_single_variable_Greater_than_0 = value_dict["mark_single_variable_Greater_than_0"]
		self.single_variable = value_dict["single_variable"]
		self.find_stop = value_dict["find_stop"]
		self.break_time = value_dict["break_time"]

		self.blast_list = []
		self.thread_list = []
		self.thread_count = 0

		if self.single_variable:
			fopen = open(self.request_file)		
			self.request_content = fopen.read()
			fopen.close()
			self.username_variable = None
		else:
			self.request_content = value_dict["new_request_content"]
			self.username_variable = value_dict["username_variable"]

		self.blastthread_start()

	def blastthread_start(self):
		thread_id = 0

		with open(self.single_variable_file, "rb") as f:
			for line in f:	
				self.blast_list.append(line)
				if len(self.blast_list) % 50 == 0 and self.thread_count == self.thread:
					if thread_id+1 >= self.thread:
						thread_id = 0
					else:
						thread_id += 1
					self.thread_list[thread_id].join()
					self.blastthread_update(thread_id)
				elif len(self.blast_list) % 50 == 0 and self.thread_count < self.thread:
					self.blastthread_creat(thread_id)
					self.thread_count += 1
					thread_id += 1
		self.blastthread_creat(self.thread_count)
		for line in self.thread_list:
			line.join()

	def blastthread_creat(self, thread_id):
		self.thread_list.append(Single_ThreadBlast.Single_ThreadBlast(self.request_content, self.errors_mark_dict, self.verbose, self.blast_list, thread_id, self.timeout, self.number_of_times, self.mark_single_variable, self.mark_single_Greater_than_0, self.mark_single_variable_Greater_than_0, self.ssl_variable, self.username_variable, self.find_stop, self.break_time))
		self.blast_list.clear()
		self.thread_list[thread_id].start()

	def blastthread_update(self, thread_id):
		self.thread_list[thread_id] = Single_ThreadBlast.Single_ThreadBlast(self.request_content, self.errors_mark_dict, self.verbose, self.blast_list, thread_id, self.timeout, self.number_of_times, self.mark_single_variable, self.mark_single_Greater_than_0, self.mark_single_variable_Greater_than_0, self.ssl_variable, self.username_variable, self.find_stop, self.break_time)
		self.blast_list.clear()
		self.thread_list[thread_id].start()
