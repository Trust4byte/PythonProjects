import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

response_dicts = r.json()
repo_dicts = response_dicts["items"]

repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# Make visualisation
data = [{
    "type" : "bar",
    "x" : repo_names,
    "y" : stars,
    "marker" : {
        "color" : "rgb(0, 0, 0)",
        "line" : {"width" : 1.5, "color" : "rgb(0, 0, 0)"}
    },
    "opacity" : 0.5,
}]

my_Layout = {
    "title" : "Most Starred Python Projects on Github",
    "xaxis" : {
        "title" : "Repositories",
        "titlefont" : {"size" : 24},
        "tickfont" : {"size" : 12},
    },
    "yaxis" : {
        "title" : "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 18},
    },
}

fig = {"data" : data, "layout" : my_Layout}
offline.plot(fig, filename="python_repos2.html")