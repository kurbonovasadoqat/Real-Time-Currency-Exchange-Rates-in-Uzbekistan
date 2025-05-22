# currency_bot/interfaces/rate_provider_interface.py

from abc import ABC, abstractmethod
from typing import Optional

class RateProviderInterface(ABC):
    @abstractmethod
    async def get_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        """Valyuta kursini qaytaradi: from → to"""
        pass
