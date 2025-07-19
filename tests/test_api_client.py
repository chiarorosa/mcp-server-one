"""
Testes para o MCP Server One
"""
import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock

from mcp_server_one.api_client import APIClient, JSONPlaceholderAPI, CatFactsAPI, JokeAPI, QRcodeAPI


@pytest.fixture
def mock_client():
    """Fixture para cliente HTTP mock"""
    client = AsyncMock(spec=APIClient)
    return client


@pytest.fixture
def jsonplaceholder_api(mock_client):
    """Fixture para JSONPlaceholder API"""
    return JSONPlaceholderAPI(mock_client)


@pytest.fixture
def catfacts_api(mock_client):
    """Fixture para Cat Facts API"""
    return CatFactsAPI(mock_client)


@pytest.fixture
def joke_api(mock_client):
    """Fixture para Joke API"""
    return JokeAPI(mock_client)

@pytest.fixture
def qrcode_api(mock_client):
    """Fixture para QR code API"""
    return QRcodeAPI(mock_client)


class TestJSONPlaceholderAPI:
    """Testes para JSONPlaceholder API"""
    
    @pytest.mark.asyncio
    async def test_get_posts(self, jsonplaceholder_api, mock_client):
        """Testa busca de posts"""
        # Arrange
        mock_posts = [
            {"id": 1, "title": "Post 1", "body": "Body 1", "userId": 1},
            {"id": 2, "title": "Post 2", "body": "Body 2", "userId": 2}
        ]
        mock_client.get.return_value = mock_posts
        
        # Act
        result = await jsonplaceholder_api.get_posts()
        
        # Assert
        assert result == mock_posts
        mock_client.get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")
    
    @pytest.mark.asyncio
    async def test_get_posts_with_limit(self, jsonplaceholder_api, mock_client):
        """Testa busca de posts com limite"""
        # Arrange
        mock_posts = [
            {"id": 1, "title": "Post 1", "body": "Body 1", "userId": 1},
            {"id": 2, "title": "Post 2", "body": "Body 2", "userId": 2},
            {"id": 3, "title": "Post 3", "body": "Body 3", "userId": 3}
        ]
        mock_client.get.return_value = mock_posts
        
        # Act
        result = await jsonplaceholder_api.get_posts(limit=2)
        
        # Assert
        assert len(result) == 2
        assert result == mock_posts[:2]
    
    @pytest.mark.asyncio
    async def test_get_post(self, jsonplaceholder_api, mock_client):
        """Testa busca de post específico"""
        # Arrange
        mock_post = {"id": 1, "title": "Post 1", "body": "Body 1", "userId": 1}
        mock_client.get.return_value = mock_post
        
        # Act
        result = await jsonplaceholder_api.get_post(1)
        
        # Assert
        assert result == mock_post
        mock_client.get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts/1")
    
    @pytest.mark.asyncio
    async def test_get_users(self, jsonplaceholder_api, mock_client):
        """Testa busca de usuários"""
        # Arrange
        mock_users = [
            {"id": 1, "name": "User 1", "email": "user1@example.com"},
            {"id": 2, "name": "User 2", "email": "user2@example.com"}
        ]
        mock_client.get.return_value = mock_users
        
        # Act
        result = await jsonplaceholder_api.get_users()
        
        # Assert
        assert result == mock_users
        mock_client.get.assert_called_once_with("https://jsonplaceholder.typicode.com/users")
    
    @pytest.mark.asyncio
    async def test_create_post(self, jsonplaceholder_api, mock_client):
        """Testa criação de post"""
        # Arrange
        mock_post = {"id": 101, "title": "New Post", "body": "New Body", "userId": 1}
        mock_client.post.return_value = mock_post
        
        # Act
        result = await jsonplaceholder_api.create_post("New Post", "New Body", 1)
        
        # Assert
        assert result == mock_post
        mock_client.post.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/posts",
            {"title": "New Post", "body": "New Body", "userId": 1}
        )


class TestCatFactsAPI:
    """Testes para Cat Facts API"""
    
    @pytest.mark.asyncio
    async def test_get_random_fact(self, catfacts_api, mock_client):
        """Testa busca de fato aleatório"""
        # Arrange
        mock_fact = {"fact": "Cats are amazing", "length": 16}
        mock_client.get.return_value = mock_fact
        
        # Act
        result = await catfacts_api.get_random_fact()
        
        # Assert
        assert result == mock_fact
        mock_client.get.assert_called_once_with("https://catfact.ninja/fact")
    
    @pytest.mark.asyncio
    async def test_get_facts(self, catfacts_api, mock_client):
        """Testa busca de múltiplos fatos"""
        # Arrange
        mock_facts = {
            "data": [
                {"fact": "Fact 1", "length": 7},
                {"fact": "Fact 2", "length": 7}
            ]
        }
        mock_client.get.return_value = mock_facts
        
        # Act
        result = await catfacts_api.get_facts(limit=2)
        
        # Assert
        assert result == mock_facts
        mock_client.get.assert_called_once_with("https://catfact.ninja/facts", {"limit": 2})


class TestJokeAPI:
    """Testes para Joke API"""
    
    @pytest.mark.asyncio
    async def test_get_random_joke(self, joke_api, mock_client):
        """Testa busca de piada aleatória"""
        # Arrange
        mock_joke = {"setup": "Why did the chicken cross the road?", "punchline": "To get to the other side!"}
        mock_client.get.return_value = mock_joke
        
        # Act
        result = await joke_api.get_random_joke()
        
        # Assert
        assert result == mock_joke
        mock_client.get.assert_called_once_with("https://official-joke-api.appspot.com/random_joke")
    
    @pytest.mark.asyncio
    async def test_get_jokes_by_type(self, joke_api, mock_client):
        """Testa busca de piadas por tipo"""
        # Arrange
        mock_jokes = [{"setup": "Programming joke", "punchline": "Haha!"}]
        mock_client.get.return_value = mock_jokes
        
        # Act
        result = await joke_api.get_jokes_by_type("programming")
        
        # Assert
        assert result == mock_jokes
        mock_client.get.assert_called_once_with("https://official-joke-api.appspot.com/jokes/programming/random")

class TestQrCodeAPI:
    """Testes para QR code API"""

    @pytest.mark.asyncio
    async def test_generate_qr_code(self, qrcode_api, mock_client):
        """Testa gerar um QRcode"""
        # Arrange
        mock_qr=b"Pablo > Sam"
        mock_client.get_bytes.return_value = mock_qr

        # Act
        result = await qrcode_api.generate_qrcode("foo")

        # Assert
        assert result == mock_qr
        mock_client.get_bytes.assert_called_once_with("https://api.qrserver.com/v1/create-qr-code/?data=foo")

