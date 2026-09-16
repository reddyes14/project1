import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def scrape_page(page_num):
    url = BASE_URL.format(page_num)
    response = requests.get(url)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")

    data = []
    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text.strip()
        rating_class = product.find("p", class_="star-rating")["class"][1]
        rating = RATING_MAP.get(rating_class, "N/A")

        data.append({"Name": name, "Price": price, "Rating": rating})

    return data


def run_scrape():
    try:
        pages = int(pages_entry.get())
        if pages < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number of pages (1 or more).")
        return

    status_label.config(text="Scraping in progress...")
    root.update()

    all_products = []
    for page in range(1, pages + 1):
        page_data = scrape_page(page)
        if page_data is None:
            break
        all_products.extend(page_data)

    if not all_products:
        messagebox.showinfo("No Data", "No products were found.")
        status_label.config(text="")
        return

    filename = "products.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Price", "Rating"])
        writer.writeheader()
        writer.writerows(all_products)

    status_label.config(text=f"Done! Saved {len(all_products)} products to {filename}")


root = tk.Tk()
root.title("Product Data Scraper")
root.geometry("380x220")
root.configure(bg="#1e2a38")

title = tk.Label(root, text="Product Data Scraper", font=("Arial", 15, "bold"),
                  bg="#1e2a38", fg="white")
title.pack(pady=12)

form_frame = tk.Frame(root, bg="#1e2a38")
form_frame.pack(pady=5)

tk.Label(form_frame, text="Number of pages to scrape:", bg="#1e2a38", fg="white",
          font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)

pages_entry = tk.Entry(form_frame, width=6, font=("Arial", 10))
pages_entry.insert(0, "1")
pages_entry.grid(row=0, column=1, padx=5, pady=5)

scrape_button = tk.Button(root, text="Scrape & Save to CSV", command=run_scrape,
                            bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"),
                            relief="flat", cursor="hand2")
scrape_button.pack(pady=15)

status_label = tk.Label(root, text="", bg="#1e2a38", fg="#cccccc", wraplength=320,
                          font=("Arial", 9))
status_label.pack(pady=5)

root.mainloop()
