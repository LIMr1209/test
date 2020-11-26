'''
基于websocket+flask实现的群聊无昵称即时通信
设计列表client_list = []来存储客户端与服务器的连接，
服务收到任意客户端的信息（信息时），对连接存储列表进行遍历获取每个连接，直接进行转发
'''
from flask import Flask, render_template, request

# pip install gevent-websocket导入IO多路复用模块
from geventwebsocket.handler import WebSocketHandler  # 提供WS（websocket）协议处理
from geventwebsocket.server import WSGIServer  # websocket服务承载
# WSGIServer导入的就是gevent.pywsgi中的类
# from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket  # websocket语法提示

app = Flask(__name__)

# @app.route('/websocket')
# 多个客户端可以同时给falsk服务端发送ws协议的信息
# def websocket():
#     client_socket=request.environ.get('wsgi.websocket') #type:WebSocket
#     while 1:
#             msg_from_cli=client_socket.receive()
#             print(msg_from_cli)
# 多个客户端可以同时给falsk服务端发送ws协议的信息，同时服务端将信息转送到每个客户端页面，实现多人聊天室即时通信
client_list = []


@app.route('/websocket')
def websocket():
    client_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    client_list.append(client_socket)
    # print(len(client_list), client_list)
    while 1:
        msg_from_cli = client_socket.receive()
        # print(msg_from_cli)
        #收到任何一个客户端的信息都进行全部转发（注意如果某个客户端连接断开，在遍历发送时连接不存在会报错，需要异常处理）
        for client in client_list:
            try:
                client.send(msg_from_cli)
            except Exception as e:
                continue

@app.route('/chat')
def chat():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run('192.168.16.14',8888,debug=True)
    http_server = WSGIServer(('127.0.0.1', 5000), application=app, handler_class=WebSocketHandler)
    http_server.serve_forever()
