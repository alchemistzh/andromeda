# coding: utf-8

from sqlalchemy import BigInteger, Column, DateTime, String

from data import model


class StockProfile(model.Base):
    """ StockProfile is a data structure for simple and basic stock infomation.

    Required attributes:
        id: Unique id of a stock. Ex: 600100.
        name: Short name of the stock.

    Optional attributes:
        exchange: Exchange corporation of the stock. Ex: SSE.
        pinyin: Pinyin acronym of the name. Ex: zhgf.
        market_cap: Market capitalization.
        float_cap: Free-float capitalization.
        shares: Outstanding Shares.
        float_shares: Free-float shares.
        update_time: Last update time.
    """

    __tablename__ = "stock_profile"

    id = Column(String(16), primary_key=True)
    name = Column(String(16), nullable=False)
    exchange = Column(String(16))
    pinyin = Column(String(16))

    market_cap = Column(BigInteger)
    float_cap = Column(BigInteger)
    shares = Column(BigInteger)
    float_shares = Column(BigInteger)

    update_time = Column(DateTime)
