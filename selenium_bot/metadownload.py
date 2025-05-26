from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import os
import time

# === CARGAR VARIABLES DE ENTORNO ===
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# === CONFIGURACIÓN DE CHROME ===
chrome_options = Options()
# chrome_options.add_argument("--headless")  # dejar comentado para ver lo que pasa
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# === INICIAR CHROME ===
driver = webdriver.Chrome(options=chrome_options)
url = "http://localhost:3001/dashboard/1-e-commerce-insights"
driver.get(url)
print("✅ Página cargada")

# === LOGIN ===
try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password = driver.find_element(By.NAME, "password")
    username.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("✅ Login enviado")
except Exception as e:
    print("❌ Error en login:", e)
    driver.quit()
    exit()

time.sleep(2)

# === HOVER EN EL GRÁFICO PARA MOSTRAR EL MENÚ ===
try:
    contenedor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.emotion-onvfvp.e1w4a5v40"))
    )
    ActionChains(driver).move_to_element(contenedor).perform()
    print("✅ Hover sobre el contenedor del gráfico realizado")
except Exception as e:
    print("❌ Error al hacer hover:", e)
    driver.quit()
    exit()

time.sleep(0.8)

# === BOTÓN DE MENÚ DEL DASHBOARD ===
try:
    btn_menu = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='dashcard-menu']"))
    )
    btn_menu.click()
    print("✅ Botón de menú clickeado después del hover")
except Exception as e:
    print("❌ No se pudo hacer clic en el botón de menú:", e)
    driver.quit()
    exit()

time.sleep(1.5)

# === CLIC EN "Descarga los resultados" ===
try:
    btn_descarga = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[role='menuitem'][label='Descarga los resultados']"))
    )
    btn_descarga.click()
    print("✅ Se hizo clic en 'Descarga los resultados'")
except Exception as e:
    print("❌ Error en el botón de descarga:", e)
    driver.quit()
    exit()

time.sleep(1.5)

# === SELECCIONAR FORMATO XLSX ===
try:
    radio_xlsx = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio'][value='xlsx']"))
    )
    driver.execute_script("arguments[0].click();", radio_xlsx)
    print("✅ XLSX seleccionado")
except Exception as e:
    print("❌ Error al seleccionar formato:", e)
    driver.quit()
    exit()

time.sleep(1.5)

# === BOTÓN FINAL DE DESCARGA ===
try:
    btn_final = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='download-results-button']"))
    )
    time.sleep(1.5)
    driver.execute_script("arguments[0].click();", btn_final)
    print("✅ Botón final de descarga clickeado")
    time.sleep(5)  # esperar la descarga
except Exception as e:
    print("❌ Error al iniciar descarga:", e)
    driver.quit()
    exit()

driver.quit()
print("🎉 Script completado con éxito")
