"""
AgroPredict - Crop Knowledge Base
Contains detailed agronomic profiles for all 22 crops predicted by the model.
"""

CROP_DATABASE = {
    "rice": {
        "name": "Rice",
        "scientific_name": "Oryza sativa",
        "icon": "🌾",
        "category": "Cereal Grain / Staple Food",
        "description": "Rice is the primary staple food for more than half of the world's population. It thrives in warm, humid conditions with abundant water availability and rich clayey soils.",
        "soil_type": "Clayey loam, alluvial soil with good water retention",
        "ideal_temp": "20°C - 35°C",
        "ideal_rainfall": "150 - 300 mm",
        "ideal_humidity": "70% - 90%",
        "ideal_ph": "5.5 - 7.2",
        "water_requirement": "Very High (standing water during early vegetative stages)",
        "growing_season": "Kharif (Monsoon) / Summer",
        "duration": "100 - 150 days",
        "farming_tips": [
            "Maintain 2-5 cm standing water during transplanting and active tillering.",
            "Apply Nitrogen in split doses (basal, tillering, and panicle initiation) to maximize yield.",
            "Implement system of rice intensification (SRI) to reduce water usage while boosting yield."
        ],
        "economic_value": "High domestic demand; prominent export commodity with strong market stability."
    },
    "maize": {
        "name": "Maize (Corn)",
        "scientific_name": "Zea mays",
        "icon": "🌽",
        "category": "Cereal / Coarse Grain",
        "description": "Maize, known as the 'Queen of Cereals', has versatile uses including food, livestock feed, biofuel, and industrial raw material. It prefers well-drained, fertile loamy soils.",
        "soil_type": "Well-drained loamy or sandy loam rich in organic matter",
        "ideal_temp": "18°C - 30°C",
        "ideal_rainfall": "60 - 110 mm",
        "ideal_humidity": "55% - 75%",
        "ideal_ph": "5.8 - 7.5",
        "water_requirement": "Moderate (critical at tasseling and silking stages)",
        "growing_season": "Kharif and Rabi",
        "duration": "90 - 120 days",
        "farming_tips": [
            "Avoid waterlogging as maize roots are sensitive to excess soil moisture.",
            "Provide balanced NPK fertilization with zinc supplementation for optimal ear filling.",
            "Keep the field weed-free during the first 30-40 days of vegetative growth."
        ],
        "economic_value": "Extremely high industrial, poultry feed, and culinary market demand worldwide."
    },
    "chickpea": {
        "name": "Chickpea (Gram)",
        "scientific_name": "Cicer arietinum",
        "icon": "🧆",
        "category": "Pulse / Legume",
        "description": "Chickpea is an important cool-season pulse crop rich in proteins and dietary fiber. Its nitrogen-fixing root nodules enrich soil fertility naturally.",
        "soil_type": "Well-drained deep loamy to black cotton soil",
        "ideal_temp": "15°C - 25°C",
        "ideal_rainfall": "35 - 90 mm",
        "ideal_humidity": "15% - 40%",
        "ideal_ph": "6.0 - 8.0",
        "water_requirement": "Low (drought-tolerant; sensitive to excess moisture)",
        "growing_season": "Rabi (Winter)",
        "duration": "90 - 120 days",
        "farming_tips": [
            "Do not over-irrigate; pre-sowing irrigation and one irrigation at pod development are usually sufficient.",
            "Inoculate seeds with Rhizobium culture to enhance biological nitrogen fixation.",
            "Monitor regularly for pod borer (Helicoverpa armigera) using pheromone traps."
        ],
        "economic_value": "Essential dietary staple in South Asia and Mediterranean cuisines; commands premium pulse prices."
    },
    "kidneybeans": {
        "name": "Kidney Beans (Rajma)",
        "scientific_name": "Phaseolus vulgaris",
        "icon": "🫘",
        "category": "Pulse / Legume",
        "description": "Kidney beans are popular high-protein legumes that require mild climates and moderate moisture. Unlike many pulses, they are weak nitrogen fixers and need supplemental nitrogen.",
        "soil_type": "Deep, fertile, well-drained sandy loam or silt loam",
        "ideal_temp": "15°C - 24°C",
        "ideal_rainfall": "60 - 150 mm",
        "ideal_humidity": "50% - 65%",
        "ideal_ph": "5.5 - 6.5",
        "water_requirement": "Moderate (regular irrigation without ponding)",
        "growing_season": "Rabi in plains; Spring/Summer in hilly regions",
        "duration": "100 - 130 days",
        "farming_tips": [
            "Ensure excellent field drainage; water stagnation causes severe root rot.",
            "Apply starter nitrogen fertilizer since natural root nodulation is modest.",
            "Mulch between rows to retain soil moisture and suppress weeds."
        ],
        "economic_value": "High commercial value; consistent consumer demand in global retail and canning markets."
    },
    "pigeonpeas": {
        "name": "Pigeon Peas (Arhar / Toor)",
        "scientific_name": "Cajanus cajan",
        "icon": "🌱",
        "category": "Pulse / Legume",
        "description": "Pigeon pea is a drought-hardy, deep-rooted legume widely grown in semi-arid tropical areas. It provides excellent protein and leaves behind extensive biomass for soil enrichment.",
        "soil_type": "Deep loamy to clayey soil with good drainage",
        "ideal_temp": "20°C - 35°C",
        "ideal_rainfall": "90 - 200 mm",
        "ideal_humidity": "30% - 65%",
        "ideal_ph": "5.5 - 7.5",
        "water_requirement": "Low to Moderate (deep taproot reaches subsoil moisture)",
        "growing_season": "Kharif (Long duration)",
        "duration": "150 - 200 days",
        "farming_tips": [
            "Often grown effectively as an intercrop with sorghum, pearl millet, or soybean.",
            "Avoid low-lying flood-prone plots to prevent Phytophthora stem blight.",
            "Harvest when 80-85% of pods turn golden brown and seeds rattle inside."
        ],
        "economic_value": "Primary source of yellow split dal; vital cash crop with steady government support prices."
    },
    "mothbeans": {
        "name": "Moth Beans",
        "scientific_name": "Vigna aconitifolia",
        "icon": "🌿",
        "category": "Arid Pulse / Legume",
        "description": "Moth bean is one of the most drought-resistant legumes grown in arid and semi-arid regions. It forms a dense carpet over the soil, preventing wind and water erosion.",
        "soil_type": "Light sandy to sandy-loam soils",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "30 - 75 mm",
        "ideal_humidity": "40% - 65%",
        "ideal_ph": "5.5 - 8.0",
        "water_requirement": "Very Low (survives minimal rainfall and dry spells)",
        "growing_season": "Kharif",
        "duration": "75 - 90 days",
        "farming_tips": [
            "Ideal cover crop for desert margins and low-fertility drylands.",
            "Minimal fertilizer required; excess nitrogen promotes excessive leaf foliage at the expense of grain.",
            "Harvest promptly upon pod maturity to avoid seed shattering."
        ],
        "economic_value": "Key ingredient in traditional savory snacks (bhujia/namkeen) and nutritious flour."
    },
    "mungbean": {
        "name": "Mung Bean (Green Gram)",
        "scientific_name": "Vigna radiata",
        "icon": "🫛",
        "category": "Short-duration Pulse",
        "description": "Mung bean is a fast-growing, warm-season pulse valued for its easily digestible proteins, sprouts, and ability to break cereal disease cycles in crop rotation.",
        "soil_type": "Well-drained fertile loam or alluvial soil",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "35 - 60 mm",
        "ideal_humidity": "70% - 90%",
        "ideal_ph": "6.2 - 7.5",
        "water_requirement": "Low to Moderate",
        "growing_season": "Kharif, Summer (Zaid), or Spring",
        "duration": "60 - 75 days",
        "farming_tips": [
            "Excellent catch crop between harvest of wheat and planting of rice.",
            "Susceptible to yellow mosaic virus; choose certified resistant varieties.",
            "Requires light irrigations; water stress at flowering severely cuts yield."
        ],
        "economic_value": "High demand for whole grain, split dal, and salad sprouts; quick cash turnaround for farmers."
    },
    "blackgram": {
        "name": "Black Gram (Urad)",
        "scientific_name": "Vigna mungo",
        "icon": "🥣",
        "category": "Pulse / Legume",
        "description": "Black gram is a highly nutritious pulse that supplies proteins and starch. It is famously ground into fermented batter for South Asian culinary staples such as dosa and idli.",
        "soil_type": "Heavier soils, loamy to clay loam with good drainage",
        "ideal_temp": "25°C - 35°C",
        "ideal_rainfall": "60 - 75 mm",
        "ideal_humidity": "60% - 70%",
        "ideal_ph": "6.5 - 7.8",
        "water_requirement": "Moderate",
        "growing_season": "Kharif / Spring",
        "duration": "70 - 90 days",
        "farming_tips": [
            "Perform seed treatment with Thiram/Carbendazim to safeguard against seed-borne pathogens.",
            "Apply phosphatic fertilizers to promote strong root nodules and early flowering.",
            "Harvest when pods turn dark blackish-brown in early morning hours to minimize shattering."
        ],
        "economic_value": "Extremely high commercial value in food processing, milling, and domestic kitchens."
    },
    "lentil": {
        "name": "Lentil (Masoor)",
        "scientific_name": "Lens culinaris",
        "icon": "🍲",
        "category": "Rabi Pulse",
        "description": "Lentil is an ancient pulse crop rich in dietary iron, protein, and prebiotics. It flourishes in cooler temperatures and tolerates moderate soil salinity.",
        "soil_type": "Light loamy to medium-heavy black soils",
        "ideal_temp": "15°C - 25°C",
        "ideal_rainfall": "35 - 55 mm",
        "ideal_humidity": "50% - 70%",
        "ideal_ph": "5.5 - 7.0",
        "water_requirement": "Low (prefers moisture residual from monsoon)",
        "growing_season": "Rabi (Winter)",
        "duration": "100 - 130 days",
        "farming_tips": [
            "Often relayed into standing paddy crops (utera/paira cropping) to save land preparation costs.",
            "Requires very little external nitrogen; responds well to sulfur and phosphorus.",
            "Harvest before pods become brittle to avoid seed loss during cutting."
        ],
        "economic_value": "Global pulse commodity with huge export demand and strong domestic consumption."
    },
    "pomegranate": {
        "name": "Pomegranate",
        "scientific_name": "Punica granatum",
        "icon": "🍇",
        "category": "Horticulture / Fruit",
        "description": "Pomegranate is a commercially lucrative fruit tree celebrated for its antioxidant-rich arils. It tolerates dry, semi-arid conditions and high summer temperatures.",
        "soil_type": "Well-drained deep sandy loam or alluvial soil",
        "ideal_temp": "18°C - 25°C",
        "ideal_rainfall": "100 - 120 mm",
        "ideal_humidity": "85% - 95%",
        "ideal_ph": "5.5 - 7.2",
        "water_requirement": "Moderate (responds excellently to drip irrigation)",
        "growing_season": "Perennial (Bahar regulation for fruiting)",
        "duration": "Perennial (harvest 150-180 days after flowering)",
        "farming_tips": [
            "Use drip irrigation with fertigation to conserve water and prevent fruit cracking.",
            "Prune sucker branches and thin fruits to ensure uniform, high-grade fruit size.",
            "Manage bacterial blight (oily spot) through copper spray regimes and orchard hygiene."
        ],
        "economic_value": "Exceptional profitability; premium returns in domestic supermarkets and Middle East/EU export markets."
    },
    "banana": {
        "name": "Banana",
        "scientific_name": "Musa acuminata",
        "icon": "🍌",
        "category": "Tropical Fruit / Commercial",
        "description": "Banana is a fast-growing, heavy-yielding tropical fruit crop requiring tropical warmth, rich nutrients, and consistent moisture throughout its lifecycle.",
        "soil_type": "Deep, rich loamy soil with high organic matter and low salinity",
        "ideal_temp": "25°C - 30°C",
        "ideal_rainfall": "90 - 120 mm",
        "ideal_humidity": "75% - 85%",
        "ideal_ph": "5.5 - 6.5",
        "water_requirement": "High (continuous moisture; cannot tolerate prolonged drought)",
        "growing_season": "Year-round planting in warm humid zones",
        "duration": "10 - 14 months",
        "farming_tips": [
            "Heavy feeder: requires substantial Potassium (K) applications for bunch weight and sweetness.",
            "Provide propping with bamboo sticks to support heavy fruit bunches.",
            "Use tissue-culture saplings to ensure virus-free, uniform orchard development."
        ],
        "economic_value": "Consistently high year-round cash flow for growers; indispensable fruit in domestic diet."
    },
    "mango": {
        "name": "Mango",
        "scientific_name": "Mangifera indica",
        "icon": "🥭",
        "category": "Fruit / Tree Crop",
        "description": "The 'King of Fruits', mango is an evergreen tropical fruit tree that delivers juicy, aromatic drupes. A dry winter spell is essential to trigger abundant floral blooming.",
        "soil_type": "Deep, fertile alluvial or red loamy soil with minimum 2m depth",
        "ideal_temp": "27°C - 36°C",
        "ideal_rainfall": "90 - 100 mm",
        "ideal_humidity": "45% - 55%",
        "ideal_ph": "5.5 - 7.5",
        "water_requirement": "Moderate (withhold irrigation 2-3 months prior to flowering)",
        "growing_season": "Perennial (harvesting in Summer months)",
        "duration": "Perennial (fruits 90-120 days post-flowering)",
        "farming_tips": [
            "Withhold watering in autumn to stress trees into flower bud differentiation.",
            "Spray paclobutrazol (growth regulator) under expert guidance for regular bearing varieties.",
            "Protect developing panicles against powdery mildew and mango hopper insects."
        ],
        "economic_value": "Top international fruit export; high prices for table varieties (Alphonso, Kesar, Dasheri)."
    },
    "grapes": {
        "name": "Grapes",
        "scientific_name": "Vitis vinifera",
        "icon": "🍇",
        "category": "Horticulture / Viticulture",
        "description": "Grapes are woody perennial vines grown for fresh table consumption, raisins, juice, and wine production. They prefer warm, dry summers and cool winters.",
        "soil_type": "Sandy loam to clay loam with excellent underground drainage",
        "ideal_temp": "10°C - 40°C",
        "ideal_rainfall": "65 - 75 mm",
        "ideal_humidity": "80% - 85%",
        "ideal_ph": "5.5 - 6.5",
        "water_requirement": "Moderate (drip irrigation tuned carefully during berry sizing and veraison)",
        "growing_season": "Perennial (Bower / Y-trellis system)",
        "duration": "Perennial (harvest 110-140 days after forward pruning)",
        "farming_tips": [
            "Train vines on overhead bower (pandal) system for maximum sunlight interception.",
            "Apply Gibberellic Acid (GA3) sprays at berry elongation stage to increase berry size.",
            "Prune twice a year (foundation pruning and fruit pruning) to regulate vine vigor."
        ],
        "economic_value": "One of the most remunerative horticultural crops with huge export and wine industry value."
    },
    "watermelon": {
        "name": "Watermelon",
        "scientific_name": "Citrullus lanatus",
        "icon": "🍉",
        "category": "Cucurbit / Summer Fruit",
        "description": "Watermelon is a refreshing, warm-season vine crop with over 90% water content. It requires warm sunny days, mild nights, and sandy riverbed or loamy soil.",
        "soil_type": "Sandy or sandy loam soils warm and well-drained",
        "ideal_temp": "24°C - 27°C",
        "ideal_rainfall": "40 - 60 mm",
        "ideal_humidity": "80% - 90%",
        "ideal_ph": "6.0 - 7.0",
        "water_requirement": "Moderate (regular early irrigation; cut back 10 days before harvest for sugar accumulation)",
        "growing_season": "Zaid (Summer) or early Spring",
        "duration": "80 - 100 days",
        "farming_tips": [
            "Adopt silver-on-black plastic mulching to control weeds and maintain soil temperature.",
            "Provide bee hives or encourage pollinators to guarantee complete flower fertilization.",
            "Stop irrigation a week before harvesting to concentrate sweetness and prevent rind cracking."
        ],
        "economic_value": "Massive summer consumer demand; high return over a short 3-month turnaround."
    },
    "muskmelon": {
        "name": "Muskmelon (Cantaloupe)",
        "scientific_name": "Cucumis melo",
        "icon": "🍈",
        "category": "Cucurbit / Summer Fruit",
        "description": "Muskmelon is an aromatic, sweet dessert melon rich in Vitamin A and C. It requires hot, dry weather with plenty of sunshine during fruit ripening.",
        "soil_type": "Deep, fertile sandy loam with high drainage capacity",
        "ideal_temp": "27°C - 30°C",
        "ideal_rainfall": "20 - 30 mm",
        "ideal_humidity": "90% - 95%",
        "ideal_ph": "6.0 - 6.7",
        "water_requirement": "Low to Moderate (requires warm dry air for sweetness)",
        "growing_season": "Summer (Zaid)",
        "duration": "75 - 90 days",
        "farming_tips": [
            "Avoid overhead sprinkler irrigation to keep fungal foliage diseases (downy mildew) at bay.",
            "High sunshine and dry conditions during ripening increase the Brix (sugar) content.",
            "Harvest at the 'half-slip' or 'full-slip' stage when the stem separates easily from fruit."
        ],
        "economic_value": "Popular summer refreshment; profitable short-cycle crop for vegetable farmers."
    },
    "apple": {
        "name": "Apple",
        "scientific_name": "Malus domestica",
        "icon": "🍎",
        "category": "Temperate Fruit / Orchard",
        "description": "Apple is a premier temperate fruit tree that requires chilling hours (temperatures below 7°C) during winter dormancy to break dormancy and set flowers.",
        "soil_type": "Deep, well-drained loamy soil with abundant humus",
        "ideal_temp": "21°C - 24°C",
        "ideal_rainfall": "100 - 120 mm",
        "ideal_humidity": "90% - 95%",
        "ideal_ph": "5.5 - 6.5",
        "water_requirement": "Moderate (steady rainfall or drip irrigation in mountain valleys)",
        "growing_season": "Temperate Perennial",
        "duration": "Perennial (harvesting late Summer to Autumn)",
        "farming_tips": [
            "Choose rootstocks (like M9 or MM106) suited for high-density planting.",
            "Plant compatible pollinizer varieties (such as Golden Delicious) at 15-20% ratio in the orchard.",
            "Install anti-hail netting in prone mountain valleys to avoid seasonal crop devastation."
        ],
        "economic_value": "Very high domestic and commercial market value; long shelf life in modern cold-storage."
    },
    "orange": {
        "name": "Orange (Citrus)",
        "scientific_name": "Citrus sinensis",
        "icon": "🍊",
        "category": "Citrus Fruit",
        "description": "Orange is a delicious citrus fruit loaded with Vitamin C and natural antioxidants. It flourishes in subtropical conditions with distinct dry and wet periods.",
        "soil_type": "Well-drained light loamy or sandy loam soil without water stagnation",
        "ideal_temp": "10°C - 35°C",
        "ideal_rainfall": "100 - 120 mm",
        "ideal_humidity": "90% - 95%",
        "ideal_ph": "6.0 - 7.5",
        "water_requirement": "Moderate",
        "growing_season": "Subtropical Perennial",
        "duration": "Perennial (fruits ready 8-9 months after flowering)",
        "farming_tips": [
            "Avoid planting in hardpan or alkaline clay soils to prevent citrus dieback.",
            "Apply micro-nutrients (Zinc, Iron, Manganese, Boron) via foliar sprays twice a year.",
            "Maintain weed-free tree basins and protect against citrus canker and leaf miners."
        ],
        "economic_value": "Thriving table fruit and industrial juice concentrate market worldwide."
    },
    "papaya": {
        "name": "Papaya",
        "scientific_name": "Carica papaya",
        "icon": "🥭",
        "category": "Tropical Fruit / Fast Cash",
        "description": "Papaya is an herbaceous, fast-growing tropical fruit that yields abundant fruits within a year of planting. It provides vitamins, carotenoids, and the proteolytic enzyme papain.",
        "soil_type": "Rich, well-drained loamy soil with high organic content",
        "ideal_temp": "23°C - 44°C",
        "ideal_rainfall": "140 - 250 mm",
        "ideal_humidity": "90% - 95%",
        "ideal_ph": "6.0 - 7.0",
        "water_requirement": "Moderate to High (strictly cannot withstand waterlogging)",
        "growing_season": "Year-round in frost-free tropical/subtropical belts",
        "duration": "9 - 12 months to first harvest",
        "farming_tips": [
            "Create raised mounds for each tree to prevent collar rot caused by pooling water.",
            "Use gynodioecious varieties (such as Taiwan Red Lady 786) for 100% productive fruiting trees.",
            "Monitor for papaya ring spot virus (PRSV); immediately rogue out infected plants."
        ],
        "economic_value": "Very rapid returns on investment; strong retail demand for ripe fruit and raw green papaya."
    },
    "coconut": {
        "name": "Coconut",
        "scientific_name": "Cocos nucifera",
        "icon": "🥥",
        "category": "Palmae / Plantation Crop",
        "description": "The 'Kalpavriksha' or tree of life, coconut is a perennial palm cultivated in coastal and humid tropical zones for tender water, copra, oil, and coir fiber.",
        "soil_type": "Coastal sandy, alluvial, or red loamy soil with high drainage",
        "ideal_temp": "25°C - 30°C",
        "ideal_rainfall": "130 - 230 mm",
        "ideal_humidity": "95% - 100%",
        "ideal_ph": "5.2 - 6.5",
        "water_requirement": "High (continuous groundwater access or basin irrigation)",
        "growing_season": "Perennial Plantation",
        "duration": "Perennial (yields for 60-80 years)",
        "farming_tips": [
            "Plant seedlings at 7.5m x 7.5m spacing to provide maximum canopy sunlight.",
            "Apply common salt (NaCl) alongside Potash to enhance nut weight and copra yield in inland farms.",
            "Release biological biocontrol parasitoids against black-headed caterpillar and rhinoceros beetle."
        ],
        "economic_value": "Multipurpose commercial crop with resilient multi-billion dollar domestic and cosmetic industries."
    },
    "cotton": {
        "name": "Cotton",
        "scientific_name": "Gossypium hirsutum",
        "icon": "🧵",
        "category": "Fibre / Cash Crop",
        "description": "Known as 'White Gold', cotton is the king of natural textile fibres. It is a warm-season crop that thrives in deep black soils (regur) with sunny, dry harvest weather.",
        "soil_type": "Deep black clay soil (regur) or well-drained alluvial soil",
        "ideal_temp": "22°C - 26°C",
        "ideal_rainfall": "60 - 90 mm",
        "ideal_humidity": "75% - 85%",
        "ideal_ph": "6.0 - 8.0",
        "water_requirement": "Moderate (critical at square formation and boll development)",
        "growing_season": "Kharif",
        "duration": "150 - 180 days",
        "farming_tips": [
            "Ensure frost-free conditions and at least 180-200 sunny days throughout growth.",
            "Avoid water stress during boll bursting; dry weather at maturity ensures clean lint.",
            "Practice integrated pest management (IPM) to control pink bollworm and whitefly."
        ],
        "economic_value": "Cornerstone of the global textile industry; substantial domestic employment and export revenue."
    },
    "jute": {
        "name": "Jute",
        "scientific_name": "Corchorus olitorius",
        "icon": "🧶",
        "category": "Bast Fibre / Cash Crop",
        "description": "Known as the 'Golden Fibre', jute is an eco-friendly, biodegradable natural fibre cultivated in warm, wet river deltas and floodplains.",
        "soil_type": "New alluvial soils along river banks that receive silt deposits",
        "ideal_temp": "24°C - 35°C",
        "ideal_rainfall": "150 - 200 mm",
        "ideal_humidity": "70% - 90%",
        "ideal_ph": "6.0 - 7.4",
        "water_requirement": "High (plenty of clean, slow-moving water needed for retting)",
        "growing_season": "Early Kharif (Pre-monsoon sowing)",
        "duration": "120 - 140 days",
        "farming_tips": [
            "Broadcast or line-sow before the monsoon breaks so stems establish before heavy inundation.",
            "Harvest at 50% flowering stage for the finest strength and lustre in the harvested fibre.",
            "Ensure gentle submerged retting in clean water to separate bast fibers cleanly from woody stalks."
        ],
        "economic_value": "Surging worldwide demand for sustainable packaging, eco-friendly shopping bags, and geo-textiles."
    },
    "coffee": {
        "name": "Coffee",
        "scientific_name": "Coffea arabica / canephora",
        "icon": "☕",
        "category": "Beverage / Plantation Crop",
        "description": "Coffee is a high-value plantation crop cultivated in high-altitude shade-grown agro-forests with rich volcanic or forest humus and gentle tropical rains.",
        "soil_type": "Deep, fertile forest loam or volcanic soil rich in humus",
        "ideal_temp": "23°C - 28°C",
        "ideal_rainfall": "115 - 200 mm",
        "ideal_humidity": "50% - 70%",
        "ideal_ph": "6.0 - 7.0",
        "water_requirement": "High (needs blossom showers in spring followed by backing rains)",
        "growing_season": "Perennial Plantation (harvesting in Winter)",
        "duration": "Perennial (harvest 7-9 months after flowering)",
        "farming_tips": [
            "Grow under a two-tier shade tree canopy (silver oak, dadap) to buffer thermal extremes.",
            "Blossom showers (25-40 mm) in March-April are crucial to initiate synchronized flower opening.",
            "Selective hand-picking of bright red cherries yields specialty-grade beans."
        ],
        "economic_value": "Highly traded global commodity with booming specialty cafe culture and solid foreign exchange earnings."
    }
}


