from app import createApp

app = createApp()

if __name__ == '__main__':
    print('应用已启动')
    app.run(host='0.0.0.0', port=8888, debug=app.config['DEBUG'], threaded=True)
