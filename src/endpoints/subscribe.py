import os
import websocket, json


def on_open(ws):
    print('Opened')
    auth_data = {
        'action': 'auth',
        'key': os.getenv('APCA_API_KEY_ID'),
        'secret': os.getenv('APCA_API_SECRET_KEY')
    }
    ws.send(json.dumps(auth_data))
    trades = ['DOCN',]
    quotes = ['DOCN',]
    bars = ['DOCN',]
    daily_bars = ['DOCN',]
    statuses = ['DOCN',]
    lulds = ['DOCN',]
    corrections = ['DOCN',]
    cancel_errors = ['DOCN',]
    listen_message = {
        'action': 'subscribe',
        'trades': trades,
        'quotes': quotes, 
        'bars': bars,
        'dailyBars': daily_bars,
        'statuses': statuses,
        'lulds': lulds,
        'corrections': corrections,
        'cancelErrors': cancel_errors,
    }
    ws.send(json.dumps(listen_message))

def on_message(ws, message):
    message = json.loads(message)
    print(message)
    print(message['data'])

def on_close(ws):
    print('closed conn')

socket = 'wss://stream.data.alpaca.markets/v2/iex'
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)

ws.run_forever()
