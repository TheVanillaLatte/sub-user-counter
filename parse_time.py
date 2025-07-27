#!/usr/bin/python3

# Written and maintained by VanillaLatte. Please report any errors to him

import time
import json
import datetime
from collections import Counter


class PostParser:
	def __init__(self):
		with open('submissions.json', 'r') as f:
			self.data = json.load(f)

	def get_percentages(self, fd, as_file=False):
		"""
		Parse the json file and calculate percentages of posts by username (based on the hours given)
		It will count back from the current epoch to however many hours you enterered. I was going to use the date item
		already in each list in the dicts, but this is more precise. 

		Please note that the "fd" argument needs to be the data from the "get_epoch_data()" method. That method returns
		a dictionary with all the posts from the time-frame you selected.

		Also you can change the "as_file" argument either in the method definition above or at the bottom when calling the method.
		"""
		usernames = list()
		for post_id, post_info in fd.items():
			if len(post_info) >= 2:
				username = post_info[1]
				usernames.append(username)
			else:
				print(f"Warning: Post '{post_id}' has unexpected format, skipping username")  # Rare error, have not seen it yet in over 30 days of code running, but good to be safe

		username_counts = Counter(usernames)
		total_posts = len(usernames)

		percentage_by_username = dict()

		if total_posts == 0:
			print("No valid posts found to calculate percentages.")
		else:
			for username, count in username_counts.items():
				percentage = (count / total_posts) * 100
				percentage_by_username[username] = percentage

		# Magic
		sorted_users = sorted(
			percentage_by_username.items(),
			key=lambda item: item[1],
			reverse=True)

		if not as_file:
			print("Percentage of posts by username (Highest to Lowest)\n")
			for username, percentage in sorted_users:
				count = username_counts[username]
				print(f"- {username}: {percentage:.2f}% ({count} posts)")
		if as_file:
			with open('output.txt', 'w') as f:  # Change this to whatever dir you want I guess
				f.write("Percentage of posts by username (Highest to Lowest)\n\n")
				for username, percentage in sorted_users:
					count = username_counts[username]
					f.write(f"- {username}: {percentage:.2f}% ({count} posts)\n")
			print('File saved to current directory')

	def get_epoch_data(self):
		"""
		This method is the main interface. User is prompted to enter how many hours they would like to go back. The epoch range
		is calculated, and any item within that range is used as new data. When entering hours, if 0 is entered, it will start
		from the beginning of the submissons.json file. So use 0 for ALL data
		"""
		while True:
			current_epoch_seconds = int(time.time())
			try:
				hours_to_go_back = int(input('Enter the number of WHOLE hours to go back: '))  # TODO: Add options for days/weeks as well. Add date ranges too
				if hours_to_go_back == 0:
					return self.data
			except ValueError as e:
				print(f'Error {e}: Please use only whole number values.')  # For some reason PRAW "created_utc" attribute had these all as floats. Fixed now
				continue

			seconds_to_subtract = hours_to_go_back * 3600
			past_epoch_seconds = current_epoch_seconds - seconds_to_subtract

			filtered_data = {}

			for i in self.data:
				if self.data[i][3] >= past_epoch_seconds:
					if self.data[i][3] <= current_epoch_seconds:
						filtered_data[i] = self.data[i]

			return filtered_data


p = PostParser()
p.get_percentages(p.get_epoch_data())
