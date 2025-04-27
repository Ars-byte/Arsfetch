import platform
import psutil
import os
import datetime
import cpuinfo
import shellingham
import time
import subprocess


def portada():
	print(r"  /\___/\ ")
	print(r"  )     ( ")
	print(r" =\     /= ")
	print(r"   )   ( ")
	print(r"  /     \ ")
	print(r"  )     ( ")
	print(r" /       \ ")
	print(r" \       / ")
	print(r"  \__ __/ ")
	print(r"    ))")
	print(r"   // ")
	print(r"  ((  ")
	print(r"   \)")

portada()
print("\nArsFetch")
print("--------")

def uptime():

    tiempo_inicio_segundos = psutil.boot_time()

    tiempo_inicio = datetime.datetime.fromtimestamp(tiempo_inicio_segundos)

    ahora = datetime.datetime.now()

    tiempo_encendido = ahora - tiempo_inicio

    segundos_totales = int(tiempo_encendido.total_seconds())

    dias = segundos_totales // 86400  
    segundos_restantes = segundos_totales % 86400 

    horas = segundos_restantes // 3600
    segundos_restantes = segundos_restantes % 3600

    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    resultado = ""
    if dias > 0:
        resultado += str(dias) + " días, "  
    if horas > 0:
        resultado += str(horas) + " hours, " 
    if minutos > 0:
        resultado += str(minutos) + " minutes, "
    if segundos > 0 or resultado == "":  
        resultado += str(segundos) + " seconds "

    return resultado

otime = uptime()

print("Uptime:", otime)
print("Date", time.strftime("%Y-%m-%d  Time:%H:%M:%S"))
print("System name:", platform.node())
print("Operating system:", platform.system())
print("Machine type:", platform.machine())
print("Kernel or version with system:", platform.platform())


def memory_view():
	mem = psutil.virtual_memory()
	gb = round(mem.total / (1024 ** 3), 1)
	return gb

ram = memory_view()
print("Total memory ram:", ram, "gb")

def ram_usage():
    memoria_sistema = psutil.virtual_memory()
    porcentaje_uso = memoria_sistema.percent
    
    print(f"Total ram usage: {porcentaje_uso:.2f}%")

ram_usage()

try:
	print(f"Processor: {cpuinfo.get_cpu_info().get('brand_raw', 'Desconocido')}")

except Exception as e:
	print(f"Error: {e}")

temps = psutil.sensors_temperatures()
valores = [t.current for sensor in temps.values() for t in sensor]
print(f"CPU temperature: {max(valores)}°C ")

try:
    shell = shellingham.detect_shell()
except shellingham.ShellDetectionFailure:
    shell = provide_default()

print("Bash or Shell:", shell)

bateria = psutil.sensors_battery()
if bateria:
    print(f"Percent: {bateria.percent}% | Connected to the power (or energy): {'yes' if bateria.power_plugged else 'no'}")


print("Bye bye :) ")

