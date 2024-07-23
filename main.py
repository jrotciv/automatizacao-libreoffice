import pywinauto
import time

# Inicia o Notepad
app = pywinauto.application.Application(backend='uia').start('notepad.exe')
time.sleep(30)

dlg = app.window(title='Sem título - Bloco de notas')
dlg.wait('ready', timeout=30)

dlg.edit.type_keys('Olá, esta é uma mensagem de teste do pywinauto!', with_spaces=True)

dlg.menu_select("Arquivo->Salvar como")
save_as_dlg = app.window(title_re=".*Salvar como")

save_as_dlg.wait('ready', timeout=30)
save_as_dlg.edit.set_text("arquivo_teste.txt")
save_as_dlg.button("Salvar").click()
