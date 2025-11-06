#!/usr/bin/env python3
# Demo Visual Offline pa' Raspberry Pi - Impresiona a tus amigos sin WiFi
# Muestra animaciones y pedos chingones en la terminal
import os
import time
import random

 def clear_screen():
    """Limpia la pantalla de la terminal"""
    os.system('clear')

 def print_hacker_banner():
    """Muestra un banner hacker chingon"""
    banner = '''
    ╔══════════════════════════════════════╗
    ║     HACKER PI - MODO OFFLINE        ║
    ╚══════════════════════════════════════╝
    ╔══════════════════════════════════════╗
    ║   Controlando el juego sin WiFi!    ║
    ╚══════════════════════════════════════╝
    '''
    print(banner)

 def print_matrix_effect():
    """Efecto Matrix pa' parecer hacker"""
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
    for _ in range(10):
        line = ''.join(random.choice(chars) for _ in range(40))
        print(line)
        time.sleep(0.1)
    clear_screen()

 def fake_hack_simulation():
    """Simula un hackeo pa' impresionar"""
    print("Iniciando simulacion de hackeo...")
    time.sleep(1)
    print("Buscando sistemas vulnerables...")
    time.sleep(2)
    print("Sistema encontrado: [Colegio_Secreto]")
    time.sleep(2)
    print("Crackeando contrasena...")
    for i in range(1, 101, 10):
        print(f"Progreso: {i}%")
        time.sleep(0.5)
    print("Acceso concedido! Sistema hackeado.")
    time.sleep(2)
    print("Descargando datos secretos...")
    time.sleep(3)
    print("Datos guardados. Eres el rey del hack!")
    time.sleep(2)
    clear_screen()

 def mini_game():
    """Juego simple pa' impresionar"""
    print("Juego: Adivina el codigo secreto!")
    print("Tienes 3 intentos pa' adivinar un numero entre 1 y 10.")
    secret = random.randint(1, 10)
    for attempt in range(3):
        guess = input(f"Intento {attempt+1}: Ingresa un numero: ")
        try:
            guess = int(guess)
            if guess == secret:
                print("Felicidades, crack! Encontraste el codigo secreto!")
                return
            else:
                print("Incorrecto. Intenta de nuevo.")
        except ValueError:
            print("Ingresa un numero valido, pendejo!")
    print(f"Perdiste! El codigo era {secret}.")

 def main():
    """Funcion principal pa' la demo offline"""
    clear_screen()
    print_hacker_banner()
    time.sleep(2)
    print("Iniciando demo hacker sin WiFi...")
    time.sleep(2)
    clear_screen()
    
    # Efecto Matrix
    for _ in range(3):
        print_matrix_effect()
        print_hacker_banner()
        time.sleep(1)
    
    # Simulacion de hackeo
    fake_hack_simulation()
    print_hacker_banner()
    
    # Juego simple
    mini_game()
    
    print("Demo terminada. Eres el mas chingon!")
    print("Presiona Ctrl+C pa' salir.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("`nDemo detenida. Hasta luego, hacker!")

if __name__ == '__main__':
    main()
