import pytest
from app.main import app

def test_home_endpoint():
    """Test the home endpoint returns 200"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to CI/CD Pipeline Demo!' in response.data

def test_health_endpoint():
    """Test the health endpoint"""
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_info_endpoint():
    """Test the info endpoint"""
    client = app.test_client()
    response = client.get('/api/info')
    assert response.status_code == 200
    assert b'CI/CD Python Flask App' in response.data