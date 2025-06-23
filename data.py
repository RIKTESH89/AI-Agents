# data.py

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

# Weather data for the weather tool
WEATHER_DATA = {
    "specific_dates": {
        "january_1": [
            "🎉 New Year's Day Forecast:\n- Temperature: 25-35°F (-4 to 2°C)\n- Conditions: Clear but cold\n- Precipitation Chance: 10%\n- A crisp, clear start to the new year!",
            "🥶 Chilly January 1st:\n- High: 34°F (1°C), Low: 24°F (-4°C)\n- Sky: Mostly sunny and bright\n- Note: Bundle up if you're heading out for a New Year's walk.",
            "❄️ January 1st Weather:\n- Temperature: 28-38°F (-2 to 3°C)\n- Mostly cloudy with a slight breeze\n- Chance of flurries: 20%\n- Perfect for staying indoors and relaxing."
        ],
        "january_2": [
            "❄️ January 2nd Weather:\n- Temperature: 26-36°F (-3 to 2°C)\n- Cloudy with a chance of light snow\n- Precipitation Chance: 30%\n- Roads could be slick.",
            "🧣 Brisk January 2nd:\n- Temperature: 24-33°F (-4 to 1°C)\n- Conditions: Windy and cold\n- Wind: 15-20 mph\n- A good day for a hot cup of cocoa."
        ],
        "january_3": [
            "☀️ Cold Sun on January 3rd:\n- Temperature: 22-32°F (-6 to 0°C)\n- Sunny but frigid\n- No precipitation expected\n- Remember to protect skin from the cold.",
            "🥶 January 3rd Forecast:\n- Temperature: 25-35°F (-4 to 2°C)\n- Clear skies, cold temperatures\n- Humidity: 40%\n- Dress in warm layers."
        ],
        "january_4": [
            "🌨️ January 4th Snow Watch:\n- Temperature: 28-34°F (-2 to 1°C)\n- Overcast with steady snow developing\n- Precipitation Chance: 60%\n- Accumulation of 1-2 inches possible.",
            "🧤 Winter Weather for January 4th:\n- Temperature: 27-33°F (-3 to 1°C)\n- Light snow throughout the day\n- Perfect for building a snowman!\n- Allow extra time for travel."
        ],
        "january_5": [
            "🌬️ Windy January 5th:\n- Temperature: 30-40°F (-1 to 4°C)\n- Partly cloudy and windy\n- Wind Gusts: up to 25 mph\n- Secure any loose outdoor items.",
            "🥶 January 5th Update:\n- Temperature: 32-39°F (0 to 4°C)\n- A mix of sun and clouds, but feeling cold due to wind.\n- Precipitation Chance: 10%"
        ],
        "january_6": [
            "☁️ Cloudy January 6th:\n- Temperature: 33-41°F (1 to 5°C)\n- Grey and overcast all day\n- Precipitation Chance: 20% (drizzle)\n- A quiet day indoors is a good plan.",
            "🧤 January 6th Forecast:\n- Temperature: 34-42°F (1 to 6°C)\n- Conditions: Overcast and damp\n- A good day to visit a museum or library."
        ],
        "january_7": [
            "❄️ January 7th Flurries:\n- Temperature: 29-36°F (-2 to 2°C)\n- Cloudy with occasional snow flurries\n- Precipitation Chance: 40%\n- No significant accumulation expected.",
            "🧣 January 7th Weather:\n- Temperature: 30-37°F (-1 to 3°C)\n- Brisk and cloudy\n- A perfect evening for a warm fireplace."
        ],
        "january_8": [
            "☀️ Sunny & Cold January 8th:\n- Temperature: 25-35°F (-4 to 2°C)\n- Bright sun but a sharp chill in the air\n- No precipitation\n- Enjoy the winter sun!",
            "🥶 January 8th Forecast:\n- Temperature: 26-36°F (-3 to 2°C)\n- Clear skies, ideal for a winter hike if you bundle up."
        ],
        "january_9": [
            "🌨️ January 9th Snowfall:\n- Temperature: 28-33°F (-2 to 1°C)\n- Light to moderate snow\n- Precipitation Chance: 70%\n- Travel may be impacted.",
            "❄️ Winter Wonderland on January 9th:\n- Temperature: 27-32°F (-3 to 0°C)\n- Consistent snowfall expected\n- Potential for 2-4 inches of accumulation."
        ],
        "january_10": [
            "🌬️ Blustery January 10th:\n- Temperature: 26-34°F (-3 to 1°C)\n- Lingering flurries and strong winds\n- Wind chill making it feel like 15°F (-9°C)\n- Stay warm and safe!",
            "🥶 Post-Snow Chill on January 10th:\n- Temperature: 25-33°F (-4 to 1°C)\n- Partly sunny but very cold\n- Watch for icy spots on roads and sidewalks."
        ],
        "january_11": [
            "☁️ Overcast January 11th:\n- Temperature: 32-40°F (0 to 4°C)\n- A grey, cloudy day\n- Precipitation Chance: 15%\n- A slight warm-up from previous days.",
            "🧤 January 11th Weather:\n- Temperature: 33-41°F (1 to 5°C)\n- No sun, but no snow either.\n- A calm winter day."
        ],
        "january_12": [
            "❄️ Icy Mix for January 12th:\n- Temperature: 30-35°F (-1 to 2°C)\n- Chance of freezing rain or sleet\n- Precipitation Chance: 50%\n- Exercise caution when traveling.",
            "🧊 January 12th Forecast:\n- Temperature: 31-36°F (0 to 2°C)\n- Cloudy with potential for icy precipitation\n- Best to stay off the roads if possible."
        ],
        "january_13": [
            "☀️ Crisp January 13th:\n- Temperature: 28-38°F (-2 to 3°C)\n- Sunny and clear after morning chill\n- A beautiful, bright winter day.",
            "🥶 January 13th Sunshine:\n- Temperature: 29-39°F (-2 to 4°C)\n- Don't let the sun fool you, it's still cold!\n- No precipitation expected."
        ],
        "january_14": [
            "🌨️ Light Dusting on January 14th:\n- Temperature: 29-34°F (-2 to 1°C)\n- Overcast with light snow showers\n- Precipitation Chance: 40%\n- Just enough to make things pretty.",
            "❄️ January 14th Forecast:\n- Temperature: 28-35°F (-2 to 2°C)\n- Occasional flurries\n- Roads should remain in decent condition."
        ],
        "january_15": [
            "🥶 Frigid January 15th:\n- Temperature: 18-28°F (-8 to -2°C)\n- Very cold, even with some sun\n- Wind chill advisory possible\n- Limit time outdoors.",
            "🌬️ Arctic Blast on January 15th:\n- Temperature: 20-30°F (-7 to -1°C)\n- Windy and bitterly cold\n- A good day for indoor projects."
        ],
        "january_16": [
            "☀️ January 16th Cold Snap:\n- Temperature: 20-32°F (-7 to 0°C)\n- Sunny but temperatures remain well below average\n- Dry conditions.",
            "🥶 January 16th Update:\n- Temperature: 22-33°F (-6 to 1°C)\n- Clear skies, but the cold persists\n- Remember to check on elderly neighbors."
        ],
        "january_17": [
            "☁️ Grey Skies on January 17th:\n- Temperature: 28-37°F (-2 to 3°C)\n- A solid cloud cover all day\n- Precipitation Chance: 10%\n- Temperatures slowly moderating.",
            "🧤 January 17th Weather:\n- Temperature: 30-38°F (-1 to 3°C)\n- Overcast and calm\n- Not too harsh for a winter day."
        ],
        "january_18": [
            "❄️ January 18th Snow Showers:\n- Temperature: 30-36°F (-1 to 2°C)\n- On-and-off snow showers\n- Precipitation Chance: 50%\n- Little to no accumulation.",
            "🌨️ January 18th Forecast:\n- Temperature: 31-37°F (0 to 3°C)\n- Intermittent light snow\n- A classic mid-winter day."
        ],
        "january_19": [
            "🌬️ Windy and Raw on January 19th:\n- Temperature: 33-40°F (1 to 4°C)\n- Gusty winds and a mix of sun and clouds\n- Feels colder than the thermometer reads.",
            "🧣 January 19th Weather:\n- Temperature: 34-42°F (1 to 6°C)\n- Blustery conditions\n- Hold onto your hat!"
        ],
        "january_20": [
            "☀️ January 20th Sunshine:\n- Temperature: 35-45°F (2 to 7°C)\n- A pleasant, sunny winter day\n- A nice break from the grey weather.",
            "😊 Mild January 20th:\n- Temperature: 36-46°F (2 to 8°C)\n- Sunny with a light breeze\n- A great day to get some fresh air."
        ],
        "january_21": [
            "☁️ Clouds Return on January 21st:\n- Temperature: 34-43°F (1 to 6°C)\n- Overcast skies are back\n- Precipitation Chance: 20%\n- Milder temperatures remain.",
            "🧤 January 21st Forecast:\n- Temperature: 35-44°F (2 to 7°C)\n- Grey and calm\n- A standard late-January day."
        ],
        "january_22": [
            "🌨️ January 22nd Snow Event:\n- Temperature: 28-34°F (-2 to 1°C)\n- Snow developing in the afternoon\n- Precipitation Chance: 80%\n- Significant accumulation is possible.",
            "❄️ Winter Storm Warning for January 22nd:\n- Temperature: 27-33°F (-3 to 1°C)\n- Heavy snow expected, 3-6 inches\n- Avoid travel if possible."
        ],
        "january_23": [
            "🌬️ Wintry Mix on January 23rd:\n- Temperature: 32-38°F (0 to 3°C)\n- Snow changing to sleet or freezing rain\n- Precipitation Chance: 60%\n- Treacherous travel conditions.",
            "🧊 Icy January 23rd:\n- Temperature: 33-39°F (1 to 4°C)\n- Periods of freezing rain\n- Be extremely careful on foot and in the car."
        ],
        "january_24": [
            "🥶 Deep Freeze for January 24th:\n- Temperature: 15-25°F (-9 to -4°C)\n- Arctic air returns behind the storm\n- Sunny but bitterly cold.",
            "☀️ Frigid Sun on January 24th:\n- Temperature: 17-27°F (-8 to -3°C)\n- Clear skies, but dangerous wind chills\n- Stay indoors if you can."
        ],
        "january_25": [
            "☁️ January 25th Cold:\n- Temperature: 20-30°F (-7 to -1°C)\n- Mostly cloudy and very cold\n- A slight breeze adds to the chill.",
            "🧣 January 25th Weather:\n- Temperature: 22-32°F (-6 to 0°C)\n- Overcast and frigid\n- Another day to bundle up."
        ],
        "january_26": [
            "❄️ Light Flurries for January 26th:\n- Temperature: 26-34°F (-3 to 1°C)\n- A few snow flurries possible\n- Precipitation Chance: 30%\n- No major impact expected.",
            "🧤 January 26th Forecast:\n- Temperature: 28-36°F (-2 to 2°C)\n- Cloudy with a chance of snow showers\n- A typical end-of-January day."
        ],
        "january_27": [
            "☀️ January 27th Sunshine:\n- Temperature: 30-40°F (-1 to 4°C)\n- Sunny with milder temperatures\n- A pleasant winter afternoon.",
            "😊 Nice Day for January 27th:\n- Temperature: 32-42°F (0 to 6°C)\n- Abundant sunshine and light winds\n- Enjoy the break in the weather!"
        ],
        "january_28": [
            "☁️ January 28th Clouds:\n- Temperature: 33-41°F (1 to 5°C)\n- Increasing cloudiness throughout the day\n- Precipitation Chance: 25%\n- Next system approaching.",
            "🧤 January 28th Weather:\n- Temperature: 34-43°F (1 to 6°C)\n- Overcast and calm before the next storm."
        ],
        "january_29": [
            "🌨️ January 29th Snow:\n- Temperature: 29-35°F (-2 to 2°C)\n- Overcast with periods of snow\n- Precipitation Chance: 60%\n- Another 1-3 inches possible.",
            "❄️ January 29th Forecast:\n- Temperature: 30-36°F (-1 to 2°C)\n- A snowy, wintry day\n- Perfect for a movie marathon."
        ],
        "january_30": [
            "🌬️ Blustery End to January 30th:\n- Temperature: 28-36°F (-2 to 2°C)\n- Windy with leftover snow showers\n- Cold wind chills persist.",
            "🥶 January 30th Chill:\n- Temperature: 27-35°F (-3 to 2°C)\n- Partly cloudy, windy, and cold\n- Winter isn't over yet!"
        ],
        "january_31": [
            "☀️ Sunny Finale for January 31st:\n- Temperature: 30-40°F (-1 to 4°C)\n- A bright and sunny end to the month\n- Still chilly, but the sun helps.",
            "😊 January 31st Weather:\n- Temperature: 32-41°F (0 to 5°C)\n- Clear skies and manageable temperatures\n- A hopeful look towards February."
        ],
        "february_1": [
            "❄️ Welcome to February 1st:\n- Temperature: 30-38°F (-1 to 3°C)\n- Cloudy with a chance of morning flurries\n- Precipitation Chance: 30%\n- Winter's grip holds strong.",
            "🧣 February 1st Forecast:\n- Temperature: 28-37°F (-2 to 3°C)\n- Overcast and brisk\n- A typical start to the month."
        ],
        "february_2": [
            "☀️ Sunny February 2nd:\n- Temperature: 32-42°F (0 to 6°C)\n- Plenty of sunshine, a bit milder\n- Did the groundhog see his shadow?",
            "😊 February 2nd Update:\n- Temperature: 34-44°F (1 to 7°C)\n- Clear and bright\n- A lovely, crisp winter day."
        ],
        "february_3": [
            "☁️ Grey Skies on February 3rd:\n- Temperature: 35-43°F (2 to 6°C)\n- Overcast and calm\n- Precipitation Chance: 15%\n- Not too cold, not too warm.",
            "🧤 February 3rd Weather:\n- Temperature: 36-45°F (2 to 7°C)\n- Solid cloud cover, but dry\n- A good day for errands."
        ],
        "february_4": [
            "🌨️ Wintry Mix for February 4th:\n- Temperature: 31-36°F (0 to 2°C)\n- Snow mixing with sleet at times\n- Precipitation Chance: 50%\n- Slippery spots are likely.",
            "🧊 February 4th Advisory:\n- Temperature: 30-35°F (-1 to 2°C)\n- Icy mix possible, especially in the morning\n- Use caution on untreated surfaces."
        ],
        "february_5": [
            "🌬️ February 5th Wind:\n- Temperature: 28-38°F (-2 to 3°C)\n- Very windy with some sun\n- Wind chills in the low 20s (-6°C).\n- Hold onto your hats!",
            "🥶 February 5th Forecast:\n- Temperature: 29-39°F (-2 to 4°C)\n- Blustery and cold despite the sun."
        ],
        "february_6": [
            "❄️ February 6th Snowfall:\n- Temperature: 27-33°F (-3 to 1°C)\n- A steady, light snow is expected\n- Precipitation Chance: 70%\n- Plan for 2-3 inches of accumulation.",
            "☃️ Snowy Day on February 6th:\n- Temperature: 26-32°F (-3 to 0°C)\n- Perfect snowman-building weather!\n- Roads will be snow-covered."
        ],
        "february_7": [
            "☀️ Post-Snow Sun on February 7th:\n- Temperature: 25-35°F (-4 to 2°C)\n- Clearing skies but very cold\n- The fresh snow will sparkle in the sun.",
            "🥶 February 7th Chill:\n- Temperature: 24-34°F (-4 to 1°C)\n- Sunny but frigid\n- Watch for refreezing on roads."
        ],
        "february_8": [
            "☁️ Cloudy February 8th:\n- Temperature: 30-40°F (-1 to 4°C)\n- Overcast skies return\n- A slight moderation in temperature.",
            "🧤 February 8th Weather:\n- Temperature: 32-41°F (0 to 5°C)\n- A calm, grey winter day."
        ],
        "february_9": [
            "☀️ Mild February 9th:\n- Temperature: 38-48°F (3 to 9°C)\n- Surprisingly mild and sunny\n- A hint of spring in the air?",
            "😊 February 9th Update:\n- Temperature: 40-50°F (4 to 10°C)\n- A beautiful day to get outside for a walk."
        ],
        "february_10": [
            "🌧️ Rainy February 10th:\n- Temperature: 39-46°F (4 to 8°C)\n- Overcast with periods of rain\n- Precipitation Chance: 60%\n- Goodbye snow, hello mud.",
            "☔ February 10th Forecast:\n- Temperature: 40-47°F (4 to 8°C)\n- A chilly, damp, rainy day."
        ],
        "february_11": [
            "🌬️ Windy and Wet on February 11th:\n- Temperature: 37-45°F (3 to 7°C)\n- Lingering showers and strong winds\n- Not a pleasant day to be outdoors.",
            "💨 February 11th Weather:\n- Temperature: 36-44°F (2 to 7°C)\n- Blustery with a damp chill in the air."
        ],
        "february_12": [
            "🌤️ Clearing Skies for February 12th:\n- Temperature: 35-45°F (2 to 7°C)\n- A mix of sun and clouds, still breezy\n- Drier conditions prevail.",
            "🧣 February 12th Forecast:\n- Temperature: 36-46°F (2 to 8°C)\n- Partly sunny and cool."
        ],
        "february_13": [
            "☁️ Clouds Increase on February 13th:\n- Temperature: 34-42°F (1 to 6°C)\n- Overcast ahead of Valentine's Day\n- Feeling chilly again.",
            "🧤 February 13th Weather:\n- Temperature: 33-41°F (1 to 5°C)\n- Grey skies dominate the day."
        ],
        "february_14": [
            "❤️ Valentine's Day Forecast:\n- Temperature: 30-38°F (-1 to 3°C)\n- A few romantic snow flurries are possible\n- Precipitation Chance: 30%\n- Perfect weather for a cozy dinner inside.",
            "❄️ Chilly Valentine's Day, February 14th:\n- Temperature: 28-36°F (-2 to 2°C)\n- Cold and crisp, bundle up if you're going out.\n- Roads should be fine for evening plans."
        ],
        "february_15": [
            "🥶 Frigid February 15th:\n- Temperature: 22-32°F (-6 to 0°C)\n- A blast of arctic air arrives\n- Sunny but bitterly cold.",
            "☀️ February 15th Cold Snap:\n- Temperature: 20-30°F (-7 to -1°C)\n- Bright sun won't help the temperatures.\n- Dangerously low wind chills."
        ],
        "february_16": [
            "☀️ Still Cold on February 16th:\n- Temperature: 24-34°F (-4 to 1°C)\n- The cold continues, but with plenty of sun\n- Dry conditions persist.",
            "🥶 February 16th Update:\n- Temperature: 25-35°F (-4 to 2°C)\n- Another day to stay bundled up."
        ],
        "february_17": [
            "❄️ Light Snow for February 17th:\n- Temperature: 28-35°F (-2 to 2°C)\n- Overcast with light snow showers\n- Precipitation Chance: 40%\n- A minor dusting is possible.",
            "🌨️ February 17th Forecast:\n- Temperature: 29-36°F (-2 to 2°C)\n- A classic, light-snow winter day."
        ],
        "february_18": [
            "☁️ Grey Day for February 18th:\n- Temperature: 33-41°F (1 to 5°C)\n- Overcast and calm, with slightly milder temps\n- No precipitation expected.",
            "🧤 February 18th Weather:\n- Temperature: 34-42°F (1 to 6°C)\n- A quiet, uneventful winter day."
        ],
        "february_19": [
            "☀️ Sunny Break on February 19th:\n- Temperature: 36-47°F (2 to 8°C)\n- A beautiful, sunny, and milder day\n- Great for shaking off the winter blues.",
            "😊 February 19th Forecast:\n- Temperature: 38-48°F (3 to 9°C)\n- Enjoy this lovely taste of early spring!"
        ],
        "february_20": [
            "🌧️ Rain Arrives on February 20th:\n- Temperature: 40-48°F (4 to 9°C)\n- Cloudy with rain developing later\n- Precipitation Chance: 70%\n- A chilly, wet evening ahead.",
            "☔ February 20th Weather:\n- Temperature: 41-49°F (5 to 9°C)\n- Periods of rain, grab the umbrella."
        ],
        "february_21": [
            "🌬️ Windy & Damp February 21st:\n- Temperature: 38-46°F (3 to 8°C)\n- Lingering rain showers and gusty winds\n- A raw and unpleasant day.",
            "💨 February 21st Update:\n- Temperature: 37-45°F (3 to 7°C)\n- Blustery conditions continue."
        ],
        "february_22": [
            "🌤️ Clearing Out on February 22nd:\n- Temperature: 39-49°F (4 to 9°C)\n- Becoming partly sunny and staying breezy\n- Drier air is moving in.",
            "🧣 February 22nd Forecast:\n- Temperature: 40-50°F (4 to 10°C)\n- A mix of sun and clouds, but still cool."
        ],
        "february_23": [
            "☀️ Bright & Brisk February 23rd:\n- Temperature: 35-45°F (2 to 7°C)\n- Sunny but a noticeable chill returns\n- A crisp late-winter day.",
            "🥶 February 23rd Weather:\n- Temperature: 34-44°F (1 to 7°C)\n- Clear skies, but don't put the winter coat away yet."
        ],
        "february_24": [
            "❄️ Late Season Snow for February 24th:\n- Temperature: 30-36°F (-1 to 2°C)\n- Cloudy with a chance of wet snow\n- Precipitation Chance: 50%\n- Winter reminds us it's still here.",
            "🌨️ February 24th Forecast:\n- Temperature: 31-37°F (0 to 3°C)\n- Periods of snow, which may not stick to roads."
        ],
        "february_25": [
            "☁️ Overcast February 25th:\n- Temperature: 34-42°F (1 to 6°C)\n- A grey and chilly day\n- Precipitation Chance: 20%\n- The last full week of February begins.",
            "🧤 February 25th Weather:\n- Temperature: 35-43°F (2 to 6°C)\n- Calm and cloudy."
        ],
        "february_26": [
            "☀️ February 26th Sunshine:\n- Temperature: 38-48°F (3 to 9°C)\n- A pleasant and sunny day\n- A nice mid-week treat.",
            "😊 February 26th Forecast:\n- Temperature: 39-49°F (4 to 9°C)\n- Enjoy the bright skies!"
        ],
        "february_27": [
            "☁️ Clouds Gather on February 27th:\n- Temperature: 37-46°F (3 to 8°C)\n- Increasing cloudiness\n- A change in the weather is coming.",
            "🧣 February 27th Weather:\n- Temperature: 38-47°F (3 to 8°C)\n- Overcast by the afternoon."
        ],
        "february_28": [
            "🌧️ Rainy End to February 28th:\n- Temperature: 41-49°F (5 to 9°C)\n- Rain showers to end the month\n- Precipitation Chance: 60%\n- March is coming in like a lion.",
            "☔ February 28th Forecast:\n- Temperature: 42-50°F (6 to 10°C)\n- A wet and cool day. Bye-bye February!"
        ],
        "march_1": [
            "🦁 March 1st Forecast:\n- Temperature: 38-48°F (3-9°C)\n- Windy with scattered rain showers\n- Precipitation Chance: 60%\n- March is coming in like a lion!",
            "💨 Blustery Start to March:\n- Temperature: 37-46°F (3-8°C)\n- Gusty winds and a mix of sun and clouds\n- A raw, early spring day."
        ],
        "march_2": [
            "🌦️ Unsettled March 2nd:\n- Temperature: 40-50°F (4-10°C)\n- Variable clouds with a chance of passing showers\n- Precipitation Chance: 40%\n- Keep a jacket handy.",
            "🌤️ March 2nd Weather:\n- Temperature: 42-52°F (6-11°C)\n- Partly sunny but a chill in the air."
        ],
        "march_3": [
            "☀️ Brighter March 3rd:\n- Temperature: 45-55°F (7-13°C)\n- Mostly sunny and a bit milder\n- A pleasant change from the past few days.",
            "😊 March 3rd Update:\n- Temperature: 46-56°F (8-13°C)\n- Enjoy the sunshine and lighter winds."
        ],
        "march_4": [
            "☁️ Grey Skies Return on March 4th:\n- Temperature: 43-51°F (6-11°C)\n- Overcast and cool\n- Precipitation Chance: 20%\n- A typical early March day.",
            "🧥 March 4th Weather:\n- Temperature: 42-50°F (6-10°C)\n- A good day for indoor activities."
        ],
        "march_5": [
            "🌧️ Rainy March 5th:\n- Temperature: 40-48°F (4-9°C)\n- Periods of rain, especially in the afternoon\n- Precipitation Chance: 70%\n- Don't forget your umbrella.",
            "☔ March 5th Forecast:\n- Temperature: 41-49°F (5-9°C)\n- A wet and dreary day."
        ],
        "march_6": [
            "❄️ Surprise Snow for March 6th?:\n- Temperature: 33-40°F (1-4°C)\n- Rain may mix with or change to wet snow\n- Precipitation Chance: 50%\n- A last gasp of winter!",
            "🌨️ March 6th Weather:\n- Temperature: 34-41°F (1-5°C)\n- Chilly with a chance of wet flakes."
        ],
        "march_7": [
            "🌬️ Windy and Cold on March 7th:\n- Temperature: 35-45°F (2-7°C)\n- Blustery winds and clearing skies\n- Feels much colder than the thermometer shows.",
            "🥶 March 7th Update:\n- Temperature: 36-46°F (2-8°C)\n- Sunny but brisk and chilly."
        ],
        "march_8": [
            "☀️ Sunny & Crisp March 8th:\n- Temperature: 38-50°F (3-10°C)\n- A beautiful, sunny but cool day\n- Great for a bundled-up walk.",
            "😊 March 8th Forecast:\n- Temperature: 40-52°F (4-11°C)\n- Plenty of sunshine to enjoy."
        ],
        "march_9": [
            "☁️ Clouds Increase on March 9th:\n- Temperature: 42-53°F (6-12°C)\n- Becoming cloudy throughout the day\n- Next system approaches.",
            "🧥 March 9th Weather:\n- Temperature: 44-54°F (7-12°C)\n- Overcast by evening."
        ],
        "march_10": [
            "🌧️ Wet March 10th:\n- Temperature: 45-54°F (7-12°C)\n- A rainy and mild day\n- Precipitation Chance: 80%\n- Spring showers are here.",
            "☔ March 10th Forecast:\n- Temperature: 46-55°F (8-13°C)\n- Grab the rain gear before you head out."
        ],
        "march_11": [
            "🌦️ Lingering Showers on March 11th:\n- Temperature: 48-58°F (9-14°C)\n- On-and-off showers with some sun breaks\n- Precipitation Chance: 40%",
            "🌤️ March 11th Weather:\n- Temperature: 50-60°F (10-16°C)\n- Partly sunny and mild in between showers."
        ],
        "march_12": [
            "☀️ Pleasant March 12th:\n- Temperature: 52-62°F (11-17°C)\n- Mostly sunny and pleasantly mild\n- A beautiful taste of spring.",
            "🌱 March 12th Update:\n- Temperature: 54-64°F (12-18°C)\n- A great day to be outdoors."
        ],
        "march_13": [
            "💨 Breezy March 13th:\n- Temperature: 50-60°F (10-16°C)\n- Partly sunny and a bit windy\n- Cooler than yesterday.",
            "🧥 March 13th Weather:\n- Temperature: 48-58°F (9-14°C)\n- A fresh breeze all day."
        ],
        "march_14": [
            "☁️ Cool & Cloudy March 14th:\n- Temperature: 46-55°F (8-13°C)\n- Overcast skies and a cool breeze\n- Not as nice as the start of the week.",
            "🧣 March 14th Forecast:\n- Temperature: 45-54°F (7-12°C)\n- A grey and chilly day."
        ],
        "march_15": [
            "🌧️ Rainy Friday for March 15th:\n- Temperature: 44-52°F (7-11°C)\n- Rain developing and becoming steady\n- Precipitation Chance: 70%\n- A wet end to the work week.",
            "☔ March 15th Weather:\n- Temperature: 43-51°F (6-11°C)\n- A dreary, rainy day."
        ],
        "march_16": [
            "🌬️ March 16th Winds:\n- Temperature: 42-50°F (6-10°C)\n- Windy with leftover sprinkles\n- A raw and blustery day.",
            "💨 March 16th Forecast:\n- Temperature: 40-48°F (4-9°C)\n- Hold onto your hats! It's a windy one."
        ],
        "march_17": [
            "☘️ St. Patrick's Day Forecast:\n- Temperature: 45-55°F (7-13°C)\n- A mix of sun and clouds, breezy\n- Precipitation Chance: 20%\n- Decent weather for parades, but bring a jacket!",
            "🍀 March 17th Weather:\n- Temperature: 47-57°F (8-14°C)\n- Partly sunny and cool.\n- Don't forget to wear green!"
        ],
        "march_18": [
            "☀️ Sunny Monday, March 18th:\n- Temperature: 48-60°F (9-16°C)\n- A beautiful, sunny start to the week\n- Feeling more like spring.",
            "😊 March 18th Update:\n- Temperature: 50-62°F (10-17°C)\n- Enjoy the abundant sunshine!"
        ],
        "march_19": [
            "☁️ Clouds on the Move for March 19th:\n- Temperature: 50-61°F (10-16°C)\n- Increasing clouds, but staying mild\n- Rain is on the way.",
            "🧥 March 19th Weather:\n- Temperature: 52-63°F (11-17°C)\n- Enjoy the dry weather while it lasts."
        ],
        "march_20": [
            "🌧️ Spring Equinox Showers, March 20th:\n- Temperature: 48-57°F (9-14°C)\n- Rainy and cool to mark the first day of spring\n- Precipitation Chance: 60%",
            "☔ March 20th Forecast:\n- Temperature: 47-56°F (8-13°C)\n- A wet welcome to the new season."
        ],
        "march_21": [
            "🌦️ Clearing Up on March 21st:\n- Temperature: 50-60°F (10-16°C)\n- Morning showers giving way to afternoon sun\n- Still a bit breezy.",
            "🌤️ March 21st Weather:\n- Temperature: 52-62°F (11-17°C)\n- A much nicer afternoon is in store."
        ],
        "march_22": [
            "☀️ Gorgeous March 22nd:\n- Temperature: 55-68°F (13-20°C)\n- Sunny and wonderfully mild\n- A perfect spring day!",
            "🌱 March 22nd Update:\n- Temperature: 57-70°F (14-21°C)\n- Get outside and enjoy this beautiful weather."
        ],
        "march_23": [
            "☁️ Mild but Cloudy March 23rd:\n- Temperature: 56-66°F (13-19°C)\n- Overcast skies but temperatures remain pleasant\n- Good for a walk or run.",
            "🧥 March 23rd Weather:\n- Temperature: 55-65°F (13-18°C)\n- Grey but not too chilly."
        ],
        "march_24": [
            "💨 Breezy Sunday for March 24th:\n- Temperature: 54-64°F (12-18°C)\n- Partly sunny and a bit windy\n- A fresh feel to the air.",
            "🌤️ March 24th Forecast:\n- Temperature: 53-63°F (12-17°C)\n- A mix of sun, clouds, and wind."
        ],
        "march_25": [
            "🌧️ Rain Returns for March 25th:\n- Temperature: 50-58°F (10-14°C)\n- Cooler with periods of rain\n- Precipitation Chance: 70%\n- Back to the unsettled pattern.",
            "☔ March 25th Weather:\n- Temperature: 49-57°F (9-14°C)\n- A grey, wet, and cool day."
        ],
        "march_26": [
            "🌦️ Showery March 26th:\n- Temperature: 51-61°F (11-16°C)\n- Scattered showers and some sunny breaks\n- Don't get caught without an umbrella.",
            "🌤️ March 26th Forecast:\n- Temperature: 53-63°F (12-17°C)\n- A typical, unpredictable spring day."
        ],
        "march_27": [
            "☀️ Sunny & Pleasant March 27th:\n- Temperature: 55-67°F (13-19°C)\n- A lovely day with plenty of sun and mild temps\n- Perfect for spring activities.",
            "😊 March 27th Update:\n- Temperature: 56-68°F (13-20°C)\n- Enjoy this mid-week treat!"
        ],
        "march_28": [
            "☁️ Overcast March 28th:\n- Temperature: 54-65°F (12-18°C)\n- A layer of clouds moves in\n- Still feels nice and mild.",
            "🧥 March 28th Weather:\n- Temperature: 55-66°F (13-19°C)\n- Grey but pleasant."
        ],
        "march_29": [
            "💨 Windy and Cooler on March 29th:\n- Temperature: 50-60°F (10-16°C)\n- Gusty winds and a mix of sun and clouds\n- A definite chill compared to yesterday.",
            "🌬️ March 29th Forecast:\n- Temperature: 48-58°F (9-14°C)\n- A blustery day."
        ],
        "march_30": [
            "🌧️ Wet End to the Week, March 30th:\n- Temperature: 47-55°F (8-13°C)\n- A chilly rain is expected\n- Precipitation Chance: 60%\n- A good day for indoor plans.",
            "☔ March 30th Weather:\n- Temperature: 46-54°F (8-12°C)\n- Cool and rainy."
        ],
        "march_31": [
            "🌤️ Clearing Out for March 31st:\n- Temperature: 48-58°F (9-14°C)\n- Morning clouds give way to afternoon sun\n- Ending the month on a brighter note.",
            "🌱 March 31st Forecast:\n- Temperature: 50-60°F (10-16°C)\n- Hello April, goodbye March!"
        ],
        "april_1": [
            "🌷 Welcome to April 1st:\n- Temperature: 50-62°F (10-17°C)\n- Partly sunny and mild\n- Precipitation Chance: 20% (No fooling!)\n- A lovely start to the month.",
            "🌤️ April 1st Forecast:\n- Temperature: 52-64°F (11-18°C)\n- A mix of sun and clouds, very pleasant."
        ],
        "april_2": [
            "🌧️ April 2nd Showers:\n- Temperature: 48-58°F (9-14°C)\n- Cooler with scattered rain showers\n- Precipitation Chance: 50%\n- April showers have arrived.",
            "☔ April 2nd Weather:\n- Temperature: 47-57°F (8-14°C)\n- Keep the umbrella handy today."
        ],
        "april_3": [
            "💨 Breezy and Cool on April 3rd:\n- Temperature: 46-56°F (8-13°C)\n- A mix of sun and clouds with a gusty wind\n- Feels brisk out there.",
            "🌬️ April 3rd Forecast:\n- Temperature: 45-55°F (7-13°C)\n- A fresh, cool spring day."
        ],
        "april_4": [
            "☀️ Sunny April 4th:\n- Temperature: 50-65°F (10-18°C)\n- A beautiful, sunny day\n- Perfect for a walk in the park.",
            "😊 April 4th Update:\n- Temperature: 52-67°F (11-19°C)\n- Enjoy the gorgeous spring weather."
        ],
        "april_5": [
            "☁️ Clouds Increase on April 5th:\n- Temperature: 54-66°F (12-19°C)\n- Mild, but clouds will be on the increase\n- Rain is on the horizon.",
            "🧥 April 5th Weather:\n- Temperature: 55-68°F (13-20°C)\n- Pleasant, but enjoy the dry weather while you can."
        ],
        "april_6": [
            "🌧️ Rainy Saturday for April 6th:\n- Temperature: 52-60°F (11-16°C)\n- Periods of rain, steady at times\n- Precipitation Chance: 80%\n- A good day for a movie.",
            "☔ April 6th Forecast:\n- Temperature: 53-61°F (12-16°C)\n- A wet weekend day."
        ],
        "april_7": [
            "🌦️ Lingering Showers on April 7th:\n- Temperature: 55-65°F (13-18°C)\n- Morning showers followed by afternoon clearing\n- A brighter end to the weekend.",
            "🌤️ April 7th Weather:\n- Temperature: 56-67°F (13-19°C)\n- Becoming partly sunny and mild."
        ],
        "april_8": [
            "☀️ Beautiful April 8th:\n- Temperature: 58-70°F (14-21°C)\n- Sunny and warm\n- A true taste of late spring.",
            "🌸 April 8th Update:\n- Temperature: 60-72°F (16-22°C)\n- Absolutely gorgeous weather."
        ],
        "april_9": [
            "☁️ Mild and Cloudy April 9th:\n- Temperature: 59-71°F (15-22°C)\n- Overcast but very mild\n- No rain expected, just clouds.",
            "🧥 April 9th Weather:\n- Temperature: 60-70°F (16-21°C)\n- Grey but comfortable."
        ],
        "april_10": [
            "🌧️ April 10th Showers Return:\n- Temperature: 56-66°F (13-19°C)\n- Cooler with a good chance for showers\n- Precipitation Chance: 60%",
            "☔ April 10th Forecast:\n- Temperature: 55-65°F (13-18°C)\n- Another day for the rain jacket."
        ],
        "april_11": [
            "💨 Windy and Unsettled on April 11th:\n- Temperature: 54-64°F (12-18°C)\n- Gusty winds with a mix of sun and clouds\n- A stray shower is possible.",
            "🌬️ April 11th Weather:\n- Temperature: 53-63°F (12-17°C)\n- A blustery spring day."
        ],
        "april_12": [
            "☀️ Sunny Friday for April 12th:\n- Temperature: 55-68°F (13-20°C)\n- A lovely, sunny end to the week\n- Perfect for after-work plans.",
            "😊 April 12th Update:\n- Temperature: 57-70°F (14-21°C)\n- Enjoy the beautiful sunshine!"
        ],
        "april_13": [
            "🌤️ Partly Sunny Saturday, April 13th:\n- Temperature: 58-71°F (14-22°C)\n- A mix of sun and clouds, very pleasant\n- Great for weekend activities.",
            "🌸 April 13th Forecast:\n- Temperature: 60-72°F (16-22°C)\n- A beautiful spring day."
        ],
        "april_14": [
            "🌧️ Showers for Sunday, April 14th:\n- Temperature: 57-67°F (14-19°C)\n- Increasing clouds with afternoon showers likely\n- Precipitation Chance: 50%",
            "☔ April 14th Weather:\n- Temperature: 58-68°F (14-20°C)\n- Have indoor backup plans for the afternoon."
        ],
        "april_15": [
            "🌦️ Unsettled April 15th:\n- Temperature: 56-65°F (13-18°C)\n- A cool day with scattered showers\n- Precipitation Chance: 40%\n- A classic mid-April day.",
            "🧥 April 15th Forecast:\n- Temperature: 55-64°F (13-18°C)\n- Chilly with a chance of rain."
        ],
        "april_16": [
            "☀️ Brighter Skies for April 16th:\n- Temperature: 58-69°F (14-21°C)\n- Mostly sunny and turning warmer\n- A much nicer day is on tap.",
            "😊 April 16th Update:\n- Temperature: 60-71°F (16-22°C)\n- Get out and enjoy the pleasant weather."
        ],
        "april_17": [
            "🌸 Perfect Spring Day, April 17th:\n- Temperature: 62-74°F (17-23°C)\n- Sunny, warm, with a light breeze\n- The trees are in full bloom!",
            "☀️ April 17th Forecast:\n- Temperature: 64-75°F (18-24°C)\n- An absolutely stellar day."
        ],
        "april_18": [
            "☁️ Clouds on the Horizon for April 18th:\n- Temperature: 63-73°F (17-23°C)\n- A warm day, but clouds will be increasing\n- Rain arrives overnight.",
            "🧥 April 18th Weather:\n- Temperature: 62-72°F (17-22°C)\n- Enjoy the warmth before the rain."
        ],
        "april_19": [
            "🌧️ Rainy and Cooler April 19th:\n- Temperature: 55-63°F (13-17°C)\n- A period of rain will make for a damp, cool day\n- Precipitation Chance: 70%",
            "☔ April 19th Forecast:\n- Temperature: 54-62°F (12-17°C)\n- A definite need for the umbrella."
        ],
        "april_20": [
            "💨 Blustery and Chilly on April 20th:\n- Temperature: 52-61°F (11-16°C)\n- Windy with a mix of sun and clouds\n- A noticeable chill in the air.",
            "🌬️ April 20th Weather:\n- Temperature: 50-60°F (10-16°C)\n- A raw spring day."
        ],
        "april_21": [
            "☀️ Sunny Sunday, April 21st:\n- Temperature: 55-67°F (13-19°C)\n- Sunny but still on the cool side\n- A bright end to the weekend.",
            "😊 April 21st Update:\n- Temperature: 56-68°F (13-20°C)\n- The sun feels great, but keep a jacket."
        ],
        "april_22": [
            "🌸 Earth Day Forecast, April 22nd:\n- Temperature: 58-70°F (14-21°C)\n- Mostly sunny and pleasant\n- A great day to be outside and appreciate nature.",
            "🌱 April 22nd Weather:\n- Temperature: 60-72°F (16-22°C)\n- Perfect for planting flowers or a park cleanup."
        ],
        "april_23": [
            "☁️ Cloudy but Mild on April 23rd:\n- Temperature: 60-71°F (16-22°C)\n- Overcast skies but warm temperatures\n- No rain is expected.",
            "🧥 April 23rd Forecast:\n- Temperature: 61-72°F (16-22°C)\n- A comfortable, albeit grey, day."
        ],
        "april_24": [
            "🌧️ Mid-week Showers for April 24th:\n- Temperature: 58-68°F (14-20°C)\n- Periods of rain are likely\n- Precipitation Chance: 60%\n- Back to the unsettled pattern.",
            "☔ April 24th Weather:\n- Temperature: 57-67°F (14-19°C)\n- A wet and mild day."
        ],
        "april_25": [
            "🌦️ Showers Taper on April 25th:\n- Temperature: 60-70°F (16-21°C)\n- Morning showers give way to a partly sunny afternoon\n- Turning warmer.",
            "🌤️ April 25th Forecast:\n- Temperature: 62-72°F (17-22°C)\n- A much nicer end to the day."
        ],
        "april_26": [
            "☀️ Warm Friday for April 26th:\n- Temperature: 65-78°F (18-26°C)\n- Sunny and feeling like summer!\n- A great day for a BBQ.",
            "😎 April 26th Update:\n- Temperature: 67-80°F (19-27°C)\n- A warm and beautiful end to the week."
        ],
        "april_27": [
            "🌤️ Partly Sunny and Warm, April 27th:\n- Temperature: 66-79°F (19-26°C)\n- A mix of sun and clouds, staying very warm\n- Great for outdoor weekend plans.",
            "🌸 April 27th Forecast:\n- Temperature: 68-81°F (20-27°C)\n- A gorgeous late April day."
        ],
        "april_28": [
            "⛈️ Thunderstorm Chance for April 28th:\n- Temperature: 64-76°F (18-24°C)\n- Warm and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ April 28th Weather:\n- Temperature: 65-77°F (18-25°C)\n- Keep an eye on the sky in the afternoon."
        ],
        "april_29": [
            "💨 Cooler and Breezy on April 29th:\n- Temperature: 58-68°F (14-20°C)\n- A much cooler day with a noticeable breeze\n- A mix of sun and clouds.",
            "🌬️ April 29th Forecast:\n- Temperature: 57-67°F (14-19°C)\n- A fresh, cool feel to the air."
        ],
        "april_30": [
            "☀️ Sunny End to April 30th:\n- Temperature: 60-72°F (16-22°C)\n- A beautiful, sunny end to the month\n- Perfect spring weather. Hello May!",
            "😊 April 30th Update:\n- Temperature: 62-74°F (17-23°C)\n- Enjoy the pleasant sunshine."
        ],
        "may_1": [
            "🌸 Welcome to May 1st!:\n- Temperature: 62-75°F (17-24°C)\n- Sunny and beautiful\n- A perfect start to the month.",
            "☀️ May 1st Forecast:\n- Temperature: 64-77°F (18-25°C)\n- Abundant sunshine, great for any outdoor activity."
        ],
        "may_2": [
            "☁️ Clouds Increase on May 2nd:\n- Temperature: 63-76°F (17-24°C)\n- Still warm, but clouds will be on the increase\n- Rain approaches for tomorrow.",
            "🧥 May 2nd Weather:\n- Temperature: 65-78°F (18-26°C)\n- Enjoy the warmth before the weather changes."
        ],
        "may_3": [
            "🌧️ Rainy May 3rd:\n- Temperature: 60-70°F (16-21°C)\n- Cooler with periods of rain\n- Precipitation Chance: 70%\n- A good day for indoor chores.",
            "☔ May 3rd Forecast:\n- Temperature: 58-68°F (14-20°C)\n- A damp and dreary day."
        ],
        "may_4": [
            "🌦️ Lingering Showers on May 4th:\n- Temperature: 62-72°F (17-22°C)\n- Scattered showers, especially in the morning\n- Some sun may break through later.",
            "🌤️ May 4th Weather:\n- Temperature: 64-74°F (18-23°C)\n- A mix of sun and clouds with a chance of rain."
        ],
        "may_5": [
            "☀️ Cinco de Mayo Forecast:\n- Temperature: 65-78°F (18-26°C)\n- Mostly sunny and turning much warmer\n- Perfect weather for a fiesta!",
            "🥳 May 5th Update:\n- Temperature: 67-80°F (19-27°C)\n- Sunny, warm, and beautiful."
        ],
        "may_6": [
            "🌤️ Warm and Breezy May 6th:\n- Temperature: 68-81°F (20-27°C)\n- A mix of sun and high clouds, warm and a bit windy\n- Summer is knocking on the door.",
            "😎 May 6th Forecast:\n- Temperature: 70-83°F (21-28°C)\n- A very warm day."
        ],
        "may_7": [
            "⛈️ Thunderstorm Potential on May 7th:\n- Temperature: 69-82°F (21-28°C)\n- Hot and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ May 7th Weather:\n- Temperature: 70-84°F (21-29°C)\n- Be aware of changing conditions in the afternoon."
        ],
        "may_8": [
            "💨 Cooler Air Arrives on May 8th:\n- Temperature: 63-73°F (17-23°C)\n- Less humid and cooler behind yesterday's front\n- Breezy with a mix of sun and clouds.",
            "🌬️ May 8th Forecast:\n- Temperature: 62-72°F (17-22°C)\n- A much more comfortable day."
        ],
        "may_9": [
            "☀️ Pleasant May 9th:\n- Temperature: 64-76°F (18-24°C)\n- Sunny and delightful\n- Low humidity and comfortable temperatures.",
            "😊 May 9th Update:\n- Temperature: 65-77°F (18-25°C)\n- A perfect mid-spring day."
        ],
        "may_10": [
            "☁️ Clouds Return on May 10th:\n- Temperature: 66-78°F (19-26°C)\n- Increasing clouds, but staying warm\n- Rain is possible overnight.",
            "🧥 May 10th Weather:\n- Temperature: 67-79°F (19-26°C)\n- A warm, but increasingly cloudy day."
        ],
        "may_11": [
            "🌧️ Rainy Saturday for May 11th:\n- Temperature: 64-72°F (18-22°C)\n- A cool and rainy day is expected\n- Precipitation Chance: 70%\n- A good day to relax indoors.",
            "☔ May 11th Forecast:\n- Temperature: 63-71°F (17-22°C)\n- Periods of rain will dominate the day."
        ],
        "may_12": [
            "🌸 Mother's Day Forecast:\n- Temperature: 65-75°F (18-24°C)\n- Morning clouds give way to afternoon sun\n- A pleasant day for Mom's special day.",
            "🌤️ May 12th Weather:\n- Temperature: 66-76°F (19-24°C)\n- A nice afternoon for a family gathering."
        ],
        "may_13": [
            "☀️ Beautiful May 13th:\n- Temperature: 68-80°F (20-27°C)\n- Sunny and warm, a perfect day\n- Low humidity makes it feel great.",
            "😎 May 13th Update:\n- Temperature: 70-82°F (21-28°C)\n- Summer-like warmth is here."
        ],
        "may_14": [
            "🌤️ Partly Sunny & Warm on May 14th:\n- Temperature: 70-83°F (21-28°C)\n- A mix of sun and clouds, very warm\n- Humidity will be on the rise.",
            "🥵 May 14th Forecast:\n- Temperature: 72-85°F (22-29°C)\n- Feeling hot and a bit sticky."
        ],
        "may_15": [
            "⛈️ Mid-week Thunderstorms, May 15th:\n- Temperature: 71-84°F (22-29°C)\n- Hot and humid, with a good chance for afternoon storms\n- Precipitation Chance: 50%",
            "🌩️ May 15th Weather:\n- Temperature: 72-86°F (22-30°C)\n- Some storms could be strong. Stay weather aware."
        ],
        "may_16": [
            "🌦️ Lingering Storms on May 16th:\n- Temperature: 68-78°F (20-26°C)\n- A lingering morning storm possible, then partly sunny\n- Less humid and not as hot.",
            "🌤️ May 16th Forecast:\n- Temperature: 69-79°F (21-26°C)\n- A much more comfortable afternoon."
        ],
        "may_17": [
            "☀️ Gorgeous Friday for May 17th:\n- Temperature: 67-79°F (19-26°C)\n- Sunny and pleasant with low humidity\n- A fantastic end to the week.",
            "😊 May 17th Update:\n- Temperature: 68-80°F (20-27°C)\n- Perfect weather for outdoor dining."
        ],
        "may_18": [
            "☁️ Cloudy but Warm Saturday, May 18th:\n- Temperature: 69-81°F (21-27°C)\n- Overcast skies, but it will still be warm\n- Rain holds off until nighttime.",
            "🧥 May 18th Forecast:\n- Temperature: 70-82°F (21-28°C)\n- A good day for outdoor plans, despite the clouds."
        ],
        "may_19": [
            "🌧️ Rainy Sunday for May 19th:\n- Temperature: 66-74°F (19-23°C)\n- A cool and rainy day\n- Precipitation Chance: 80%\n- A washout for the end of the weekend.",
            "☔ May 19th Weather:\n- Temperature: 65-73°F (18-23°C)\n- A good day to stay in and read a book."
        ],
        "may_20": [
            "💨 Breezy and Cool on May 20th:\n- Temperature: 64-73°F (18-23°C)\n- Leftover showers in the morning, then breezy and cool\n- A mix of sun and clouds in the afternoon.",
            "🌬️ May 20th Forecast:\n- Temperature: 63-72°F (17-22°C)\n- A much cooler airmass has moved in."
        ],
        "may_21": [
            "☀️ Sunny and Cool May 21st:\n- Temperature: 62-74°F (17-23°C)\n- A beautiful sunny day, but cooler than normal\n- A light jacket might be needed.",
            "😊 May 21st Update:\n- Temperature: 64-75°F (18-24°C)\n- Enjoy the sunshine and low humidity."
        ],
        "may_22": [
            "🌤️ Warming Up on May 22nd:\n- Temperature: 65-78°F (18-26°C)\n- Partly sunny and getting warmer\n- A very pleasant mid-week day.",
            "🌸 May 22nd Forecast:\n- Temperature: 67-80°F (19-27°C)\n- A return to more seasonal temperatures."
        ],
        "may_23": [
            "☀️ Sunny and Warm May 23rd:\n- Temperature: 70-82°F (21-28°C)\n- A great day with lots of sun and warm temps\n- Perfect for pre-holiday weekend errands.",
            "😎 May 23rd Update:\n- Temperature: 72-84°F (22-29°C)\n- Summer is just around the corner."
        ],
        "may_24": [
            "🌤️ Partly Sunny Friday, May 24th:\n- Temperature: 72-85°F (22-29°C)\n- A mix of sun and clouds, hot and getting more humid\n- Great for kicking off the long weekend.",
            "🥵 May 24th Forecast:\n- Temperature: 74-87°F (23-31°C)\n- The heat is on!"
        ],
        "may_25": [
            "⛈️ Holiday Weekend Storms, May 25th:\n- Temperature: 73-86°F (23-30°C)\n- Hot and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ May 25th Weather:\n- Temperature: 74-88°F (23-31°C)\n- Have a backup plan for your BBQ."
        ],
        "may_26": [
            "🌦️ Unsettled Sunday, May 26th:\n- Temperature: 71-83°F (22-28°C)\n- Not as hot, with a chance of a pop-up shower\n- A mix of sun and clouds.",
            "🌤️ May 26th Forecast:\n- Temperature: 72-84°F (22-29°C)\n- An improvement over yesterday, but keep an eye out."
        ],
        "may_27": [
            "🇺🇸 Memorial Day Forecast:\n- Temperature: 70-81°F (21-27°C)\n- Partly sunny and pleasant, with lower humidity\n- A nice day to honor and remember.",
            "☀️ May 27th Weather:\n- Temperature: 72-83°F (22-28°C)\n- A beautiful end to the holiday weekend."
        ],
        "may_28": [
            "☀️ Pleasant May 28th:\n- Temperature: 68-79°F (20-26°C)\n- Sunny with comfortable temperatures\n- A great day to be outside.",
            "😊 May 28th Update:\n- Temperature: 69-80°F (21-27°C)\n- Enjoy this fantastic weather."
        ],
        "may_29": [
            "☁️ Cloudy but Warm on May 29th:\n- Temperature: 70-81°F (21-27°C)\n- Overcast skies, but remaining warm\n- Rain holds off for one more day.",
            "🧥 May 29th Forecast:\n- Temperature: 71-82°F (22-28°C)\n- A good day despite the lack of sun."
        ],
        "may_30": [
            "🌧️ Rainy May 30th:\n- Temperature: 67-75°F (19-24°C)\n- Cooler with periods of rain\n- Precipitation Chance: 60%\n- A damp end to the month.",
            "☔ May 30th Weather:\n- Temperature: 66-74°F (19-23°C)\n- A grey and wet day."
        ],
        "may_31": [
            "🌤️ Clearing Out for May 31st:\n- Temperature: 68-78°F (20-26°C)\n- Morning clouds give way to afternoon sun\n- A brighter and warmer end to May.",
            "😊 May 31st Forecast:\n- Temperature: 70-80°F (21-27°C)\n- Hello June, goodbye May!"
        ],
        "june_1": [
            "☀️ Welcome to June 1st:\n- Temperature: 70-82°F (21-28°C)\n- Sunny and warm, a perfect start to meteorological summer!\n- Low chance of rain: 10%",
            "😎 June 1st Forecast:\n- Temperature: 72-85°F (22-29°C)\n- Clear skies, perfect for the beach or pool."
        ],
        "june_2": [
            "🌤️ Partly Sunny & Warm on June 2nd:\n- Temperature: 73-86°F (23-30°C)\n- A mix of sun and clouds, feeling hot\n- Humidity is creeping up.",
            "🥵 June 2nd Weather:\n- Temperature: 75-88°F (24-31°C)\n- A hot and somewhat sticky day."
        ],
        "june_3": [
            "⛈️ Afternoon Storms for June 3rd:\n- Temperature: 74-87°F (23-31°C)\n- Hot and humid with scattered afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ June 3rd Update:\n- Temperature: 76-89°F (24-32°C)\n- Keep an eye on the sky for your outdoor plans."
        ],
        "june_4": [
            "🌦️ Less Humid June 4th:\n- Temperature: 72-84°F (22-29°C)\n- A lingering morning shower, then partly sunny and less humid\n- A much more comfortable afternoon.",
            "🌤️ June 4th Forecast:\n- Temperature: 73-85°F (23-29°C)\n- A mix of sun and clouds with a pleasant breeze."
        ],
        "june_5": [
            "☀️ Beautiful June 5th:\n- Temperature: 71-83°F (22-28°C)\n- Sunny and pleasant with low humidity\n- An ideal early summer day.",
            "😊 June 5th Weather:\n- Temperature: 72-84°F (22-29°C)\n- Perfect for a picnic or park visit."
        ],
        "june_6": [
            "☁️ Cloudy but Warm on June 6th:\n- Temperature: 74-85°F (23-29°C)\n- Overcast skies but still feeling very warm\n- Rain should hold off until overnight.",
            "🧥 June 6th Forecast:\n- Temperature: 75-86°F (24-30°C)\n- A warm day even without direct sun."
        ],
        "june_7": [
            "🌧️ Rainy Friday for June 7th:\n- Temperature: 70-78°F (21-26°C)\n- Cooler with periods of rain, possibly heavy at times\n- Precipitation Chance: 70%",
            "☔ June 7th Weather:\n- Temperature: 69-77°F (21-25°C)\n- A washout for any outdoor evening plans."
        ],
        "june_8": [
            "💨 Breezy and Showery Saturday, June 8th:\n- Temperature: 68-76°F (20-24°C)\n- Windy with scattered showers, especially in the morning\n- A cool and unsettled day.",
            "🌬️ June 8th Forecast:\n- Temperature: 67-75°F (19-24°C)\n- Not a great day for the pool."
        ],
        "june_9": [
            "☀️ Sunny and Pleasant Sunday, June 9th:\n- Temperature: 70-80°F (21-27°C)\n- A beautiful day with lots of sun and lower humidity\n- A great rebound for the weekend.",
            "😊 June 9th Update:\n- Temperature: 72-82°F (22-28°C)\n- Perfect weather for a BBQ."
        ],
        "june_10": [
            "☀️ Sunny and Warm June 10th:\n- Temperature: 73-85°F (23-29°C)\n- Another gorgeous day with abundant sunshine\n- The heat is building again.",
            "😎 June 10th Forecast:\n- Temperature: 75-87°F (24-31°C)\n- A classic summer day."
        ],
        "june_11": [
            "🌤️ Hot and Humid June 11th:\n- Temperature: 76-88°F (24-31°C)\n- A mix of sun and clouds, feeling steamy\n- Stay hydrated!",
            "🥵 June 11th Weather:\n- Temperature: 77-90°F (25-32°C)\n- A scorcher of a day."
        ],
        "june_12": [
            "⛈️ Pop-up Storms for June 12th:\n- Temperature: 75-87°F (24-31°C)\n- Hot and humid with the chance of an isolated thunderstorm\n- Precipitation Chance: 30%",
            "🌩️ June 12th Update:\n- Temperature: 76-89°F (24-32°C)\n- Most areas will stay dry, but have a plan B."
        ],
        "june_13": [
            "☀️ Sunny and Hot on June 13th:\n- Temperature: 78-90°F (26-32°C)\n- A very hot day with plenty of strong sun\n- UV Index will be high.",
            "😎 June 13th Forecast:\n- Temperature: 79-92°F (26-33°C)\n- A good day to find some A/C."
        ],
        "june_14": [
            "☁️ Cloudy but Still Hot, June 14th:\n- Temperature: 77-88°F (25-31°C)\n- More clouds than sun, but the heat and humidity remain\n- A front is approaching.",
            "🥵 June 14th Weather:\n- Temperature: 78-89°F (26-32°C)\n- A muggy end to the week."
        ],
        "june_15": [
            "🌧️ Showers and Storms for June 15th:\n- Temperature: 72-80°F (22-27°C)\n- Cooler with a good chance of showers and thunderstorms\n- Precipitation Chance: 60%",
            "☔ June 15th Forecast:\n- Temperature: 71-79°F (22-26°C)\n- A wet and unsettled start to the weekend."
        ],
        "june_16": [
            "🌤️ Father's Day Forecast:\n- Temperature: 74-84°F (23-29°C)\n- Partly sunny and much more pleasant\n- A great day to celebrate Dad outdoors.",
            "😊 June 16th Weather:\n- Temperature: 75-85°F (24-29°C)\n- Lower humidity and a light breeze."
        ],
        "june_17": [
            "☀️ Picture Perfect June 17th:\n- Temperature: 72-83°F (22-28°C)\n- Sunny, warm, and not too humid\n- An absolutely beautiful day.",
            "😎 June 17th Update:\n- Temperature: 73-84°F (23-29°C)\n- Enjoy this fantastic start to the week."
        ],
        "june_18": [
            "🌤️ Warming Up on June 18th:\n- Temperature: 74-86°F (23-30°C)\n- Partly sunny with temperatures on the rise\n- Another great day overall.",
            "☀️ June 18th Forecast:\n- Temperature: 76-88°F (24-31°C)\n- Feeling more like deep summer."
        ],
        "june_19": [
            "☀️ Juneteenth Celebration Weather:\n- Temperature: 77-89°F (25-32°C)\n- Sunny and hot, perfect for cookouts and community events\n- Remember to stay hydrated.",
            "😎 June 19th Update:\n- Temperature: 78-91°F (26-33°C)\n- A hot day with plenty of sunshine."
        ],
        "june_20": [
            "⛈️ Stormy Afternoon for June 20th:\n- Temperature: 76-88°F (24-31°C)\n- Hot and sticky, with afternoon thunderstorms likely\n- Precipitation Chance: 50%",
            "🌩️ June 20th Weather:\n- Temperature: 77-90°F (25-32°C)\n- Some storms could produce heavy rain."
        ],
        "june_21": [
            "☀️ Summer Solstice Forecast:\n- Temperature: 75-85°F (24-29°C)\n- A beautiful day to mark the longest day of the year!\n- Sunny, warm, and less humid.",
            "🌅 June 21st Weather:\n- Temperature: 76-86°F (24-30°C)\n- Enjoy the extended daylight with fantastic weather."
        ],
        "june_22": [
            "☀️ Sunny Saturday, June 22nd:\n- Temperature: 76-87°F (24-31°C)\n- A great weekend day with lots of sun and warmth\n- Perfect for any outdoor plans.",
            "😎 June 22nd Forecast:\n- Temperature: 78-89°F (26-32°C)\n- Beach weather is here!"
        ],
        "june_23": [
            "🌤️ Partly Sunny and Hot, June 23rd:\n- Temperature: 78-90°F (26-32°C)\n- A mix of sun and clouds, very hot and humid\n- A slight chance of a pop-up storm.",
            "🥵 June 23rd Weather:\n- Temperature: 79-92°F (26-33°C)\n- Take it easy in the heat today."
        ],
        "june_24": [
            "☁️ Cloudy but Steamy on June 24th:\n- Temperature: 77-88°F (25-31°C)\n- Overcast skies will provide little relief from the heat\n- Rain is on the way for tomorrow.",
            "💧 June 24th Forecast:\n- Temperature: 78-89°F (26-32°C)\n- A very muggy day."
        ],
        "june_25": [
            "🌧️ Rainy and Cooler June 25th:\n- Temperature: 71-79°F (22-26°C)\n- A welcome cool down, but it comes with rain\n- Precipitation Chance: 70%",
            "☔ June 25th Weather:\n- Temperature: 70-78°F (21-26°C)\n- A good day to catch up on indoor tasks."
        ],
        "june_26": [
            "🌦️ Lingering Showers for June 26th:\n- Temperature: 72-81°F (22-27°C)\n- Morning showers giving way to some afternoon sun\n- Still feeling fresh and pleasant.",
            "🌤️ June 26th Forecast:\n- Temperature: 73-82°F (23-28°C)\n- A much nicer afternoon is ahead."
        ],
        "june_27": [
            "☀️ Beautiful June 27th:\n- Temperature: 74-84°F (23-29°C)\n- Sunny and warm with comfortable humidity\n- A picture-perfect late June day.",
            "😊 June 27th Update:\n- Temperature: 75-85°F (24-29°C)\n- Get out and enjoy it!"
        ],
        "june_28": [
            "☀️ Sunny and Hotter, June 28th:\n- Temperature: 76-88°F (24-31°C)\n- The heat builds under strong sunshine\n- A great day for the pool.",
            "😎 June 28th Forecast:\n- Temperature: 78-90°F (26-32°C)\n- Approaching true summer heat."
        ],
        "june_29": [
            "⛈️ Pre-Holiday Weekend Storms:\n- Temperature: 77-89°F (25-32°C)\n- Hot and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ June 29th Weather:\n- Temperature: 78-91°F (26-33°C)\n- Keep an eye to the sky if you have outdoor plans."
        ],
        "june_30": [
            "🌤️ Weather Forecast for June 30th:\n- Temperature: 75-80°F (24-27°C)\n- Conditions: Partly cloudy with light breeze\n- Chance of rain: 20%\n- Perfect for outdoor activities!\n- Backup indoor plan recommended just in case",
            "☀️ June 30th Weather Update:\n- Temperature: 78-85°F (26-29°C)\n- Sunny with occasional clouds\n- Rain probability: 10%\n- Light winds from southwest\n- Excellent conditions for outdoor events",
            "🌥️ June 30th Forecast:\n- Temperature: 72-77°F (22-25°C)\n- Mostly cloudy, clearing by afternoon\n- 30% chance of morning drizzle\n- Humidity: 65%\n- Good for covered outdoor venues",
            "🌞 Beautiful June 30th Expected:\n- Temperature: 80-86°F (27-30°C)\n- Clear skies with gentle breeze\n- No precipitation expected\n- UV index: 7 (high) - sun protection advised\n- Perfect weather for garden parties",
            "⛅ June 30th Weather:\n- Temperature: 74-79°F (23-26°C)\n- Partly sunny with scattered clouds\n- 15% chance of brief showers\n- Wind: 8-12 mph\n- Great for outdoor celebrations with tent backup"
        ],
        "july_1": [
            "🇺🇸 Kicking off July 1st:\n- Temperature: 80-88°F (27-31°C)\n- Sunny and hot, a classic start to the month\n- Low chance of rain: 10%",
            "☀️ July 1st Forecast:\n- Temperature: 82-90°F (28-32°C)\n- Perfect weather for pre-holiday preparations and BBQs."
        ],
        "july_2": [
            "🥵 Hot & Humid on July 2nd:\n- Temperature: 84-92°F (29-33°C)\n- A mix of sun and clouds, feeling very steamy\n- Stay cool and hydrated!",
            "💧 July 2nd Weather:\n- Temperature: 85-94°F (29-34°C)\n- Heat advisory possible, limit strenuous activity."
        ],
        "july_3": [
            "⛈️ Pre-4th Storms on July 3rd:\n- Temperature: 83-91°F (28-33°C)\n- Hot and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%\n- Keep an eye on the forecast for your holiday plans.",
            "🌩️ July 3rd Update:\n- Temperature: 84-93°F (29-34°C)\n- Storms could bring heavy rain and gusty winds."
        ],
        "july_4": [
            "🎆 July 4th Weather Forecast:\n- Temperature: 82-88°F (28-31°C)\n- Sunny and warm - perfect for BBQs!\n- Rain chance: 5%\n- Light breeze ideal for fireworks\n- Remember sunscreen and hydration",
            "☀️ Independence Day Weather:\n- Temperature: 85-92°F (29-33°C)\n- Hot and sunny conditions\n- No rain expected\n- Consider heat precautions for guests\n- Evening will be perfect for outdoor festivities",
            "🌤️ July 4th Update:\n- Temperature: 79-84°F (26-29°C)\n- Partly cloudy with sun breaks\n- 20% chance of afternoon thunderstorms\n- Have covered areas ready\n- Great grilling weather overall"
        ],
        "july_5": [
            "☀️ Sunny & Hot July 5th:\n- Temperature: 85-93°F (29-34°C)\n- A scorcher of a day with abundant sunshine\n- A great day to hit the pool or beach.",
            "😎 July 5th Forecast:\n- Temperature: 86-95°F (30-35°C)\n- Use plenty of sunscreen, the UV index is very high."
        ],
        "july_6": [
            "🌤️ Partly Sunny & Steamy on July 6th:\n- Temperature: 84-92°F (29-33°C)\n- A mix of sun and clouds with high humidity\n- Another hot summer day.",
            "🥵 July 6th Weather:\n- Temperature: 85-93°F (29-34°C)\n- Feels like summer in full swing."
        ],
        "july_7": [
            "⛈️ Weekend Storms for July 7th:\n- Temperature: 82-90°F (28-32°C)\n- Hot and humid, with scattered thunderstorms in the afternoon\n- Precipitation Chance: 50%",
            "🌩️ July 7th Forecast:\n- Temperature: 83-91°F (28-33°C)\n- Be ready to move festivities indoors if needed."
        ],
        "july_8": [
            "🌦️ Lingering Showers on July 8th:\n- Temperature: 78-86°F (26-30°C)\n- A morning shower possible, then turning partly sunny\n- Less humid and more comfortable.",
            "🌤️ July 8th Update:\n- Temperature: 79-87°F (26-31°C)\n- A much more pleasant afternoon."
        ],
        "july_9": [
            "☀️ Beautiful July 9th:\n- Temperature: 77-85°F (25-29°C)\n- Sunny and warm with low humidity\n- An ideal mid-summer day.",
            "😊 July 9th Weather:\n- Temperature: 78-86°F (26-30°C)\n- Perfect for any and all outdoor activities."
        ],
        "july_10": [
            "☀️ Sunny and Hotter, July 10th:\n- Temperature: 80-88°F (27-31°C)\n- The heat is back on under sunny skies\n- A classic summer day.",
            "😎 July 10th Forecast:\n- Temperature: 82-90°F (28-32°C)\n- Don't forget to water the plants!"
        ],
        "july_11": [
            "🥵 Heat Wave Continues on July 11th:\n- Temperature: 85-94°F (29-34°C)\n- Very hot and increasingly humid\n- Take precautions against the heat.",
            "💧 July 11th Weather:\n- Temperature: 86-96°F (30-36°C)\n- A good day to stay in the A/C."
        ],
        "july_12": [
            "⛈️ Pop-up Storm Chance, July 12th:\n- Temperature: 84-93°F (29-34°C)\n- Oppressively hot and humid with an isolated storm possible\n- Precipitation Chance: 30%",
            "🌩️ July 12th Update:\n- Temperature: 85-95°F (29-35°C)\n- Any storm that forms could be strong."
        ],
        "july_13": [
            "☁️ Cloudy but Still Hot, July 13th:\n- Temperature: 83-91°F (28-33°C)\n- Mostly cloudy skies won't provide much relief from the heat\n- A cold front is on its way.",
            "🥵 July 13th Weather:\n- Temperature: 84-92°F (29-33°C)\n- A muggy and uncomfortable day."
        ],
        "july_14": [
            "🌧️ Stormy Sunday for July 14th:\n- Temperature: 76-84°F (24-29°C)\n- Widespread showers and thunderstorms expected\n- Precipitation Chance: 70%\n- A welcome, albeit wet, break from the heat.",
            "☔ July 14th Forecast:\n- Temperature: 75-83°F (24-28°C)\n- A good day to stay inside."
        ],
        "july_15": [
            "☀️ Delightful July 15th:\n- Temperature: 75-83°F (24-28°C)\n- Sunny, dry, and much less humid\n- A perfect day!",
            "😊 July 15th Update:\n- Temperature: 76-84°F (24-29°C)\n- Enjoy this fantastic weather."
        ],
        "july_16": [
            "🌤️ Pleasant and Sunny July 16th:\n- Temperature: 76-85°F (24-29°C)\n- A mix of sun and clouds with comfortable temperatures\n- Another great summer day.",
            "☀️ July 16th Forecast:\n- Temperature: 77-86°F (25-30°C)\n- Great weather continues."
        ],
        "july_17": [
            "☀️ Heat Builds Again on July 17th:\n- Temperature: 78-88°F (26-31°C)\n- Sunny skies and rising temperatures\n- Humidity will also be on the increase.",
            "😎 July 17th Forecast:\n- Temperature: 80-90°F (27-32°C)\n- Back to the summer heat."
        ],
        "july_18": [
            "🥵 Hot and Humid July 18th:\n- Temperature: 82-92°F (28-33°C)\n- A hazy, hot, and humid day\n- A good day for the pool.",
            "💧 July 18th Weather:\n- Temperature: 84-94°F (29-34°C)\n- Stay hydrated!"
        ],
        "july_19": [
            "⛈️ Afternoon Storms Likely, July 19th:\n- Temperature: 83-91°F (28-33°C)\n- Hot and sticky with scattered thunderstorms developing\n- Precipitation Chance: 50%",
            "🌩️ July 19th Update:\n- Temperature: 84-92°F (29-33°C)\n- Be prepared for interruptions to outdoor plans."
        ],
        "july_20": [
            "🌦️ Unsettled Weekend for July 20th:\n- Temperature: 80-88°F (27-31°C)\n- A chance of a shower or storm at any time\n- Otherwise, a mix of sun and clouds.",
            "🌤️ July 20th Forecast:\n- Temperature: 81-89°F (27-32°C)\n- Not a washout, but have a plan B."
        ],
        "july_21": [
            "☀️ Sunny Sunday, July 21st:\n- Temperature: 82-90°F (28-32°C)\n- A hot and sunny end to the weekend\n- A classic summer day.",
            "😎 July 21st Update:\n- Temperature: 84-92°F (29-33°C)\n- Perfect for a BBQ or lake day."
        ],
        "july_22": [
            "🥵 Peak Summer Heat on July 22nd:\n- Temperature: 86-96°F (30-36°C)\n- One of the hottest days of the year is likely\n- Excessive heat warning possible.",
            "🔥 July 22nd Weather:\n- Temperature: 87-98°F (31-37°C)\n- Avoid strenuous activity and stay in the A/C."
        ],
        "july_23": [
            "⛈️ Heat-breaking Storms, July 23rd:\n- Temperature: 85-95°F (29-35°C)\n- Still very hot and humid, but with a chance of a late-day thunderstorm\n- Precipitation Chance: 40%",
            "🌩️ July 23rd Update:\n- Temperature: 86-96°F (30-36°C)\n- A storm could bring some brief relief."
        ],
        "july_24": [
            "☀️ Less Humid July 24th:\n- Temperature: 80-88°F (27-31°C)\n- Sunny and still hot, but the humidity will be noticeably lower\n- A much more comfortable day.",
            "😊 July 24th Forecast:\n- Temperature: 81-89°F (27-32°C)\n- Enjoy the break from the oppressive humidity."
        ],
        "july_25": [
            "☀️ Beautiful July 25th:\n- Temperature: 78-86°F (26-30°C)\n- Sunny and warm with low humidity\n- An absolutely perfect summer day.",
            "😎 July 25th Update:\n- Temperature: 79-87°F (26-31°C)\n- Get out and enjoy it!"
        ],
        "july_26": [
            "🌤️ Partly Sunny & Warm on July 26th:\n- Temperature: 80-89°F (27-32°C)\n- A mix of sun and clouds as heat and humidity build again\n- A great day for the lake.",
            "☀️ July 26th Forecast:\n- Temperature: 82-91°F (28-33°C)\n- A fine summer Friday."
        ],
        "july_27": [
            "⛈️ Weekend Storm Chance, July 27th:\n- Temperature: 83-92°F (28-33°C)\n- Hot and humid with a chance for an afternoon storm\n- Precipitation Chance: 30%",
            "🌩️ July 27th Weather:\n- Temperature: 84-93°F (29-34°C)\n- Most of the day will be dry and hot."
        ],
        "july_28": [
            "☀️ Hot & Sunny Sunday, July 28th:\n- Temperature: 85-94°F (29-34°C)\n- A very hot day with plenty of sunshine\n- The dog days of summer are here.",
            "🥵 July 28th Forecast:\n- Temperature: 86-95°F (30-35°C)\n- Stay cool and hydrated."
        ],
        "july_29": [
            "☁️ Cloudy but Steamy on July 29th:\n- Temperature: 84-92°F (29-33°C)\n- Overcast skies will do little to cut the humidity\n- A front approaches with rain for tomorrow.",
            "💧 July 29th Forecast:\n- Temperature: 85-93°F (29-34°C)\n- A very muggy and uncomfortable day."
        ],
        "july_30": [
            "🌧️ Rainy and Cooler July 30th:\n- Temperature: 77-85°F (25-29°C)\n- Periods of rain and thunderstorms will bring relief from the heat\n- Precipitation Chance: 60%",
            "☔ July 30th Weather:\n- Temperature: 76-84°F (24-29°C)\n- A wet but welcome change."
        ],
        "july_31": [
            "🌤️ Clearing Skies for July 31st:\n- Temperature: 78-86°F (26-30°C)\n- Lingering morning clouds, then a sunny and pleasant afternoon\n- A nice end to the month!",
            "😊 July 31st Forecast:\n- Temperature: 79-87°F (26-31°C)\n- Goodbye July, Hello August!"
        ],
        "august_1": [
            "☀️ Welcome to August 1st:\n- Temperature: 78-87°F (26-31°C)\n- Sunny and warm with comfortable humidity\n- A beautiful start to the month.",
            "😎 August 1st Forecast:\n- Temperature: 80-89°F (27-32°C)\n- Classic mid-summer weather."
        ],
        "august_2": [
            "☀️ Hot & Sunny August 2nd:\n- Temperature: 82-91°F (28-33°C)\n- The heat is on with abundant sunshine\n- A perfect day for the pool.",
            "🥵 August 2nd Weather:\n- Temperature: 84-93°F (29-34°C)\n- Make sure to use sunscreen!"
        ],
        "august_3": [
            "⛈️ Weekend Storm Threat, August 3rd:\n- Temperature: 83-92°F (28-33°C)\n- Hot and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ August 3rd Update:\n- Temperature: 85-94°F (29-34°C)\n- Keep an eye on the sky for your weekend plans."
        ],
        "august_4": [
            "🌦️ Unsettled Sunday, August 4th:\n- Temperature: 81-89°F (27-32°C)\n- Not as hot, but a lingering shower or storm is possible\n- A mix of sun and clouds.",
            "🌤️ August 4th Forecast:\n- Temperature: 82-90°F (28-32°C)\n- An okay day, but not perfect."
        ],
        "august_5": [
            "☀️ Beautiful August 5th:\n- Temperature: 79-87°F (26-31°C)\n- Sunny and warm with lower humidity\n- A gorgeous summer day.",
            "😊 August 5th Update:\n- Temperature: 80-88°F (27-31°C)\n- Enjoy this fantastic weather!"
        ],
        "august_6": [
            "🌤️ Partly Sunny & Warm, August 6th:\n- Temperature: 80-89°F (27-32°C)\n- A mix of sun and clouds, still very pleasant\n- A great day for being outdoors.",
            "☀️ August 6th Forecast:\n- Temperature: 82-90°F (28-32°C)\n- Another fine summer day."
        ],
        "august_7": [
            "🥵 Heat & Humidity Return on August 7th:\n- Temperature: 83-92°F (28-33°C)\n- A hazy, hot, and humid day is on tap\n- Stay cool!",
            "💧 August 7th Weather:\n- Temperature: 85-94°F (29-34°C)\n- The dog days of summer continue."
        ],
        "august_8": [
            "⛈️ Scattered Storms for August 8th:\n- Temperature: 84-93°F (29-34°C)\n- Hot and sticky with a chance of a pop-up thunderstorm\n- Precipitation Chance: 30%",
            "🌩️ August 8th Update:\n- Temperature: 86-95°F (30-35°C)\n- Any storm could produce a quick downpour."
        ],
        "august_9": [
            "☀️ Sunny & Oppressive August 9th:\n- Temperature: 87-97°F (31-36°C)\n- A dangerously hot day with tons of sun\n- Take heat precautions seriously.",
            "🔥 August 9th Forecast:\n- Temperature: 88-99°F (31-37°C)\n- An excessive heat warning is likely."
        ],
        "august_10": [
            "☁️ Cloudy but Steamy Saturday, August 10th:\n- Temperature: 85-94°F (29-34°C)\n- Clouds will do little to ease the oppressive heat and humidity\n- Relief is on the way tomorrow.",
            "🥵 August 10th Weather:\n- Temperature: 86-95°F (30-35°C)\n- A very uncomfortable day."
        ],
        "august_11": [
            "🌧️ Stormy Relief on August 11th:\n- Temperature: 78-86°F (26-30°C)\n- Showers and thunderstorms will bring an end to the heat wave\n- Precipitation Chance: 60%",
            "☔ August 11th Forecast:\n- Temperature: 77-85°F (25-29°C)\n- A wet but welcome change for the end of the weekend."
        ],
        "august_12": [
            "☀️ Spectacular August 12th:\n- Temperature: 76-84°F (24-29°C)\n- Sunny, dry, and wonderfully pleasant\n- A perfect summer day.",
            "😊 August 12th Update:\n- Temperature: 77-85°F (25-29°C)\n- A great start to the week!"
        ],
        "august_13": [
            "☀️ More Sunshine for August 13th:\n- Temperature: 77-86°F (25-30°C)\n- Another beautiful day with plenty of sun\n- Ideal summer weather continues.",
            "😎 August 13th Forecast:\n- Temperature: 78-87°F (26-31°C)\n- Enjoy it while it lasts."
        ],
        "august_14": [
            "🌤️ Warming Up on August 14th:\n- Temperature: 79-88°F (26-31°C)\n- Partly sunny as the heat starts to build again\n- A fine mid-week day.",
            "☀️ August 14th Forecast:\n- Temperature: 80-90°F (27-32°C)\n- Feeling more like typical August weather."
        ],
        "august_15": [
            "⛈️ Mid-August Storms:\n- Temperature: 81-90°F (27-32°C)\n- Hot and humid with a chance for afternoon storms\n- Precipitation Chance: 40%",
            "🌩️ August 15th Weather:\n- Temperature: 82-91°F (28-33°C)\n- Keep an eye out for changing weather."
        ],
        "august_16": [
            "🌦️ Unsettled Friday, August 16th:\n- Temperature: 80-88°F (27-31°C)\n- A lingering shower is possible, otherwise partly sunny\n- Still warm and a bit humid.",
            "🌤️ August 16th Forecast:\n- Temperature: 81-89°F (27-32°C)\n- An okay day to end the week."
        ],
        "august_17": [
            "☀️ Sunny Saturday, August 17th:\n- Temperature: 82-90°F (28-32°C)\n- A hot and sunny weekend day\n- Perfect for the beach or lake.",
            "😎 August 17th Forecast:\n- Temperature: 84-92°F (29-33°C)\n- Classic summer weekend weather."
        ],
        "august_18": [
            "☀️ More Sun & Heat for August 18th:\n- Temperature: 83-92°F (28-33°C)\n- Another hot one with abundant sunshine\n- Stay cool and hydrated.",
            "🥵 August 18th Forecast:\n- Temperature: 85-94°F (29-34°C)\n- The heat is relentless."
        ],
        "august_19": [
            "☁️ Cloudy & Muggy August 19th:\n- Temperature: 82-90°F (28-32°C)\n- Overcast skies and high humidity\n- Rain is on the way for tomorrow.",
            "💧 August 19th Forecast:\n- Temperature: 83-91°F (28-33°C)\n- An uncomfortable, sticky day."
        ],
        "august_20": [
            "🌧️ Rainy August 20th:\n- Temperature: 75-83°F (24-28°C)\n- Periods of rain will cool things down\n- Precipitation Chance: 70%",
            "☔ August 20th Weather:\n- Temperature: 74-82°F (23-28°C)\n- A good day to stay dry inside."
        ],
        "august_21": [
            "💨 Breezy and Fresher on August 21st:\n- Temperature: 74-82°F (23-28°C)\n- A noticeable breeze with a mix of sun and clouds\n- A much more comfortable feel to the air.",
            "🌬️ August 21st Forecast:\n- Temperature: 75-83°F (24-28°C)\n- A refreshing change."
        ],
        "august_22": [
            "☀️ Pleasant August 22nd:\n- Temperature: 76-85°F (24-29°C)\n- Sunny and warm, but not too humid\n- A beautiful late summer day.",
            "😊 August 22nd Update:\n- Temperature: 77-86°F (25-30°C)\n- Enjoy this delightful weather."
        ],
        "august_23": [
            "🌤️ Warming Trend for August 23rd:\n- Temperature: 78-87°F (26-31°C)\n- Partly sunny and getting warmer\n- A great day to kick off the weekend.",
            "☀️ August 23rd Forecast:\n- Temperature: 80-89°F (27-32°C)\n- Summer is still going strong."
        ],
        "august_24": [
            "⛈️ Weekend Storms Possible, August 24th:\n- Temperature: 80-89°F (27-32°C)\n- Hot and humid with a chance of afternoon thunderstorms\n- Precipitation Chance: 40%",
            "🌩️ August 24th Weather:\n- Temperature: 82-91°F (28-33°C)\n- Have a backup plan for your Saturday."
        ],
        "august_25": [
            "☀️ Sunny Sunday, August 25th:\n- Temperature: 81-90°F (27-32°C)\n- A hot and sunny day to end the weekend\n- Great for one last big summer BBQ.",
            "😎 August 25th Forecast:\n- Temperature: 83-92°F (28-33°C)\n- Enjoy the heat and sun."
        ],
        "august_26": [
            "🥵 Hazy, Hot, and Humid August 26th:\n- Temperature: 84-93°F (29-34°C)\n- The classic 'dog days' of summer continue\n- Take it easy outdoors.",
            "💧 August 26th Weather:\n- Temperature: 85-94°F (29-34°C)\n- Stay hydrated and find some shade."
        ],
        "august_27": [
            "☁️ Cloudy but Oppressive August 27th:\n- Temperature: 83-91°F (28-33°C)\n- Gray skies will trap the heat and humidity\n- Relief is a day away.",
            "🥵 August 27th Forecast:\n- Temperature: 84-92°F (29-33°C)\n- An uncomfortable day."
        ],
        "august_28": [
            "🌧️ Stormy Mid-week for August 28th:\n- Temperature: 77-85°F (25-29°C)\n- Scattered showers and thunderstorms likely\n- Precipitation Chance: 50%\n- A break in the intense heat.",
            "☔ August 28th Weather:\n- Temperature: 76-84°F (24-29°C)\n- A wet and unsettled day."
        ],
        "august_29": [
            "☀️ Beautiful August 29th:\n- Temperature: 75-83°F (24-28°C)\n- Sunny, dry, and much less humid\n- A hint of autumn in the air?",
            "😊 August 29th Update:\n- Temperature: 76-84°F (24-29°C)\n- A spectacular late summer day."
        ],
        "august_30": [
            "☀️ Gorgeous Friday, August 30th:\n- Temperature: 76-85°F (24-29°C)\n- Sunny and warm, perfect for end-of-summer plans\n- Enjoy the long weekend weather.",
            "😎 August 30th Forecast:\n- Temperature: 78-87°F (26-31°C)\n- A fantastic day."
        ],
        "august_31": [
            "🌤️ Partly Sunny and Warm August 31st:\n- Temperature: 77-86°F (25-30°C)\n- A mix of sun and clouds to end the month\n- A great day for a final summer trip.",
            "☀️ August 31st Forecast:\n- Temperature: 79-88°F (26-31°C)\n- Farewell August, hello September!"
        ],
        "september_1": [
            "🍂 Welcome to September 1st:\n- Temperature: 75-84°F (24-29°C)\n- Mostly sunny and warm, a gentle start to the month\n- Low chance of rain.",
            "☀️ September 1st Forecast:\n- Temperature: 76-85°F (24-29°C)\n- Still feels like summer, but with a hint of fall."
        ],
        "september_2": [
            "☀️ Labor Day Forecast:\n- Temperature: 76-86°F (24-30°C)\n- Sunny and warm, a perfect day for the last big BBQ of summer\n- Enjoy the holiday!",
            "😎 September 2nd Weather:\n- Temperature: 78-88°F (26-31°C)\n- A beautiful end to the unofficial summer season."
        ],
        "september_3": [
            "🌤️ Partly Sunny September 3rd:\n- Temperature: 74-83°F (23-28°C)\n- A mix of sun and clouds, still very pleasant\n- A great day to ease back into routine.",
            "😊 September 3rd Update:\n- Temperature: 75-84°F (24-29°C)\n- Comfortable early fall weather."
        ],
        "september_4": [
            "☁️ Cloudy but Warm September 4th:\n- Temperature: 73-82°F (23-28°C)\n- Overcast skies but temperatures remain warm\n- Rain is on the way for tomorrow.",
            "🧥 September 4th Forecast:\n- Temperature: 74-83°F (23-28°C)\n- Enjoy the dry conditions while they last."
        ],
        "september_5": [
            "🌧️ Rainy September 5th:\n- Temperature: 68-76°F (20-24°C)\n- Cooler with periods of rain\n- Precipitation Chance: 60%\n- A more autumnal feel today.",
            "☔ September 5th Weather:\n- Temperature: 67-75°F (19-24°C)\n- A damp and grey day."
        ],
        "september_6": [
            "💨 Breezy and Cooler on September 6th:\n- Temperature: 66-74°F (19-23°C)\n- Windy with a mix of sun and clouds\n- A noticeable freshness in the air.",
            "🌬️ September 6th Forecast:\n- Temperature: 65-73°F (18-23°C)\n- A blustery end to the week."
        ],
        "september_7": [
            "☀️ Sunny and Crisp Saturday, September 7th:\n- Temperature: 67-77°F (19-25°C)\n- A beautiful, sunny day with low humidity\n- Perfect for apple picking or a football game.",
            "🍂 September 7th Update:\n- Temperature: 68-78°F (20-26°C)\n- A gorgeous early fall day."
        ],
        "september_8": [
            "☀️ More Sunshine for September 8th:\n- Temperature: 69-79°F (21-26°C)\n- Another lovely day with plenty of sun\n- A great end to the weekend.",
            "😊 September 8th Forecast:\n- Temperature: 70-80°F (21-27°C)\n- Enjoy this fantastic weather."
        ],
        "september_9": [
            "🌤️ Warming Up on September 9th:\n- Temperature: 72-82°F (22-28°C)\n- Partly sunny and feeling more like summer again\n- A warm start to the week.",
            "☀️ September 9th Forecast:\n- Temperature: 74-84°F (23-29°C)\n- Summer's last stand?"
        ],
        "september_10": [
            "⛈️ Pop-up Storm Chance, September 10th:\n- Temperature: 75-85°F (24-29°C)\n- Warm and humid with a chance of a late day storm\n- Precipitation Chance: 30%",
            "🌩️ September 10th Weather:\n- Temperature: 76-86°F (24-30°C)\n- Most of the day will be fine."
        ],
        "september_11": [
            "☁️ Somber & Cloudy September 11th:\n- Temperature: 73-81°F (23-27°C)\n- A day of reflection under cloudy skies\n- Staying warm and a bit humid.",
            " memorials.\n- September 11th Forecast:\n- Temperature: 74-82°F (23-28°C)\n- Quiet weather for a day of remembrance."
        ],
        "september_12": [
            "🌧️ Rainy and Cooler September 12th:\n- Temperature: 68-75°F (20-24°C)\n- A front brings needed rain and cooler temps\n- Precipitation Chance: 70%",
            "☔ September 12th Weather:\n- Temperature: 67-74°F (19-23°C)\n- A wet day is in store."
        ],
        "september_13": [
            "☀️ Sunny Friday the 13th:\n- Temperature: 66-76°F (19-24°C)\n- Nothing spooky here! A beautiful, sunny, and pleasant day.\n- Perfect fall weather.",
            "🍂 September 13th Update:\n- Temperature: 68-78°F (20-26°C)\n- A spectacular end to the week."
        ],
        "september_14": [
            "☀️ Gorgeous Saturday for September 14th:\n- Temperature: 69-79°F (21-26°C)\n- Sunny and warm, ideal for any outdoor activity\n- Get out and enjoy it!",
            "😊 September 14th Forecast:\n- Temperature: 70-80°F (21-27°C)\n- Perfect fall festival weather."
        ],
        "september_15": [
            "🌤️ Partly Sunny & Warm on September 15th:\n- Temperature: 72-82°F (22-28°C)\n- A mix of sun and clouds, feeling warm\n- A great day, but change is coming.",
            "☀️ September 15th Weather:\n- Temperature: 74-84°F (23-29°C)\n- Enjoy the summer-like warmth."
        ],
        "september_16": [
            "💨 Windy and Cooler September 16th:\n- Temperature: 65-73°F (18-23°C)\n- A strong cold front moves through, bringing wind and much cooler air\n- A chance of a shower early.",
            "🌬️ September 16th Forecast:\n- Temperature: 64-72°F (18-22°C)\n- A blustery, autumnal day."
        ],
        "september_17": [
            "☀️ Cool and Sunny September 17th:\n- Temperature: 60-70°F (16-21°C)\n- A crisp, sunny day, definitely feels like fall\n- A light jacket will be needed.",
            "🍂 September 17th Update:\n- Temperature: 62-72°F (17-22°C)\n- The perfect day for a pumpkin spice latte."
        ],
        "september_18": [
            "☁️ Cloudy and Chilly September 18th:\n- Temperature: 58-66°F (14-19°C)\n- Overcast skies and cool temperatures\n- A raw, grey day.",
            "🧥 September 18th Forecast:\n- Temperature: 57-65°F (14-18°C)\n- Sweater weather is here."
        ],
        "september_19": [
            "🌧️ Dreary Rain for September 19th:\n- Temperature: 59-67°F (15-19°C)\n- A cool, steady rain is expected for much of the day\n- Precipitation Chance: 80%",
            "☔ September 19th Weather:\n- Temperature: 60-68°F (16-20°C)\n- A good day to stay inside."
        ],
        "september_20": [
            "🌦️ Lingering Showers on September 20th:\n- Temperature: 62-70°F (17-21°C)\n- On-and-off showers with some peeks of sun\n- A slow clearing process.",
            "🌤️ September 20th Forecast:\n- Temperature: 63-71°F (17-22°C)\n- A brighter afternoon is possible."
        ],
        "september_21": [
            "☀️ Sunny Saturday, September 21st:\n- Temperature: 65-75°F (18-24°C)\n- A beautiful, sunny, and pleasant weekend day\n- Great for all your fall activities.",
            "😊 September 21st Update:\n- Temperature: 66-76°F (19-24°C)\n- Enjoy this spectacular weather."
        ],
        "september_22": [
            "🍂 First Day of Autumn Forecast:\n- Temperature: 67-77°F (19-25°C)\n- A perfect day to welcome the new season!\n- Sunny and pleasantly warm.",
            "🍁 September 22nd Weather:\n- Temperature: 68-78°F (20-26°C)\n- Enjoy the beautiful fall equinox."
        ],
        "september_23": [
            "☁️ Clouds Increase on September 23rd:\n- Temperature: 66-75°F (19-24°C)\n- A mild day, but clouds will be on the increase\n- Next system is approaching.",
            "🧥 September 23rd Forecast:\n- Temperature: 67-76°F (19-24°C)\n- Enjoy the dry weather while it lasts."
        ],
        "september_24": [
            "🌧️ Rainy September 24th:\n- Temperature: 63-70°F (17-21°C)\n- A cool and rainy day is expected\n- Precipitation Chance: 70%",
            "☔ September 24th Weather:\n- Temperature: 62-69°F (17-21°C)\n- Don't forget the rain gear."
        ],
        "september_25": [
            "💨 Breezy and Raw on September 25th:\n- Temperature: 60-68°F (16-20°C)\n- Windy with lingering clouds and drizzle\n- A very chilly day for late September.",
            "🌬️ September 25th Forecast:\n- Temperature: 59-67°F (15-19°C)\n- A raw, unpleasant day."
        ],
        "september_26": [
            "☀️ Sunny but Cool September 26th:\n- Temperature: 61-71°F (16-22°C)\n- A sunny day, but the air remains crisp and cool\n- A nice autumn day.",
            "🍂 September 26th Update:\n- Temperature: 62-72°F (17-22°C)\n- The sun feels nice, but you'll need a jacket."
        ],
        "september_27": [
            "☀️ Gorgeous Friday for September 27th:\n- Temperature: 64-74°F (18-23°C)\n- Sunny and a bit warmer, a perfect fall day\n- A great way to end the week.",
            "😊 September 27th Forecast:\n- Temperature: 65-75°F (18-24°C)\n- Get out and enjoy the fall foliage."
        ],
        "september_28": [
            "🌤️ Partly Sunny Saturday, September 28th:\n- Temperature: 66-76°F (19-24°C)\n- A mix of sun and clouds, very pleasant\n- Great for a trip to the pumpkin patch.",
            "🍁 September 28th Weather:\n- Temperature: 68-78°F (20-26°C)\n- A beautiful fall weekend day."
        ],
        "september_29": [
            "☁️ Cloudy Sunday on September 29th:\n- Temperature: 65-74°F (18-23°C)\n- Overcast skies move in, but it remains mild\n- Rain holds off until overnight.",
            "🧥 September 29th Forecast:\n- Temperature: 66-75°F (19-24°C)\n- A good day for a drive to see the leaves."
        ],
        "september_30": [
            "🌧️ Rainy End to September 30th:\n- Temperature: 62-69°F (17-21°C)\n- A cool, rainy day to end the month\n- Precipitation Chance: 60%\n- Hello October!",
            "☔ September 30th Weather:\n- Temperature: 61-68°F (16-20°C)\n- A grey and damp farewell to September."
        ],
        "october_1": [
            "🎃 Welcome to October 1st:\n- Temperature: 58-68°F (14-20°C)\n- Lingering morning clouds, then afternoon sun\n- Cool and crisp autumn air.",
            "🍂 October 1st Forecast:\n- Temperature: 60-70°F (16-21°C)\n- A classic start to the spookiest month."
        ],
        "october_2": [
            "☀️ Sunny and Pleasant October 2nd:\n- Temperature: 60-72°F (16-22°C)\n- A beautiful, sunny fall day\n- Perfect for a hayride.",
            "😊 October 2nd Update:\n- Temperature: 62-74°F (17-23°C)\n- Enjoy this gorgeous autumn weather."
        ],
        "october_3": [
            "🌤️ Partly Sunny and Mild, October 3rd:\n- Temperature: 63-75°F (17-24°C)\n- A mix of sun and clouds, unseasonably warm\n- A taste of 'Indian Summer'.",
            "☀️ October 3rd Forecast:\n- Temperature: 65-77°F (18-25°C)\n- Enjoy the warmth!"
        ],
        "october_4": [
            "☁️ Cloudy but Warm October 4th:\n- Temperature: 64-76°F (18-24°C)\n- Overcast skies, but temperatures remain very mild\n- Change is coming tomorrow.",
            "🧥 October 4th Forecast:\n- Temperature: 66-78°F (19-26°C)\n- Enjoy the last of the warmth."
        ],
        "october_5": [
            "🌧️ Rainy and Cooler Saturday, October 5th:\n- Temperature: 55-63°F (13-17°C)\n- A significant cool down with periods of rain\n- Precipitation Chance: 70%",
            "☔ October 5th Weather:\n- Temperature: 54-62°F (12-17°C)\n- A wet and chilly weekend day."
        ],
        "october_6": [
            "💨 Windy and Chilly October 6th:\n- Temperature: 50-58°F (10-14°C)\n- A blustery day with a mix of sun and clouds\n- Definitely feels like fall has arrived.",
            "🌬️ October 6th Forecast:\n- Temperature: 48-56°F (9-13°C)\n- Bundle up, it's a cold one."
        ],
        "october_7": [
            "☀️ Sunny but Cold October 7th:\n- Temperature: 45-57°F (7-14°C)\n- A frosty start, then a sunny but very cool day\n- The leaves are at their peak color!",
            "🍁 October 7th Update:\n- Temperature: 46-58°F (8-14°C)\n- A beautiful, crisp autumn day."
        ],
        "october_8": [
            "☁️ Cloudy and Cool October 8th:\n- Temperature: 48-59°F (9-15°C)\n- Overcast skies and continued cool temperatures\n- A typical grey October day.",
            "🧥 October 8th Forecast:\n- Temperature: 47-58°F (8-14°C)\n- Sweater and jacket weather."
        ],
        "october_9": [
            "☀️ Moderating Temps for October 9th:\n- Temperature: 52-65°F (11-18°C)\n- Sunny skies and a return to more pleasant temperatures\n- A nice mid-week rebound.",
            "😊 October 9th Update:\n- Temperature: 54-67°F (12-19°C)\n- Enjoy the comfortable conditions."
        ],
        "october_10": [
            "🌤️ Partly Sunny and Mild, October 10th:\n- Temperature: 55-68°F (13-20°C)\n- A mix of sun and clouds, a very nice day\n- Perfect for a walk.",
            "🍂 October 10th Forecast:\n- Temperature: 56-70°F (13-21°C)\n- Another beautiful fall day."
        ],
        "october_11": [
            "🌧️ Rainy Friday for October 11th:\n- Temperature: 58-66°F (14-19°C)\n- Rain developing and becoming steady\n- Precipitation Chance: 80%\n- A wet end to the work week.",
            "☔ October 11th Weather:\n- Temperature: 57-65°F (14-18°C)\n- Grab the umbrella and rain boots."
        ],
        "october_12": [
            "🌦️ Lingering Showers on October 12th:\n- Temperature: 56-64°F (13-18°C)\n- Scattered showers, especially in the morning\n- Some sun may appear in the afternoon.",
            "🌤️ October 12th Forecast:\n- Temperature: 57-65°F (14-18°C)\n- An unsettled but mild day."
        ],
        "october_13": [
            "☀️ Sunny and Beautiful Sunday, October 13th:\n- Temperature: 58-69°F (14-21°C)\n- A spectacular autumn day with plenty of sun\n- Perfect for a fall festival.",
            "🍁 October 13th Update:\n- Temperature: 60-71°F (16-22°C)\n- Get out and enjoy this gorgeous weather."
        ],
        "october_14": [
            "💨 Breezy and Cooler October 14th:\n- Temperature: 54-62°F (12-17°C)\n- A windy day with a mix of sun and clouds\n- A noticeable chill returns to the air.",
            "🌬️ October 14th Forecast:\n- Temperature: 52-60°F (11-16°C)\n- A blustery, cool day."
        ],
        "october_15": [
            "☀️ Sunny and Crisp October 15th:\n- Temperature: 50-61°F (10-16°C)\n- A beautiful, sunny day, but you'll need a jacket\n- Classic mid-October weather.",
            "🍂 October 15th Update:\n- Temperature: 51-62°F (11-17°C)\n- Enjoy the bright autumn sunshine."
        ],
        "october_16": [
            "☁️ Cloudy and Chilly October 16th:\n- Temperature: 49-58°F (9-14°C)\n- Overcast skies and cool temps all day\n- A good day for a hot cider.",
            "🧥 October 16th Forecast:\n- Temperature: 48-57°F (9-14°C)\n- A grey and brisk day."
        ],
        "october_17": [
            "🌧️ Dreary Rain for October 17th:\n- Temperature: 47-55°F (8-13°C)\n- A cold, steady rain is on tap\n- Precipitation Chance: 70%\n- Definitely an indoor day.",
            "☔ October 17th Weather:\n- Temperature: 46-54°F (8-12°C)\n- A raw and unpleasant day."
        ],
        "october_18": [
            "💨 Windy and Raw October 18th:\n- Temperature: 45-53°F (7-12°C)\n- A very cold day for October with gusty winds and lingering drizzle\n- Feels more like November.",
            "🥶 October 18th Forecast:\n- Temperature: 44-52°F (7-11°C)\n- Bundle up, it's a harsh one."
        ],
        "october_19": [
            "☀️ Sunny but Frigid Saturday, October 19th:\n- Temperature: 42-55°F (6-13°C)\n- A frosty start followed by a sunny but very cold day\n- Hard freeze possible overnight.",
            "🍁 October 19th Update:\n- Temperature: 43-56°F (6-13°C)\n- Don't be fooled by the sun, it is cold!"
        ],
        "october_20": [
            "☀️ Sunny and Milder Sunday, October 20th:\n- Temperature: 48-62°F (9-17°C)\n- A beautiful, sunny day with a nice rebound in temps\n- A great day to be outside.",
            "😊 October 20th Forecast:\n- Temperature: 50-64°F (10-18°C)\n- A perfect fall day."
        ],
        "october_21": [
            "🌤️ Partly Sunny and Pleasant, October 21st:\n- Temperature: 52-66°F (11-19°C)\n- A mix of sun and clouds, staying mild\n- A great start to the week.",
            "🍂 October 21st Update:\n- Temperature: 54-68°F (12-20°C)\n- Very comfortable for this time of year."
        ],
        "october_22": [
            "☁️ Cloudy and Mild October 22nd:\n- Temperature: 55-65°F (13-18°C)\n- Overcast skies but temperatures remain pleasant\n- Rain moves in late.",
            "🧥 October 22nd Forecast:\n- Temperature: 56-66°F (13-19°C)\n- Enjoy the mild air before the rain."
        ],
        "october_23": [
            "🌧️ Rainy October 23rd:\n- Temperature: 54-61°F (12-16°C)\n- A rainy and mild day\n- Precipitation Chance: 80%\n- A good day for indoor projects.",
            "☔ October 23rd Weather:\n- Temperature: 53-60°F (12-16°C)\n- Periods of rain throughout the day."
        ],
        "october_24": [
            "🌦️ Lingering Showers for October 24th:\n- Temperature: 56-64°F (13-18°C)\n- On-and-off showers with a few breaks of sun\n- Still on the mild side.",
            "🌤️ October 24th Forecast:\n- Temperature: 57-65°F (14-18°C)\n- An unsettled but not unpleasant day."
        ],
        "october_25": [
            "☀️ Sunny Friday for October 25th:\n- Temperature: 55-67°F (13-19°C)\n- A beautiful, sunny, and mild end to the week\n- Perfect for after-work plans.",
            "😊 October 25th Forecast:\n- Temperature: 56-68°F (13-20°C)\n- Enjoy the gorgeous fall weather."
        ],
        "october_26": [
            "🎃 Pre-Halloween Weekend, October 26th:\n- Temperature: 57-69°F (14-21°C)\n- Partly sunny and unseasonably warm\n- Great for pumpkin carving and parties.",
            "🍁 October 26th Weather:\n- Temperature: 58-70°F (14-21°C)\n- A spectacular fall day."
        ],
        "october_27": [
            "💨 Windy and Cooler Sunday, October 27th:\n- Temperature: 50-60°F (10-16°C)\n- A front moves through, bringing wind and cooler air\n- A mix of sun and clouds.",
            "🌬️ October 27th Forecast:\n- Temperature: 48-58°F (9-14°C)\n- A blustery end to the weekend."
        ],
        "october_28": [
            "☀️ Sunny and Cool October 28th:\n- Temperature: 46-57°F (8-14°C)\n- A sunny but crisp day\n- Getting into the Halloween spirit.",
            "🍂 October 28th Update:\n- Temperature: 47-58°F (8-14°C)\n- A classic late October day."
        ],
        "october_29": [
            "☁️ Cloudy and Chilly October 29th:\n- Temperature: 45-54°F (7-12°C)\n- Overcast skies and a brisk chill\n- Feels like Halloween is near.",
            "🧥 October 29th Forecast:\n- Temperature: 44-53°F (7-12°C)\n- A grey and cool day."
        ],
        "october_30": [
            "🌧️ Rainy October 30th:\n- Temperature: 43-51°F (6-11°C)\n- A cold rain for Mischief Night\n- Precipitation Chance: 60%\n- A dreary day before the big one.",
            "☔ October 30th Weather:\n- Temperature: 42-50°F (6-10°C)\n- A raw and wet day."
        ],
        "october_31": [
            "👻 Halloween Forecast:\n- Temperature: 45-55°F (7-13°C)\n- Clearing skies but cool for trick-or-treating\n- Precipitation Chance: 20%\n- A classic, spooky evening!",
            "🎃 October 31st Weather:\n- Temperature: 46-56°F (8-13°C)\n- Dry but chilly for the evening's festivities.\n- Make sure costumes have layers!"
        ],
        "november_1": [
            "🍂 Welcome to November 1st:\n- Temperature: 44-54°F (7-12°C)\n- A mix of sun and clouds, cool and crisp\n- The slide towards winter begins.",
            "🌬️ November 1st Forecast:\n- Temperature: 42-52°F (6-11°C)\n- A brisk start to the new month."
        ],
        "november_2": [
            "☀️ Sunny and Chilly Saturday, November 2nd:\n- Temperature: 45-56°F (7-13°C)\n- A beautiful, sunny day, but with a definite chill\n- Great for a hike to see the last of the leaves.",
            "🍁 November 2nd Update:\n- Temperature: 46-57°F (8-14°C)\n- Enjoy the autumn sunshine."
        ],
        "november_3": [
            "☁️ Cloudy and Cool Sunday, November 3rd:\n- Temperature: 46-55°F (8-13°C)\n- Overcast skies return, staying cool\n- Don't forget to 'fall back' your clocks!",
            "🧥 November 3rd Forecast:\n- Temperature: 45-54°F (7-12°C)\n- A grey end to the weekend."
        ],
        "november_4": [
            "🌧️ Rainy November 4th:\n- Temperature: 48-56°F (9-13°C)\n- Periods of rain, mild for the time of year\n- Precipitation Chance: 70%",
            "☔ November 4th Weather:\n- Temperature: 47-55°F (8-13°C)\n- A damp and dreary day."
        ],
        "november_5": [
            "💨 Windy and Colder November 5th:\n- Temperature: 40-48°F (4-9°C)\n- A blustery day with clearing skies but falling temps\n- First flakes of the season possible at night?",
            "🥶 November 5th Forecast:\n- Temperature: 38-46°F (3-8°C)\n- A raw, cold day."
        ],
        "november_6": [
            "☀️ Sunny but Frigid November 6th:\n- Temperature: 35-45°F (2-7°C)\n- A very cold day, especially for early November\n- A hard freeze is likely overnight.",
            "🧣 November 6th Update:\n- Temperature: 34-44°F (1-7°C)\n- Break out the winter coats."
        ],
        "november_7": [
            "☁️ Cloudy and Cold November 7th:\n- Temperature: 37-46°F (3-8°C)\n- Overcast and staying cold\n- Feels like winter is here.",
            "🧤 November 7th Forecast:\n- Temperature: 36-45°F (2-7°C)\n- A grey and brisk day."
        ],
        "november_8": [
            "☀️ Milder Temps Return on November 8th:\n- Temperature: 42-55°F (6-13°C)\n- Sunny skies and a pleasant rebound in temperatures\n- A nice end to the work week.",
            "😊 November 8th Update:\n- Temperature: 44-57°F (7-14°C)\n- Enjoy this break from the cold."
        ],
        "november_9": [
            "🌤️ Partly Sunny and Mild, November 9th:\n- Temperature: 45-58°F (7-14°C)\n- A mix of sun and clouds, a very nice day\n- Great for getting yard work done.",
            "🍂 November 9th Forecast:\n- Temperature: 46-59°F (8-15°C)\n- A beautiful autumn day."
        ],
        "november_10": [
            "🌧️ Rainy Sunday for November 10th:\n- Temperature: 48-57°F (9-14°C)\n- Rain developing during the day\n- Precipitation Chance: 60%\n- A wet end to a nice weekend.",
            "☔ November 10th Weather:\n- Temperature: 49-58°F (9-14°C)\n- Grab the umbrella."
        ],
        "november_11": [
            "🇺🇸 Veterans Day Forecast:\n- Temperature: 44-52°F (7-11°C)\n- Lingering showers in the morning, then breezy and cool\n- A somber day to honor our veterans.",
            "🌬️ November 11th Weather:\n- Temperature: 42-50°F (6-10°C)\n- A mix of sun and clouds in the afternoon."
        ],
        "november_12": [
            "☀️ Sunny and Brisk November 12th:\n- Temperature: 40-50°F (4-10°C)\n- A sunny day, but a sharp chill in the air\n- Classic mid-November weather.",
            "🧣 November 12th Update:\n- Temperature: 38-48°F (3-9°C)\n- Enjoy the sun, but bundle up."
        ],
        "november_13": [
            "☁️ Cloudy and Cold November 13th:\n- Temperature: 39-47°F (4-8°C)\n- Overcast skies and cold temperatures persist\n- A good day for a warm drink.",
            "☕ November 13th Forecast:\n- Temperature: 38-46°F (3-8°C)\n- A grey and chilly day."
        ],
        "november_14": [
            "❄️ First Flakes for November 14th?:\n- Temperature: 35-42°F (2-6°C)\n- Rain mixing with or changing to wet snow is possible\n- Precipitation Chance: 40%\n- Winter is knocking.",
            "🌨️ November 14th Weather:\n- Temperature: 34-41°F (1-5°C)\n- A cold, damp day with a chance of snowflakes."
        ],
        "november_15": [
            "💨 Blustery and Frigid November 15th:\n- Temperature: 32-40°F (0-4°C)\n- Very windy and cold with some sun\n- Wind chills will be in the 20s (-6 to -1°C).",
            "🥶 November 15th Forecast:\n- Temperature: 30-38°F (-1-3°C)\n- A harsh, winter-like day."
        ],
        "november_16": [
            "☀️ Sunny but Cold Saturday, November 16th:\n- Temperature: 34-45°F (1-7°C)\n- After a very cold start, a sunny but chilly day\n- The sun has little warmth.",
            "🧤 November 16th Update:\n- Temperature: 33-44°F (1-7°C)\n- A good day to stay active to keep warm."
        ],
        "november_17": [
            "🌤️ Partly Sunny, Still Cold, November 17th:\n- Temperature: 36-47°F (2-8°C)\n- A mix of sun and clouds, temperatures remain below average\n- A quiet, cold Sunday.",
            "🧣 November 17th Forecast:\n- Temperature: 35-46°F (2-8°C)\n- Another day for the winter gear."
        ],
        "november_18": [
            "☁️ Cloudy and Raw November 18th:\n- Temperature: 38-46°F (3-8°C)\n- Overcast skies and a persistent chill\n- Feels like the holidays are near.",
            "🧥 November 18th Forecast:\n- Temperature: 37-45°F (3-7°C)\n- A classic grey November day."
        ],
        "november_19": [
            "🌧️ Rainy and Mild November 19th:\n- Temperature: 45-55°F (7-13°C)\n- A surge of milder air brings rain instead of snow\n- Precipitation Chance: 80%",
            "☔ November 19th Weather:\n- Temperature: 46-56°F (8-13°C)\n- A wet and dreary day."
        ],
        "november_20": [
            "🌦️ Lingering Showers on November 20th:\n- Temperature: 48-58°F (9-14°C)\n- On-and-off showers with some sun breaking through\n- Staying unseasonably mild.",
            "🌤️ November 20th Forecast:\n- Temperature: 50-60°F (10-16°C)\n- A brighter and warmer afternoon."
        ],
        "november_21": [
            "☀️ Beautiful November 21st:\n- Temperature: 47-59°F (8-15°C)\n- A stunning, sunny, and mild late fall day\n- Enjoy this beautiful weather!",
            "😊 November 21st Update:\n- Temperature: 48-60°F (9-16°C)\n- A great day to get a jump on holiday shopping."
        ],
        "november_22": [
            "💨 Colder and Windy Friday, November 22nd:\n- Temperature: 40-49°F (4-9°C)\n- A front passes, bringing much colder air and gusty winds\n- A mix of sun and clouds.",
            "🌬️ November 22nd Forecast:\n- Temperature: 38-47°F (3-8°C)\n- A harsh change from yesterday."
        ],
        "november_23": [
            "☀️ Sunny but Cold Saturday, November 23rd:\n- Temperature: 36-45°F (2-7°C)\n- A bright, sunny day, but cold from start to finish\n- Good for a brisk walk.",
            "🧣 November 23rd Update:\n- Temperature: 35-44°F (2-7°C)\n- Bundle up if you're heading out."
        ],
        "november_24": [
            "☁️ Clouds Increase on Sunday, November 24th:\n- Temperature: 38-46°F (3-8°C)\n- Becoming cloudy and staying cold\n- Snow is on the way for the travel week.",
            "❄️ November 24th Forecast:\n- Temperature: 37-45°F (3-7°C)\n- Overcast by evening, with a wintry feel."
        ],
        "november_25": [
            "🌨️ Pre-Thanksgiving Snow, November 25th:\n- Temperature: 33-39°F (1-4°C)\n- Light snow developing, making roads slick\n- Precipitation Chance: 60%\n- A messy start to the holiday week.",
            "❄️ November 25th Weather:\n- Temperature: 32-38°F (0-3°C)\n- Accumulation of 1-2 inches possible."
        ],
        "november_26": [
            "🌬️ Blustery and Cold November 26th:\n- Temperature: 30-38°F (-1-3°C)\n- Windy with leftover flurries\n- A very cold day for travel.",
            "🥶 November 26th Forecast:\n- Temperature: 28-36°F (-2-2°C)\n- Wind chills will be brutal."
        ],
        "november_27": [
            "☀️ Sunny but Frigid Travel Day, November 27th:\n- Temperature: 28-37°F (-2-3°C)\n- A sunny day, but very cold for one of the busiest travel days\n- Roads should be dry.",
            "🚗 November 27th Update:\n- Temperature: 29-38°F (-2-3°C)\n- Bundle up for your holiday travels."
        ],
        "november_28": [
            "🦃 Thanksgiving Day Forecast:\n- Temperature: 32-42°F (0-6°C)\n- A mix of sun and clouds, chilly but dry\n- Perfect weather for staying inside and cooking!",
            "🍂 November 28th Weather:\n- Temperature: 34-44°F (1-7°C)\n- A classic, crisp Thanksgiving day."
        ],
        "november_29": [
            "🛍️ Black Friday Forecast:\n- Temperature: 35-45°F (2-7°C)\n- Cloudy and cool, good weather for shopping\n- A chance of a light shower.",
            "🧥 November 29th Weather:\n- Temperature: 36-46°F (2-8°C)\n- Stay warm while you hunt for deals."
        ],
        "november_30": [
            "🌧️ Rainy End to November 30th:\n- Temperature: 40-48°F (4-9°C)\n- A chilly rain to end the month\n- Precipitation Chance: 50%\n- Goodbye November!",
            "☔ November 30th Weather:\n- Temperature: 39-47°F (4-8°C)\n- A damp and grey Saturday."
        ],
        "december_1": [
            "🎄 Welcome to December 1st:\n- Temperature: 38-46°F (3-8°C)\n- Lingering morning clouds, then some afternoon sun\n- Cool and festive.",
            "🧣 December 1st Forecast:\n- Temperature: 37-45°F (3-7°C)\n- The holiday season is officially here!"
        ],
        "december_2": [
            "☀️ Sunny and Brisk December 2nd:\n- Temperature: 35-44°F (2-7°C)\n- A sunny but chilly day\n- Perfect for putting up outdoor decorations.",
            "🧤 December 2nd Update:\n- Temperature: 34-43°F (1-6°C)\n- Enjoy the winter sunshine."
        ],
        "december_3": [
            "☁️ Cloudy and Cold December 3rd:\n- Temperature: 36-43°F (2-6°C)\n- Overcast skies return, staying cold\n- Feels like snow is in the air.",
            "🧥 December 3rd Forecast:\n- Temperature: 35-42°F (2-6°C)\n- A grey and wintery day."
        ],
        "december_4": [
            "❄️ December 4th Snow Showers:\n- Temperature: 32-38°F (0-3°C)\n- Cloudy with periods of light snow or flurries\n- Precipitation Chance: 50%",
            "🌨️ December 4th Weather:\n- Temperature: 31-37°F (0-3°C)\n- A coating to an inch of snow is possible."
        ],
        "december_5": [
            "🌬️ Blustery and Frigid December 5th:\n- Temperature: 28-36°F (-2-2°C)\n- Windy with leftover flurries and some sun\n- A very cold, harsh day.",
            "🥶 December 5th Forecast:\n- Temperature: 26-34°F (-3-1°C)\n- Wind chills will be in the teens (-10 to -5°C)."
        ],
        "december_6": [
            "☀️ Sunny but Bitterly Cold December 6th:\n- Temperature: 25-35°F (-4-2°C)\n- Abundant sunshine will do little to warm things up\n- A frigid day.",
            "🧤 December 6th Update:\n- Temperature: 24-34°F (-4-1°C)\n- Bundle up from head to toe."
        ],
        "december_7": [
            "☁️ Clouds Increase, Still Cold on December 7th:\n- Temperature: 28-37°F (-2-3°C)\n- Becoming cloudy and remaining cold\n- Next system approaches.",
            "🧣 December 7th Forecast:\n- Temperature: 27-36°F (-3-2°C)\n- Overcast by evening."
        ],
        "december_8": [
            "🌨️ Wintry Mix for Sunday, December 8th:\n- Temperature: 33-40°F (1-4°C)\n- Snow changing to a messy mix of sleet and rain\n- Precipitation Chance: 70%",
            "🧊 December 8th Weather:\n- Temperature: 34-41°F (1-5°C)\n- Travel could be tricky."
        ],
        "december_9": [
            "🌧️ Rainy and Mild December 9th:\n- Temperature: 40-48°F (4-9°C)\n- Rain showers and unseasonably mild temperatures\n- All snow will melt.",
            "☔ December 9th Forecast:\n- Temperature: 42-50°F (6-10°C)\n- A damp and dreary Monday."
        ],
        "december_10": [
            "💨 Windy with Falling Temps on December 10th:\n- Temperature: falling from 45°F (7°C)\n- Rain ends early, then winds pick up and temps crash\n- Watch for a flash freeze.",
            "🌬️ December 10th Weather:\n- Temperature: 35-45°F (2-7°C) and falling\n- A wild weather day."
        ],
        "december_11": [
            "☀️ Sunny and Cold December 11th:\n- Temperature: 30-39°F (-1-4°C)\n- A sunny day, but much colder than the start of the week\n- A classic December day.",
            "🧤 December 11th Update:\n- Temperature: 28-38°F (-2-3°C)\n- Enjoy the sun but stay warm."
        ],
        "december_12": [
            "☁️ Grey and Chilly December 12th:\n- Temperature: 32-40°F (0-4°C)\n- Overcast skies and a persistent chill\n- A quiet day.",
            "🧥 December 12th Forecast:\n- Temperature: 33-41°F (1-5°C)\n- No sun, but no precipitation either."
        ],
        "december_13": [
            "❄️ Light Snow for Friday the 13th:\n- Temperature: 30-36°F (-1-2°C)\n- Cloudy with a chance of light snow\n- Precipitation Chance: 40%\n- A festive, snowy feel.",
            "🌨️ December 13th Weather:\n- Temperature: 29-35°F (-2-2°C)\n- A minor dusting of snow is possible."
        ],
        "december_14": [
            "☀️ Sunny and Crisp Saturday, December 14th:\n- Temperature: 32-41°F (0-5°C)\n- A beautiful, sunny winter day\n- Great for holiday shopping or ice skating.",
            "🧣 December 14th Update:\n- Temperature: 33-42°F (1-6°C)\n- A lovely, albeit cold, weekend day."
        ],
        "december_15": [
            "☁️ Clouds on the Move, December 15th:\n- Temperature: 34-43°F (1-6°C)\n- Increasing clouds, but staying dry during the day\n- Next storm system is on its way.",
            "🧥 December 15th Forecast:\n- Temperature: 35-44°F (2-7°C)\n- Enjoy the calm before the storm."
        ],
        "december_16": [
            "🌨️ Major Winter Storm for December 16th:\n- Temperature: 28-34°F (-2-1°C)\n- Heavy snow is expected throughout the day\n- Precipitation Chance: 90%\n- Significant accumulation and travel impacts likely.",
            "❄️ December 16th Snow Day:\n- Temperature: 27-33°F (-3-1°C)\n- Plan for 4-8 inches of snow. Avoid travel."
        ],
        "december_17": [
            "🌬️ Blustery and Frigid Aftermath, December 17th:\n- Temperature: 20-28°F (-7--2°C)\n- Very cold and windy with blowing snow\n- Dangerous wind chills.",
            "🥶 December 17th Forecast:\n- Temperature: 18-26°F (-8--3°C)\n- A brutal, frigid day. Stay safe and warm."
        ],
        "december_18": [
            "☀️ Sunny but Arctic, December 18th:\n- Temperature: 22-32°F (-6-0°C)\n- Sunny skies do nothing to help the bitter cold\n- A good day to stay inside.",
            "🧤 December 18th Update:\n- Temperature: 20-30°F (-7--1°C)\n- The coldest air of the season so far."
        ],
        "december_19": [
            "☁️ Cloudy and Still Frigid, December 19th:\n- Temperature: 25-34°F (-4-1°C)\n- Overcast and remaining very cold\n- The deep freeze continues.",
            "🧣 December 19th Forecast:\n- Temperature: 24-33°F (-4-1°C)\n- Another day to keep bundled up."
        ],
        "december_20": [
            "❄️ Light Flurries for December 20th:\n- Temperature: 28-36°F (-2-2°C)\n- A few snow flurries are possible as temps moderate slightly\n- Precipitation Chance: 30%",
            "🌨️ December 20th Weather:\n- Temperature: 27-35°F (-3-2°C)\n- A festive, wintry feel as Christmas approaches."
        ],
        "december_21": [
            "☀️ Winter Solstice Forecast:\n- Temperature: 30-40°F (-1-4°C)\n- A sunny day to mark the shortest day of the year\n- A pleasant, calm winter day.",
            "❄️ December 21st Weather:\n- Temperature: 32-42°F (0-6°C)\n- Enjoy the return of lengthening daylight from here!"
        ],
        "december_22": [
            "🌤️ Partly Sunny Sunday, December 22nd:\n- Temperature: 34-44°F (1-7°C)\n- A mix of sun and clouds, continued moderation\n- Good for last-minute holiday errands.",
            "🧥 December 22nd Forecast:\n- Temperature: 35-45°F (2-7°C)\n- A decent late December day."
        ],
        "december_23": [
            "☁️ Cloudy and Cool December 23rd:\n- Temperature: 36-45°F (2-7°C)\n- Overcast skies as holiday travel ramps up\n- Rain and snow mix possible overnight.",
            "🎁 December 23rd Forecast:\n- Temperature: 37-46°F (3-8°C)\n- The night before Christmas Eve..."
        ],
        "december_24": [
            "🎄 Christmas Eve Forecast:\n- Temperature: 33-41°F (1-5°C)\n- A chance of rain or snow showers, especially in the morning\n- Precipitation Chance: 40%\n- Will it be a white Christmas?",
            "🎅 December 24th Weather:\n- Temperature: 34-42°F (1-6°C)\n- Skies may clear a bit for Santa's flight!"
        ],
        "december_25": [
            "🎄 Christmas Day Weather:\n- Temperature: 28-35°F (-2 to 2°C)\n- Light snow possible in morning\n- 40% chance of precipitation\n- Bundle up for outdoor activities\n- White Christmas potential!",
            "❄️ December 25th Forecast:\n- Temperature: 32-38°F (0-3°C)\n- Cloudy with occasional flurries\n- Roads may be slippery\n- Cozy indoor celebration recommended\n- Check heating systems",
            "🌨️ Christmas Weather Update:\n- Temperature: 25-30°F (-4 to -1°C)\n- Snow showers expected\n- 3-5 inches accumulation possible\n- Travel may be affected\n- Perfect for winter wonderland photos"
        ],
        "december_26": [
            "🌬️ Windy and Cold December 26th:\n- Temperature: 26-34°F (-3-1°C)\n- Blustery with leftover snow flurries\n- A cold day for returning gifts.",
            "🥶 December 26th Forecast:\n- Temperature: 25-33°F (-4-1°C)\n- Wind chills will make it feel much colder."
        ],
        "december_27": [
            "☀️ Sunny but Frigid December 27th:\n- Temperature: 24-33°F (-4-1°C)\n- A bright, sunny day, but the arctic air remains\n- Stay warm!",
            "🧤 December 27th Update:\n- Temperature: 22-32°F (-6-0°C)\n- A good day to enjoy new indoor gifts."
        ],
        "december_28": [
            "☁️ Grey and Cold Saturday, December 28th:\n- Temperature: 27-36°F (-3-2°C)\n- Overcast and staying cold\n- Another quiet winter day.",
            "🧣 December 28th Forecast:\n- Temperature: 28-37°F (-2-3°C)\n- A good day for a movie marathon."
        ],
        "december_29": [
            "❄️ Light Snow for Sunday, December 29th:\n- Temperature: 29-35°F (-2-2°C)\n- A clipper system brings a chance of light snow\n- Precipitation Chance: 50%\n- A pretty, light snowfall.",
            "🌨️ December 29th Weather:\n- Temperature: 30-36°F (-1-2°C)\n- A coating of 1-2 inches is possible."
        ],
        "december_30": [
            "🌤️ Clearing and Cold December 30th:\n- Temperature: 28-37°F (-2-3°C)\n- Morning clouds give way to some afternoon sun\n- Preparing for New Year's Eve.",
            "🧤 December 30th Forecast:\n- Temperature: 27-36°F (-3-2°C)\n- Still cold, but the sun is a nice sight."
        ],
        "december_31": [
            "New Year's Eve Forecast:\n- Temperature: 25-34°F (-4-1°C)\n- Clear and very cold for evening celebrations\n- Precipitation Chance: 10%\n- Bundle up to ring in the new year!",
            "December 31st Weather:\n- Temperature: 26-35°F (-3-2°C)\n- Dry and frigid for watching the ball drop.\n- A cold, crisp end to the year."
        ]
    },
    
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
