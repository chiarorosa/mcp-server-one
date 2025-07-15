"""
Cliente HTTP para interagir com APIs públicas
"""
import httpx
from typing import Any, Dict, List, Optional
import json
import asyncio


class APIClient:
    """Cliente HTTP para APIs públicas"""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=timeout)
    
    async def close(self):
        """Fecha o cliente HTTP"""
        await self.client.aclose()
    
    async def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Realiza uma requisição GET"""
        try:
            response = await self.client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise Exception(f"Erro HTTP: {e}")
        except json.JSONDecodeError:
            raise Exception("Resposta não é um JSON válido")
    
    async def post(self, url: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Realiza uma requisição POST"""
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise Exception(f"Erro HTTP: {e}")
        except json.JSONDecodeError:
            raise Exception("Resposta não é um JSON válido")


class JSONPlaceholderAPI:
    """Cliente para JSONPlaceholder API"""
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self, client: APIClient):
        self.client = client
    
    async def get_posts(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Busca posts do JSONPlaceholder"""
        url = f"{self.BASE_URL}/posts"
        posts = await self.client.get(url)
        if limit:
            posts = posts[:limit]
        return posts
    
    async def get_post(self, post_id: int) -> Dict[str, Any]:
        """Busca um post específico"""
        url = f"{self.BASE_URL}/posts/{post_id}"
        return await self.client.get(url)
    
    async def get_comments(self, post_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Busca comentários (opcionalmente de um post específico)"""
        if post_id:
            url = f"{self.BASE_URL}/posts/{post_id}/comments"
        else:
            url = f"{self.BASE_URL}/comments"
        return await self.client.get(url)
    
    async def get_users(self) -> List[Dict[str, Any]]:
        """Busca usuários"""
        url = f"{self.BASE_URL}/users"
        return await self.client.get(url)
    
    async def get_user(self, user_id: int) -> Dict[str, Any]:
        """Busca um usuário específico"""
        url = f"{self.BASE_URL}/users/{user_id}"
        return await self.client.get(url)
    
    async def get_todos(self, user_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Busca todos (opcionalmente de um usuário específico)"""
        if user_id:
            url = f"{self.BASE_URL}/users/{user_id}/todos"
        else:
            url = f"{self.BASE_URL}/todos"
        return await self.client.get(url)
    
    async def create_post(self, title: str, body: str, user_id: int) -> Dict[str, Any]:
        """Cria um novo post (fake)"""
        url = f"{self.BASE_URL}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return await self.client.post(url, data)


class CatFactsAPI:
    """Cliente para Cat Facts API"""
    
    BASE_URL = "https://catfact.ninja"
    
    def __init__(self, client: APIClient):
        self.client = client
    
    async def get_random_fact(self) -> Dict[str, Any]:
        """Busca um fato aleatório sobre gatos"""
        url = f"{self.BASE_URL}/fact"
        return await self.client.get(url)
    
    async def get_facts(self, limit: int = 10) -> Dict[str, Any]:
        """Busca múltiplos fatos sobre gatos"""
        url = f"{self.BASE_URL}/facts"
        params = {"limit": limit}
        return await self.client.get(url, params)


class JokeAPI:
    """Cliente para Official Joke API"""
    
    BASE_URL = "https://official-joke-api.appspot.com"
    
    def __init__(self, client: APIClient):
        self.client = client
    
    async def get_random_joke(self) -> Dict[str, Any]:
        """Busca uma piada aleatória"""
        url = f"{self.BASE_URL}/random_joke"
        return await self.client.get(url)
    
    async def get_jokes_by_type(self, joke_type: str) -> List[Dict[str, Any]]:
        """Busca piadas por tipo"""
        url = f"{self.BASE_URL}/jokes/{joke_type}/random"
        return await self.client.get(url)


class APIManager:
    """Gerenciador de todas as APIs"""
    
    def __init__(self):
        self.client = APIClient()
        self.jsonplaceholder = JSONPlaceholderAPI(self.client)
        self.catfacts = CatFactsAPI(self.client)
        self.jokes = JokeAPI(self.client)
    
    async def close(self):
        """Fecha todas as conexões"""
        await self.client.close()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
