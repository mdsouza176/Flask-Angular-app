from flask import Flask, request, send_from_directory
import os

os.chdir("../ui/")
print(os.getcwd())
os.system("ng build --outputPath=../backend/static")


app = Flask(__name__, static_url_path='/static')


@app.route('/test')
def test_route():
    return request.args.get('user')

@app.route('/', defaults={'path': '/static'})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(port=8080)