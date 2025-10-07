import streamlit as st
import streamlit.components.v1 as components

# --- 1. GAME DATA LIST (User Provided) ---

GAME_LIST = [
    {
        "name": "Retro Bowl",
        "game_url": "https://hfmanor.com/retro-bowl",
        "game_image_icon": "https://hfmanor.com/image/retro-bowl",
        "game-id": "retro-bowl",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/retro-bowl\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Subway Surfers",
        "game_url": "https://hfmanor.com/subway-surfers",
        "game_image_icon": "https://hfmanor.com/image/subway-surfers",
        "game-id": "subway-surfers",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/subway-surfers\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Basketball Stars",
        "game_url": "https://hfmanor.com/basketball-stars",
        "game_image_icon": "https://hfmanor.com/image/basketball-stars",
        "game-id": "basketball-stars",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/basketball-stars\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Basket Random",
        "game_url": "https://hfmanor.com/basket-random",
        "game_image_icon": "https://hfmanor.com/image/basket-random",
        "game-id": "basket-random",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/basket-random\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Stickman Hook",
        "game_url": "https://hfmanor.com/stickman-hook",
        "game_image_icon": "https://hfmanor.com/image/stickman-hook",
        "game-id": "stickman-hook",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/stickman-hook\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Smash Karts",
        "game_url": "https://hfmanor.com/Smash Karts",
        "game_image_icon": "https://hfmanor.com/image/Smash Karts",
        "game-id": "Smash Karts",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/Smash Karts\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Cookie Clicker",
        "game_url": "https://hfmanor.com/cookie-clicker",
        "game_image_icon": "https://hfmanor.com/image/cookie-clicker",
        "game-id": "cookie-clicker",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/cookie-clicker\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Moto X3M",
        "game_url": "https://hfmanor.com/moto-X3M",
        "game_image_icon": "https://hfmanor.com/image/moto-X3M",
        "game-id": "moto-X3M",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/moto-X3M\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Bitlife",
        "game_url": "https://hfmanor.com/bitlife",
        "game_image_icon": "https://hfmanor.com/image/bitlife",
        "game-id": "bitlife",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/bitlife\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Superhot",
        "game_url": "https://hfmanor.com/superhot",
        "game_image_icon": "https://hfmanor.com/image/superhot",
        "game-id": "superhot",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/superhot\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "1v1lol",
        "game_url": "https://hfmanor.com/1v1lol",
        "game_image_icon": "https://hfmanor.com/image/1v1lol",
        "game-id": "1v1lol",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/1v1lol\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Roblox",
        "game_url": "https://hfmanor.com/roblox",
        "game_image_icon": "https://hfmanor.com/image/roblox",
        "game-id": "roblox",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/roblox\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Among Us",
        "game_url": "https://hfmanor.com/among-us",
        "game_image_icon": "https://hfmanor.com/image/among-us",
        "game-id": "among-us",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/among-us\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Snow Rider 3D",
        "game_url": "https://games.mathpapers.org/snowrider3d/index.html",
        "game_image_icon": "https://hfmanor.com/image/Snow Rider 3D",
        "game-id": "Snow Rider 3D",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/Snow-Rider-3D\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Minecraft",
        "game_url": "https://hfmanor.com/Minecraft",
        "game_image_icon": "https://hfmanor.com/image/Minecraft",
        "game-id": "Minecraft",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/Minecraft\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Soundboard",
        "game_url": "https://hfmanor.com/soundboard",
        "game_image_icon": "https://hfmanor.com/image/soundboard",
        "game-id": "soundboard",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/soundboard\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Madalin Stunt Cars 2",
        "game_url": "https://hfmanor.com/madalin-stunt-cars-2",
        "game_image_icon": "https://hfmanor.com/image/madalin-stunt-cars-2",
        "game-id": "madalin-stunt-cars-2",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/madalin-stunt-cars-2\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Deepest Sword",
        "game_url": "https://hfmanor.com/deepest-sword",
        "game_image_icon": "https://hfmanor.com/image/deepest-sword",
        "game-id": "deepest-sword",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/deepest-sword\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Soccer Skills",
        "game_url": "https://hfmanor.com/soccer-skills",
        "game_image_icon": "https://hfmanor.com/image/soccer-skills",
        "game-id": "soccer-skills",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/soccer-skills\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Javascript Snake",
        "game_url": "https://hfmanor.com/javascript-snake",
        "game_image_icon": "https://hfmanor.com/image/javascript-snake",
        "game-id": "javascript-snake",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/javascript-snake\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Basketbros Io",
        "game_url": "https://hfmanor.com/basketbros-io",
        "game_image_icon": "https://hfmanor.com/image/basketbros-io",
        "game-id": "basketbros-io",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/basketbros-io\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Slitherio",
        "game_url": "https://hfmanor.com/slitherio",
        "game_image_icon": "https://hfmanor.com/image/slitherio",
        "game-id": "slitherio",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/slitherio\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Fortnite",
        "game_url": "https://hfmanor.com/fortnite",
        "game_image_icon": "https://hfmanor.com/image/fortnite",
        "game-id": "fortnite",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/fortnite\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Slope 2",
        "game_url": "https://hfmanor.com/slope-2",
        "game_image_icon": "https://hfmanor.com/image/slope-2",
        "game-id": "slope-2",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/slope-2\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Madalin Stunt Cars 3",
        "game_url": "https://hfmanor.com/madalin-stunt-cars-3",
        "game_image_icon": "https://hfmanor.com/image/madalin-stunt-cars-3",
        "game-id": "madalin-stunt-cars-3",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/madalin-stunt-cars-3\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Geodash",
        "game_url": "https://hfmanor.com/geodash",
        "game_image_icon": "https://hfmanor.com/image/geodash",
        "game-id": "geodash",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/geodash\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Stick Duel Battle",
        "game_url": "https://hfmanor.com/stick-duel-battle",
        "game_image_icon": "https://hfmanor.com/image/stick-duel-battle",
        "game-id": "stick-duel-battle",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/stick-duel-battle\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Getaway Shootout",
        "game_url": "https://hfmanor.com/getaway-shootout",
        "game_image_icon": "https://hfmanor.com/image/getaway-shootout",
        "game-id": "getaway-shootout",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/getaway-shootout\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Cluster Rush",
        "game_url": "https://hfmanor.com/cluster-rush",
        "game_image_icon": "https://hfmanor.com/image/cluster-rush",
        "game-id": "cluster-rush",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/cluster-rush\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Tunnel Rush",
        "game_url": "https://hfmanor.com/tunnel-rush",
        "game_image_icon": "https://hfmanor.com/image/tunnel-rush",
        "game-id": "tunnel-rush",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/tunnel-rush\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Tiny Fishing",
        "game_url": "https://hfmanor.com/tiny-fishing",
        "game_image_icon": "https://hfmanor.com/image/tiny-fishing",
        "game-id": "tiny-fishing",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/tiny-fishing\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Pixel Gun Survival",
        "game_url": "https://hfmanor.com/pixel-gun-survival",
        "game_image_icon": "https://hfmanor.com/image/pixel-gun-survival",
        "game-id": "pixel-gun-survival",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/pixel-gun-survival\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Aquapark Slides",
        "game_url": "https://hfmanor.com/aquapark-slides",
        "game_image_icon": "https://hfmanor.com/image/aquapark-slides",
        "game-id": "aquapark-slides",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/aquapark-slides\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Getting Over It",
        "game_url": "https://hfmanor.com/getting-over-it",
        "game_image_icon": "https://hfmanor.com/image/getting-over-it",
        "game-id": "getting-over-it",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/getting-over-it\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Rocket League",
        "game_url": "https://hfmanor.com/Rocket-League",
        "game_image_icon": "https://hfmanor.com/image/Rocket-League",
        "game-id": "Rocket-League",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/Rocket-League\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Doodle Jump",
        "game_url": "https://hfmanor.com/doodle-jump",
        "game_image_icon": "https://hfmanor.com/image/doodle-jump",
        "game-id": "doodle-jump",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/doodle-jump\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Merge Round Racers",
        "game_url": "https://hfmanor.com/merge-round-racers",
        "game_image_icon": "https://hfmanor.com/image/merge-round-racers",
        "game-id": "merge-round-racers",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/merge-round-racers\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Bloxors",
        "game_url": "https://hfmanor.com/bloxors",
        "game_image_icon": "https://hfmanor.com/image/bloxors",
        "game-id": "bloxors",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/bloxors\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Temple Run 2",
        "game_url": "https://hfmanor.com/temple-run-2",
        "game_image_icon": "https://hfmanor.com/image/temple-run-2",
        "game-id": "temple-run-2",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/temple-run-2\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Google Feud",
        "game_url": "https://hfmanor.com/google-feud",
        "game_image_icon": "https://hfmanor.com/image/google-feud",
        "game-id": "google-feud",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/google-feud\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Drift Boss",
        "game_url": "https://hfmanor.com/drift-boss",
        "game_image_icon": "https://hfmanor.com/image/drift-boss",
        "game-id": "drift-boss",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/drift-boss\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Soccer Random",
        "game_url": "https://hfmanor.com/soccer-random",
        "game_image_icon": "https://hfmanor.com/image/soccer-random",
        "game-id": "soccer-random",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/soccer-random\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Moto X3M Pool",
        "game_url": "https://hfmanor.com/moto-X3M-pool",
        "game_image_icon": "https://hfmanor.com/image/moto-X3M-pool",
        "game-id": "moto-X3M-pool",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/moto-X3M-pool\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Vex6",
        "game_url": "https://hfmanor.com/vex6",
        "game_image_icon": "https://hfmanor.com/image/vex6",
        "game-id": "vex6",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/vex6\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Blockpost",
        "game_url": "https://hfmanor.com/blockpost",
        "game_image_icon": "https://hfmanor.com/image/blockpost",
        "game-id": "blockpost",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/blockpost\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Tanuki Sunset",
        "game_url": "https://hfmanor.com/tanuki-sunset",
        "game_image_icon": "https://hfmanor.com/image/tanuki-sunset",
        "game-id": "tanuki-sunset",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/tanuki-sunset\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Crossyroad",
        "game_url": "https://hfmanor.com/crossyroad",
        "game_image_icon": "https://hfmanor.com/image/crossyroad",
        "game-id": "crossyroad",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/crossyroad\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Volley Random",
        "game_url": "https://hfmanor.com/volley-random",
        "game_image_icon": "https://hfmanor.com/image/volley-random",
        "game-id": "volley-random",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/volley-random\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "2048",
        "game_url": "https://hfmanor.com/2048",
        "game_image_icon": "https://hfmanor.com/image/2048",
        "game-id": "2048",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/2048\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Monster Tracks",
        "game_url": "https://hfmanor.com/monster-tracks",
        "game_image_icon": "https://hfmanor.com/image/monster-tracks",
        "game-id": "monster-tracks",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/monster-tracks\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Monkey Mart",
        "game_url": "https://hfmanor.com/Monkey Mart",
        "game_image_icon": "https://hfmanor.com/image/Monkey Mart",
        "game-id": "Monkey Mart",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/Monkey Mart\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Baldis Basics",
        "game_url": "https://hfmanor.com/baldis-basics",
        "game_image_icon": "https://hfmanor.com/image/baldis-basics",
        "game-id": "baldis-basics",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/baldis-basics\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Worlds Hardest Game 2",
        "game_url": "https://hfmanor.com/worlds-hardest-game-2",
        "game_image_icon": "https://hfmanor.com/image/worlds-hardest-game-2",
        "game-id": "worlds-hardest-game-2",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/worlds-hardest-game-2\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Krunker",
        "game_url": "https://hfmanor.com/krunker",
        "game_image_icon": "https://hfmanor.com/image/krunker",
        "game-id": "krunker",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/krunker\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Drive Mad",
        "game_url": "https://hfmanor.com/drive-mad",
        "game_image_icon": "https://hfmanor.com/image/drive-mad",
        "game-id": "drive-mad",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/drive-mad\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Draw The Hill",
        "game_url": "https://hfmanor.com/draw-the-hill",
        "game_image_icon": "https://hfmanor.com/image/draw-the-hill",
        "game-id": "draw-the-hill",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/draw-the-hill\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Sm64",
        "game_url": "https://hfmanor.com/sm64",
        "game_image_icon": "https://hfmanor.com/image/sm64",
        "game-id": "sm64",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/sm64\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Ducklife4",
        "game_url": "https://hfmanor.com/ducklife4",
        "game_image_icon": "https://hfmanor.com/image/ducklife4",
        "game-id": "ducklife4",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/ducklife4\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Tactical Weapon Pack 2",
        "game_url": "https://hfmanor.com/tactical-weapon-pack-2",
        "game_image_icon": "https://hfmanor.com/image/tactical-weapon-pack-2",
        "game-id": "tactical-weapon-pack-2",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/tactical-weapon-pack-2\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Scrapmetal",
        "game_url": "https://hfmanor.com/scrapmetal",
        "game_image_icon": "https://hfmanor.com/image/scrapmetal",
        "game-id": "scrapmetal",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/scrapmetal\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Ovo",
        "game_url": "https://hfmanor.com/ovo",
        "game_image_icon": "https://hfmanor.com/image/ovo",
        "game-id": "ovo",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/ovo\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Stealingthediamond",
        "game_url": "https://hfmanor.com/stealingthediamond",
        "game_image_icon": "https://hfmanor.com/image/stealingthediamond",
        "game-id": "stealingthediamond",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/stealingthediamond\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    },
    {
        "name": "Jetpack Joyride",
        "game_url": "https://hfmanor.com/jetpack-joyride",
        "game_image_icon": "https://hfmanor.com/image/jetpack-joyride",
        "game-id": "jetpack-joyride",
        "iframe": " <iframe width=\"1366\" height=\"768\" src=\"https://hfmanor.com/jetpack-joyride\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe> "
    }
]


