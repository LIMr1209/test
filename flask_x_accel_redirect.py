# nginx 文件服务器， 特定文件通过程序鉴权，调用nginx内部使用的路由 nginx返回文件


from flask import Flask, make_response, abort

app = Flask(__name__)


#     server {
#
#         listen       9000;
#         root C:/Users/aaa10/Desktop/project/;
#         location /img/yunpan/ {
#             internal;
# 	        root C:/Users/aaa10/Desktop/project/; #磁盘的目录路径
#         }
#
#         location /img/yunpian/ {
#             proxy_pass http://127.0.0.1:5000;
#
#         }
#         location /img {
#             root C:/Users/aaa10/Desktop/project/;
#             autoindex on; #是否开启目录浏览
#         }
#     }

@app.route('/img/yunpian/<file_name>')
def image_path(file_name):
    # abort(401)
    response = make_response()
    response.headers['X-Accel-Redirect'] = ("/img/yunpan/" + file_name).encode('utf-8')
    response.headers['Content-type'] = 'image/jpeg'
    # response.headers['Content-Disposition'] = 'attachment; filename=' + file_name
    return response


if __name__ == '__main__':
    app.run()
