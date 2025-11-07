#!/usr/bin/env python3
# Script pa' Raspberry Pi - Hackeo de red local Windows y Ransomware
# Escanea red WLAN y simula ataque a dispositivos Windows
# AVISO: Solo pa' uso educativo en redes propias. Ilegal sin permiso.
import os
import subprocess
import time
import logging
from datetime import datetime

# Configura logging pa' guardar lo que pasa
log_file = f'network_hack_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

 def run_command(command):
    """Ejecuta un comando y devuelve el output"""
    try:
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return result
    except subprocess.CalledProcessError as e:
        return f'Error ejecutando {command}: {e.output}'

 def scan_network():
    """Escanea la red local pa' encontrar dispositivos (usa nmap si esta, sino algo basico)"""
    logging.info('Escaneando red local (192.168.31.0/24)...')
    print('Escaneando red local (192.168.31.0/24)...')
    # Intenta usar nmap si esta instalado
    try:
        scan_result = run_command('nmap -sn 192.168.31.0/24')
        logging.info(f'Resultado de escaneo con nmap: {scan_result}')
        print('Escaneo con nmap completado. Revisa el log pa' detalles.')
        return scan_result
    except:
        # Si nmap no esta, hace un ping sweep basico
        logging.warning('Nmap no encontrado. Usando ping sweep basico.')
        print('Nmap no encontrado. Usando ping sweep basico...')
        devices = []
        for i in range(1, 255):
            ip = f'192.168.31.{i}'
            result = run_command(f'ping -c 1 -W 1 {ip}')
            if '1 received' in result:
                devices.append(ip)
                print(f'Dispositivo encontrado: {ip}')
                logging.info(f'Dispositivo encontrado: {ip}')
            time.sleep(0.1)
        return devices

 def detect_windows_devices(scan_output):
    """Detecta posibles dispositivos Windows en el escaneo"""
    logging.info('Detectando dispositivos Windows...')
    print('Detectando dispositivos Windows...')
    windows_devices = []
    if isinstance(scan_output, list):
        # Si es el ping sweep basico
        windows_devices = scan_output
    else:
        # Si es output de nmap
        lines = scan_output.splitlines()
        for line in lines:
            if 'Nmap scan report for' in line:
                ip = line.split()[-1].strip('()')
                if '192.168.31.' in ip:
                    windows_devices.append(ip)
                    logging.info(f'Posible dispositivo Windows: {ip}')
                    print(f'Posible dispositivo Windows: {ip}')
    return windows_devices

 def attempt_windows_attack(ip):
    """Intenta atacar un dispositivo Windows (simulacion o SMB)"""
    logging.info(f'Intentando atacar {ip}...')
    print(f'Intentando atacar {ip}...')
    # Simula un ataque por SMB (necesita smbclient, sino solo simula)
    try:
        result = run_command(f'smbclient -L //{ip} -N')
        if 'Sharename' in result or 'Disk' in result:
            logging.info(f'Acceso SMB exitoso a {ip}. Listando compartidos.')
            print(f'Acceso SMB exitoso a {ip}. Listando compartidos.')
            # Simula envio de ransomware (en realidad no envia nada real)
            logging.info(f'Enviando ransomware simulado a {ip}...')
            print(f'Enviando ransomware simulado a {ip}...')
            time.sleep(2)
            logging.info(f'Ransomware desplegado en {ip}.')
            print(f'Ransomware desplegado en {ip}.')
        else:
            logging.info(f'No se pudo acceder a {ip} por SMB. Simulando ataque.')
            print(f'No se pudo acceder a {ip} por SMB. Simulando ataque.')
            time.sleep(1)
            logging.info(f'Ataque simulado completado en {ip}.')
            print(f'Ataque simulado completado en {ip}.')
    except:
        logging.error(f'Error al atacar {ip}. Simulando...')
        print(f'Error al atacar {ip}. Simulando...')
        time.sleep(1)
        logging.info(f'Ataque simulado completado en {ip}.')
        print(f'Ataque simulado completado en {ip}.')
    return True

 def main():
    """Funcion principal pa' el hackeo de red"""
    print('Iniciando Hackeo de Red Local desde Raspberry Pi...')
    print('Esto es solo pa' fines educativos. Usa con permiso.')
    logging.info('Inicio del hackeo de red local.')
    
    # Checa si esta como root (mejores resultados)
    if os.geteuid() != 0:
        print('AVISO: Ejecuta como root (sudo python3 network_hack_raspberry.py) pa' mejores resultados.')
        logging.warning('Script no ejecutado como root. Funcionalidad limitada.')
    
    # Escanea la red
    scan_output = scan_network()
    time.sleep(2)
    
    # Detecta dispositivos Windows
    windows_devices = detect_windows_devices(scan_output)
    if not windows_devices:
        logging.warning('No se encontraron dispositivos en la red.')
        print('No se encontraron dispositivos en la red.')
        return
    
    # Ataca cada dispositivo Windows detectado
    for device in windows_devices:
        attempt_windows_attack(device)
        time.sleep(3)  # Delay pa' no saturar
    
    logging.info('Hackeo de red completado.')
    print('Hackeo de red completado. Revisa', log_file, 'pa' detalles.')
    print('Ransomware simulado desplegado en dispositivos Windows.')
    print('Mensaje: Desbloqueen todos los Chromebooks por una semana.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('`nHackeo detenido por el usuario.')
        logging.info('Hackeo detenido por el usuario.')
    except Exception as e:
        print('Error cabron: ', str(e))
        logging.error(f'Error: {str(e)}')
