# Holiday planner: agent instructions

Use this file to build a phone-friendly holiday planner for a trip: a single static web page on GitHub Pages that lists walks, places to eat, towns, things to do and essentials near where we're staying, each with its distance from our base and a Google Maps link.

The page in `reference/index.html` is the finished Forest of Dean planner (Oct 2026, live at https://waterdrips.github.io/forest-of-dean-trip/). Start from a copy of it and replace the data; don't redesign from scratch.

## 1. Get the brief

Ask for anything below that the prompt doesn't give, in one message, then get on with it:

- **Base:** the address or postcode where we're staying.
- **Dates:** arrival and departure.
- **Who's coming:** adults, children and babies (ages), and whether we have prams, carriers or both.
- **Dogs:** how many, and anything that matters (nervous, reactive, needs space, off-lead recall).
- **Eating:** roughly how many nights out vs in, dietary needs, and the kind of place we like (e.g. "spacious and relaxed").
- **Daily rhythm:** e.g. "leave at 9am, walk in the morning, then lunch in a town and wander the afternoon".
- **Preferences:** towns vs attractions, walk length and difficulty, how far we'll drive.
- **Format:** by default a list grouped by area, not a day-by-day itinerary (we found the day plan too rigid). Only plan by day if asked.
- **Publishing:** public repo on the `Waterdrips` GitHub account unless told otherwise.

Defaults if not given: dogs and babies are with us, we have carriers, we prefer towns over paid attractions, and we're happy to drive up to about 30 minutes.

## 2. Research

Use web search. Cover every category, aiming for 60–80 places in total:

| Type key | What to find |
|---|---|
| `walk` | Walks from the door, short scenic walks, a couple of big ones, flat options for bad weather. Note length, steepness and whether a pram works. |
| `breakfast` | Breakfast and brunch cafés, and bakeries that open early. |
| `lunch` | Cafés and pubs, especially ones at or near walk start points. |
| `dinner` | Relaxed, roomy places with space for a nervous dog. Big pubs, hotels with dog areas, and outdoor heated seating are good. |
| `town` | Towns and villages worth wandering, with what to see. |
| `todo` | Attractions that allow dogs (railways, castles, gardens, crafts). |
| `rainy` | Indoor or covered options. |
| `food` | Supermarkets, delis, farm shops, bakeries, food halls for nights in. |
| `essential` | Vets, pharmacies, pet shops, urgent care / minor injuries, supermarkets. |

Rules:

- **Dog and child policies:** only state what a source says. If no source confirms a venue's dog policy, set `check: true`. The page shows "Ring ahead: dog policy not confirmed" for those.
- **Exclusions:** if a famous local attraction bans dogs or pushchairs, say so in the Tips box rather than listing it.
- **Season:** check school holidays (book dinners early), clock changes and sunset time, and off-season closures. Put them in Tips.
- **Don't invent facts:** no made-up opening hours, phone numbers, postcodes or "Michelin" claims. Quote sources' claims as claims.
- Keep a list of the sources you used; they go in the page footer and your reply.

## 3. Distances

- Give each place `mi` (approx road miles from base) and `min` (approx drive minutes). Use `mode: "walking"` for places within about a mile.
- These are estimates: the header says so, and every card has a Directions button for the real time.
- Group places into 5–8 **areas** by geography (e.g. "On your doorstep", each nearby town, "Further afield", "Essentials"). Each area gets a one-line note on how its places relate ("all within 10 minutes of each other").
- Give each place a `near` line saying what it's close to, so pairings are obvious ("Next to the Buckstone; 10 min to Monmouth").
- Add a "Good pairings" box: walk, then lunch, then a town, in the same area.

## 4. Links

- **Directions:** `https://www.google.com/maps/dir/?api=1&origin=<base>&destination=<q>&travelmode=driving|walking`.
- **Map:** `https://www.google.com/maps/search/?api=1&query=<q>`. Make `q` specific: name plus town or postcode.
- **Websites (`WEB` map):** only add a URL after checking it responds, e.g. `curl -s -o /dev/null -L -m 12 -A "Mozilla/5.0" -w "%{http_code} %{url_effective}" <url>`. Use the final URL, not the guess. Official tourism or heritage pages (Forestry England, National Trust, English Heritage, Cadw, local tourism sites) are fine. Never guess a domain.
- If no website is verified, the card shows a Google **Search** button instead. That's automatic.

## 5. Photos: credit everything

We only use freely licensed photos from Wikimedia Commons, and every photo is credited. No images scraped from venue sites, Google, Tripadvisor or Instagram.

1. List English Wikipedia article titles for places, villages and landmarks (one per line), e.g. `Tintern Abbey`, `Symonds Yat`, `Coleford, Gloucestershire`.
2. Run `python3 -I tools/photos.py titles.txt photos.json`. It takes each article's lead image, keeps it only if it's on Commons, and records the thumbnail URL, file page, artist, licence and licence URL. It batches requests (Wikimedia rate-limits single calls).
3. Map place ids to titles in `PHOTO_FOR`. A pub can use its village's photo; the caption names what the photo shows. Skip photos of something misleading (e.g. a whole long-distance path's photo for one walk).
4. Embed `photos.json` as `PHOTOS` (replace the `/*PHOTOS*/{}` placeholder or the existing object). Clean artist strings: drop "(talk)" and duplicated "Unknown author".
5. The page shows photos collapsed (`<details>`, lazy-loaded) with an inline credit — "Photo: <title> by <artist>, <licence link>, via Wikimedia Commons" — and a **Photo credits** section listing every photo used. Keep both.

## 6. Build the page

Copy `reference/index.html` and change:

- `<title>`, description, header (place and dates), `ORIGIN` (the base address).
- `AREAS`, `P` (and any `P.push(...)` blocks), `WEB`, `PHOTO_FOR`, `PHOTOS`.
- The Good pairings, Tips and footer source list.
- `localStorage` keys (`fod-done`, `fod-stars`, `fod-filter`): give them a new prefix for this trip.

Each place is:

```js
{id:"short-id", a:"area-id", n:"Name, Town", t:["walk","lunch"], mi:3, min:8, mode:"walking"?, q:"Google Maps query",
 note:"What it is and why it suits us (dog/baby details).", near:"What it's close to", check:true?}
```

Keep what's already in the page: mobile-first layout, light and dark mode, sticky filter chips, search, "Hide done", Star (shortlist) and Mark done (saved per phone in localStorage), a "Directions back to base" button, and sorting by distance within each area. No build step, no frameworks, no external JS.

## 7. Publish and check

1. Repo name: `<place>-trip` (add the year if that name is taken), in its own folder under `~/code/`. Add a short README with the live link.
2. `git init -b main`, commit, `gh repo create Waterdrips/<name> --public --source . --push`.
3. Turn on Pages: `gh api -X POST repos/Waterdrips/<name>/pages -f "source[branch]=main" -f "source[path]=/"`.
4. Wait for `gh api repos/Waterdrips/<name>/pages/builds/latest --jq .status` to be `built`, then open the live URL at phone width. Check: cards render, filters work, a photo opens and loads with its credit, Directions links point at the base.
5. Reply with the link and a short summary of what's in it, what's unconfirmed, and the sources.

## Don'ts

- No personal data on the page: no names, home addresses, phone numbers or emails. The holiday base's address is fine.
- Don't fabricate venues, policies or URLs. If unsure, mark `check: true` or leave it out.
- Don't write a day-by-day plan unless asked.
- Don't hotlink or copy non-free images.
