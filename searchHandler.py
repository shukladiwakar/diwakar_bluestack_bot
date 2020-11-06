from googleSearch import google_bot_query
from dBConnection import insert_data, search_history


def query_router(message):
    response = []
    if message.content == 'hi':  # init condition
        return 'hey'
    elif message.content[:7] == '!google':  # slice the message to check for the reply
        google_query = message.content[8:]
        google_response = google_bot_query(google_query)  # store the reponse
        insert_data(message)  # insert the data in the database to maintain the history
        response = google_response  # send back the response the the chat screen
    elif message.content[:7] == '!recent':
        search_history_response = search_history(message)  # search the history in the database
        response = search_history_response
    else:
        response = 'This functionality is not available ! Please bring me on board to get this done'
    return response
