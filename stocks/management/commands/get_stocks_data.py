import requests
from django.core.management import BaseCommand


def getData() :
    tickers = [
        "AAPL",  # Apple Inc.
        "MSFT",  # Microsoft Corporation
        "GOOGL",  # Alphabet Inc. (Class A)
        "GOOG",  # Alphabet Inc. (Class C)
        "AMZN",  # Amazon.com Inc.
        "META",  # Meta Platforms Inc.
        "NVDA",  # NVIDIA Corporation
        "TSLA",  # Tesla Inc.
        "PEP",  # PepsiCo Inc.
        "INTC",  # Intel Corporation
        "CSCO",  # Cisco Systems Inc.
        "ADBE",  # Adobe Inc.
        "CMCSA",  # Comcast Corporation
        "AVGO",  # Broadcom Inc.
        "COST",  # Costco Wholesale Corporation
        "TMUS",  # T-Mobile US Inc.
        "TXN",  # Texas Instruments Inc.
        "AMGN",  # Amgen Inc.
        "QCOM",  # Qualcomm Incorporated
        "INTU",  # Intuit Inc.
        "PYPL",  # PayPal Holdings Inc.
        "BKNG",  # Booking Holdings Inc.
        "GILD",  # Gilead Sciences Inc.
        "SBUX",  # Starbucks Corporation
        "MU",  # Micron Technology Inc.
        "ADP",  # Automatic Data Processing Inc.
        "MDLZ",  # Mondelez International Inc.
        "ISRG",  # Intuitive Surgical Inc.
        "ADI",  # Analog Devices Inc.
        "MAR",  # Marriott International Inc.
        "LRCX",  # Lam Research Corporation
        "REGN",  # Regeneron Pharmaceuticals Inc.
        "ATVI",  # Activision Blizzard Inc.
        "ILMN",  # Illumina Inc.
        "WDAY",  # Workday Inc.
        "SNPS",  # Synopsys Inc.
        "ASML",  # ASML Holding N.V.
        "EBAY",  # eBay Inc.
        "ROST",  # Ross Stores Inc.
        "CTAS",  # Cintas Corporation
        "BIIB",  # Biogen Inc.
        "MELI",  # MercadoLibre Inc.
        "ORLY",  # O'Reilly Automotive Inc.
        "VRTX",  # Vertex Pharmaceuticals Inc.
        "DLTR",  # Dollar Tree Inc.
        "KHC",  # The Kraft Heinz Company
        "EXC",  # Exelon Corporation
        "FAST",  # Fastenal Company
        "JD",  # JD.com Inc.
        "CRWD"  # CrowdStrike Holdings Inc.
    ]

    headers = {
        'Content-Type': 'application/json'
    }
    token = "fced443141e501d554d0b38c4a34bba085172b1e"
    url = f"https://api.tiingo.com/iex/?tickers={','.join(tickers)}&token={token}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for stock in data:
                print(f"{stock['ticker']}: {stock['last']}")
                # Save or update stock price in your DB here
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error fetching batch data: {e}")

class Command(BaseCommand):
    help = "Fetches and updates stock prices from Tiingo API"

    def handle(self, *args, **kwargs):
            getData()
            self.stdout.write(self.style.SUCCESS("Stock prices updated successfully."))