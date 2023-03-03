from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class Action(str, Enum):
    Bundle="Bundle"
    Exclude="Exclude"
    Unbundle="Unbundle"
    Include="Include"

class Routing(str, Enum):
    Genoa="Genoa"
    Group="Group"
 



class Data(BaseModel):
    
    Pharmacy_Report_Name: str
    Attribute: str
    Action: Action
    Value: str
    RuleOrder: int=Field(le=4, gt=0)
    RoutingAddress1: Optional[str]


class Bundle(BaseModel):
    Pharmacy_Report_Name: str
    Attribute: str
    Action = Action
    Routing: str=Field(max_length=5)
    RoutingAttribute: str=Field(max_length=8)
    Value: str
    RuleOrder: int=Field(le=4, gt=0)
