import os
import requests

# 從環境變數讀取 Token
token = os.getenv("GITHUB_TOKEN")
username = "Freedom-Hank"

# 三個卡片的 API
urls = {
    "stats": f"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&count_private=true&theme=tokyonight",
    "langs": f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&count_private=true&theme=tokyonight&card_width=500",
    "streak": f"https://github-readme-streak-stats.herokuapp.com?user={username}&theme=tokyonight"
}

# 逐一抓取並存成 svg 檔
headers = {"Authorization": f"token {token}"}
for name, url in urls.items():
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        with open(f"{name}.svg", "wb") as f:
            f.write(res.content)
        print(f"✅ {name}.svg updated.")
    else:
        print(f"❌ Failed to fetch {name}: {res.status_code}")
