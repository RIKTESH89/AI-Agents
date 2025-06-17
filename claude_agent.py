from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import os
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, List, Dict, Any, Sequence
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import json
import random
import json
import requests
from datetime import datetime, timedelta

# Configuration
GEMINI_API_KEY = "AIzaSyA1TNnxoO491zkl_9hUOTMrwey6MvnRXgQ"  # Set your API key as environment variable
GEMINI_MODEL = "gemini-2.0-flash"

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "hermes3:8b"

# Validate API key
if not GEMINI_API_KEY:
    raise ValueError("Please set GEMINI_API_KEY environment variable")

# Global state to store event planning data
event_planning_data = {
    "user_request": "",
    "calendar_info": "",
    "finance_info": "",
    "health_info": "",
    "weather_info": "",
    "traffic_info": "",
    "invitation_info": "",
    "whatsapp_status": "",
    "email_status": "",
    "current_step": "start"
}

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    current_agent: str
    next_action: str

# ============================================================================
# ENHANCED SCHEDULER AGENT TOOLS (6 tools)
# ============================================================================

@tool
def calendar(query: str) -> str:
    """
    Check calendar events and availability for specific dates and times.
    
    WHEN TO USE:
    - ANY event that requires scheduling (birthdays, meetings, conferences, parties, gatherings)
    - When user mentions specific dates or asks about availability
    - For events that need time coordination with multiple people
    - When checking for conflicts with existing commitments
    
    CONTEXTS:
    ✅ Use for: Birthdays, meetings, conferences, parties, social gatherings, appointments
    ❌ Skip for: Simple reminders, one-time tasks without specific timing
    
    This tool provides date availability, suggests optimal time slots, and identifies potential conflicts.
    """
    global event_planning_data
    
    # Extract date information from query
    if "30th june" in query.lower() or "june 30" in query.lower():
        result = "📅 Calendar Check: June 30th is available! No conflicts found. Recommended time slots: 2:00 PM - 6:00 PM or 10:00 AM - 2:00 PM. Weekend timing is perfect for family gatherings."
    elif any(keyword in query.lower() for keyword in ["birthday", "party", "celebration"]):
        result = "📅 Calendar Analysis: Weekend dates are optimal for parties. Multiple time slots available. Consider 2-6 PM for family events or 7-11 PM for adult celebrations."
    elif any(keyword in query.lower() for keyword in ["meeting", "conference", "business"]):
        result = "📅 Calendar Check: Weekday business hours available. Recommended slots: 10:00 AM - 12:00 PM or 2:00 PM - 4:00 PM. Conference rooms available."
    else:
        result = f"📅 Calendar checked for: {query}. Available time slots found. No major conflicts detected."
    
    event_planning_data["calendar_info"] = result
    return result

@tool
def finance(query: str) -> str:
    """
    Analyze budget requirements and provide cost estimates for events.
    
    WHEN TO USE:
    - Events involving significant expenses (parties, conferences, weddings, corporate events)
    - When user mentions budget concerns or asks about costs
    - For events requiring multiple vendors or services
    - When planning needs cost optimization
    
    CONTEXTS:
    ✅ Use for: Birthday parties, weddings, conferences, corporate events, large gatherings
    ❌ Skip for: Simple meetings, small gatherings (under 5 people), free events
    
    This tool provides detailed cost breakdowns, budget recommendations, and cost-saving suggestions.
    """
    global event_planning_data
    
    if "birthday" in query.lower() and "party" in query.lower():
        result = "💰 Budget Analysis: For a birthday party at home (15-20 guests):\n- Decorations: $50-80\n- Food & Cake: $150-250\n- Activities/Games: $30-50\n- Party Favors: $40-60\nTotal Estimated Budget: $270-440\nTip: Consider potluck to reduce food costs!"
    elif "meeting" in query.lower() or "conference" in query.lower():
        result = "💰 Budget Analysis: For business meetings/conferences:\n- Venue: $200-500\n- Catering: $25-50 per person\n- AV Equipment: $100-300\n- Materials: $50-150\nConsider virtual options to reduce costs."
    elif "wedding" in query.lower():
        result = "💰 Budget Analysis: Wedding planning requires detailed budgeting:\n- Venue: 40-50% of budget\n- Catering: 25-30%\n- Photography: 10-15%\n- Recommend setting total budget first, then allocating by category."
    else:
        result = f"💰 Budget planning for: {query}. Please specify event type and guest count for accurate estimates. Consider venue, catering, and activity costs."
    
    event_planning_data["finance_info"] = result
    return result

@tool
def health(query: str) -> str:
    """
    Check health and safety considerations, dietary restrictions, and accessibility needs.
    
    WHEN TO USE:
    - Events involving food service (parties, meetings with catering, celebrations)
    - When planning for diverse groups or elderly/children attendees
    - For events in public spaces or requiring safety protocols
    - When user mentions health concerns or dietary restrictions
    
    CONTEXTS:
    ✅ Use for: Food-related events, large gatherings, events with vulnerable populations, outdoor events
    ❌ Skip for: Simple meetings without food, small familiar groups, virtual events
    
    This tool ensures safety compliance and inclusive planning for all attendees.
    """
    global event_planning_data
    
    if any(keyword in query.lower() for keyword in ["food", "party", "birthday", "celebration"]):
        result = "🏥 Health & Safety Check for Food Events:\n- Common allergens to avoid: Nuts, dairy, gluten, shellfish\n- Ensure vegetarian/vegan options available\n- Keep first aid kit accessible\n- Ask guests about dietary restrictions in advance\n- Consider food handling safety if homemade items"
    elif any(keyword in query.lower() for keyword in ["outdoor", "park", "garden"]):
        result = "🏥 Health & Safety Check for Outdoor Events:\n- Sun protection and shade availability\n- Insect repellent considerations\n- Weather contingency plans\n- Emergency contact information\n- Accessibility for mobility-impaired guests"
    elif any(keyword in query.lower() for keyword in ["children", "kids", "family"]):
        result = "🏥 Health & Safety Check for Family Events:\n- Child-proof environment\n- Age-appropriate activities and food\n- Supervision requirements\n- Emergency contacts for all children\n- Allergy awareness and medical information"
    else:
        result = "🏥 General Health & Safety Guidelines:\n- Ensure venue accessibility\n- Have emergency contact information\n- Consider any special needs of attendees\n- Maintain clean and safe environment"
    
    event_planning_data["health_info"] = result
    return result


