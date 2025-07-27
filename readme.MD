# Subreddit Post Analysis Engine (parse_time.py)

## Overview

This Python script, `parse_time.py`, functions as a specialized analysis tool for processing a `submissions.json` database of subreddit posts. Its primary objective is to calculate and present the percentage of posts contributed by individual usernames within a user-defined historical timeframe.

## Core Functionality

The script provides two main operational modes:

1.  **Time-Filtered Data Extraction (`get_epoch_data`):**
    * Prompts the user to specify a number of whole hours to look back from the current time.
    * Filters the `submissions.json` data to include only posts created within the specified epoch range.
    * Supports `0` hours to process all available data in `submissions.json`.

2.  **Username Percentage Calculation (`get_percentages`):**
    * Processes the filtered post data.
    * Identifies and counts posts per unique username.
    * Calculates each user's percentage contribution relative to the total number of posts within the selected timeframe.
    * Sorts users by their percentage of posts from highest to lowest.
    * Outputs results directly to the console or to an `output.txt` file based on configuration.

## Data Input (`submissions.json` Schema)

This script relies on a `submissions.json` file located in the same directory. This file is expected to be a JSON object (dictionary) where:

* **Keys:** Represent unique post IDs (strings).
* **Values:** Are lists containing post information, specifically:
    * `[1]` (index 1): The **username** (string) of the post author.
    * `[3]` (index 3): The **epoch timestamp** (integer or float) of when the post was created.

Example `submissions.json` structure:
```json
{
  "post_id_1": ["Date (Y/M/D)", "username_A", "test title", 1678886400],
  "post_id_2": ["Date (Y/M/D)", "username_B", "title", 1678890000],
  "post_id_3": ["Date (Y/M/D)", "username_A", "another title", 1678900000]
}