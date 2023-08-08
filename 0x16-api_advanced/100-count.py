import requests

def get_hot_articles(subreddit, after=None):
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "Reddit Keyword Counter"}
    
    response = requests.get(base_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]
        return articles, data["data"]["after"]
    else:
        return [], None

def count_keywords(keyword, titles):
    return sum(title.lower().count(keyword) for title in titles)

def count_words_recursive(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    
    articles, new_after = get_hot_articles(subreddit, after)
    
    if articles:
        for article in articles:
            title = article["data"]["title"]
            for keyword in word_list:
                keyword = keyword.lower()
                counts[keyword] = counts.get(keyword, 0) + title.lower().count(keyword)
        
        return count_words_recursive(subreddit, word_list, new_after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")

def count_words(subreddit, word_list):
    count_words_recursive(subreddit, word_list)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)