WEATHER_DATA = {
    "specific_dates": {},
    
    "outdoor_events": [
        "🌤️ Outdoor Event Weather Considerations:\n- Current conditions: Partly sunny, 76°F (24°C)\n- 7-day outlook shows stable weather\n- Recommend tent rental for shade\n- Wind speeds 5-10 mph - good for decorations\n- Evening temperatures dropping to 68°F",
        "☀️ Perfect Outdoor Weather Expected:\n- Temperature range: 72-82°F (22-28°C)\n- Clear skies forecasted\n- Low humidity at 45%\n- Gentle breeze from the west\n- No precipitation in 10-day outlook",
        "⛅ Mixed Outdoor Conditions:\n- Morning: 70°F, partly cloudy\n- Afternoon: 78°F, mostly sunny\n- 25% chance of brief showers\n- Have backup indoor space ready\n- Consider weather-resistant decorations",
        "🌥️ Overcast but Pleasant:\n- Temperature: 74-76°F (23-24°C)\n- Cloudy skies, no rain expected\n- Perfect for photography (soft lighting)\n- Comfortable conditions for guests\n- Light jacket recommended for evening",
        "🌦️ Variable Weather Alert:\n- Temperature: 68-75°F (20-24°C)\n- 60% chance of scattered showers\n- Consider postponement or indoor venue\n- If proceeding, ensure covered areas\n- Weather may clear by evening",
        "🌞 Hot Summer Day:\n- Temperature: 88-95°F (31-35°C)\n- Sunny and hot conditions\n- Provide shade and hydration stations\n- Schedule during cooler morning/evening hours\n- Heat advisory may be in effect",
        "🍃 Breezy Conditions:\n- Temperature: 71-77°F (22-25°C)\n- Partly cloudy with a strong breeze (15-20 mph)\n- Secure all decorations and signage\n- Great for kite flying or sailing events\n- May affect sound systems",
        "🌈 Post-Storm Clearing:\n- Temperature: 75-80°F (24-27°C)\n- Recent rain, now clearing\n- Ground may be muddy or saturated\n- Beautiful post-rain atmosphere\n- Double-check venue drainage and accessibility",
        "🍂 Crisp Autumn Day:\n- Temperature: 55-65°F (13-18°C)\n- Clear, sunny skies, low humidity\n- Perfect for fall festivals, hayrides, apple picking\n- Recommend warm beverages (cider, coffee)\n- Beautiful foliage colors for photos",
        "⛈️ Thunderstorm Watch Issued:\n- Temperature: 75-85°F (24-29°C), high humidity\n- Conditions favorable for severe storms\n- Monitor weather updates closely\n- Have a clear and communicated evacuation plan\n- Unplug sensitive electronic equipment",
        "🌫️ Ethereal Foggy Morning:\n- Temperature: 50-60°F (10-16°C)\n- Dense fog, low visibility\n- Creates a mystical, moody atmosphere\n- May delay start times for safety\n- Use lighting and clear signage to guide guests",
        "❄️ Gentle Snowfall:\n- Temperature: 28-34°F (-2 to 1°C)\n- Light, steady snow expected\n- Creates a magical 'Winter Wonderland' scene\n- Ensure paths are salted/shoveled for safety\n- Provide warming stations or fire pits",
        "💧 Humid & Muggy Conditions:\n- Temperature: 85-92°F (29-33°C) with 80%+ humidity\n- Feels hotter than the actual temperature\n- High risk of heat exhaustion; provide cooling towels\n- Misting fans are highly recommended\n- Increased presence of insects (mosquitoes, gnats)",
        "🤧 Peak Allergy Season:\n- Temperature: 65-75°F (18-24°C), often breezy\n- High pollen count reported in the area\n- Inform guests with severe allergies beforehand\n- Consider having allergy medication (antihistamines) on-site\n- May affect choice of floral decorations",
        "🌊 Coastal Beach Day:\n- Temperature: 78-84°F (26-29°C)\n- Strong, steady onshore sea breeze\n- Be mindful of blowing sand; secure food and belongings\n- Sunscreen and UV protection are critical due to water reflection\n- Check tide charts as they will affect available beach space",
        "⛰️ High Altitude Event:\n- Temperature can vary drastically (e.g., 50-75°F / 10-24°C)\n- Thinner air and stronger UV radiation\n- Guests may need to acclimate; remind them to pace themselves\n- Unpredictable mountain weather (afternoon storms are common)\n- Hydration is key to combating altitude effects",
        "🌇 Golden Hour Perfection:\n- Timed for the hour before sunset\n- Warm, soft, diffused lighting ideal for photography\n- Perfect for romantic settings, weddings, and proposals\n- Temperature will drop quickly as the sun sets\n- Plan for a smooth transition to evening lighting",
        "🌌 Clear Night for Stargazing:\n- Temperature: 55-65°F (13-18°C)\n- No cloud cover, low moonlight (new moon phase is best)\n- Perfect for astronomy events or late-night gatherings\n- Provide blankets and warm drinks\n- Minimize artificial light pollution for the best viewing",
        "🔥 High Fire Danger:\n- Temperature: 90°F+ (32°C+)\n- Extremely dry conditions, low humidity, and breezy\n- Strict ban on open flames (grills, fire pits, candles, smoking)\n- Check and adhere to all local fire restrictions\n- Have fire extinguishers readily available",
        "🥶 Chilly Evening Gathering:\n- Temperature: 45-55°F (7-13°C)\n- Clear skies but a sharp drop in temperature after sunset\n- Patio heaters and fire pits are a must\n- Encourage guests to dress in layers; provide a basket of blankets\n- Serve warm food and drinks to keep guests comfortable",
        "🌧️ Persistent Drizzle:\n- Temperature: 60-68°F (16-20°C)\n- Light, continuous mist or drizzle that soaks everything over time\n- Not a downpour, but will make guests damp and cold\n- Large umbrellas or marquee tents are essential\n- Surfaces can become very slippery; use caution signs",
        "🌡️ Unseasonably Warm/Cold:\n- A sudden, unexpected shift from seasonal norms\n- May catch guests off-guard with their attire\n- Communicate the forecast to guests ahead of time\n- Requires flexible planning (e.g., have fans or heaters on standby)\n- Can impact blooming flowers or fall colors"
    ],
    
    "seasonal_weather": {
        "spring": [
            "🌸 Spring Weather Pattern:\n- Temperature range: 60-75°F (16-24°C)\n- Variable conditions with rain showers\n- Perfect for garden parties and weddings\n- Recommend backup plans for sudden changes\n- Beautiful blooming season backdrop",
            "🌱 Early Spring Conditions:\n- Temperature: 55-68°F (13-20°C)\n- Mix of sun and clouds\n- 40% chance of spring showers\n- Fresh, crisp air ideal for outdoor gatherings\n- Consider guests may need light jackets",
            "🌺 Late Spring Forecast:\n- Temperature: 70-78°F (21-26°C)\n- Mostly sunny with gentle breeze\n- Low chance of rain (15%)\n- Perfect weather for outdoor ceremonies\n- Comfortable for all-day events"
        ],
        "summer": [
            "☀️ Peak Summer Conditions:\n- Temperature: 85-92°F (29-33°C)\n- Hot and sunny - plan accordingly\n- High UV index - provide shade\n- Early morning or evening events recommended\n- Ensure adequate hydration stations",
            "🌞 Typical Summer Day:\n- Temperature: 80-87°F (27-31°C)\n- Sunny with afternoon clouds\n- 20% chance of evening thunderstorms\n- Great pool party weather\n- Consider heat management for guests",
            "🌤️ Mild Summer Weather:\n- Temperature: 75-82°F (24-28°C)\n- Partly cloudy, comfortable conditions\n- Light breeze provides natural cooling\n- Perfect for all-day outdoor events\n- Evening may require light layers"
        ],
        "fall": [
            "🍂 Beautiful Fall Weather:\n- Temperature: 65-72°F (18-22°C)\n- Crisp air with colorful foliage\n- Low humidity, comfortable conditions\n- Perfect for harvest festivals\n- Guests may need sweaters for evening",
            "🍁 Autumn Conditions:\n- Temperature: 58-70°F (14-21°C)\n- Partly cloudy with cool breeze\n- 30% chance of light rain\n- Beautiful seasonal backdrop\n- Consider warming stations for outdoor events",
            "🌾 Late Fall Forecast:\n- Temperature: 50-62°F (10-17°C)\n- Mostly cloudy, cool conditions\n- Possible frost in early morning\n- Cozy weather for bonfire events\n- Indoor backup recommended"
        ],
        "winter": [
            "❄️ Winter Weather Advisory:\n- Temperature: 25-35°F (-4 to 2°C)\n- Snow possible, accumulation 2-4 inches\n- Roads may be hazardous\n- Indoor venues strongly recommended\n- Consider guest travel safety",
            "🌨️ Cold Winter Day:\n- Temperature: 30-38°F (-1 to 3°C)\n- Overcast with light snow flurries\n- Wind chill makes it feel colder\n- Ensure adequate heating\n- Beautiful winter scenery for photos",
            "☃️ Snowy Conditions:\n- Temperature: 20-28°F (-7 to -2°C)\n- Heavy snow expected (6-10 inches)\n- Travel not recommended\n- Perfect for cozy indoor celebrations\n- Check heating and backup power"
        ]
    },
    
    "venue_specific": {
        "garden_party": [
        "🌷 Garden Party Weather:\n- Temperature: 73-79°F (23-26°C)\n- Gentle sunshine filtering through clouds\n- Light breeze perfect for outdoor dining\n- 10% chance of rain - mostly clear\n- Flowers will look spectacular in this light",
        "🌹 Perfect Garden Conditions:\n- Temperature: 68-75°F (20-24°C)\n- Partly sunny with soft light\n- Ideal for photography\n- No wind to disturb table settings\n- Comfortable for guests of all ages",
        "🌻 Sunny Garden Weather:\n- Temperature: 76-83°F (24-28°C)\n- Bright sunshine with gentle breeze\n- May need shade structures\n- Perfect for showcasing garden blooms\n- Consider sunscreen for guests"
        ],
        "beach_event": [
        "🏖️ Beach Weather Forecast:\n- Temperature: 78-84°F (26-29°C)\n- Sunny with ocean breeze\n- Wave height: 2-3 feet\n- UV index: 8 - sunscreen essential\n- Perfect beach party conditions",
        "🌊 Coastal Conditions:\n- Temperature: 75-80°F (24-27°C)\n- Partly cloudy, comfortable sea breeze\n- Tide times favorable for beach activities\n- 15% chance of brief showers\n- Great for water sports",
        "⛵ Breezy Beach Day:\n- Temperature: 72-78°F (22-26°C)\n- Sunny with strong sea breeze (15-20 mph)\n- Excellent for sailing events\n- May be choppy for swimming\n- Secure lightweight decorations"
        ],
        "park_picnic": [
        "🧺 Perfect Picnic Weather:\n- Temperature: 74-80°F (23-27°C)\n- Sunny with scattered clouds\n- Light breeze keeps insects away\n- No rain in forecast\n- Ideal conditions for outdoor dining",
        "🌳 Park Event Conditions:\n- Temperature: 70-76°F (21-24°C)\n- Partly sunny, very pleasant\n- Tree coverage provides natural shade\n- Ground conditions dry and comfortable\n- Great for games and activities",
        "🦋 Nature Perfect Day:\n- Temperature: 72-78°F (22-26°C)\n- Clear skies with gentle wind\n- Wildlife active - great for nature walks\n- Comfortable for extended outdoor time\n- Don't forget the sunscreen"
        ],
        "rooftop_event": [
            "🌇 Golden Hour Perfection:\n- Temperature: 70-77°F (21-25°C)\n- Clear skies, stunning sunset views\n- Light breeze, won't spill the cocktails\n- Visibility: Excellent\n- Perfect for evening socials and photos",
            "🏙️ Crisp City Night:\n- Temperature: 65-72°F (18-22°C)\n- Clear and cool, stars visible\n- May require light jackets or heaters\n- Great for a cozy, upscale atmosphere\n- City lights will look sharp",
            "🌬️ Breezy & Dynamic:\n- Temperature: 72-78°F (22-26°C)\n- Partly cloudy with a noticeable breeze (10-15 mph)\n- Feels fresh and energetic\n- Secure napkins and light items\n- Dramatic cloudscapes for photos"
        ],
        "outdoor_wedding": [
            "💒 Storybook Wedding Day:\n- Temperature: 70-76°F (21-24°C)\n- Soft, diffused sunlight through thin clouds\n- Gentle breeze, perfect for photos\n- Low humidity, comfortable for formal wear\n- Ceremony will be picture-perfect",
            "💍 Golden Hour Glamour:\n- Temperature: 75-82°F (24-28°C)\n- Clear skies leading to a brilliant sunset\n- Warm, but comfortable as the evening approaches\n- Ideal for a late afternoon ceremony\n- No chance of rain to spoil the day",
            "🤍 Elegant Overcast Skies:\n- Temperature: 68-74°F (20-23°C)\n- Fully overcast, providing even, shadow-free light\n- No wind to disturb decor or hairstyles\n- Creates a romantic and intimate mood\n- Guests won't be squinting in the sun"
        ],
        "vineyard_tour": [
            "🍇 Perfect Tasting Weather:\n- Temperature: 72-78°F (22-26°C)\n- Sunny with a few puffy clouds\n- Light breeze rustling through the vines\n- Ideal for walking the grounds\n- Enhances the outdoor tasting experience",
            "🍂 Crisp Harvest Day:\n- Temperature: 65-72°F (18-22°C)\n- Bright sun, cool and crisp air\n- Perfect for autumn tours\n- Highlights the colors of the foliage\n- Comfortable for a full day of activities",
            "🍷 Moody & Atmospheric:\n- Temperature: 68-75°F (20-24°C)\n- Overcast with a chance of light mist\n- Creates a dramatic, moody landscape\n- Best for indoor tasting portions\n- Unique photography opportunities"
        ],
        "mountain_hike": [
            "⛰️ Ideal Summit Conditions:\n- Temperature: 65-75°F (18-24°C) at base\n- Clear skies, unlimited visibility\n- Light winds, even at higher elevations\n- Trails are dry and firm\n- Pack layers, it's cooler at the top",
            "🌲 Cool Forest Trek:\n- Temperature: 60-70°F (16-21°C)\n- Partly cloudy, shaded by tree cover\n- Comfortable for strenuous climbing\n- Slight chance of a passing shower\n- Trail conditions mostly good",
            "⚠️ Challenging Alpine Weather:\n- Temperature: 55-65°F (13-18°C)\n- Strong winds and fast-moving clouds\n- Visibility may be limited at times\n- High chance of rain, pack waterproof gear\n- For experienced hikers only"
        ],
        "ski_resort": [
            "⛷️ Perfect Bluebird Day:\n- Temperature: 25-32°F (-4-0°C)\n- Fresh powder, deep blue skies\n- No wind, sun feels warm\n- Excellent visibility on all runs\n- Goggles and sunscreen are a must",
            "❄️ Powder Day!:\n- Temperature: 20-28°F (-7 to -2°C)\n- Continuous light-to-moderate snowfall\n- Accumulation of 4-6 inches expected\n- Visibility reduced, ski with caution\n- The fresh snow will be incredible",
            "☀️ Spring Skiing Conditions:\n- Temperature: 35-45°F (2-7°C)\n- Sunny and mild, softens the snow\n- Perfect for slushy, fun runs\n- Wear layers you can shed\n- Party atmosphere on the mountain"
        ],
        "lakeside_event": [
            "🛶 Serene Lake Day:\n- Temperature: 75-82°F (24-28°C)\n- Sunny with calm winds\n- Water will be like glass, perfect for kayaking\n- Ideal for swimming and paddleboarding\n- Warm and pleasant by the shore",
            "⛵ Breezy Sailing Weather:\n- Temperature: 70-77°F (21-25°C)\n- Consistent breeze of 10-15 mph\n- Sunny with some passing clouds\n- Water will have a light chop\n- Excellent for sailing or windsurfing",
            "🌅 Misty Morning on the Water:\n- Temperature: 65-72°F (18-22°C)\n- Cool, with fog lifting off the lake as the sun rises\n- Calm and quiet, very atmospheric\n- Great for fishing or a peaceful coffee by the water\n- Burns off to a pleasant, mild day"
        ],
        "outdoor_concert": [
            "🎤 Flawless Festival Weather:\n- Temperature: 74-81°F (23-27°C)\n- Mostly sunny with a light breeze\n- Dry ground, no mud concerns\n- Comfortable for standing and dancing all day\n- Sound will carry perfectly",
            "🎸 Hot Summer Gig:\n- Temperature: 85-92°F (29-33°C)\n- Bright, strong sunshine\n- High energy, but stay hydrated!\n- Seek shade between sets\n- UV index will be very high",
            "🌧️ Rain or Shine Rock Show:\n- Temperature: 68-75°F (20-24°C)\n- Overcast with a 60% chance of showers\n- Pack a poncho, prepare for mud\n- Cooler temperatures will be comfortable for a crowd\n- Creates a memorable, dramatic experience"
        ],
        "pool_party": [
            "☀️ Ultimate Pool Day:\n- Temperature: 85-95°F (29-35°C)\n- Intense, non-stop sunshine\n- No wind, perfect for tanning\n- Water will be refreshingly cool\n- Sunscreen and hydration are non-negotiable",
            "😎 Comfortable Cabana Weather:\n- Temperature: 80-86°F (27-30°C)\n- Sunny with scattered clouds for breaks of shade\n- Light breeze making it very pleasant\n- Perfect for lounging and swimming\n- Great for a full day by the pool",
            "⛈️ Afternoon Thunderstorm Risk:\n- Temperature: 82-88°F (28-31°C)\n- Hot and humid morning/early afternoon\n- High probability of thunderstorms after 3 PM\n- Listen for thunder and be ready to clear the pool\n- Have an indoor backup plan ready"
        ],
        "stadium_game": [
            "⚾ Perfect Day at the Ballpark:\n- Temperature: 73-80°F (23-27°C)\n- Partly cloudy, no sun glare issues\n- Light, variable winds won't affect play\n- Ideal comfort for players and spectators\n- Classic game day conditions",
            "🏈 Blustery Football Weather:\n- Temperature: 55-65°F (13-18°C)\n- Strong, gusty winds will be a factor\n- Mix of sun and clouds, feels colder than the temp\n- Dress in warm layers\n- Adds an extra challenge to the game",
            "⚽ Rain Delay Likely:\n- Temperature: 70-76°F (21-24°C)\n- Overcast and humid with a 70% chance of rain\n- High likelihood of a game delay\n- Bring rain gear\n- Field conditions could get slippery"
        ]
    },
    
    "weather_alerts": [
        "⚠️ Weather Advisory:\n- Severe thunderstorm watch in effect\n- Heavy rain and strong winds possible\n- Consider postponing outdoor events\n- Monitor weather updates closely\n- Indoor backup venue recommended",
        "🌡️ Heat Advisory:\n- Temperature expected to reach 95-100°F (35-38°C)\n- Heat index may exceed 105°F\n- Reschedule to cooler hours if possible\n- Provide cooling stations and frequent water breaks\n- Watch for heat-related illness signs",
        "💨 Wind Advisory:\n- Sustained winds 25-35 mph expected\n- Gusts up to 50 mph possible\n- Secure all outdoor decorations\n- Consider tent safety and stability\n- May affect sound systems",
        "🌧️ Flood Watch:\n- Heavy rainfall expected (2-4 inches)\n- Possible flash flooding in low areas\n- Check venue drainage systems\n- Have evacuation plan ready\n- Monitor local emergency alerts"
    ],
    
    "general_forecasts": [
        "🌤️ General Weather Outlook:\n- Variable conditions expected\n- Temperature: 68-78°F (20-26°C)\n- Mix of sun and clouds throughout week\n- 30% chance of scattered showers\n- Monitor forecast as event approaches",
        "☀️ Stable Weather Pattern:\n- High pressure system bringing clear skies\n- Temperature: 75-82°F (24-28°C)\n- Sunny conditions for next 5 days\n- Light winds, low humidity\n- Excellent for outdoor planning",
        "🌥️ Changeable Conditions:\n- Weather front moving through area\n- Temperature varying 65-80°F (18-27°C)\n- Alternating sun and clouds\n- Possible brief showers\n- Flexible planning recommended",
        "🌦️ Unsettled Weather:\n- Low pressure system nearby\n- Temperature: 62-72°F (17-22°C)\n- 50% chance of rain throughout period\n- Consider covered venue options\n- Have weather backup plans ready"
    ]
}

