# IG Connection Parser 🎯

A lightweight, privacy-first Python utility that parses messy Instagram data exports and generates a clean, clickable dashboard of accounts that don't follow you back. 

## The Problem
When requesting account data from Meta/Instagram in HTML format, the resulting files are notoriously difficult to audit. The lists are often split across multiple files (followers_1.html, followers_2.html, etc.), embedded with tracking links (_u/), and littered with timestamps, making simple spreadsheet comparisons frustrating and inaccurate.

## The Solution
This tool processes your raw HTML data entirely locally. It uses Regex to bypass the messy formatting, extracts the pure usernames, runs a comparison, and outputs a sleek, dark-mode HTML dashboard so you can easily audit your connections without pasting names into a search bar.

### Features
* 100% Local & Private: No API calls, no third-party logins, and no data leaves your machine.
* Auto-Aggregation: Automatically detects and merges multiple followers files.
* Smart Cleaning: Strips out Meta system links, timestamps, and tracking tags.
* Interactive UI: Generates a clickable dark-mode HTML dashboard that opens profiles in new tabs.

---

## ⚙️ Prerequisites
* Python 3.x installed on your machine.
* Your Instagram Data Export (specifically the followers_and_following folder) in HTML format.

## 🚀 How to Use

### 1. Get Your Data
1. Open the Instagram App > Settings and Privacy > Accounts Center > Your information and permissions.
2. Select Download your information.
3. Choose Followers and Following.
4. Set the Format to HTML and the Date Range to All time.
5. Download and extract the ZIP file once it arrives.

### 2. Setup the Tool
1. Clone this repository to your local machine.
2. Open your extracted Instagram data and locate the connections/followers_and_following folder.
3. Copy following.html and all followers_*.html files and paste them directly into the root folder of this repository.

### 3. Run the Audit
Open your terminal in the repository folder and run the parser:

python ig_script.py

Next, generate the interactive dashboard:

python make_html.py

### 4. Curate Your Network
Double-click clickable_hitlist.html to open it in your web browser. Click on any username to open their Instagram profile directly in a new tab. 

---

## ⚠️ Disclaimer & Safety Warning
This script strictly parses locally downloaded HTML files and does not interact with the Instagram API. 

However, when manually auditing your account using the generated dashboard, do not unfollow more than 50-70 accounts per hour. Instagram has strict rate limits and automated bot-detection. Unfollowing accounts too rapidly will result in a temporary action block or shadowban. Use this tool responsibly. 

## License
Distributed under the MIT License.