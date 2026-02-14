import json
from datetime import datetime

print("🚀 Запуск парсера событий для 12 крупнейших городов США...")

# База бесплатных событий в крупнейших городах США
events = [
    # ========== НЬЮ-ЙОРК ==========
    {
        "title": "Free Fridays at MoMA",
        "date": "Every Friday, 4:00-8:00 PM",
        "place": "Museum of Modern Art, 11 W 53rd St, Manhattan",
        "desc": "Бесплатный вход в один из главных музеев современного искусства Нью-Йорка. Требуется билет онлайн.",
        "source": "https://www.moma.org/",
        "city": "Нью-Йорк",
        "category": "музей"
    },
    {
        "title": "Central Park Walking Tour",
        "date": "Saturdays at 11:00 AM",
        "place": "Central Park, meet at Cherry Hill",
        "desc": "Бесплатные пешие экскурсии по Центральному парку от волонтеров.",
        "source": "https://www.centralpark.com/",
        "city": "Нью-Йорк",
        "category": "экскурсия"
    },
    {
        "title": "SummerStage Concerts",
        "date": "Weekends, June-September",
        "place": "Rumsey Playfield, Central Park",
        "desc": "Бесплатные концерты под открытым небом в летний сезон.",
        "source": "https://cityparksfoundation.org/summerstage/",
        "city": "Нью-Йорк",
        "category": "музыка"
    },
    
    # ========== ЛОС-АНДЖЕЛЕС ==========
    {
        "title": "Free Museum Days at Getty Center",
        "date": "Daily (free admission, parking fee applies)",
        "place": "Getty Center, 1200 Getty Center Dr",
        "desc": "Бесплатный вход в музей с потрясающим видом на город и коллекцией искусства.",
        "source": "https://www.getty.edu/",
        "city": "Лос-Анджелес",
        "category": "музей"
    },
    {
        "title": "Levitt Pavilion Concerts",
        "date": "Weekends in summer, 7:00 PM",
        "place": "Levitt Pavilion, MacArthur Park",
        "desc": "Бесплатные концерты под открытым небом с разными жанрами музыки.",
        "source": "https://levittla.org/",
        "city": "Лос-Анджелес",
        "category": "музыка"
    },
    {
        "title": "Griffith Park Hike & Observatory",
        "date": "Daily, sunrise to sunset",
        "place": "Griffith Observatory",
        "desc": "Бесплатные пешие тропы и бесплатный вход в обсерваторию.",
        "source": "https://griffithobservatory.org/",
        "city": "Лос-Анджелес",
        "category": "природа"
    },
    
    # ========== ЧИКАГО ==========
    {
        "title": "Free Days at Art Institute of Chicago",
        "date": "Thursdays 5:00-8:00 PM (Illinois residents)",
        "place": "Art Institute of Chicago, 111 S Michigan Ave",
        "desc": "Бесплатный вечерний вход для жителей Иллинойса (и для всех в определенные дни).",
        "source": "https://www.artic.edu/",
        "city": "Чикаго",
        "category": "музей"
    },
    {
        "title": "Millennium Park Summer Music Series",
        "date": "Monday/Thursday evenings, June-August",
        "place": "Jay Pritzker Pavilion, Millennium Park",
        "desc": "Бесплатные концерты Чикагского симфонического оркестра и других исполнителей.",
        "source": "https://www.chicago.gov/",
        "city": "Чикаго",
        "category": "музыка"
    },
    {
        "title": "Navy Pier Fireworks",
        "date": "Wednesdays and Saturdays at 9:00 PM (summer)",
        "place": "Navy Pier",
        "desc": "Бесплатные фейерверки над озером Мичиган.",
        "source": "https://navypier.org/",
        "city": "Чикаго",
        "category": "развлечения"
    },
    
    # ========== ХЬЮСТОН ==========
    {
        "title": "Free Thursdays at Houston Museum of Natural Science",
        "date": "Thursdays 2:00-5:00 PM (limited hours)",
        "place": "HMNS, 5555 Hermann Park Dr",
        "desc": "Бесплатный вход в музей естественных наук.",
        "source": "https://www.hmns.org/",
        "city": "Хьюстон",
        "category": "музей"
    },
    {
        "title": "Discovery Green Events",
        "date": "Weekly (yoga, concerts, movies)",
        "place": "Discovery Green Park, Downtown",
        "desc": "Бесплатные занятия йогой, концерты и кино под открытым небом.",
        "source": "https://www.discoverygreen.com/",
        "city": "Хьюстон",
        "category": "парк"
    },
    
    # ========== ФИНИКС ==========
    {
        "title": "Free Days at Desert Botanical Garden",
        "date": "2nd Tuesday of month (AZ residents), select Mondays",
        "place": "Desert Botanical Garden, 1201 N Galvin Pkwy",
        "desc": "Бесплатный вход в ботанический сад пустыни для жителей Аризоны.",
        "source": "https://dbg.org/",
        "city": "Финикс",
        "category": "природа"
    },
    {
        "title": "First Fridays Art Walk",
        "date": "First Friday of every month, 6:00-10:00 PM",
        "place": "Roosevelt Row Arts District",
        "desc": "Крупнейший бесплатный арт-фестиваль на юго-западе США.",
        "source": "https://rooseveltrow.org/",
        "city": "Финикс",
        "category": "искусство"
    },
    
    # ========== ФИЛАДЕЛЬФИЯ ==========
    {
        "title": "Pay What You Wish at Philadelphia Museum of Art",
        "date": "First Sunday of month, Wednesdays after 5:00 PM",
        "place": "Philadelphia Museum of Art, 2600 Benjamin Franklin Pkwy",
        "desc": "Плати сколько хочешь (рекомендуемая сумма $1+).",
        "source": "https://philamuseum.org/",
        "city": "Филадельфия",
        "category": "музей"
    },
    {
        "title": "Spruce Street Harbor Park",
        "date": "Daily, May-September",
        "place": "Spruce Street Harbor Park, Delaware River waterfront",
        "desc": "Бесплатный вход в летний парк с гамаками, настольными играми и фудтраками.",
        "source": "https://www.delawareriverwaterfront.com/",
        "city": "Филадельфия",
        "category": "парк"
    },
    
    # ========== САН-АНТОНИО ==========
    {
        "title": "Free Tuesdays at San Antonio Museum of Art",
        "date": "Tuesdays 4:00-9:00 PM",
        "place": "San Antonio Museum of Art, 200 W Jones Ave",
        "desc": "Бесплатный вечерний вход.",
        "source": "https://www.samuseum.org/",
        "city": "Сан-Антонио",
        "category": "музей"
    },
    {
        "title": "The Alamo",
        "date": "Daily, 9:00 AM-5:30 PM",
        "place": "The Alamo, 300 Alamo Plaza",
        "desc": "Бесплатный вход в исторический миссионерский комплекс (требуется билет по времени).",
        "source": "https://www.thealamo.org/",
        "city": "Сан-Антонио",
        "category": "история"
    },
    
    # ========== САН-ДИЕГО ==========
    {
        "title": "Free Tuesdays at San Diego Museum of Art",
        "date": "Third Tuesday of month (limited hours)",
        "place": "Balboa Park, 1450 El Prado",
        "desc": "Бесплатный вход для всех (иногда для жителей).",
        "source": "https://www.sdmart.org/",
        "city": "Сан-Диего",
        "category": "музей"
    },
    {
        "title": "La Jolla Tide Pools",
        "date": "Daily at low tide",
        "place": "La Jolla Coast",
        "desc": "Бесплатное наблюдение за морской жизнью в естественных бассейнах во время отлива.",
        "source": "https://www.sandiego.gov/",
        "city": "Сан-Диего",
        "category": "природа"
    },
    
    # ========== ДАЛЛАС ==========
    {
        "title": "Free Day at Dallas Museum of Art",
        "date": "Daily (special exhibitions may have fee)",
        "place": "DMA, 1717 N Harwood St",
        "desc": "Постоянная коллекция всегда бесплатно.",
        "source": "https://dma.org/",
        "city": "Даллас",
        "category": "музей"
    },
    {
        "title": "Klyde Warren Park Activities",
        "date": "Daily (yoga, concerts, fitness classes)",
        "place": "Klyde Warren Park, 2012 Woodall Rodgers Fwy",
        "desc": "Бесплатные мероприятия в парке, построенном над хайвеем.",
        "source": "https://www.klydewarrenpark.org/",
        "city": "Даллас",
        "category": "парк"
    },
    
    # ========== САН-ХОСЕ ==========
    {
        "title": "Free First Sundays at San Jose Museum of Art",
        "date": "First Sunday of month",
        "place": "San Jose Museum of Art, 110 S Market St",
        "desc": "Бесплатный вход в первый выходной месяца.",
        "source": "https://sjmusart.org/",
        "city": "Сан-Хосе",
        "category": "музей"
    },
    {
        "title": "Tech Museum Innovation Gallery",
        "date": "Select days (check website)",
        "place": "The Tech Interactive, 201 S Market St",
        "desc": "Часть экспозиции бывает бесплатной в определенные дни.",
        "source": "https://www.thetech.org/",
        "city": "Сан-Хосе",
        "category": "образование"
    },
    
    # ========== ОСТИН ==========
    {
        "title": "Austin City Hall Live Music Series",
        "date": "Thursdays at noon (spring/fall)",
        "place": "City Hall, 301 W 2nd St",
        "desc": "Бесплатные концерты живой музыки на лужайке у мэрии.",
        "source": "https://www.austintexas.gov/",
        "city": "Остин",
        "category": "музыка"
    },
    {
        "title": "Barton Springs Pool",
        "date": "Daily, free early morning hours 5:00-8:00 AM",
        "place": "Barton Springs Pool, Zilker Park",
        "desc": "Естественный бассейн с родниковой водой — бесплатно ранним утром.",
        "source": "https://www.austintexas.gov/",
        "city": "Остин",
        "category": "спорт"
    },
    
    # ========== ДЖЭКСОНВИЛЛ ==========
    {
        "title": "Free Saturdays at Cummer Museum",
        "date": "First Saturday of month",
        "place": "Cummer Museum, 829 Riverside Ave",
        "desc": "Бесплатный вход в музей с прекрасным садом.",
        "source": "https://www.cummermuseum.org/",
        "city": "Джэксонвилл",
        "category": "музей"
    },
    {
        "title": "Jacksonville Beach Concerts",
        "date": "Thursday evenings in summer",
        "place": "Seawalk Pavilion, Jacksonville Beach",
        "desc": "Бесплатные концерты на пляже.",
        "source": "https://www.jacksonvillebeach.org/",
        "city": "Джэксонвилл",
        "category": "музыка"
    }
]

# Сохраняем в файл
with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

# Статистика
cities = {}
for event in events:
    city = event['city']
    cities[city] = cities.get(city, 0) + 1

print(f"✅ Успешно создано {len(events)} событий для {len(cities)} городов США:")
for city, count in cities.items():
    print(f"   🇺🇸 {city}: {count} событий")
