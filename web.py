from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

@app.route('/key=<key>')
def show_key(key):
    safe_key = html.escape(key)
    html_content = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <title>Key của bạn</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Nhận key của bạn để sử dụng với bot Telegram">
        <meta property="og:title" content="Key của bạn">
        <meta property="og:description" content="Nhận key của bạn để sử dụng với bot Telegram">
        <meta property="og:type" content="website">
        <link rel="icon" type="image/png" href="https://www.favicon.cc/logo3d/519577.png">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .container { animation: fadeIn 0.5s ease-out; }
            .key { transition: transform 0.2s; }
            .key:hover { transform: scale(1.05); }
        </style>
    </head>
    <body class="bg-gradient-to-r from-blue-100 via-purple-100 to-pink-100 min-h-screen flex items-center justify-center">
        <div class="container bg-white p-8 rounded-2xl shadow-xl max-w-md w-full mx-4">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Xin chào, đây là key của bạn</h2>
            <p class="key bg-green-100 text-green-700 font-mono text-lg font-bold p-4 rounded-lg text-center">{{key}}</p>
            <p class="text-gray-600 mt-4">Hãy nhập key này vào bot với lệnh <code>/key</code> để xác nhận.</p>
            <button onclick="copyKey('{{key}}')" class="mt-6 bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-200">Sao chép Key</button>
        </div>
        <script>
            function copyKey(key) {
                navigator.clipboard.writeText(key).then(() => {
                    alert('Key đã được sao chép!');
                }).catch(err => {
                    console.error('Lỗi khi sao chép key:', err);
                });
            }
        </script>
    </body>
    </html>
    """  # <-- dán toàn bộ phần HTML bạn có vào đây
    return render_template_string(html_content, key=safe_key)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
