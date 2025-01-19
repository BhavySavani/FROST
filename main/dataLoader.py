import requests
from bs4 import BeautifulSoup

def get_supported_fpgas_xilinx(vivado_version):
    url = f"https://www.xilinx.com/products/silicon-devices/fpga/vivado-supported-devices.html?v={vivado_version}" 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, "html.parser")
        # ... (Use BeautifulSoup to find and extract part numbers from the HTML)
        supported_fpgas = [] 
        # ... (Logic to extract part numbers from the parsed HTML)
        for part_number in soup.find_all("td", class_="part-number"):
            supported_fpgas.append(part_number.text)
        print(supported_fpgas)
        return supported_fpgas
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Xilinx: {e}")
        return []

get_supported_fpgas_xilinx("2024.2")
