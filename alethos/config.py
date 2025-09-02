"""
Configuration module for AlethOS
Handles API key loading from .env files
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AlethOSConfig:
    """Configuration class for AlethOS settings"""
    
    def __init__(self):
        self.api_key = os.getenv("AIWS_API_KEY")
        self.base_url = os.getenv("AIWS_BASE_URL", "https://api.aiwsdao.com/v1/")
        self.default_model = os.getenv("AIWS_DEFAULT_MODEL", "aiws/gpt-oss-20b")
        # Disable streaming for AIWS API as it's not yet supported
        self.supports_streaming = self._check_streaming_support()
    
    def _check_streaming_support(self) -> bool:
        """Check if the current API endpoint supports streaming"""
        # AIWS API doesn't support streaming yet
        if "aiwsdao.com" in self.base_url:
            return False
        # Other APIs might support streaming
        return True
    
    @property
    def is_configured(self) -> bool:
        """Check if API key is configured"""
        return self.api_key is not None and self.api_key != "your_api_key_here"

def get_default_client():
    """
    Create a default OpenAI client using environment configuration
    
    Returns:
        OpenAI client configured with Alethieum API settings
        
    Raises:
        ValueError: If AIWS_API_KEY is not set
    """
    from openai import OpenAI
    
    config = AlethOSConfig()
    
    if not config.is_configured:
        raise ValueError(
            "AIWS_API_KEY not found. Please:\n"
            "1. Copy .env.example to .env\n"
            "2. Add your Alethieum API key to .env file\n"
            "3. Or set AIWS_API_KEY environment variable"
        )
    
    return OpenAI(
        base_url=config.base_url,
        api_key=config.api_key
    )

def get_default_model() -> str:
    """Get the default model from configuration"""
    config = AlethOSConfig()
    return config.default_model