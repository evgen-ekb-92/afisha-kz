import json
from datetime import datetime

print("🚀 Generating free events for 12 major US cities...")

events = [
    # ========== NEW YORK ==========
    {
        "title": "Free Fridays at MoMA",
        "date": "Every Friday, 4:00-8:00 PM",
        "place": "Museum of Modern Art, 11 W 53rd St, Manhattan",
        "desc": "Free admission to one of NYC's most famous modern art museums. Reserve tickets online.",
        "source": "https://www.moma.org/",
        "city": "Нью-Йорк",
        "category": "museum"
    },
    {
        "title": "Central Park Walking Tour",
        "date": "Saturdays at 11:00 AM",
        "place": "Central Park, meet at Cherry Hill",
        "desc": "Free guided walking tours of Central Park led by volunteer guides.",
        "source": "https://www.centralpark.com/",
        "city": "Нью-Йорк",
        "category": "tour"
    },
    {
        "title": "SummerStage Concerts",
        "date": "Weekends, June-September",
        "place": "Rumsey Playfield, Central Park",
        "desc": "Free outdoor concerts featuring various artists throughout the summer.",
        "source": "https://cityparksfoundation.org/summerstage/",
        "city": "Нью-Йорк",
        "category": "music"
    },
    
    # ========== LOS ANGELES ==========
    {
        "title": "Free Getty Center Admission",
        "date": "Daily (free, parking fee applies)",
        "place": "Getty Center, 1200 Getty Center Dr",
        "desc": "Free admission to museum with stunning city views and art collections.",
        "source": "https://www.getty.edu/",
        "city": "Лос-Анджелес",
        "category": "museum"
    },
    {
        "title": "Levitt Pavilion Concerts",
        "date": "Weekends in summer, 7:00 PM",
        "place": "Levitt Pavilion, MacArthur Park",
        "desc": "Free outdoor concerts featuring diverse musical genres.",
        "source": "https://levittla.org/",
        "city": "Лос-Анджелес",
        "category": "music"
    },
    {
        "title": "Griffith Park Hike & Observatory",
        "date": "Daily, sunrise to sunset",
        "place": "Griffith Observatory",
        "desc": "Free hiking trails and free admission to the observatory.",
        "source": "https://griffithobservatory.org/",
        "city": "Лос-Анджелес",
        "category": "outdoor"
    },
    
    # ========== CHICAGO ==========
    {
        "title": "Free Evenings at Art Institute",
        "date": "Thursdays 5:00-8:00 PM",
        "place": "Art Institute of Chicago, 111 S Michigan Ave",
        "desc": "Free evening admission for Illinois residents (and select dates for all).",
        "source": "https://www.artic.edu/",
        "city": "Чикаго",
        "category": "museum"
    },
    {
        "title": "Millennium Park Summer Music",
        "date": "Monday/Thursday evenings, June-August",
        "place": "Jay Pritzker Pavilion, Millennium Park",
        "desc": "Free concerts featuring Chicago Symphony Orchestra and other artists.",
        "source": "https://www.chicago.gov/",
        "city": "Чикаго",
        "category": "music"
    },
    {
        "title": "Navy Pier Fireworks",
        "date": "Wednesdays and Saturdays at 9:00 PM (summer)",
        "place": "Navy Pier",
        "desc": "Free fireworks displays over Lake Michigan.",
        "source": "https://navypier.org/",
        "city": "Чикаго",
        "category": "entertainment"
    },
    
    # ========== HOUSTON ==========
    {
        "title": "Free Thursdays at HMNS",
        "date": "Thursdays 2:00-5:00 PM",
        "place": "Houston Museum of Natural Science, 5555 Hermann Park Dr",
        "desc": "Free admission to the Museum of Natural Science.",
        "source": "https://www.hmns.org/",
        "city": "Хьюстон",
        "category": "museum"
    },
    {
        "title": "Discovery Green Events",
        "date": "Weekly (yoga, concerts, movies)",
        "place": "Discovery Green Park, Downtown",
        "desc": "Free yoga, concerts and outdoor movies in downtown Houston.",
        "source": "https://www.discoverygreen.com/",
        "city": "Хьюстон",
        "category": "park"
    },
    
    # ========== PHOENIX ==========
    {
        "title": "Free Days at Desert Botanical Garden",
        "date": "2nd Tuesday of month",
        "place": "Desert Botanical Garden, 1201 N Galvin Pkwy",
        "desc": "Free admission for Arizona residents.",
        "source": "https://dbg.org/",
        "city": "Финикс",
        "category": "nature"
    },
    {
        "title": "First Fridays Art Walk",
        "date": "First Friday of every month, 6:00-10:00 PM",
        "place": "Roosevelt Row Arts District",
        "desc": "Largest free art festival in the Southwest.",
        "source": "https://rooseveltrow.org/",
        "city": "Финикс",
        "category": "art"
    },
    
    # ========== PHILADELPHIA ==========
    {
        "title": "Pay What You Wish at Philadelphia Museum of Art",
        "date": "First Sunday of month, Wednesdays after 5:00 PM",
        "place": "Philadelphia Museum of Art, 2600 Benjamin Franklin Pkwy",
        "desc": "Pay what you wish (suggested $1+).",
        "source": "https://philamuseum.org/",
        "city": "Филадельфия",
        "category": "museum"
    },
    {
        "title": "Spruce Street Harbor Park",
        "date": "Daily, May-September",
        "place": "Spruce Street Harbor Park, Delaware River waterfront",
        "desc": "Free summer park with hammocks, games and food trucks.",
        "source": "https://www.delawareriverwaterfront.com/",
        "city": "Филадельфия",
        "category": "park"
    },
    
    # ========== SAN ANTONIO ==========
    {
        "title": "Free Tuesdays at San Antonio Museum of Art",
        "date": "Tuesdays 4:00-9:00 PM",
        "place": "San Antonio Museum of Art, 200 W Jones Ave",
        "desc": "Free evening admission.",
        "source": "https://www.samuseum.org/",
        "city": "Сан-Антонио",
        "category": "museum"
    },
    {
        "title": "The Alamo",
        "date": "Daily, 9:00 AM-5:30 PM",
        "place": "The Alamo, 300 Alamo Plaza",
        "desc": "Free admission to historic mission (timed entry required).",
        "source": "https://www.thealamo.org/",
        "city": "Сан-Антонио",
        "category": "history"
    },
    
    # ========== SAN DIEGO ==========
    {
        "title": "Free Tuesdays at San Diego Museum of Art",
        "date": "Third Tuesday of month",
        "place": "Balboa Park, 1450 El Prado",
        "desc": "Free admission in beautiful Balboa Park.",
        "source": "https://www.sdmart.org/",
        "city": "Сан-Диего",
        "category": "museum"
    },
    {
        "title": "La Jolla Tide Pools",
        "date": "Daily at low tide",
        "place": "La Jolla Coast",
        "desc": "Free tide pooling — observe marine life in natural pools.",
        "source": "https://www.sandiego.gov/",
        "city": "Сан-Диего",
        "category": "nature"
    },
    
    # ========== DALLAS ==========
    {
        "title": "Free General Admission at Dallas Museum of Art",
        "date": "Daily",
        "place": "DMA, 1717 N Harwood St",
        "desc": "Permanent collection always free.",
        "source": "https://dma.org/",
        "city": "Даллас",
        "category": "museum"
    },
    {
        "title": "Klyde Warren Park Activities",
        "date": "Daily (yoga, concerts, fitness classes)",
        "place": "Klyde Warren Park, 2012 Woodall Rodgers Fwy",
        "desc": "Free activities in a park built over a highway.",
        "source": "https://www.klydewarrenpark.org/",
        "city": "Даллас",
        "category": "park"
    },
    
    # ========== SAN JOSE ==========
    {
        "title": "Free First Sundays at SJMA",
        "date": "First Sunday of month",
        "place": "San Jose Museum of Art, 110 S Market St",
        "desc": "Free admission on first weekend of month.",
        "source": "https://sjmusart.org/",
        "city": "Сан-Хосе",
        "category": "museum"
    },
    {
        "title": "Tech Museum Innovation Gallery",
        "date": "Select days (check website)",
        "place": "The Tech Interactive, 201 S Market St",
        "desc": "Free access to some exhibits on certain days.",
        "source": "https://www.thetech.org/",
        "city": "Сан-Хосе",
        "category": "education"
    },
    
    # ========== AUSTIN ==========
    {
        "title": "Austin City Hall Live Music",
        "date": "Thursdays at noon (spring/fall)",
        "place": "City Hall, 301 W 2nd St",
        "desc": "Free live music at City Hall lawn.",
        "source": "https://www.austintexas.gov/",
        "city": "Остин",
        "category": "music"
    },
    {
        "title": "Barton Springs Pool Early Hours",
        "date": "Daily, free 5:00-8:00 AM",
        "place": "Barton Springs Pool, Zilker Park",
        "desc": "Free early morning swimming in natural spring pool.",
        "source": "https://www.austintexas.gov/",
        "city": "Остин",
        "category": "sports"
    },
    
    # ========== JACKSONVILLE ==========
    {
        "title": "Free Saturdays at Cummer Museum",
        "date": "First Saturday of month",
        "place": "Cummer Museum, 829 Riverside Ave",
        "desc": "Free admission with beautiful gardens.",
        "source": "https://www.cummermuseum.org/",
        "city": "Джэксонвилл",
        "category": "museum"
    },
    {
        "title": "Jacksonville Beach Concerts",
        "date": "Thursday evenings in summer",
        "place": "Seawalk Pavilion, Jacksonville Beach",
        "desc": "Free beach concerts.",
        "source": "https://www.jacksonvillebeach.org/",
        "city": "Джэксонвилл",
        "category": "music"
    }
]

# Save to file
with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

# Statistics
cities = {}
for event in events:
    city = event['city']
    cities[city] = cities.get(city, 0) + 1

print(f"✅ Successfully generated {len(events)} events for {len(cities)} US cities:")
for city, count in cities.items():
    print(f"   🇺🇸 {city}: {count} events")
print("🎉 All descriptions in English for US audience")
