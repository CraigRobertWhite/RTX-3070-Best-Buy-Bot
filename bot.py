from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decouple import config

item = input('Item URL: ')
driver = webdriver.Chrome(config('CHROME_DRIVER_PATH'))
driver.get(item)

while True:
    # Add to Cart ------------------------------------------------------------------------------------------------------
    try:
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except Exception:
        driver.refresh()
        continue
    print("Add to cart button found")
    add_to_cart_button.click()

    # Go to Cart -------------------------------------------------------------------------------------------------------
    driver.get("https://www.bestbuy.com/cart")

    # Go to Checkout ---------------------------------------------------------------------------------------------------
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-buttons__checkout"))
    )
    checkout_button.click()
    print("Beginning checkout")

    # Login ------------------------------------------------------------------------------------------------------------
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-e"))
    )
    email_input.send_keys(config('EMAIL'))

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-p1"))
    )
    password_input.send_keys(config('PASSWORD'))

    sign_in_button = driver.find_element_by_class_name("btn-lg")
    sign_in_button.click()
    print("Logging in")

    # Populate CVV -----------------------------------------------------------------------------------------------------
    cvv_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cvv"))
    )
    cvv_input.send_keys(config('CVV'))
    print("Placing order")

    # Place Order ------------------------------------------------------------------------------------------------------
    place_order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
    )
    place_order_button.click()

    raise Exception(f"Bought: {item}")
