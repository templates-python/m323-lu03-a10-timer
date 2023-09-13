import pytest
from unittest.mock import Mock, patch, AsyncMock
from sol import api_response_callback, async_timer, fetch_data_from_api


# 1. Test für api_response_callback
def test_api_response_callback(capsys):
    api_response_callback({"message": "test"})
    captured = capsys.readouterr()
    assert "API Response: {'message': 'test'}" in captured.out


# 2. Test für async_timer
@pytest.mark.asyncio
async def test_async_timer(capsys):
    with patch('asyncio.sleep', side_effect=[None, None, StopAsyncIteration]):
        try:
            await async_timer()
        except StopAsyncIteration:
            pass
    captured = capsys.readouterr()
    assert "0\n1\n" in captured.out


# 3. Test für fetch_data_from_api
@pytest.mark.asyncio
async def test_fetch_data_from_api():
    mock_callback = Mock()
    mock_response = Mock()
    mock_response.text = "test response"  # Setzen Sie den Response-Text
    with patch('httpx.AsyncClient', return_value=Mock(get=AsyncMock(return_value=mock_response))), \
         patch('asyncio.sleep', side_effect=[None, StopAsyncIteration]):
        try:
            await fetch_data_from_api(mock_callback)
        except StopAsyncIteration:
            pass
    mock_callback.assert_called_with(mock_response)
