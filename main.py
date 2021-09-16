from logging import debug
from webapp import create_app

app = create_app()

if __name__ == '__main__':
    # print('hello')
    app.run(debug=True)
