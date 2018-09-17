
precisa instalar tudo antes do gevent-socketio
renomear a pasta socketio para socketio_python (faz parte do python-socketio)
refatorar os arquivos das pastas python-socketio e flask_socketio de from socketio para from socketio_python
o do namespace de flask_socketio tem q colocar import socketio_python as socketio em vez de import socketio
requirements.txt possui o necessário para o virtual enviroment.
