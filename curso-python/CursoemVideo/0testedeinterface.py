from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário: ', size= (20,2)), sg.InputText(key='usuário', size= (20,1)),],
    [sg.Text('Senha: ', size= (20,2)), sg.InputText(key='senha', password_char='*', size= (20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar'), sg.Cancel()]]

# Janela
window = sg.Window('Tela de Login', layout, size= (400,300))

# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuário'] == 'Matheus' and valores['senha'] == '1234':
            sg.popup('Login efetuado com sucesso!')
        else:
            sg.popup('Login ou senha incorreto.')
# Finalizar janela
