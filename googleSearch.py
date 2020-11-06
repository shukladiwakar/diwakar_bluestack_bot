from googlesearch import search


def google_bot_query(query):
    result = []
    for output in search(query, tld="com", num=5, stop=10, pause=2):
        result.append(output)
    return result