@tool
def weather(query: str) -> str:
    """
    Get weather forecasts and climate considerations for event planning.
    
    WHEN TO USE:
    - Outdoor events (parties, weddings, sports, festivals)
    - Events sensitive to weather conditions
    - When planning seasonal activities
    - For events requiring weather-dependent backup plans
    
    CONTEXTS:
    ✅ Use for: Outdoor parties, weddings, sports events, festivals, picnics, garden parties
    ❌ Skip for: Indoor events, virtual meetings, events in climate-controlled venues
    
    This tool provides weather forecasts and helps plan weather-contingent activities.
    """
    global event_planning_data
    
    query_lower = query.lower()
    
    with open('specific_dates.json', 'r') as file:
        data = json.load(file)
    
    WEATHER_DATA["specific_dates"] = data["specific_dates"]
    
    with open('outdoor.json', 'r') as file:
        data = json.load(file)

    WEATHER_DATA["outdoor_events"] = data["outdoor_events"]
    
    # Check for specific dates
    if "june 30" in query_lower or "30th june" in query_lower:
        result = random.choice(WEATHER_DATA["specific_dates"]["june_30"])
    elif "july 4" in query_lower or "4th july" in query_lower or "independence day" in query_lower:
        result = random.choice(WEATHER_DATA["specific_dates"]["july_4"])
    elif "december 25" in query_lower or "christmas" in query_lower:
        result = random.choice(WEATHER_DATA["specific_dates"]["december_25"])
    
    # Check for venue-specific requests
    elif "garden" in query_lower and ("party" in query_lower or "wedding" in query_lower):
        result = random.choice(WEATHER_DATA["venue_specific"]["garden_party"])
    elif "beach" in query_lower:
        result = random.choice(WEATHER_DATA["venue_specific"]["beach_event"])
    elif "park" in query_lower or "picnic" in query_lower:
        result = random.choice(WEATHER_DATA["venue_specific"]["park_picnic"])
    
    # Check for seasonal requests
    elif any(keyword in query_lower for keyword in ["spring", "march", "april", "may"]):
        result = random.choice(WEATHER_DATA["seasonal_weather"]["spring"])
    elif any(keyword in query_lower for keyword in ["summer", "june", "july", "august"]):
        result = random.choice(WEATHER_DATA["seasonal_weather"]["summer"])
    elif any(keyword in query_lower for keyword in ["fall", "autumn", "september", "october", "november"]):
        result = random.choice(WEATHER_DATA["seasonal_weather"]["fall"])
    elif any(keyword in query_lower for keyword in ["winter", "december", "january", "february"]):
        result = random.choice(WEATHER_DATA["seasonal_weather"]["winter"])
    
    # Check for outdoor event keywords
    elif any(keyword in query_lower for keyword in ["outdoor", "festival", "concert", "fair"]):
        # 10% chance of weather alert for outdoor events
        if random.random() < 0.1:
            result = random.choice(WEATHER_DATA["weather_alerts"])
        else:
            result = random.choice(WEATHER_DATA["outdoor_events"])
    
    # Default to general forecast
    else:
        result = random.choice(WEATHER_DATA["general_forecasts"])
    
    # Store the result
    event_planning_data["weather_info"] = result
    return result

