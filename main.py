import requests
import subprocess
from pathlib import Path
from pywinauto import Application
import time

def download_exe(url: str, new_name: str = None) -> str:
    res = requests.get(url, stream=True)

    if new_name:
        out_name = new_name
    else:
        out_name = Path(url).name
    print(f'Download {out_name}')
    with open(out_name, 'wb') as f:
        for chunk in res.iter_content(chunk_size=8192):
            f.write(chunk)
    return out_name

def install_winRAR(out_name):
    
    subprocess.Popen(out_name, shell=True)
    
    time.sleep(5)
    app = Application().connect(title='WinRAR 7.13')
    # app = Application().start(out_name)
    time.sleep(2)
    window = app.top_window()
    window.child_window(class_name="Edit").type_keys("D:\Program Files\WinRAR", with_spaces=True)
    time.sleep(0.5)
    window.child_window(title="Install", class_name="Button").click()
    
    time.sleep(2)
    app = Application().connect(title='WinRAR Setup')
    time.sleep(1)
    window = app.top_window()
    window.child_window(title="OK", class_name="Button").click()
    
    time.sleep(2)
    window = app.top_window()
    window.child_window(title="Done", class_name="Button").click()
    # print(window.print_control_identifiers())
    
def install_notepad(out_name):
    subprocess.Popen(out_name, shell=True)
    
    time.sleep(5)
    app = Application().connect(title='Installer Language')
    window = app.top_window()
    window.child_window(title="OK", class_name="Button").click()
    time.sleep(0.5)
    
    window = app.top_window()
    window.child_window(title="&Next >", class_name="Button").click()
    time.sleep(0.5)
    
    window.child_window(title="I &Agree", class_name="Button").click()
    time.sleep(0.5)
    
    window.child_window(class_name="Edit").type_keys(r'D:\Program Files\Notepad{+}{+}', with_spaces=True)
    time.sleep(0.5)
    window.child_window(title="&Next >", class_name="Button").click()
    
    time.sleep(0.5)
    window.child_window(title="&Next >", class_name="Button").click()
    
    time.sleep(0.5)
    window.child_window(title="&Install", class_name="Button").click()
    
    
    time.sleep(10)
    window.child_window(title="&Run Notepad++ v8.9", class_name="Button").click()
    
    time.sleep(0.5)
    window.child_window(title="&Finish", class_name="Button").click()
    
    # print(window.print_control_identifiers())
    
    
    
install_path_winRAR = Path('D:\Program Files\WinRAR')
if not install_path_winRAR.exists():
    out_name = download_exe('https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-713.exe')
    # subprocess.run([out_name, '/S', f'/D{install_path_winRAR}'], shell=True, check=True)
    install_winRAR(out_name)
    


install_path_notepad = Path(r'D:\Program Files\Notepad++')
if not install_path_notepad.exists():
    out_name = download_exe('https://release-assets.githubusercontent.com/github-production-release-asset/33014811/1100992b-2033-432e-b89f-c72fe97a4fcc?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-01-09T08%3A33%3A30Z&rscd=attachment%3B+filename%3Dnpp.8.9.Installer.x64.exe&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-01-09T07%3A32%3A33Z&ske=2026-01-09T08%3A33%3A30Z&sks=b&skv=2018-11-09&sig=X0u2gi5Cz%2FlzJcIxG1T4MJXvyEzzq230omebNHKvSBc%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2Nzk0NTI0MywibmJmIjoxNzY3OTQ0OTQzLCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.afH6WzYQxLaQqDiga7EgWEL3wa1brgOV4Gb2_bBJy0Y&response-content-disposition=attachment%3B%20filename%3Dnpp.8.9.Installer.x64.exe&response-content-type=application%2Foctet-stream',
                               'notepad.exe')
    # subprocess.run([out_name, '/S', f'/D{install_path_notepad}'], shell=True, check=True)
    install_notepad(out_name)
    

# install_path_virtualBox = Path('D:\Program Files\Oracle\VirtualBox')
# if not install_path_virtualBox.exists():
#     out_name = download_exe('https://download.virtualbox.org/virtualbox/6.1.18/VirtualBox-6.1.18-142142-Win.exe')

#     subprocess.run([out_name, '/S', f'/D{install_path_virtualBox}'], shell=True, check=True)