import http.server
import socketserver

PORT = 8080  # Порт, на котором будет запущен сервер


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Логируем запрашиваемый путь
        print(f"Запрос на: {self.path}")

        # Устанавливаем заголовок ответа
        self.send_response(200)  # Успешный ответ
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Читаем содержимое из файла contact.html
        try:
            with open('contact.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            self.wfile.write(html_content.encode('utf-8'))  # Отправляем HTML-код
        except FileNotFoundError:
            self.send_error(404, "File not found")  # Обработка 404 ошибки


# Запуск сервера
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()