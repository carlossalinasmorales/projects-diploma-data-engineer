import schedule, time
from datetime import datetime
from etl import run_etl, CSV_PATH, DB_PATH

segundos_de_ejecucion = 3
ciclos = 3
count = 0

def job():
    global count
    print(f'{datetime.now()} - Ejecutando proceso ETL de ventas')
    run_id, timestamp = run_etl(CSV_PATH, DB_PATH)
    print(f'run_id={run_id}, timestamp={timestamp}')
    count += 1
    print(f'{datetime.now()} - Proceso ETL de ventas completado')

schedule.every(segundos_de_ejecucion).seconds.do(job)
    
while count < ciclos:
    schedule.run_pending()
    time.sleep(1)

print(f'Scheduler finalizado después de {ciclos} ciclos.')