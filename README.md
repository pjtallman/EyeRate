**Matika** | Version: **v0.0.1** | Copyright (c) 2026 Patrick James Tallman

# EyeRate (AppLug Plugin)

EyeRate is the reference implementation of an AppLug plugin for the Matika Framework. It provides financial security maintenance, real-time data lookups, and yield tracking capabilities.

## Features

- **Financial Security Maintenance:** Create, update, and delete financial securities (ETFs, Stocks, Mutual Funds).
- **Multi-Source Data Fetching:** Supports Yahoo Finance (scraper), Finnhub API, and Alpha Vantage API.
- **Bulk Operations:** Automated bulk creation and deletion of securities by ticker symbols.
- **Metadata-Driven UI:** UI layout and form fields are defined using a standardized JSON grammar.

## Folder Structure

The EyeRate project follows the AppLug plugin standard for Matika.

```text
/
├── src/                    # Plugin source code root
│   └── eyerate/            # Main EyeRate package
│       ├── locales/        # Translation JSON files (en.json, es.json)
│       ├── metadata/       # JSON metadata for the Maintenance Activity UI
│       ├── static/         # Compiled JS and plugin-specific assets
│       ├── templates/      # Jinja2 HTML templates for securities views
│       ├── admin_securities.ts # TypeScript manager for securities maintenance
│       ├── endpoints.py    # Financial data provider implementation (Scrapers/APIs)
│       ├── lookup_dialog.ts # Shared TypeScript component for ticker lookups
│       ├── models.py       # SQLAlchemy models for FinancialSecurity and enums
│       └── routes.py       # FastAPI route definitions for securities endpoints
└── tests/                  # Plugin-specific test suite
    ├── test_securities.py  # Unit tests for CRUD operations
    ├── test_securities_scraper.py # Tests for data fetching logic
    └── test_symbol_uniqueness.py # Tests for data integrity and validation
```
