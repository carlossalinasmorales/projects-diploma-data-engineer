import schedule, time
from datetime import datetime
from etl import run_etl_orquestator, CSV_PATH, DB_PATH

segundos_de_ejecucion = 60
ciclos = 1
count = 0

def job():
    global count
    try:
        run_id, timestamp = run_etl_orquestator(CSV_PATH, DB_PATH)
        count += 1
        print(f'timestamp: {timestamp}, run_id: {run_id} - Ciclo scheduler completado con excito. Ciclo {count}/{ciclos}')
    except Exception as e:
        print(f'timestamp: {timestamp}, run_id: {run_id} - Error al ejecutar scheduler: {e}')


job()  # Ejecutar el job una vez al iniciar el script
schedule.every(segundos_de_ejecucion).seconds.do(job)
    
while count < ciclos:
    schedule.run_pending()
    time.sleep(1)

print(f'Scheduler finalizado después de {ciclos} ciclos. \n Puedes ver los resultados en la base de datos SQLite en db/sales.db y en los logs en logs/etl.log')