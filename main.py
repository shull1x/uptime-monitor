import time
from config import SITES, CHECK_INTERVAL
from checker import check_site
from notifier import send_alert

def start_monitoring():
    print(f"Мониторинг запущен. Проверка {len(SITES)} сайтов...")
    state = {site: True for site in SITES}

    while True:
        for site in SITES:
            is_up = check_site(site)
            
            if is_up != state[site]:
                if not is_up:
                    msg = f"🔴 ВНИМАНИЕ: Сайт {site} недоступен!"
                else:
                    msg = f"🟢 ВОССТАНОВЛЕНИЕ: Сайт {site} снова в строю."
                
                print(msg)
                send_alert(msg)
                state[site] = is_up
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    start_monitoring()
