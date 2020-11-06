from googleSearch import google_bot_query
from dBConnection import insert_data, search_history


def query_router(message):
    response = []
    if message.content == 'hi':
        return 'hey'
    elif message.content[:7] == '!google':
        google_query = message.content[8:]
        google_response = google_bot_query(google_query)
        insert_data(message)
        response = google_response
    elif message.content[:7] == '!recent':
        search_history_response = search_history(message)
        response = search_history_response
    else:
        response = 'This functionality is not available ! Please bring me on board to get this done'
    return response
