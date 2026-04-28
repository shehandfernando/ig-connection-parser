# Added encoding='utf-8' here just to be safe
with open('hitlist.txt', 'r', encoding='utf-8') as file:
    usernames = file.read().splitlines()

html_content = """<!DOCTYPE html>
<html>
<head>
    <title>The Hitlist</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #121212; color: #e0e0e0; padding: 40px; }
        .container { max-width: 500px; margin: 0 auto; background: #1e1e1e; padding: 20px; border-radius: 10px; }
        h2 { color: #ffffff; border-bottom: 1px solid #333; padding-bottom: 10px; }
        a { display: block; color: #4da6ff; text-decoration: none; padding: 8px 0; font-size: 16px; border-bottom: 1px solid #2a2a2a; }
        a:hover { color: #ff4d4d; background-color: #2a2a2a; padding-left: 10px; transition: 0.2s; }
    </style>
</head>
<body>
    <div class="container">
        <h2>The Hitlist 🎯</h2>
        <p>Click to open in a new tab.</p>
"""

for user in usernames:
    if user.strip():
        clean_name = user.strip()
        link = f'<a href="https://www.instagram.com/{clean_name}/" target="_blank">@{clean_name}</a>\n'
        html_content += link

html_content += """
    </div>
</body>
</html>
"""

# The fix is added right here
with open('clickable_hitlist.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Done! Open 'clickable_hitlist.html' in your browser.")