# --- 2. PAGE RENDERING FUNCTION ---

def render_game_page(game_data):
    """Renders the Streamlit content for a single game page."""
    st.set_page_config(
        page_title=f"Game Hub | {game_data['name']}",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title(f"🎮 {game_data['name']}")
    st.markdown("---")

    # Display the Game Image and Link
    col1, col2 = st.columns([1, 4])
    with col1:
        # Use a smaller width for the icon in the page body
        st.image(game_data['game_image_icon'], width=150)
        st.markdown(f"[Launch in New Tab]({game_data['game_url']})")

    with col2:
        st.subheader("Instructions/Notes")
        st.info("Maximize your browser window for the best full-screen experience.")

    st.markdown("---")

    # Embed the Game using the exact iframe code
    st.subheader("Embedded Game Window")

    # The iframe code is hardcoded with 1366x768, so we use that for the container size.
    components.html(
        game_data['iframe'],
        height=768 + 20,  # Add a little extra space for scrolling safety
        width=1366,
        scrolling=True
    )

    st.caption(f"Content embedded from: `{game_data['game_url']}`")
    st.warning("⚠️ **Security Disclaimer:** This content is embedded from an external source. Use with caution.")


# --- 3. MULTIPAGE LOGIC (Using Session State) ---

# Get the list of game names for the sidebar selector
game_names = [game['name'] for game in GAME_LIST]

# Initialize session state to track the current page (game)
if 'current_game_name' not in st.session_state:
    st.session_state['current_game_name'] = GAME_LIST[0]['name']

# Custom sidebar design
with st.sidebar:
    st.title("🕹️ Game Navigator")
    st.markdown("---")

    # Use st.radio or st.selectbox for navigation
    selected_game_name = st.radio(
        "Select a Game:",
        game_names,
        index=game_names.index(st.session_state['current_game_name']),
        key='sidebar_game_selector'
    )

    # Update the session state when a new game is selected
    if selected_game_name != st.session_state['current_game_name']:
        st.session_state['current_game_name'] = selected_game_name
        st.experimental_rerun()  # Rerun to switch the page content

# --- 4. MAIN APP EXECUTION ---

# Find the currently selected game data
current_game_data = next(
    (game for game in GAME_LIST if game['name'] == st.session_state['current_game_name']),
    GAME_LIST[0]  # Default to the first game if somehow not found
)

# Render the page based on the selected game data
render_game_page(current_game_data)
