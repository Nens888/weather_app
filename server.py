from websocket_server import WebsocketServer

# Список подключенных клиентов
clients = []

# Обработка нового клиента
def new_client(client, server):
    clients.append(client)
    print(f"Новый клиент подключен: {client['id']}")

# Обработка отключения клиента
def client_left(client, server):
    clients.remove(client)
    print(f"Клиент отключен: {client['id']}")

# Обработка полученного сообщения
def message_received(client, server, message):
    print(f"Сообщение от клиента {client['id']}: {message}")
    # Рассылка сообщения всем клиентам
    for c in clients:
        server.send_message(c, message)

# Запуск сервера WebSocket
server = WebsocketServer(host='127.0.0.1', port=12345)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

print("Сервер запущен на ws://127.0.0.1:12345")
server.run_forever()