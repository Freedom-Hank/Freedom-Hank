import os
import requests

output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

token = os.getenv("GITHUB_TOKEN")
username = "Freedom-Hank"

themes = {"dark": "tokyonight", "light": "github_light"}
urls = {
    "stats": "https://github-readme-stats.vercel.app/api?username={u}&show_icons=true&count_private=true&theme={t}",
    "langs": "https://github-readme-stats.vercel.app/api/top-langs/?username={u}&layout=compact&count_private=true&theme={t}&card_width=500",
    "streak": "https://github-readme-streak-stats.herokuapp.com?user={u}&theme={t}"
}

headers = {"Authorization": f"token {token}"}

for mode, theme in themes.items():
    for name, url in urls.items():
        api_url = url.format(u=username, t=theme)
        res = requests.get(api_url, headers=headers)
        if res.status_code == 200:
            filename = f"{output_dir}/{name}-{mode}.svg"
            with open(filename, "wb") as f:
                f.write(res.content)
            print(f"✅ {filename} updated.")
        else:
            print(f"❌ Failed to fetch {name} ({mode}): {res.status_code}")
