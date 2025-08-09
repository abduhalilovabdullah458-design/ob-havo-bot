import httpx
import asyncio
async def get_weather(region_name):
 url=f"http://api.openweathermap.org/data/2.5/weather?q={region_name},UZ&units=metric&appid=a9d86a9dc54f8caf39ac424735ffc2e6"
 async with httpx.AsyncClient() as client:
  resp= await client.get(url)
  return resp.json()
