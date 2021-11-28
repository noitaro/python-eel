import os
import eel

# python -m eel main_script.py web --onefile --noconsole --icon=Icojam-Animals-01-horse.ico
def main():

    eel.init('web')
    eel.start('index.html', port=0, size=(800, 600))

    pass

@eel.expose
def run_python():

    files = os.listdir()
    print(files)
    eel.sleep(3)
    return files

if __name__ == '__main__':
    try:
        main()
    except Exception:
        pass