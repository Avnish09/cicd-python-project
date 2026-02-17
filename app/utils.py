"""Utility functions for the application"""

def format_response(data: dict, status: str = "success") -> dict:
    """
    Format API response consistently
    
    Args:
        data: Response data
        status: Response status (success/error)
    
    Returns:
        Formatted response dictionary
    """
    return {
        "status": status,
        "data": data
    }

def validate_environment(env: str) -> bool:
    """
    Validate environment name
    
    Args:
        env: Environment name
    
    Returns:
        True if valid, False otherwise
    """
    valid_envs = ['development', 'staging', 'production']
    return env in valid_envs