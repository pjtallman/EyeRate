**Matika** | Version: **v0.0.1** | Copyright (c) 2026 Patrick James Tallman

# EyeRate User Guide

EyeRate is a financial security tracking plugin for the Matika framework. It allows you to manage a list of stocks, ETFs, and mutual funds with real-time data lookups.

## 1. Getting Started

### Installation
To install EyeRate into your Matika instance:
1.  Copy the `eyerate` folder into the `plugins/` directory of your Matika installation.
2.  Restart the Matika server.
3.  Log in as an Administrator.
4.  You will see a new **Securities** item under the **Activities** menu.

## 2. Managing Securities

### Viewing Securities
Navigate to **Activities -> Securities**. You will see a list of all tracked financial instruments.

### Adding a New Security
1.  Click the **New Financial Security** button.
2.  Enter the **Ticker Symbol** (e.g., VOO, AAPL).
3.  Click the **Search** icon (magnifying glass) next to the symbol to perform a real-time lookup.
4.  EyeRate will automatically populate the Name, Price, and other metadata if found.
5.  Click **Save** to add it to your tracking list.

### Editing/Deleting
- Select a security from the list to view its details in the maintenance panel.
- Click **Delete** to stop tracking a specific security.

## 3. Data Endpoints
EyeRate supports multiple data sources for real-time lookups. You can configure the preferred source in the Matika System Settings (if supported) or via the plugin configuration.

Supported sources:
- **Yahoo Finance:** No API key required (uses web scraping).
- **Finnhub:** Fast and reliable. Requires a free API key from [finnhub.io](https://finnhub.io).
- **Alpha Vantage:** Comprehensive data. Requires a free API key from [alphavantage.co](https://www.alphavantage.co).

## 4. Bulk Operations
You can manage multiple tickers at once by using the bulk entry features (if enabled in your version), allowing you to quickly bootstrap your portfolio tracking.

---
Copyright (c) 2026 Patrick James Tallman. All Rights Reserved.
