from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=tavily_api_key)

def tavily_search(query: str):
    """
    Search for a query using Tavily API.

    Args:
        query (str): The search query.

    Returns:
        dict: The search results from Tavily API.
    """
    try:
        response = client.search(query=query, max_results=5)
        results = []

        for index, result in enumerate(response.get("results", []), start=1):
            title = result.get("title", "Unknown Title")
            url = result.get("url", "No URL")
            snippet = result.get("content", "").strip()

            # Limit snippet length
            if len(snippet) > 300:
                snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

            formatted_result = (
                f"{index}. {title}\n"
                f"   🔗 {url}\n"
                f"   📝 {snippet}"
            )

            results.append(formatted_result)

        return "\n\n".join(results) if results else "No search results found."

    except Exception as e:
        print(f"Error while searching Tavily: {e}")
        return None