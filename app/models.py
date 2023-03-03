from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,DateTime, Identity,CHAR
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.schema import Sequence


class NewReportRule(Base):

    __tablename__ = "AR_report_rules_FASTAPI"

    id = Column(Integer, primary_key=True)
    Pharmacy_Report_Name = Column(String, nullable=False)
    Attribute= Column(String, nullable=False)
    Action= Column(String, nullable=False)
    Value= Column(String, nullable=False)
    RuleOrder= Column(Integer, nullable=False)
    Routing= Column(String)
    RoutingAttribute= Column(String)
    Express= Column(Boolean)
    RoutingName= Column(String)
    RoutingAddress1= Column(String)
    RoutingCity= Column(String)
    routingState= Column(String)
    routhingZip= Column(String) #Freeman spelled it like this :) 
    PayeeID= Column(Integer)
    payeeSecondID= Column(String, server_default=text('left(convert(varchar(36), newid()) + convert(varchar(36), newid()), 10)'))
    created_at = Column(DateTime(timezone=False), nullable=False, server_default=text('getdate()'))


class BackupRulesReport(Base):

    __tablename__ = "AR_report_rules_FASTAPI-BACKUP_DB"

    id = Column(Integer, primary_key=True)
    Pharmacy_Report_Name = Column(String, nullable=False)
    Attribute= Column(String, nullable=False)
    Action= Column(String, nullable=False)
    Value= Column(String, nullable=False)
    RuleOrder= Column(Integer, nullable=False)
    Routing= Column(String)
    RoutingAttribute= Column(String)
    Express= Column(Boolean)
    RoutingName= Column(String)
    RoutingAddress1= Column(String)
    RoutingCity= Column(String)
    routingState= Column(String)
    routhingZip= Column(String) #Freeman spelled it like this :) 
    PayeeID= Column(Integer, Sequence("PayeeID_seq", start=502000, increment=1))
    payeeSecondID= Column(String, server_default=text('left(convert(varchar(36), newid()) + convert(varchar(36), newid()), 10)'))
    created_at = Column(DateTime(timezone=False), nullable=False, server_default=text('getdate()'))