@tool
def traffic(query: str) -> str:
    """
    Analyze transportation, parking, and accessibility for event venues.
    
    WHEN TO USE:
    - Events at specific venues (not virtual)
    - When guests need to travel to location
    - For events during peak traffic times
    - When parking or transportation is a concern
    
    CONTEXTS:
    ✅ Use for: Venue-based events, large gatherings, events in busy areas, out-of-town events
    ❌ Skip for: Virtual events, home-based small gatherings, walking-distance events
    
    This tool helps optimize guest arrival and provides transportation guidance.
    """
    global event_planning_data
    
    if "home" in query.lower():
        result = "🚗 Traffic & Transportation Analysis for Home Events:\n- Residential area with good access\n- Moderate traffic expected on weekend\n- Recommend guests arrive 15-20 minutes early\n- Street parking available\n- Consider carpooling for larger groups\n- Provide clear directions and landmarks"
    elif any(keyword in query.lower() for keyword in ["downtown", "city", "urban"]):
        result = "🚗 Urban Venue Transportation:\n- Peak traffic congestion expected\n- Public transportation recommended\n- Parking may be limited and expensive\n- Consider ride-sharing options\n- Provide multiple arrival options\n- Allow extra travel time"
    elif any(keyword in query.lower() for keyword in ["venue", "hall", "hotel"]):
        result = "🚗 Event Venue Transportation:\n- Venue parking policies and costs\n- Valet service availability\n- Accessibility for elderly/disabled guests\n- Distance from major transportation hubs\n- Coordinate group transportation if needed"
    else:
        result = f"🚗 Traffic analysis for: {query}. Check venue accessibility and parking options. Provide clear directions and transportation alternatives to guests."
    
    event_planning_data["traffic_info"] = result
    return result

