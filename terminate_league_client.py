import psutil

def terminate_league_client():
    league_process_names = [
        "Riot",
        "League"
    ]
    
    terminated = False
    
    for proc in psutil.process_iter(['name']):
        try:
            for name in league_process_names:
                if name in proc.info['name']:
                    proc.terminate()
                    terminated = True
                    try:
                        proc.wait(timeout=3)
                    except psutil.NoSuchProcess:
                        pass
                    break
        except psutil.NoSuchProcess:
            continue
    
    return terminated

if __name__ == "__main__":
    if terminate_league_client():
        print("League of Legends client terminated successfully")
    else:
        print("No League of Legends client process found")
