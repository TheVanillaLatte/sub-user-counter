#!/usr/bin/python3

from collections import Counter
import json
import datetime


current_date = datetime.datetime.today()
formatted_date = current_date.strftime("%Y-%m-%d")


def get_percentages(d):
	with open('/home/prometheus/Desktop/dev/python/RedditNews/filtered_submissions.json', 'r') as f:
		data = json.load(f)
	usernames = []
	for post_id, post_info in data.items():
		if len(post_info) >= 2:
			username = post_info[1]
			usernames.append(username)
		else:
			print(f"Warning: Post '{post_id}' has unexpected format, skipping username")
	username_counts = Counter(usernames)


	total_posts = len(usernames)

	# Prepare the results
	percentage_by_username = {}

	if total_posts == 0:
		print("No valid posts found to calculate percentages.")
	else:
		for username, count in username_counts.items():
			percentage = (count / total_posts) * 100
			percentage_by_username[username] = percentage
	sorted_users = sorted(
		percentage_by_username.items(),
		key=lambda item: item[1],
		reverse=True)

	with open(f'/home/prometheus/Desktop/dev/python/RedditNews/{d}.txt', 'w') as f:

		f.write("Percentage of posts by username (Highest to Lowest)\n\n")
		for username, percentage in sorted_users:
			count = username_counts[username]
			f.write(f"- {username}: {percentage:.2f}% ({count} posts)\n")


get_percentages(formatted_date)
