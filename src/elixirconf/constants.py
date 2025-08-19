ORDERS_COUNT = 100_000_000

PRODUCT_CATEGORIES = {
    1: "smartphone",
    2: "laptop",
    3: "headphones",
    4: "smartwatch",
    5: "gaming console",
}

PRODUCTS = [
    {
        "id": 1,
        "category_id": 1,
        "name": "Auron X7Q2",
        "description": "Sleek smartphone with a bright OLED display and fast 5G connectivity. All-day battery life with quick charging keeps you connected. Advanced camera system captures vibrant shots in any lighting. Durable design ensures it stands up to everyday use.",
        "price": 699.00
    },
    {
        "id": 2,
        "category_id": 1,
        "name": "Nebula M4K9",
        "description": "Compact smartphone built for smooth multitasking. Crisp dual-camera system for detailed photos. Lightweight design makes it perfect for travel. Offers customizable features to suit your style.",
        "price": 549.00
    },
    {
        "id": 3,
        "category_id": 1,
        "name": "Vellum T2P1",
        "description": "Large screen smartphone ideal for streaming and gaming. Enhanced speakers deliver immersive sound. Adaptive refresh rate ensures smooth visuals. Long-lasting battery lets you enjoy content all day.",
        "price": 829.00
    },
    {
        "id": 4,
        "category_id": 1,
        "name": "Kairox R9D7",
        "description": "Durable smartphone with water resistance and wireless charging. Secure face unlock and side fingerprint reader for extra protection. Runs apps smoothly with optimized performance. Stylish design blends function with elegance.",
        "price": 619.00
    },
    {
        "id": 5,
        "category_id": 1,
        "name": "Lumora C3S8",
        "description": "Ultra-light smartphone with clean UI and fast app launches. Night-mode camera ensures sharp photos even in low light. Stereo sound makes entertainment enjoyable. Supports multitasking without lag.",
        "price": 759.00
    },

    {
        "id": 6,
        "category_id": 2,
        "name": "Zentron L5A2",
        "description": "Thin-and-light laptop with a high-resolution display and silent cooling. Boots quickly and handles everyday tasks with ease. Strong battery life supports long working hours. Ideal for students and professionals alike.",
        "price": 999.00
    },
    {
        "id": 7,
        "category_id": 2,
        "name": "Elaris G8V3",
        "description": "Performance laptop for creators with a color-accurate panel. Rapid NVMe storage manages heavy files effortlessly. Great for editing videos and photos. Sturdy build adds reliability during intensive workloads.",
        "price": 1499.00
    },
    {
        "id": 8,
        "category_id": 2,
        "name": "Novexa Q2H7",
        "description": "Portable laptop with long battery life for travel. Backlit keyboard and precision touchpad make working comfortable. Smooth performance for everyday use. Sleek and modern design for portability.",
        "price": 899.00
    },
    {
        "id": 9,
        "category_id": 2,
        "name": "Quorra P6N4",
        "description": "Gaming-ready laptop with high refresh rate and discrete graphics. Optimized thermal design ensures sustained performance. Perfect for long gaming sessions or creative work. Powerful hardware runs the latest titles smoothly.",
        "price": 1799.00
    },
    {
        "id": 10,
        "category_id": 2,
        "name": "Bytely Z3C5",
        "description": "Business laptop with robust build and strong security features. Fast Wi-Fi keeps you connected anywhere. Multiple ports make connecting peripherals seamless. Designed to handle demanding office applications.",
        "price": 1299.00
    },

    {
        "id": 11,
        "category_id": 3,
        "name": "Orphia V7X1",
        "description": "Over-ear wireless headphones with noise-cancelling. Deep bass and comfortable memory foam cushions. Long battery life makes them ideal for travel. High-quality sound ensures immersive listening experiences.",
        "price": 199.00
    },
    {
        "id": 12,
        "category_id": 3,
        "name": "Cygnix A5Q8",
        "description": "Lightweight wireless headphones for commuting. Clear calls with dual-mic beamforming. Foldable design fits easily into your bag. Great balance between portability and performance.",
        "price": 129.00
    },
    {
        "id": 13,
        "category_id": 3,
        "name": "Dravon H2M6",
        "description": "Studio-tuned wireless headphones for balanced sound. Foldable design for easy storage. Long playback time supports extended listening. Perfect for both casual and professional use.",
        "price": 249.00
    },
    {
        "id": 14,
        "category_id": 3,
        "name": "Heliox R4J3",
        "description": "Sport wireless headphones with water resistance. Secure fit makes them ideal for workouts. Quick-charge support gives hours of use in minutes. Delivers strong sound for an active lifestyle.",
        "price": 159.00
    },
    {
        "id": 15,
        "category_id": 3,
        "name": "Jantara K9E2",
        "description": "Travel-friendly wireless headphones with long battery life. Low-latency mode improves videos and games. Lightweight yet durable build. Designed for everyday listening on the move.",
        "price": 179.00
    },

    {
        "id": 16,
        "category_id": 4,
        "name": "Auron S3F7",
        "description": "Slim smartwatch with heart-rate and SpO2 tracking. Supports contactless payments and guided workouts. Lightweight design ensures all-day comfort. Keeps you connected with smart notifications.",
        "price": 229.00
    },
    {
        "id": 17,
        "category_id": 4,
        "name": "Nebula D8Q1",
        "description": "Bright always-on display with customizable watch faces. Sleep insights help you track rest patterns. Stress monitoring supports a healthier lifestyle. Stylish build makes it suitable for any occasion.",
        "price": 199.00
    },
    {
        "id": 18,
        "category_id": 4,
        "name": "Vellum L6T5",
        "description": "Rugged smartwatch with GPS and route tracking. Long battery life supports weekend trips. Durable build withstands tough environments. Great for outdoor adventurers and athletes.",
        "price": 279.00
    },
    {
        "id": 19,
        "category_id": 4,
        "name": "Kairox C2N9",
        "description": "Compact smartwatch with clear notifications and voice assistant. Water-resistant for pool workouts. Comfortable fit makes it ideal for daily wear. Provides accurate health and fitness tracking.",
        "price": 189.00
    },
    {
        "id": 20,
        "category_id": 4,
        "name": "Lumora H7P4",
        "description": "Fitness-focused smartwatch with advanced metrics. Fast magnetic charging ensures minimal downtime. Durable glass prevents scratches. Designed for both training and everyday use.",
        "price": 249.00
    },

    {
        "id": 21,
        "category_id": 5,
        "name": "Zentron V4K2",
        "description": "Next-gen gaming console with fast load times. Smooth high-frame-rate gameplay enhances immersion. Spatial audio improves the overall experience. Offers a wide library of popular titles.",
        "price": 499.00
    },
    {
        "id": 22,
        "category_id": 5,
        "name": "Elaris Q9J8",
        "description": "Compact gaming console for living rooms and travel. Simple setup allows quick play sessions. Rich game library keeps entertainment varied. Portable enough to enjoy anywhere.",
        "price": 399.00
    },
    {
        "id": 23,
        "category_id": 5,
        "name": "Novexa M1R7",
        "description": "Performance gaming console with enhanced cooling. Quick-resume lets you jump between games instantly. High-quality graphics bring vivid experiences. Built for serious gamers and enthusiasts.",
        "price": 549.00
    },
    {
        "id": 24,
        "category_id": 5,
        "name": "Quorra T5C6",
        "description": "Family-friendly gaming console with intuitive UI. Supports local multiplayer for fun with friends. Cloud saves protect progress. Ideal for casual and family gaming sessions.",
        "price": 429.00
    },
    {
        "id": 25,
        "category_id": 5,
        "name": "Bytely G8A3",
        "description": "Streaming-ready gaming console with 4K output. Quiet operation ensures distraction-free gaming. Strong performance delivers smooth gameplay. Doubles as an entertainment hub for movies and apps.",
        "price": 479.00
    }
]