def get_crop_info(crop_name: str) -> dict:
    """
    Retrieves agronomic information for a predicted crop.
    
    Args:
        crop_name (str): Lowercase crop name
        
    Returns:
        dict: Detailed crop information, or default metadata if crop not cataloged.
    """
    key = crop_name.strip().lower()
    if key in CROP_DATABASE:
        return CROP_DATABASE[key]
    
    # Sensible fallback if unexpected crop is queried
    return {
        "name": crop_name.capitalize(),
        "scientific_name": "Not specified",
        "icon": "🌱",
        "category": "Agricultural Crop",
        "description": f"Recommended crop: {crop_name.capitalize()} based on your soil and climatic parameters.",
        "soil_type": "Fertile, well-drained agricultural soil",
        "ideal_temp": "Optimal local ambient range",
        "ideal_rainfall": "Standard regional requirement",
        "ideal_humidity": "Moderate",
        "ideal_ph": "6.0 - 7.0",
        "water_requirement": "Moderate",
        "growing_season": "Seasonal",
        "duration": "Standard maturity cycle",
        "farming_tips": [
            "Perform comprehensive soil testing before sowing.",
            "Use certified high-yield disease-resistant seeds.",
            "Apply balanced fertilizer according to extension guidelines."
        ],
        "economic_value": "Good commercial potential under sound agronomic practices."
    }


def get_all_crop_keys() -> list:
    """Returns sorted list of all cataloged crop keys."""
    return sorted(list(CROP_DATABASE.keys()))
