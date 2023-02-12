#https://development-tools.net/python-obfuscator/ DeObfuscator by CSEC (ent1tydev)
#Actually for 12.02.2023
import sys, codecs, base64

filename=None

try:
    option=sys.argv[1]
    filename=sys.argv[2]
except:
    print(f'''
Usage:
    python3 {sys.argv[0]} -f example_file_to_deobfuscation.py
''')
    sys.exit()

def deobfuscate(file):
    try:
        name=file.replace('.py', '') + '_deobfuscated.py'
        print(f'\n[*]Trying to open and read {file}...')
        deobfs, another=open(file).read().replace('import base64, codecs', '').split('trust =')
        print(f'\n[+]Working with {file}...')
        exec('import codecs, base64' + deobfs + f'''trust = magic + codecs.decode(love, 'rot13') + god + codecs.decode(destiny, 'rot13')
r = open('{name}','wb')
r.write(base64.b64decode(trust))
r.close()''')
        print(f'\n[+]Saved as {name}')
    except Exception as inerror:
        print(f'\n[!]Exception: {inerror}')

if __name__ == '__main__':
    if option == '-f':
        deobfuscate(filename)
    else:
        print(f'''
Usage:
    python3 {sys.argv[0]} -f example_file_to_deobfuscation.py
''')
