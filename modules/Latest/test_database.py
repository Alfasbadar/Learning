
from products import Product

class ArrayListGenerator():
    @staticmethod
    def generate_product_tuple():
        print("function generate_product_tuple()")
        product_tuple=()
        name = [
                "The Enigmatic Echo", "Chronicles of Elysium", "Whispers of the Abyss", "Lost in Luminescence",
                "Echoes of the Forgotten", "Serpents of Stardust", "Realm of Resonance", "Echoes from the Ether",
                "The Shattered Scepter", "Harmony's Heir", "The Obsidian Oracle", "Beyond the Horizon",
                "Astral Ascendance", "Crimson Cataclysm", "The Celestial Cipher", "The Ebon Enigma",
                "Starsong Symphony", "The Luminous Labyrinth", "The Ethereal Emissary", "Crest of Cosmos",
                "Song of the Selenites", "Aetherium Alchemy", "The Enchanted Echo", "Veil of Verdant Visions",
                "Empire of Eldritch Echoes", "Whispers of Wraiths", "The Sapphire Seraph", "Inferno's Illumination",
                "The Zephyr Zone", "Echoes of Eternity", "Abyssal Aria", "Chronicles of the Celestial Citadel",
                "The Ephemeral Epoch", "Echoes in the Ember", "The Forgotten Fable", "Specters of Starlight",
                "Moonlit Melodies", "Chronicles of the Crystal Crown", "The Solar Serenade", "Elysian Echo",
                "The Ethereal Epiphany", "The Everlasting Echo", "Sirens of Starfall", "The Shrouded Sonata",
                "Songs of the Sable Sky", "The Whispering Wyrm", "Astral Adagio", "Veiled Visions", "Eternal Echoes",
                "The Enigmatic Epoch", "Whispers of the Whispering Willow", "The Enchanted Eon", "Harmony's Haven",
                "Echoes of Eldritch Enchantment", "Abyssal Allegro", "Celestial Cadence", "Serpentine Symphony",
                "The Crystal Chalice", "Whispers of the Winter Willow", "Chronicles of the Crimson Citadel",
                "The Enchanted Equinox", "Eternal Ember", "Luminescent Lullabies", "The Ephemeral Epilogue",
                "Elysian Echoes", "The Ethereal Elysium", "Veil of the Violet Void", "Sirens of the Sable Sea",
                "Whispers of the Whispering Winds", "Abyssal Aria", "Celestial Chronicles", "The Enchanted Echoes",
                "The Ember Enigma", "Serpentine Sonnet", "Moonlit Melodies", "Elysium's Enchantment", "Whispers of the Winter Willow",
                "Chronicles of the Celestial Cascade", "The Ethereal Eon", "Abyssal Allegiance", "Harmony's Hymn",
                "The Enigmatic Eldritch", "Veil of the Verdant Valley", "Echoes of Eclipsed Eternity", "Eternal Echoes",
                "The Whispering Willow", "Chronicles of the Cosmic Citadel", "Astral Aria", "Sirens of the Solar Sea",
                "The Shrouded Sonata", "Veil of the Velvet Void", "Celestial Cadence", "The Enchanted Ephemera",
                "Chronicles of the Crystal Crown", "Eternal Ember", "Whispers of the Wandering Wraith", "Abyssal Allegro"
            ]

        desc = [
                "A tale of mystery and intrigue set in a world where echoes hold the key to forgotten secrets.",
                "A saga chronicling the epic battles and alliances in the mythical realm of Elysium.",
                "Whispers from the abyss reveal the hidden truths that shape the fate of the cosmos.",
                "Embark on a journey where lost souls find themselves bathed in the radiant glow of luminescence.",
                "Echoes of a forgotten era resurface, challenging the very fabric of time and memory.",
                "Serpents of Stardust weave a mesmerizing tale of deceit, loyalty, and cosmic power.",
                "Explore a realm where resonance is the language of the land, and harmony reigns supreme.",
                "Journey through the ethereal echoes, where each whisper carries the weight of destiny.",
                "The shattered scepter holds the key to a kingdom's destiny, but at what cost?",
                "Harmony's heir must navigate a world teetering on the brink of discord and chaos.",
                "The obsidian oracle foretells of a future where shadows dance with the light of the beyond.",
                "Venture beyond the horizon to discover realms uncharted and destinies intertwined.",
                "Astral ascendance leads the way to realms unknown, where stars guide the journey.",
                "Witness the cataclysmic events that unfold in the crimson glow of destiny.",
                "The celestial cipher unravels the secrets written in the stars, revealing cosmic truths.",
                "Embark on a journey into the ebon enigma, where shadows hold the keys to enlightenment.",
                "Starsong symphony serenades the cosmos, orchestrating the dance of celestial bodies.",
                "Navigate the luminous labyrinth, where each step reveals a new layer of enchantment.",
                "The ethereal emissary bridges the gap between worlds, delivering messages beyond mortal comprehension.",
                "Crest of cosmos rises, marking the zenith of a celestial journey that transcends time and space.",
                "Song of the selenites enchants with melodies that echo through the moonlit expanse.",
                "Aetherium alchemy unveils the secrets of crafting wonders from the ethereal substance.",
                "The enchanted echo reverberates through the ages, leaving an indelible mark on the tapestry of time.",
                "Veil of verdant visions shrouds the landscape, revealing the beauty hidden within the greenery.",
                "Empire of eldritch echoes stands as a testament to the ancient power that once ruled the lands.",
                "Whispers of wraiths haunt the nights, telling stories of souls trapped between realms.",
                "The sapphire seraph guards a realm of unimaginable beauty, where precious stones hold divine power.",
                "Inferno's illumination casts light on the darkest corners, exposing the truths concealed in shadows.",
                "Zephyr zone beckons explorers to a land where winds carry tales of adventure and discovery.",
                "Echoes of eternity echo through time, a timeless melody that transcends mortal understanding.",
                "Abyssal aria resounds in the depths, weaving a haunting melody that draws souls to the unknown.",
                "Chronicles of the celestial citadel unfold, revealing the epic tales etched into the castle's stones.",
                "The ephemeral epoch captures fleeting moments, immortalizing them in the annals of history.",
                "Echoes in the ember tell stories of flames that once burned brightly, now reduced to smoldering embers.",
                "The forgotten fable whispers the tales of beings lost to time, their stories etched in the winds of history.",
                "Specters of starlight dance in the celestial ballet, their luminescent forms painting the night sky.",
                "Moonlit melodies serenade the world, enchanting all who listen with the silver glow of the moon.",
                "Chronicles of the crystal crown reveal the trials and tribulations of a monarchy forged in gemstone.",
                "The solar serenade bathes the world in golden light, a symphony of warmth that embraces all.",
                "Elysian echo resonates in the idyllic landscapes, where nature's chorus sings in perfect harmony.",
                "The ethereal epiphany unlocks the mysteries hidden within the ethereal plane, revealing profound truths.",
                "The everlasting echo reverberates through time, an eternal reminder of the tales that endure.",
                "Sirens of starfall beckon with voices as ethereal as the falling stars, luring adventurers into the night.",
                "The shrouded sonata weaves a tapestry of darkness and light, each note a step on the journey to understanding.",
                "Songs of the sable sky paint a canvas of celestial beauty, where darkness becomes a backdrop for shining stars.",
                "The whispering wyrm guards ancient knowledge, its serpentine form a symbol of wisdom and enigma.",
                "Astral adagio guides travelers through the cosmos, each movement a step in the dance of the universe.",
                "Veiled visions conceal the truth, challenging those who seek knowledge to unravel the mysteries.",
                "Eternal echoes resound in the timeless void, a melody that transcends the boundaries of existence.",
                "The enigmatic epoch unfolds the chapters of a mysterious era, each page revealing a new enigma.",
                "Whispers of the whispering willow echo through the ages, carrying the secrets of the ancient tree.",
                "The enchanted eon spans across the ages, a magical era where time itself dances to an otherworldly rhythm.",
                "Harmony's haven offers refuge in a world filled with discord, a sanctuary for those seeking peace.",
                "Echoes of eldritch enchantment weave a spellbinding narrative, entwining the mystical with the mundane.",
                "Abyssal allegro propels adventurers forward with a rhythm born from the depths of the abyss.",
                "Celestial cadence orchestrates the dance of celestial bodies, creating a cosmic harmony.",
                "Serpentine symphony unfolds in movements, each note revealing a chapter in the tale of the serpentine kingdom.",
                "The crystal chalice holds the elixir of life, its radiant glow promising eternal youth and vitality.",
                "Whispers of the winter willow carry the tales of a tree that thrives in the coldest of seasons.",
                "Chronicles of the crimson citadel recount the trials and triumphs of a fortress built in the hues of red.",
                "The enchanted equinox marks the balance between light and darkness, a moment of celestial equilibrium.",
                "Eternal ember glows with an everlasting flame, a symbol of enduring passion and unwavering hope.",
                "Luminescent lullabies cradle the world in a soothing melody, easing it into a peaceful slumber.",
                "The ephemeral epilogue concludes the tale with a bittersweet note, leaving readers with a sense of closure.",
                "Elysian echoes resonate with the purity of paradise, a harmonious blend of nature's wonders.",
                "The ethereal elysium stands as a testament to the divine beauty that transcends mortal understanding.",
                "Veil of the violet void shrouds the cosmos in a mystical haze, obscuring the boundaries of reality.",
                "Sirens of the sable sea sing haunting melodies, their voices echoing through the depths of the ocean.",
                "Whispers of the whispering winds carry messages from distant lands, connecting realms with unseen threads.",
                "Abyssal aria enchants with a melody that rises from the depths, captivating all who hear its haunting notes.",
                "Celestial chronicles unfold the stories etched into the tapestry of the cosmos, a celestial narrative.",
                "The enchanted echoes linger in the air, leaving traces of magic and mystery for those who listen.",
                "The ember enigma conceals the secrets within the dying flames, an enigma waiting to be unraveled.",
                "Serpentine sonnet weaves a lyrical tale, each verse revealing a facet of the serpentine kingdom.",
                "Moonlit melodies serenade the world with the ethereal glow of the moon, a symphony of night.",
                "Elysium's enchantment captivates with the magic of paradise, where every moment is a breath of wonder.",
                "Whispers of the winter willow tell the tales of a tree that thrives in the frosty embrace of winter.",
                "Chronicles of the celestial cascade reveal the celestial waterfalls that flow through the cosmic realms.",
                "The ethereal eon spans across the ages, a magical era where time itself dances to an otherworldly rhythm.",
                "Abyssal allegiance binds souls to the depths, forging an unbreakable connection to the abyssal realm.",
                "Harmony's hymn resonates with the melody of peace, creating a harmonious atmosphere in the world.",
                "The enigmatic eldritch conceals ancient mysteries, a veil that separates the known from the unknown.",
                "Veil of the verdant valley shrouds the landscape in a cloak of green, revealing the beauty of nature.",
                "Echoes of eclipsed eternity reveal tales of a time when the sun and moon shared the celestial stage.",
                "Eternal echoes persist through time, a timeless melody that continues to echo in the hearts of all.",
                "The whispering willow carries the secrets of the ancient tree, its leaves rustling with hidden knowledge.",
                "Chronicles of the cosmic citadel unfold the celestial stories etched into the castle's cosmic stones.",
                "Astral aria resounds in the cosmic expanse, a celestial melody that captivates all who listen.",
                "Sirens of the solar sea sing enchanting melodies, their voices resonating through the celestial waves.",
                "The shrouded sonata weaves a tapestry of darkness and light, each note a step on the journey to understanding.",
                "Veil of the velvet void conceals the mysteries within the cosmic fabric, inviting explorers into the unknown.",
                "Celestial cadence orchestrates the dance of celestial bodies, creating a cosmic harmony.",
                "The enchanted ephemera reveals the transient magic that weaves through the cosmic realms, ever-changing.",
                "Chronicles of the crystal crown recount the tales etched into the gemstone throne, a regal narrative.",
                "Eternal ember glows with an everlasting flame, a symbol of enduring passion and unwavering hope.",
                "Whispers of the wandering wraith echo through the realms, tales of ethereal beings lost to time.",
                "Abyssal allegro propels adventurers forward with a rhythm born from the depths of the abyss."
            ]

        bp = [
                123, 456, 789, 234, 567, 890, 345, 678, 901, 456,
                789, 234, 567, 890, 345, 678, 901, 234, 567, 890,
                123, 456, 789, 345, 678, 901, 234, 567, 890, 123,
                456, 789, 234, 567, 890, 345, 678, 901, 234, 567,
                890, 123, 456, 789, 345, 678, 901, 234, 567, 890,
                123, 456, 789, 234, 567, 890, 345, 678, 901, 456,
                789, 234, 567, 890, 345, 678, 901, 234, 567, 890,
                123, 456, 789, 345, 678, 901, 234, 567, 890, 123,
                456, 789, 234, 567, 890, 345, 678, 901, 234, 567,
                890, 123, 456, 789, 345, 678, 901, 234, 567, 890
            ]
        sp = [
                197, 536, 796, 240, 579, 899, 352, 695, 972, 526,
                797, 243, 576, 897, 350, 685, 911, 240, 575, 899,
                190, 533, 797, 351, 682, 908, 247, 579, 898, 187,
                532, 791, 245, 573, 899, 358, 689, 908, 236, 572,
                899, 130, 467, 798, 350, 678, 906, 233, 577, 893,
                129, 463, 800, 233, 570, 889, 348, 689, 908, 526,
                794, 242, 576, 899, 350, 682, 901, 239, 569, 892,
                127, 461, 797, 349, 681, 906, 230, 575, 891, 190,
                533, 794, 241, 575, 902, 350, 685, 908, 238, 573,
                902, 189, 539, 797, 348, 683, 901, 239, 569, 894
            ]

        qty = [
                97, 36, 96, 40, 79, 99, 52, 95, 72, 26,
                97, 43, 76, 97, 50, 85, 11, 40, 75, 99,
                90, 33, 97, 51, 82, 89, 47, 79, 98, 87,
                32, 91, 45, 73, 99, 58, 89, 8, 36, 72,
                99, 30, 67, 98, 50, 78, 6, 33, 78, 93,
                29, 63, 5, 33, 70, 89, 48, 89, 8, 26,
                94, 42, 76, 99, 50, 82, 1, 39, 69, 92,
                27, 61, 97, 48, 81, 6, 30, 75, 91, 90,
                33, 94, 41, 75, 2, 50, 85, 8, 38, 73,
                2, 89, 39, 97, 48, 83, 1, 39, 69, 94
            ]
        product_tuple = ()
        for i in range(0, 90):
            product_id = i
            product_name = name[i-1]
            product_desc = desc[i-1]
            product_sp = sp[i-1]
            product_bp = bp[i-1]
            product_qty = qty[i-1]
            product = Product(product_id, product_name, product_desc, product_sp, product_bp, product_qty, "")
            print(product)
            product_tuple += (product,)
        return product_tuple
