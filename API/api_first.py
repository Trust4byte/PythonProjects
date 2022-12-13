import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict["items"]

print(f"Repositories returned: {len(repo_dicts)}")

# Esamine the first repository
repo_dict = repo_dicts[0]

repo_links, stars, labels = [], [], []


for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}"
    repo_links.append(repo_link)


    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"Owner: {owner} <br />{description}"
    labels.append(label)

# Make Visualisation
data = [{
    "type" : "bar",
    "x" : repo_links,
    "y" : stars,
    "hovertext" : labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    "opacity" : 0.6,
}]

my_Layout = {
    "title" : "Most-Starred Python Projects on Github",
    "xaxis" : {
        "title" : "Repositorys",
        "titlefont" : {"size": 24},
        "tickfont" : {"size" : 14}
    },

    "yaxis" : {
        "title" : "Stars",
        "titlefont" : {"size": 24},
        "tickfont" : {"size" : 14}
    }
}

fig = {"data" : data, "layout" : my_Layout}
offline.plot(fig, filename="python_repos.html")
