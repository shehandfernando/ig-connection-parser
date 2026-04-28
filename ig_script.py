import os
import re

def get_usernames(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Grabs exactly the username from the href link, ignoring the _u/ garbage
    usernames = re.findall(r'href="https://www\.instagram\.com/(?:_u/)?([^/"]+)', content)
    return set(usernames)

# 1. Get Following
following = get_usernames('following.html')

# 2. Automatically find and combine ALL follower files
followers = set()
for file in os.listdir():
    if file.startswith('followers') and file.endswith('.html'):
        followers.update(get_usernames(file))

# 3. Clean up any Meta system links
ignore_list = {'p', 'stories', 'reel', 'reels', 'explore', 'about', 'legal', 'help', 'instagram'}
following = {u for u in following if u not in ignore_list}
followers = {u for u in followers if u not in ignore_list}

# 4. Find the culprits
not_following_back = following - followers

print(f"Total Followers found: {len(followers)}")
print(f"Total Following found: {len(following)}")
print(f"--- TOTAL NOT FOLLOWING BACK: {len(not_following_back)} ---")

# 5. Save straight to a clean text file
with open('hitlist.txt', 'w') as f:
    for u in sorted(not_following_back):
        f.write(f"{u}\n")
        
print("Success! Open 'hitlist.txt' in your folder to see the final clean list.")