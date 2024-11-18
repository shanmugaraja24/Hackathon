from flask import Flask, render_template, request, jsonify
import json
import msgpack

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_json_to_msgpack():
    data = request.get_json()
    json_data = data.get('json')
    encoding_type = data.get('encoding_type', 'normal')  # Default to 'normal'

    # Convert to MessagePack based on selected encoding type
    if encoding_type == 'binary':
        msgpack_data = msgpack.packb(json_data, use_bin_type=True)
    else:
        msgpack_data = msgpack.packb(json_data, use_bin_type=False)

    # Calculate sizes
    before_size = len(json.dumps(json_data).encode('utf-8')) / 1024  # in KB
    after_size = len(msgpack_data) / 1024  # in KB

    # Return both the MessagePack data and size info
    return jsonify({
        'msgpack': msgpack_data.hex(),  # Convert bytes to hex for display
        'before_size': round(before_size, 2),
        'after_size': round(after_size, 2),
    })

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import json
# import msgpack

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')  # Renders the index.html file

# @app.route('/convert', methods=['POST'])
# def convert_json_to_msgpack():
#     data = request.get_json()
#     json_data = data.get('json')

#     # Convert to MessagePack
#     msgpack_data = msgpack.packb(json_data)

#     # Calculate sizes
#     before_size = len(json.dumps(json_data).encode('utf-8')) / 1024  # in KB
#     after_size = len(msgpack_data) / 1024  # in KB

#     # Return both the MessagePack data and size info
#     return jsonify({
#         'msgpack': msgpack_data.hex(),  # Convert bytes to hex for display
#         'before_size': round(before_size, 2),
#         'after_size': round(after_size, 2),
#     })

# if __name__ == '__main__':
#     app.run(debug=True)