@tool
def invite_people(query: str) -> str:
    """
    Generate invitation content and manage guest lists based on event type and formality.
    
    WHEN TO USE:
    - ALL events requiring attendee coordination
    - When user wants to invite specific people or groups
    - For events needing RSVP management
    - When creating guest communications
    
    CONTEXTS:
    ✅ Use for: ANY event with attendees (parties, meetings, weddings, conferences, gatherings)
    ❌ Skip for: Personal reminders, solo activities, events with pre-confirmed attendees
    
    This tool creates appropriate invitations and manages guest list considerations.
    """
    global event_planning_data
    
    # Determine event formality and type
    is_informal = any(word in query.lower() for word in ["birthday", "party", "home", "casual", "family", "friends"])
    is_business = any(word in query.lower() for word in ["meeting", "conference", "professional", "corporate", "business"])
    is_formal = any(word in query.lower() for word in ["wedding", "gala", "formal", "ceremony"])
    
    if is_informal:
        result = """📧 Invitation Generated - INFORMAL EVENT:
        
🎉 You're Invited to a Birthday Celebration! 🎉

Join us for a wonderful birthday party!
📅 Date: June 30th
🕐 Time: 2:00 PM - 6:00 PM  
🏠 Venue: At our home
🌤️ Weather: Perfect outdoor weather expected!

What to expect:
- Delicious food and birthday cake
- Fun games and activities
- Great company with family and friends
- Please let us know about any dietary restrictions

🚗 Parking: Street parking available
⏰ Arrival: Please arrive 15-20 minutes early

RSVP by June 25th!

Target Audience: Family and close friends (15-20 people)
Invitation Style: Warm and casual tone"""
    
    elif is_business:
        result = """📧 Invitation Generated - BUSINESS EVENT:
        
Subject: Meeting Invitation - [Event Topic]

Dear [Name],

You are invited to attend our upcoming business meeting.

📅 Date: [Date]
🕐 Time: [Time]
🏢 Location: [Venue/Virtual Link]
📋 Agenda: [Key Discussion Points]

Please confirm your attendance by [RSVP Date].

Meeting materials will be provided in advance.

Best regards,
[Your Name]

Target Audience: Professional colleagues and stakeholders
Invitation Style: Professional and concise"""
    
    elif is_formal:
        result = """📧 Invitation Generated - FORMAL EVENT:
        
You are cordially invited to attend

[EVENT NAME]

Date: [Event Date]
Time: [Event Time]  
Venue: [Event Location]

Dress Code: Formal attire required
RSVP: By [Date] to [Contact Information]

We look forward to celebrating with you.

With warm regards,
[Host Names]

Target Audience: Extended family, friends, and honored guests
Invitation Style: Elegant and traditional"""
    
    else:
        result = """📧 Invitation Generated - GENERAL EVENT:
        
You're Invited!

Event: [Event Name]
Date: [Date]
Time: [Time]
Location: [Venue]

[Event Description]

Please RSVP by [Date]

Target Audience: Relevant stakeholders based on event type
Invitation Style: Adaptable to event context"""
    
    event_planning_data["invitation_info"] = result
    return result

