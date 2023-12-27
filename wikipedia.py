import requests
import speech_recognition as sr

from rich import print
from rich.console import Console
from speaker import speak

# Create a speech recognition object
recognizer = sr.Recognizer()

# Set the initial energy threshold
recognizer.energy_threshold = 900

def search_wikipedia_api(query):
    base_url = "https://en.wikipedia.org/w/api.php"

    # Request information about the page
    params_info = {
        "action": "query",
        "format": "json",
        "titles": query,
        "prop": "info",
        "inprop": "url",
    }
    response_info = requests.get(base_url, params=params_info)
    data_info = response_info.json()

    # Extract information from the API response
    pages = data_info.get("query", {}).get("pages", {})
    if pages:
        page_info = next(iter(pages.values()))
        pageid = page_info.get("pageid")
        title = page_info.get("title")
        url = page_info.get("fullurl")

        # Check if page ID is None
        if pageid is not None:
            # Request the extract (summary) of the page
            params_extract = {
                "action": "query",
                "format": "json",
                "pageids": pageid,
                "prop": "extracts",
                "exintro": True,
                "explaintext": True,
            }
            response_extract = requests.get(base_url, params=params_extract)
            data_extract = response_extract.json()
            extract = data_extract.get("query", {}).get("pages", {}).get(str(pageid), {}).get("extract", "")

            result = {
                "pageid": pageid,
                "title": title,
                "url": url,
                "extract": extract,
            }

            return result
        else:
            return "No results found on Wikipedia."
    else:
        return "No results found on Wikipedia."

# Example usage:
def display_wikipedia_results(result):
    # Create a Rich Console
    console = Console()

    if isinstance(result, dict):
        # Display the formatted output using rich
        console.print("Wikipedia Search Results:", style="bold underline")
        console.print(f"[link={result['url']}]{result['title']}[/link]")
        console.print(f"Page ID: {result['pageid']}")
        console.print("\nSummary:")
        console.print(result['extract'])
    else:
        console.print(result)

def wiki_query():  

    with sr.Microphone() as source:
                print("loading resources...")
                recognizer.adjust_for_ambient_noise(source)
                             

                # Start listening with dynamic threshold
                print("what do you want to search for...")
                speak("what do you want to search for... ")
                audio = recognizer.listen(source)

                try:
                    # Recognize speech using Google Speech Recognition
                    text = recognizer.recognize_google(audio)
                    print(f"query: {text}")                    
                    
                    query = text
                    wikipedia_api_result = search_wikipedia_api(query)
                    
                    if isinstance(wikipedia_api_result, dict):
                        # Check if the extract is not empty before displaying and speaking
                        if wikipedia_api_result['extract']:
                            display_wikipedia_results(wikipedia_api_result)
                            speak(wikipedia_api_result['extract'])
                        else:
                            print("No information available on wikipedia.")
                            speak("No information available on wikipedia.")
                    else:
                        print(wikipedia_api_result)
                
                except sr.UnknownValueError:
                    print("Sorry, could not understand audio.")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

