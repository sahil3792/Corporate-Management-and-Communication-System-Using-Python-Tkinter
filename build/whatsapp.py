import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_message():
    phone_number = phone_number_entry.get()
    message = message_entry.get("1.0", "end").strip()

    # Start Chrome WebDriver
    driver = webdriver.Chrome()

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)  # Wait for the user to scan the QR code

    # Locate the search box and type the phone number
    search_box = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
    search_box.click()
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.RETURN)

    # Locate the message input box and type the message
    message_box = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
    message_box.click()
    message_box.send_keys(message)

    # Click on the send button
    send_button = driver.find_element_by_xpath("//button[@class='_1U1xa']")
    send_button.click()

    # Close the WebDriver
    driver.quit()

# GUI setup
root = tk.Tk()
root.title("WhatsApp Message Sender")

phone_label = tk.Label(root, text="Enter Phone Number:")
phone_label.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()

message_label = tk.Label(root, text="Enter Message:")
message_label.pack()
message_entry = tk.Text(root, height=5)
message_entry.pack()

send_button = tk.Button(root, text="Send Message", command=send_whatsapp_message)
send_button.pack()

root.mainloop()