# ============================================================================
# ENHANCED COMMUNICATION AGENT TOOLS (2 tools)
# ============================================================================

@tool
def whatsapp_message(message: str, contacts: str = "auto_detect") -> str:
    """
    Send WhatsApp messages to specified contact groups.
    
    WHEN TO USE:
    - Informal events (birthdays, casual parties, family gatherings)
    - Quick updates or reminders
    - When targeting younger demographics or close personal contacts
    - For immediate, casual communication needs
    
    CONTEXTS:
    ✅ Use for: Birthday parties, casual gatherings, family events, friend meetups, informal updates
    ❌ Skip for: Formal business events, professional meetings, events requiring documentation
    
    This tool sends casual, immediate invitations via WhatsApp to personal contacts.
    """
    global event_planning_data
    
    # Auto-detect contact type based on message content
    if contacts == "auto_detect":
        if any(word in message.lower() for word in ["birthday", "party", "family", "friends"]):
            contacts = "family_and_friends"
        elif any(word in message.lower() for word in ["meeting", "business", "professional"]):
            contacts = "colleagues"
        else:
            contacts = "general_contacts"
    
    result = f"""📱 WhatsApp Message Sent Successfully!
    
To: {contacts}
Message Preview: {message[:100]}...
Status: ✅ Delivered to all contacts
Delivery Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Platform: WhatsApp
Recipients: {'Personal group chat' if 'family' in contacts else 'Professional contacts' if 'colleagues' in contacts else 'General contacts'}
Message Type: Instant casual communication"""
    
    event_planning_data["whatsapp_status"] = result
    return result

@tool
def email_message(message: str, contacts: str = "auto_detect") -> str:
    """
    Send formal email invitations to specified email contact lists.
    
    WHEN TO USE:
    - Formal events (business meetings, conferences, weddings, formal parties)
    - When detailed information needs to be communicated
    - For events requiring documentation and paper trail
    - When targeting professional or mixed demographics
    
    CONTEXTS:
    ✅ Use for: Business meetings, conferences, formal celebrations, weddings, professional events
    ❌ Skip for: Very casual gatherings, last-minute informal updates, close family-only events
    
    This tool sends professional, detailed email invitations with full event information.
    """
    global event_planning_data
    
    # Auto-detect contact type and formality based on message content
    if contacts == "auto_detect":
        if any(word in message.lower() for word in ["meeting", "conference", "business", "professional"]):
            contacts = "professional_contacts"
        elif any(word in message.lower() for word in ["wedding", "formal", "ceremony"]):
            contacts = "extended_family_and_friends"
        else:
            contacts = "general_email_list"
    
    # Determine subject line based on content
    if "birthday" in message.lower():
        subject = "Birthday Party Invitation"
    elif "meeting" in message.lower():
        subject = "Meeting Invitation"
    elif "wedding" in message.lower():
        subject = "Wedding Invitation"
    else:
        subject = "Event Invitation"
    
    result = f"""📧 Email Invitations Sent Successfully!
    
To: {contacts}
Subject: {subject}
Message: {message[:100]}...
Status: ✅ Sent to all recipients
Send Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Platform: Email
Recipients: {'Professional email list' if 'professional' in contacts else 'Extended social network' if 'extended' in contacts else 'General email contacts'}
Message Type: Formal written invitation with full details"""
    
    event_planning_data["email_status"] = result
    return result

# ============================================================================
# TOOLS SETUP
# ============================================================================

# Scheduler tools
scheduler_tools = [calendar, finance, health, weather, traffic, invite_people]
scheduler_tool_node = ToolNode(scheduler_tools)

# Communication tools  
communication_tools = [whatsapp_message, email_message]
communication_tool_node = ToolNode(communication_tools)

# All tools combined
all_tools = scheduler_tools + communication_tools
all_tool_node = ToolNode(all_tools)

# ============================================================================
# MODELS WITH TOOLS
# ============================================================================

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0.1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# model = ChatOllama(
#     base_url=OLLAMA_BASE_URL,
#     model=OLLAMA_MODEL,
#     temperature=0.1
# )

# Bind tools to models
scheduler_model = model.bind_tools(scheduler_tools)
communication_model = model.bind_tools(communication_tools)
orchestrator_model = model.bind_tools([])  # Orchestrator doesn't use tools directly

# ============================================================================
# ENHANCED AGENT FUNCTIONS
# ============================================================================

