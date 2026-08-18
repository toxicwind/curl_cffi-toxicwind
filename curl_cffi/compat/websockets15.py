"""websockets v15+ compatibility patches.

websockets 15.0 changed from legacy to asyncio-based implementation.
asyncio.wait_for() cancellation on ws.recv() causes CancelledError cascade.
Use asyncio.timeout() instead.
"""
import asyncio

async def safe_recv(ws, timeout_sec=5):
    """Recv with proper websockets v15 error handling."""
    try:
        async with asyncio.timeout(timeout_sec):
            return await ws.recv()
    except asyncio.TimeoutError:
        return None
    except asyncio.CancelledError:
        return None
    except Exception:
        return None
