import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://bluestack_user:bluestack_11_nov@cluster0.6oftr.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

posts = db.posts


def insert_data(data):
    author = str(data.author)
    query = (str(data.content))[8:]
    document = {
        "author": author,
        "query": query
    }
    result = posts.insert_one(document)
    print('User  Data Added : {0}'.format(result.inserted_id))


def search_history(data):
    author = str(data.author)
    history_user = {"author": author}
    history_string = (str(data.content))[8:]

    history_cursor = list(posts.find(history_user))
    print(history_cursor)
    result = []
    for h in history_cursor:
        val = h['query']
        if val.find(history_string) is not -1:
            result.append(h['query'])
    return result