def orchestrator_agent(state: AgentState) -> AgentState:
    """Main orchestrator agent that routes requests to appropriate agents."""
    global event_planning_data
    
    messages = state["messages"]
    
    # Get the latest user message
    user_message = None
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            user_message = msg.content
            event_planning_data["user_request"] = user_message
            break
    
    system_prompt = SystemMessage(content="""You are the Orchestrator Agent for an intelligent event planning system.

Your responsibilities:
1. Analyze user requests to understand event type, complexity, and requirements
2. Route requests to the appropriate agent (scheduler or communication)
3. Provide brief analysis of what the user needs

ROUTING DECISION CRITERIA:
- Route to SCHEDULER for: Event planning, organizing, coordinating (birthdays, meetings, conferences, parties, etc.)
- Route to COMMUNICATION for: Sending messages, invitations, or updates when event details are already known

The Scheduler Agent has 6 specialized tools and will intelligently select which ones to use based on the event context.
The Communication Agent will choose the appropriate channel (WhatsApp for casual, Email for formal) based on event type.

Provide a brief analysis of the request and specify the next agent.""")
    
    # Determine if this is an event planning request
    if user_message and any(keyword in user_message.lower() for keyword in ["plan", "organize", "schedule", "coordinate", "birthday", "party", "event", "meeting", "celebration", "gathering", "conference", "wedding"]):
        next_agent = "scheduler"
        response_content = f"""🎯 ORCHESTRATOR ANALYSIS:

Request: "{user_message}"

This is an EVENT PLANNING request. Routing to Scheduler Agent.

The Scheduler Agent will intelligently select from these available tools based on your specific needs:
• Calendar - For date/time coordination
• Finance - For budget planning and cost analysis  
• Health - For safety and dietary considerations
• Weather - For outdoor events and weather planning
• Traffic - For venue accessibility and transportation
• Invite People - For creating appropriate invitations

After planning, the Communication Agent will send invitations through the most suitable channel."""
    else:
        next_agent = "communication"
        response_content = f"""🎯 ORCHESTRATOR ANALYSIS:

Request: "{user_message}"

This appears to be a COMMUNICATION request. Routing to Communication Agent.

The Communication Agent will select the appropriate channel:
• WhatsApp - For casual, immediate communication
• Email - For formal, detailed invitations"""
    
    response = AIMessage(content=response_content)
    
    return {
        "messages": [response],
        "current_agent": next_agent,
        "next_action": next_agent
    }

def scheduler_agent(state: AgentState) -> AgentState:
    """Enhanced scheduler agent that intelligently selects appropriate tools based on context."""
    global event_planning_data
    
    messages = state["messages"]
    user_request = event_planning_data.get("user_request", "")
    
    system_prompt = SystemMessage(content=f"""You are the Scheduler Agent responsible for intelligent event planning.

For the user request: "{user_request}"

You have 6 specialized tools available. READ EACH TOOL'S DOCSTRING CAREFULLY to understand when to use it:

1. **calendar** - Use for ANY event needing date/time coordination
2. **finance** - Use for events with significant costs (parties, conferences, large gatherings)
3. **health** - Use for events involving food, large groups, or safety considerations
4. **weather** - Use ONLY for outdoor events or weather-sensitive activities
5. **traffic** - Use for venue-based events where transportation matters
6. **invite_people** - Use for ANY event requiring attendee coordination

INTELLIGENT SELECTION GUIDELINES:
- For a simple home birthday party: Use calendar, finance, health, invite_people
- For outdoor events: Add weather tool
- For venue-based events: Add traffic tool
- For small informal gatherings: May skip finance if budget isn't a concern
- For virtual meetings: Use calendar, invite_people (skip weather, traffic)

Select and use ONLY the tools that are relevant to this specific event context. 
Don't use tools unnecessarily - be smart about what this event actually needs.

After using the appropriate tools, provide a comprehensive summary and indicate readiness for communication.""")
    
    # Check if we've already processed this request
    if event_planning_data.get("current_step") == "scheduling_complete":
        response = AIMessage(content="Scheduling already completed. Ready for communication agent.")
        return {
            "messages": [response],
            "current_agent": "communication", 
            "next_action": "communication"
        }
    
    # Process the request with the model
    all_messages = [system_prompt] + list(messages)
    if user_request:
        all_messages.append(HumanMessage(content=f"Please intelligently plan this event using only the relevant tools: {user_request}"))
    
    response = scheduler_model.invoke(all_messages)
    
    # Mark scheduling as complete
    event_planning_data["current_step"] = "scheduling_complete"
    
    return {
        "messages": [response],
        "current_agent": "scheduler",
        "next_action": "tools" if response.tool_calls else "communication"
    }

def communication_agent(state: AgentState) -> AgentState:
    """Enhanced communication agent that intelligently selects communication channels."""
    global event_planning_data
    
    messages = state["messages"]
    user_request = event_planning_data.get("user_request", "")
    invitation_content = event_planning_data.get("invitation_info", "")
    
    system_prompt = SystemMessage(content=f"""You are the Communication Agent responsible for intelligent invitation distribution.

Original request: "{user_request}"
Available invitation content: {invitation_content}

You have 2 communication tools available. READ EACH TOOL'S DOCSTRING to understand when to use each:

1. **whatsapp_message** - For informal, casual events (birthdays, family gatherings, friend meetups)
2. **email_message** - For formal events (business meetings, conferences, weddings, professional events)

INTELLIGENT SELECTION GUIDELINES:
- Casual events (birthday parties, family gatherings): Use WhatsApp primarily, optionally Email for broader reach
- Formal events (business meetings, conferences): Use Email primarily
- Mixed events (wedding, large celebrations): Use both WhatsApp and Email for different groups
- Virtual meetings: Use Email for professional context
- Last-minute informal updates: Use WhatsApp only

Select the appropriate communication channel(s) based on the event type and formality level.
You don't need to use both tools for every event - choose what makes sense for this specific context.

After sending appropriate invitations, provide a summary of the communication strategy used.""")
    
    # Check if communication is already complete
    if event_planning_data.get("whatsapp_status") and event_planning_data.get("email_status"):
        summary = f"""📱 COMMUNICATION COMPLETED!

WhatsApp: {event_planning_data['whatsapp_status'][:100]}...
Email: {event_planning_data['email_status'][:100]}...

Multi-channel communication strategy executed successfully! 🎉"""
        
        response = AIMessage(content=summary)
        return {
            "messages": [response],
            "current_agent": "communication",
            "next_action": "end"
        }
    
    # Process with the model
    all_messages = [system_prompt] + list(messages)
    response = communication_model.invoke(all_messages)
    
    return {
        "messages": [response],
        "current_agent": "communication", 
        "next_action": "tools" if response.tool_calls else "end"
    }

# ============================================================================
# CONDITIONAL ROUTING FUNCTIONS (Same as before)
# ============================================================================

def route_after_orchestrator(state: AgentState) -> str:
    """Route from orchestrator to the appropriate agent."""
    next_action = state.get("next_action", "scheduler")
    return next_action

def route_after_scheduler(state: AgentState) -> str:
    """Route from scheduler agent."""
    messages = state["messages"]
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls:
        return "scheduler_tools"
    return "communication"

