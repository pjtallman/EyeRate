from enum import Enum
from sqlalchemy import Column, String, Integer, Enum as SQLEnum
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FinancialSecurityType(str, Enum):
    STOCK = "Stock"
    BOND = "Bond"
    MUTUAL_FUND = "Mutual Fund"
    ETF = "ETF"
    MONEY_MARKET = "Money Market"

class AssetClass(str, Enum):
    LARGE_CAP_STOCK = "Large Cap Stock"
    SMALL_CAP_STOCK = "Small Cap Stock"
    INTERNATIONAL_STOCK = "International Stock"
    DOMESTIC_BOND = "Domestic Bond"
    INTERNATIONAL_BOND = "International Bond"
    MONEY_MARKET = "Money Market"
    CASH = "Cash"

class FinancialSecurity(Base):
    __tablename__ = "securities"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    financial_security_type = Column(SQLEnum(FinancialSecurityType), nullable=False)
    asset_class = Column(SQLEnum(AssetClass), nullable=True)
    
    previous_close = Column(String, nullable=True)
    open_price = Column(String, nullable=True)
    current_price = Column(String, nullable=True)
    nav = Column(String, nullable=True)
    range_52_week = Column(String, nullable=True)
    avg_volume = Column(String, nullable=True)
    yield_30_day = Column(String, nullable=True)
    yield_7_day = Column(String, nullable=True)
