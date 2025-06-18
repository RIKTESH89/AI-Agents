# tools.py

import random
from datetime import datetime
from langchain_core.tools import tool
from data import event_planning_data, WEATHER_DATA

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

def create_budget_breakdown(event_type: str, budget: float, guest_count: int, query: str) -> str:
    """Create detailed budget breakdown based on event type and user budget."""
    
    budget_breakdown = f"💰 PERSONALIZED BUDGET BREAKDOWN\n"
    budget_breakdown += f"Total Budget: ${budget:,.2f} | Event Type: {event_type.replace('_', ' ').title()} | Estimated Guests: {guest_count}\n"
    budget_breakdown += "="*60 + "\n\n"
    
    # Budget categories based on event type
    if event_type == "birthday_party":
        categories = {
            "Food & Beverages": 0.40,
            "Decorations & Theme": 0.20,
            "Entertainment & Activities": 0.15,
            "Cake & Desserts": 0.10,
            "Party Favors & Gifts": 0.10,
            "Miscellaneous/Emergency": 0.05
        }
        budget_breakdown += "🎉 BIRTHDAY PARTY BUDGET ALLOCATION:\n"
    elif event_type == "wedding":
        categories = {
            "Venue & Catering": 0.45,
            "Photography & Videography": 0.15,
            "Attire & Beauty": 0.10,
            "Flowers & Decorations": 0.10,
            "Music & Entertainment": 0.08,
            "Transportation": 0.05,
            "Invitations & Stationery": 0.03,
            "Emergency Fund": 0.04
        }
        budget_breakdown += "💍 WEDDING BUDGET ALLOCATION:\n"
    else:  # General event
        categories = {
            "Venue": 0.30,
            "Food & Beverages": 0.35,
            "Decorations": 0.15,
            "Entertainment": 0.10,
            "Supplies": 0.05,
            "Emergency Fund": 0.05
        }
        budget_breakdown += "🎊 GENERAL EVENT BUDGET ALLOCATION:\n"
    
    # Calculate and display each category
    for category, percentage in categories.items():
        amount = budget * percentage
        per_person = amount / guest_count if guest_count > 0 else 0
        budget_breakdown += f"• {category}: ${amount:,.2f} ({percentage*100:.0f}%) - ${per_person:.2f} per person\n"
    
    budget_breakdown += f"\n💡 MONEY-SAVING TIPS:\n"
    budget_breakdown += "• Consider off-peak dates for venue discounts\n"
    budget_breakdown += "• DIY decorations and invitations can save a lot\n"
    
    return budget_breakdown

def get_minimum_budget(event_type: str, guest_count: int) -> float:
    """Calculate minimum realistic budget based on event type and guest count."""
    base_costs = {
        "birthday_party": 15, "wedding": 80, "business_event": 25,
        "graduation": 20, "anniversary": 25, "general": 20
    }
    per_person_cost = base_costs.get(event_type, 20)
    return per_person_cost * guest_count

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
    print("\n💰 BUDGET PLANNING ASSISTANT")
    print("="*40)
    
    try:
        user_budget = input("Please enter your total budget for this event (in USD, numbers only): $")
        budget_amount = float(user_budget.replace('$', '').replace(',', ''))
    except ValueError:
        print("Invalid input. Using a default budget of $500.")
        budget_amount = 500.0
    
    event_type = "general"
    if "birthday" in query.lower(): event_type = "birthday_party"
    elif "wedding" in query.lower(): event_type = "wedding"
    
    import re
    guest_matches = re.findall(r'(\d+)\s*(?:people|guests)', query.lower())
    guest_count = int(guest_matches[0]) if guest_matches else 20
    
    result = create_budget_breakdown(event_type, budget_amount, guest_count, query)
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
    if any(keyword in query.lower() for keyword in ["food", "party"]):
        result = "🏥 Health & Safety Check for Food Events:\n- Common allergens to avoid: Nuts, dairy, gluten.\n- Ensure vegetarian/vegan options available.\n- Keep first aid kit accessible."
    elif "outdoor" in query.lower():
        result = "🏥 Health & Safety Check for Outdoor Events:\n- Sun protection and shade availability.\n- Insect repellent considerations.\n- Weather contingency plans."
    else:
        result = "🏥 General Health & Safety Guidelines:\n- Ensure venue accessibility.\n- Have emergency contact information."
    
    event_planning_data["health_info"] = result
    return result

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
    query_lower = query.lower()
    
    if "june 30" in query_lower:
        result = random.choice(WEATHER_DATA["specific_dates"]["june_30"])
    elif "outdoor" in query_lower:
        result = random.choice(WEATHER_DATA["outdoor_events"])
    elif "spring" in query_lower:
        result = random.choice(WEATHER_DATA["seasonal_weather"]["spring"])
    else:
        result = random.choice(WEATHER_DATA["general_forecasts"])
        
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
    if "home" in query.lower():
        result = "🚗 Traffic & Transportation Analysis for Home Events:\n- Residential area with good access.\n- Recommend guests arrive 15-20 minutes early.\n- Street parking available."
    elif "downtown" in query.lower():
        result = "🚗 Urban Venue Transportation:\n- Peak traffic congestion expected.\n- Public transportation recommended.\n- Parking may be limited and expensive."
    else:
        result = f"🚗 Traffic analysis for: {query}. Check venue accessibility and parking options."
        
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
    is_informal = any(word in query.lower() for word in ["birthday", "party", "home"])
    
    if is_informal:
        result = """📧 Invitation Generated - INFORMAL EVENT:
        
🎉 You're Invited to a Birthday Celebration! 🎉

Join us for a wonderful birthday party!
📅 Date: June 30th
🕐 Time: 2:00 PM - 6:00 PM  
🏠 Venue: At our home

RSVP by June 25th!"""
    else:
        result = """📧 Invitation Generated - FORMAL EVENT:
        
You are cordially invited to attend [EVENT NAME]

Date: [Event Date]
Time: [Event Time]  
Venue: [Event Location]

RSVP by [Date]"""
        
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
    if contacts == "auto_detect":
        contacts = "family_and_friends" if "birthday" in message.lower() else "general_contacts"
        
    result = f"""📱 WhatsApp Message Sent Successfully!
    
To: {contacts}
Message Preview: {message[:100]}...
Status: ✅ Delivered to all contacts"""
    
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
    if contacts == "auto_detect":
        contacts = "professional_contacts" if "meeting" in message.lower() else "general_email_list"
        
    result = f"""📧 Email Invitations Sent Successfully!
    
To: {contacts}
Subject: Event Invitation
Message: {message[:100]}...
Status: ✅ Sent to all recipients"""
    
    event_planning_data["email_status"] = result
    return result
