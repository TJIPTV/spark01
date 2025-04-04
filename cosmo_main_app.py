from flask import Flask, request, jsonify

cosmo = Flask(__name__)

@cosmo.route('/')
def home():
    return "Hello 这里是宇宙映画的第一个后端程序！"

@cosmo.route('/submit', methods=['POST'])
def receive():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    print(f"小如意收到：{name} - {phone}")
    return jsonify({"status": "received"})

if __name__ == '__main__':
    cosmo.run()