def route_after_communication(state: AgentState) -> str:
    """Route from communication agent."""
    messages = state["messages"]
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls:
        return "communication_tools"
    return "end"

def route_after_scheduler_tools(state: AgentState) -> str:
    """Route after scheduler tools execution."""
    # Check if we have sufficient planning information
    tools_used = []
    for msg in state["messages"]:
        if isinstance(msg, ToolMessage):
            tools_used.append(msg.name if hasattr(msg, 'name') else 'unknown')
    
    # If we have at least some planning done, move to communication
    if len(tools_used) >= 2:
        return "communication"
    else:
        return "scheduler"

def route_after_communication_tools(state: AgentState) -> str:
    """Route after communication tools execution."""
    return "end"

# ============================================================================
# GRAPH CONSTRUCTION (Same as before)
# ============================================================================

def create_event_planning_graph():
    """Create the multi-agent event planning graph."""
    
    # Create the graph
    graph = StateGraph(AgentState)
    
    # Add agent nodes
    graph.add_node("orchestrator", orchestrator_agent)
    graph.add_node("scheduler", scheduler_agent)
    graph.add_node("communication", communication_agent)
    
    # Add tool nodes
    graph.add_node("scheduler_tools", scheduler_tool_node)
    graph.add_node("communication_tools", communication_tool_node)
    
    # Set entry point
    graph.set_entry_point("orchestrator")
    
    # Add conditional edges
    graph.add_conditional_edges(
        "orchestrator",
        route_after_orchestrator,
        {
            "scheduler": "scheduler",
            "communication": "communication"
        }
    )
    
    graph.add_conditional_edges(
        "scheduler", 
        route_after_scheduler,
        {
            "scheduler_tools": "scheduler_tools",
            "communication": "communication"
        }
    )
    
    graph.add_conditional_edges(
        "scheduler_tools",
        route_after_scheduler_tools,
        {
            "scheduler": "scheduler", 
            "communication": "communication"
        }
    )
    
    graph.add_conditional_edges(
        "communication",
        route_after_communication, 
        {
            "communication_tools": "communication_tools",
            "end": END
        }
    )
    
    graph.add_conditional_edges(
        "communication_tools",
        route_after_communication_tools,
        {
            "end": END
        }
    )
    
    return graph.compile()


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_messages(messages):
    """Print messages in a readable format."""
    if not messages:
        return
    
    for message in messages[-3:]:
        if isinstance(message, AIMessage):
            print(f"\n🤖 AI: {message.content}")
        elif isinstance(message, ToolMessage):
            print(f"\n🛠️ TOOL RESULT: {message.content}")
        elif isinstance(message, HumanMessage):
            print(f"\n👤 USER: {message.content}")

def reset_planning_data():
    """Reset the global planning data for a new session."""
    global event_planning_data
    event_planning_data = {
        "user_request": "",
        "calendar_info": "",
        "finance_info": "",
        "health_info": "",
        "weather_info": "",
        "traffic_info": "",
        "invitation_info": "",
        "whatsapp_status": "",
        "email_status": "",
        "current_step": "start"
    }

# ============================================================================
# MAIN EXECUTION FUNCTION
# ============================================================================

def run_event_planning_system():
    """Main function to run the multi-agent event planning system."""
    
    print("\n" + "="*80)
    print("🎉 MULTI-AGENT EVENT PLANNING SYSTEM (Powered by Gemini 2.0 Flash) 🎉")
    print("="*80)
    print("Welcome! I can help you plan events with my team of AI agents:")
    print("🎯 Orchestrator: Routes and coordinates requests")
    print("📅 Scheduler: Handles comprehensive event planning")
    print("📱 Communication: Sends invitations via WhatsApp & Email")
    print("="*80)
    
    # Create the graph
    app = create_event_planning_graph()
    
    while True:
        try:
            # Reset data for new planning session
            reset_planning_data()
            
            # Get user input
            user_input = input("\n👤 Describe the event you'd like to plan (or 'quit' to exit): ")
            print()
            
            if user_input.lower() in ['quit', 'exit', 'done', 'finish']:
                print("👋 Thank you for using the Multi-Agent Event Planning System!")
                break
            
            # Initial state
            initial_state = {
                "messages": [HumanMessage(content=user_input)],
                "current_agent": "orchestrator",
                "next_action": "scheduler"
            }
            
            print(f"🚀 Processing request: '{user_input}'")
            print("-" * 60)
            
            # Run the graph
            final_state = None
            for step in app.stream(initial_state, stream_mode="values"):
                final_state = step
                if "messages" in step:
                    print_messages(step["messages"])
                    
                # Show current agent
                current_agent = step.get("current_agent", "unknown")
                print(f"\n📍 Current Agent: {current_agent.upper()}")
                print("-" * 40)
            
            # Show final summary
            print("\n" + "="*60)
            print("📋 EVENT PLANNING SUMMARY")
            print("="*60)
            
            if event_planning_data["calendar_info"]:
                print(f"📅 Calendar: {event_planning_data['calendar_info'][:100]}...")
            if event_planning_data["finance_info"]:
                print(f"💰 Finance: {event_planning_data['finance_info'][:100]}...")
            if event_planning_data["weather_info"]:
                print(f"🌤️ Weather: {event_planning_data['weather_info'][:100]}...")
            if event_planning_data["whatsapp_status"]:
                print(f"📱 WhatsApp: Sent successfully!")
            if event_planning_data["email_status"]:
                print(f"📧 Email: Sent successfully!")
                
            print("\n✅ Event planning completed successfully!")
            print("="*60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Let's try again...")

# ============================================================================
# TESTING FUNCTIONS
# ============================================================================

def test_individual_tools():
    """Test individual tools to ensure they work correctly."""
    print("\n🧪 TESTING INDIVIDUAL TOOLS")
    print("="*50)
    
    test_query = "Plan my son's birthday on June 30th at home"
    
    # Test scheduler tools
    print("\n📅 Testing Scheduler Tools:")
    print("-" * 30)
    print("1. Calendar:", calendar(test_query))
    print("\n2. Finance:", finance(test_query))
    print("\n3. Health:", health(test_query))
    print("\n4. Weather:", weather(test_query))
    print("\n5. Traffic:", traffic(test_query))
    print("\n6. Invite People:", invite_people(test_query))
    
    # Test communication tools
    print("\n📱 Testing Communication Tools:")
    print("-" * 30)
    invitation = event_planning_data.get("invitation_info", "Test invitation")
    print("7. WhatsApp:", whatsapp_message(invitation, "family_and_friends"))
    print("\n8. Email:", email_message(invitation, "family_and_friends"))

if __name__ == "__main__":
    # Uncomment to test individual tools
    # test_individual_tools()
    
    # Run the main system
    run_event_planning_system()