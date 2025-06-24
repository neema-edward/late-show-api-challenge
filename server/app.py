from flask import Flask
from server.config import app, db
from server.controllers import register, login, get_guests, get_episodes, get_episode, delete_episode, create_appearance

app.route('/register', methods=['POST'])(register)
app.route('/login', methods=['POST'])(login)
app.route('/guests', methods=['GET'])(get_guests)
app.route('/episodes', methods=['GET'])(get_episodes)
app.route('/episodes/<int:id>', methods=['GET'])(get_episode)
app.route('/episodes/<int:id>', methods=['DELETE'])(delete_episode)
app.route('/appearances', methods=['POST'])(create_appearance)

if __name__ == '__main__':
    app.run(debug=True)