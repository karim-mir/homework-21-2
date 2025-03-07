from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # Путь к файлу index.html
        file_path = os.path.join(os.getcwd(), "index.html")

        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                page_content = file.read()  # Читаем содержимое HTML-файла
        else:
            page_content = "<html><body><h1>404 Not Found</h1></body></html>"

        self.send_response(200)  # Отправляем статус 200 OK
        self.send_header("Content-type", "text/html")  # Устанавливаем правильный тип содержимого
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))  # Отправляем содержимое HTML-страницы

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")