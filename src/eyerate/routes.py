from fastapi import APIRouter, Depends, HTTPException, Request, Form, Header
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from .models import FinancialSecurity, FinancialSecurityType, AssetClass

router = APIRouter()

@router.get("/securities", response_class=HTMLResponse)
async def list_securities(request: Request, accept_language: str = Header(None), db: Session = Depends(lambda: None)):
    pass

@router.post("/securities/create")
async def create_security(symbol: str = Form(...), name: str = Form(...), security_type: FinancialSecurityType = Form(...), asset_class: Optional[AssetClass] = Form(None), previous_close: Optional[str] = Form(None), open_price: Optional[str] = Form(None), current_price: Optional[str] = Form(None), nav: Optional[str] = Form(None), range_52_week: Optional[str] = Form(None), avg_volume: Optional[str] = Form(None), yield_30_day: Optional[str] = Form(None), yield_7_day: Optional[str] = Form(None), db: Session = Depends(lambda: None)):
    if db.query(FinancialSecurity).filter(FinancialSecurity.symbol == symbol.upper()).first(): raise HTTPException(status_code=400, detail="already exists")
    db.add(FinancialSecurity(symbol=symbol.upper(), name=name, security_type=security_type, asset_class=asset_class, previous_close=previous_close, open_price=open_price, current_price=current_price, nav=nav, range_52_week=range_52_week, avg_volume=avg_volume, yield_30_day=yield_30_day, yield_7_day=yield_7_day))
    db.commit(); return RedirectResponse(url="/admin/securities", status_code=303)

@router.post("/securities/update/{sec_id}")
async def update_security(sec_id: int, symbol: str = Form(...), name: str = Form(...), security_type: FinancialSecurityType = Form(...), asset_class: Optional[AssetClass] = Form(None), previous_close: Optional[str] = Form(None), open_price: Optional[str] = Form(None), current_price: Optional[str] = Form(None), nav: Optional[str] = Form(None), range_52_week: Optional[str] = Form(None), avg_volume: Optional[str] = Form(None), yield_30_day: Optional[str] = Form(None), yield_7_day: Optional[str] = Form(None), db: Session = Depends(lambda: None)):
    sec = db.query(FinancialSecurity).filter(FinancialSecurity.id == sec_id).first()
    if sec:
        sec.symbol = symbol; sec.name = name; sec.security_type = security_type; sec.asset_class = asset_class
        sec.previous_close = previous_close; sec.open_price = open_price; sec.current_price = current_price
        sec.nav = nav; sec.range_52_week = range_52_week; sec.avg_volume = avg_volume
        sec.yield_30_day = yield_30_day; sec.yield_7_day = yield_7_day; db.commit()
    return RedirectResponse(url="/admin/securities", status_code=303)

@router.post("/securities/delete/{sec_id}")
async def delete_security(sec_id: int, db: Session = Depends(lambda: None)):
    sec = db.query(FinancialSecurity).filter(FinancialSecurity.id == sec_id).first()
    if sec: db.delete(sec); db.commit()
    return RedirectResponse(url="/admin/securities", status_code=303)

@router.get("/securities/search")
async def search_securities(q: str, db: Session = Depends(lambda: None)):
    pass

@router.get("/securities/lookup")
async def lookup_security(symbol: str, db: Session = Depends(get_db)):
    pass

class BulkCreateRequest(BaseModel): symbols: List[str]
@router.post("/securities/bulk_create")
async def bulk_create_securities(request: BulkCreateRequest, db: Session = Depends(lambda: None)):
    pass

class BulkDeleteRequest(BaseModel): symbols: List[str]
@router.post("/securities/bulk_delete")
async def bulk_delete_securities(request: BulkDeleteRequest, db: Session = Depends(lambda: None)):
    pass
