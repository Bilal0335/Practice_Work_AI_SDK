

# ! output_data_guardrails.py
from pydantic import BaseModel


class MyOutputGuardrail(BaseModel):
    is_hotel_sanata_query:bool
    is_hotel_sanata_account_or_text_query:bool
    reason:str