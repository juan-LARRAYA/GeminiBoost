from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURAR CHROME (puede sacar el modo headless si querés ver la UI)
chrome_options = Options()
chrome_options.add_argument("--headless")  # sacar esta línea si querés ver el navegador
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# INICIAR CHROME
driver = webdriver.Chrome(options=chrome_options)

# URL a visitar
url = "http://localhost:3001/dashboard/1-e-commerce-insights"
driver.get(url)
print("✅ Página cargada")

# ESPERAR Y HACER CLIC EN EL PRIMER BOTÓN: menú de tarjeta
try:
    btn_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='dashcard-menu']"))
    )
    btn_menu.click()
    print("✅ Menú abierto")
except Exception as e:
    print("❌ Error al abrir el menú:", e)
    driver.quit()
    exit()

time.sleep(1.5)

# SEGUNDO BOTÓN: "Descarga los resultados"
try:
    btn_descargar_resultados = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[div[contains(text(),'Descarga los resultados')]]"))
    )
    btn_descargar_resultados.click()
    print("✅ Se hizo clic en 'Descarga los resultados'")
except Exception as e:
    print("❌ Error en 'Descarga los resultados':", e)
    driver.quit()
    exit()

time.sleep(1.5)

# TERCERO: Seleccionar formato .xlsx
try:
    radio_xlsx = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio'][value='xlsx']"))
    )
    driver.execute_script("arguments[0].click();", radio_xlsx)
    print("✅ Se seleccionó el formato .xlsx")
except Exception as e:
    print("❌ Error al seleccionar .xlsx:", e)
    driver.quit()
    exit()

time.sleep(1.5)

# CUARTO: Botón final de descarga
try:
    btn_final_descarga = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='download-results-button']"))
    )
    btn_final_descarga.click()
    print("✅ Descarga iniciada")
except Exception as e:
    print("❌ Error al iniciar la descarga:", e)
    driver.quit()
    exit()

# CERRAR
driver.quit()
print("🎉 Script finalizado con éxito")
