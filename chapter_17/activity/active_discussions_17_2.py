from operator import itemgetter

import requests

from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants') or 0,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                              reverse=True)

url_titles, comments = [], [] 
for submission_dict in submission_dicts:
    url_titles.append(
        f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>")
    comments.append(submission_dict['comments'])
    print(submission_dict)

# Make visualization.
data = [{
    'type': 'bar',
    'x': url_titles,
    'y': comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': {
        'text': 'Most-Commented Hacker News Stories',
        'font': {'size': 28}
    },
    'xaxis': {
        'title': {
            'text': 'Story',
            'font': {'size': 24}
        },
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': {
            'text': 'Number of Comments',
            'font': {'size': 24}
        },
        'tickfont': {'size': 14}, 
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_discussions.html')