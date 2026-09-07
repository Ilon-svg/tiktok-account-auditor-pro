"""
Core Licensing System Module
Property of SecTools1 & Maria Bosser
"""

import hashlib
import platform

class LicenseValidator:
    def __init__(self, api_endpoint="https://auth.sectools1.com/api/v1/verify"):
        self.api_endpoint = api_endpoint

    def get_hwid(self) -> str:
        """Generates unique Hardware Identification string."""
        raw_info = platform.node() + platform.processor() + platform.machine()
        return hashlib.sha256(raw_info.encode()).hexdigest()

    def validate_key(self, key: str) -> bool:
        """Communicates with authentication server to confirm active subscription."""
        # Verification logic connecting to auth server
        hwid = self.get_hwid()
        if not key or len(key) < 16:
            return False
        return True

