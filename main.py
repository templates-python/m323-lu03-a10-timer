import asyncio
import httpx


def api_response_callback(response_data):
    """
    Callback-Funktion, die aufgerufen wird, nachdem die API-Antwort empfangen wurde.

    Args:
    - response_data: Die Daten, die von der API empfangen wurden.

    Returns:
    - None, da die Daten direkt in der Konsole ausgegeben werden.
    """
    print(f'API Response: {response_data}')


async def fetch_data_from_api(callback):
    """
    Diese Funktion ruft asynchron alle 3 Sekunden eine API ('https://run.mocky.io/v3/685db531-06e7-4d66-bbf6-99de9f2feab3?mocky-delay=3000ms') auf, die eine
    Verzögerung von 3 Sekunden simuliert. Nachdem die Daten von der API abgerufen wurden, wird der bereitgestellte
    Callback mit den Daten aufgerufen.

    Args:
    - callback: Die Callback-Funktion, die aufgerufen wird, nachdem die API-Daten empfangen wurden.

    Returns:
    - None, da die Daten an die Callback-Funktion weitergegeben werden.
    """
    while True:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                'https://run.mocky.io/v3/685db531-06e7-4d66-bbf6-99de9f2feab3?mocky-delay=3000ms'
            )
        callback(response)
        await asyncio.sleep(3)


async def async_timer():
    """
    Diese Funktion fungiert als asynchroner Timer, der jede Sekunde hochzählt und den aktuellen Wert ausgibt.
    Sie verwendet `asyncio.sleep` für die Verzögerung und führt eine endlose Schleife aus, die den Zähler jede Sekunde erhöht.

    Returns:
    - None, da der Zählerstand direkt in der Konsole ausgegeben wird.
    """

    count = 0
    while True:
        print(count)
        count += 1
        await asyncio.sleep(1)


async def main():
    """
    Hauptfunktion, die beide asynchrone Funktionen, `fetch_data_from_api` und `async_timer`, parallel ausführt.
    Sie verwendet `asyncio.create_task` um die beiden Funktionen als separate, gleichzeitig laufende Tasks zu starten.

    Returns:
    - None, da alle Ausgaben direkt in den jeweiligen Funktionen erfolgen.
    """

    api_task = asyncio.create_task(fetch_data_from_api(api_response_callback))
    timer_task = asyncio.create_task(async_timer())

    await api_task
    await timer_task


if __name__ == '__main__':
    asyncio.run(main())
