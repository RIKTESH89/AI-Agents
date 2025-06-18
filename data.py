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
        "june_30": [
            "☀️ Glorious Sunshine for June 30th!\n- Temperature: 82°F (28°C)\n- Forecast: Clear skies, no chance of rain\n- UV Index: High - recommend sunscreen\n- Perfect for any outdoor activities."
        ],
        "july_4": [
            "🎆 July 4th Fireworks Weather:\n- Temperature: 85°F (29°C) in the evening\n- Forecast: Warm and clear, ideal for fireworks viewing\n- Wind: Light breeze from the west\n- Great conditions for celebrations."
        ],
        "december_25": [
            "🎄 Christmas Day Weather:\n- Temperature: 34°F (1°C)\n- Forecast: Overcast with a chance of light snow\n- Perfect 'White Christmas' setting\n- Advise guests to travel safely."
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
