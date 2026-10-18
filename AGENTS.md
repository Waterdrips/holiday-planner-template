# Holiday planner: agent instructions

Use this repo to build a phone-friendly holiday planner: a static site on GitHub Pages listing walks, places to eat, towns, things to do and essentials near where the group is staying. It shows real drive times from the base, a map, Near me, the weather, bookings, shareable picks, notes and a packing list, and it works offline.

**Everything about a trip lives in `data.json`.** `index.html` is the finished app and reads that file; don't edit it for a normal trip. The `data.json` here is a real example (a Forest of Dean trip with a dog and babies, [live](https://waterdrips.github.io/forest-of-dean-trip/)). Use it as the model for every field, then replace it.

**Preferences:** if a `PREFERENCES.md` sits next to this file (or the user points you to one), read it first. It holds this group's usual party, tastes and defaults, and it overrides the generic defaults below. To make the template your own, replace it with your own `PREFERENCES.md`, or delete it to use the generic defaults. If the user has a `notes.json` from earlier trips (exported from a planner's "My notes"), read it too: favour places they rated highly and skip ones they didn't like.

## 1. Get the brief

Ask for anything below that the prompt or `PREFERENCES.md` doesn't answer, in one message, then get on with it:

- **Base:** the address or postcode of where you're staying.
- **Dates:** arrival and departure.
- **Who's coming:** adults and children (with ages).
- **Dogs:** always ask whether a dog is coming; don't assume, even if one usually does. It changes the whole plan (see "Trip modes" below). If yes: anything that matters (nervous, needs space, off-lead recall).
- **Babies and toddlers:** always ask whether they're coming. If yes: ages, and prams, carriers or both.
- **Focus:** what the trip is for: walking, food, culture, activities, relaxing. Ask; don't assume.
- **Eating:** roughly how many nights out vs in, dietary needs, budget, and the kind of place you like (e.g. "spacious and relaxed").
- **Daily rhythm:** e.g. "leave at 9am, walk in the morning, then lunch in a town and wander the afternoon".
- **Preferences:** towns vs attractions, walk length and difficulty, how far you'll drive.
- **Format:** by default a list grouped by area, not a day-by-day itinerary (a day plan tends to be too rigid). Only plan by day if asked.
- **Publishing:** public or private repo. It always goes on the GitHub account `gh` is logged in to.

Generic defaults if neither the prompt nor `PREFERENCES.md` says: a list by area, about 30 minutes' maximum drive, and a mix of walks, food and towns.

### Trip modes

**With a dog:**
- **Daily rhythm:** plan a dog walk every day.
- **Dog-friendly everything:** every place to eat must welcome dogs.
- **Dinners:** relaxed places with room for the dog. If the dog is nervous, roomy places, quiet corners and heated outdoor seating. Expect some nights eating in.
- **Weighting:** walks are a big part of the list.
- **Data:** add a "Dog" packing list, and vets and pet shops to Essentials.

**Without a dog:**
- **Dog policies don't matter.** Don't set `check` for dog policy, change `trip.checkLabel` (e.g. "Ring ahead: booking advised"), and drop dog-specific notes, tips and packing.
- **Focus:** weight the list towards whatever the group said it wants (food, culture, activities). Walks are usually fewer.

**Food-focused trips** (the group says it loves food, or `PREFERENCES.md` says so): expect more evening meals out, and make eating the centre of the plan:
- **Dinners:** the best restaurants and gastropubs in range, including tasting menus, Michelin- or AA-rosette-listed places and local favourites. Note price level, booking lead time and whether they're likely to be full in school holidays.
- **Lunches and brunches** worth a detour.
- **Food experiences:** bakeries, delis, farm shops, food halls, markets and market days, cheese, wine, cider and gin producers, breweries, tastings and cookery classes.
- **Types:** split dinner into "special" and "relaxed" by adding a type (e.g. `{"id":"dinner-special","label":"🥂 Special dinners"}`) before `dinner` in `types`, and put a tip near the top of `tips` listing the dinners to book now.
- **Food claims need a source.** Only say "Michelin" or "rosette" if a source shows it; otherwise describe the food from reviews and say it's from reviews.

**With babies or toddlers:**
- **Child-friendly places:** check that places welcome babies.
- **Timing:** prefer early dinner slots (5–6pm).
- **Walks:** each walk's `walk.difficulty` says whether it works with a pram or needs a carrier.
- **Data:** add a "Baby" packing list.

**Without babies:** later dinners and longer days out are fine.

## 2. Research

Use web search. Cover every category, aiming for 60–80 places in total. These are the type ids the page knows about (the labels and order come from `types` in `data.json`; add or drop types to suit the trip):

| Type id | What to find |
|---|---|
| `walk` | Walks from the door, short scenic walks, a couple of big ones, flat options for bad weather. |
| `breakfast` | Breakfast and brunch cafés, and bakeries that open early. |
| `lunch` | Cafés and pubs, especially ones at or near walk start points. |
| `dinner` | With a dog: relaxed places with room for it (big pubs, hotels with dog areas, heated outdoor seating). Food-focused: the best food in range (see Trip modes). |
| `food` | Supermarkets, delis, farm shops, bakeries, food halls for nights in. |
| `town` | Towns and villages worth wandering, with what to see. |
| `todo` | Attractions (railways, castles, gardens, crafts), only ones that allow dogs if one is coming. |
| `rainy` | Indoor or covered options. |
| `essential` | Pharmacies, urgent care / minor injuries, supermarkets, and vets and pet shops if a dog is coming. |

Rules:

- **Dog and child policies** (when they're coming): only state what a source says. If no source confirms it, set `"check": true`; the page shows `trip.checkLabel` on those.
- **Exclusions:** if a famous local attraction bans dogs or pushchairs, say so in `tips` rather than listing it.
- **Season:** check school holidays (book dinners early), clock changes and sunset time, and off-season closures. Put them in `tips`.
- **Don't invent facts:** no made-up opening hours, phone numbers, postcodes or "Michelin" claims. Quote sources' claims as claims.
- **Sources:** add every source you used to `sources` (`[name, url]`).

## 3. Write `data.json`

Copy the example's shape exactly:

- **`trip`:**
  - `title`, `description`, `start` and `end` (`YYYY-MM-DD`), and `timezone` (e.g. `Europe/London`);
  - `storagePrefix`: short and new for each trip, so saved stars and bookings don't mix between trips;
  - `checkLabel` and `countryCodes` (e.g. `gb`, used by geocoding);
  - `origin`: `name` (e.g. "the cottage"), `address`, and optionally `geo` (a better search text for the map lookup);
  - optionally `emoji` for the header, `subtitle`, and `mapFitMiles` (default 18: places further away don't zoom the map out).
- **`types`**: `[{id, label}]`, in the order the filter chips should appear.
- **`areas`:** 5–8 areas grouped by geography (e.g. "On your doorstep", each nearby town, "Further afield", "Essentials"). Each has `id`, `title` and a one-line `note` on how its places relate ("all within 10 minutes of each other").
- **`places`:**

  ```json
  {"id":"short-id", "a":"area-id", "n":"Name, Town", "t":["walk","lunch"], "q":"Google Maps search text", "town":"Town for geocoding fallback",
   "note":"What it is and why it suits the group (dog/baby details).", "near":"What it's close to",
   "mi":3, "min":8, "mode":"walking (only for places within about a mile)", "check":true,
   "web":"https://verified-url", "photo":"Wikipedia article title", "geo":"better geocoder search text",
   "walk":{"length":"About 3 mi loop", "difficulty":"Easy, wide gravel", "parking":"Car park (paid)", "toilets":true, "route":"https://official-route-page"}}
  ```

  `mi` and `min` can start as estimates; `tools/geo.py` replaces them. Give every place a `near` line so pairings are obvious ("Next to the Buckstone; 10 min to Monmouth").
- **`pairings`** (walk, then lunch, then a town, in the same area) and **`tips`** are lists of short HTML strings (`<b>` is fine).
- **`packing`**: `{"Group name": ["item", …]}`, e.g. Dog, Baby, Everyone.
- **`photos`** is filled in by `tools/photos.py`; don't write it by hand.

## 4. Run the tools

All are plain Python 3 with no dependencies. Run them in this order from the repo root:

1. **`python3 -I tools/geo.py data.json`**: finds coordinates for the base and every place (OpenStreetMap, one request a second, so it takes a few minutes) and real road distances and times (OSRM; foot routing for `mode: "walking"`). Then **check its output**:
   - Look for places that are wildly far (a pub "in Scotland") or that ended up on the town centre (`geoApprox`). Fix them with a better `geo`, or by setting `lat`/`lon` by hand, and rerun.
   - A walk should use the coordinates of its start point (e.g. the car park).
   - If routing picks a silly route, set `mi`/`min` by hand with `"fixedDistance": true`.
2. **`python3 -I tools/photos.py data.json`**: for each place's `photo` (a Wikipedia article title), stores a freely licensed Wikimedia Commons image and its full credit. Places without a free image lose their `photo`.
3. **`python3 -I tools/phones.py data.json`**: takes each venue's phone number from the `tel:` link on its own website (`web`), with `phoneSource`. Tourism and aggregator pages are skipped. If a page lists several numbers, check the first one is really the venue's and remove it if unsure.
4. **`python3 -I tools/validate.py data.json`**: must finish with 0 errors. Fix warnings where you can.
5. **`python3 -I tools/check_links.py data.json`**: every `web` link and photo should load. Replace or remove broken links.

## 5. Links

- **Directions and Map** buttons are built from `q` and the base address, so make `q` specific (name plus town or postcode).
- **`web`:** only add a URL after checking it loads, e.g. `curl -s -o /dev/null -L -m 12 -A "Mozilla/5.0" -w "%{http_code} %{url_effective}" <url>`. Use the final URL, not your guess. Official tourism or heritage pages (Forestry England, National Trust, English Heritage, Cadw, local tourism sites) are fine. Never guess a domain. Without `web`, the card shows a Google **Search** button.
- **Phones:** only from `tools/phones.py` or a number you read on the venue's own site, always with `phoneSource`.

## 6. Photos: credit everything

Only freely licensed photos from Wikimedia Commons, all credited: `tools/photos.py` enforces this. No images from venue sites, Google, Tripadvisor or Instagram.

- A pub can use its village's photo; the card caption names what the photo shows.
- Don't use a misleading photo (e.g. a long-distance path's photo for one walk).
- The page shows each photo collapsed with an inline credit, plus a Photo credits section listing every one. Keep both.

## 7. Publish and check

1. Get the GitHub account: `OWNER=$(gh api user --jq .login)`. If `gh` isn't logged in, ask the user to run `gh auth login`.
2. Make the trip repo. Either click **Use this template** on GitHub or copy this repo's files (not `.git`, and not `PREFERENCES.md`) into a new folder. Name it `<place>-trip` (add the year if that name is taken). Ask where to create the folder if it isn't obvious; by default, put it next to this template's folder.
3. Set `name` and `short_name` in `manifest.webmanifest` (the home-screen name), and write a short `README.md` with the live link.
4. `git init -b main`, commit, then `gh repo create $OWNER/<name> --public --source . --push` (or `--private` if asked; Pages on a private repo needs a paid GitHub plan).
5. Turn on Pages: `gh api -X POST repos/$OWNER/<name>/pages -f "source[branch]=main" -f "source[path]=/"`.
6. Wait for `gh api repos/$OWNER/<name>/pages/builds/latest --jq .status` to be `built`. Then open the live URL at phone width and check:
   - cards, filters and the map render;
   - the weather shows, if the trip is within about two weeks;
   - a photo opens with its credit;
   - Book, then the Nights & bookings box, works;
   - Directions point at the base;
   - there are no console errors.
7. The repo's GitHub Actions validate `data.json` on every push and check links every Monday, opening an issue if something breaks. Make sure the first validate run passes.
8. Reply with:
   - the link;
   - a short summary of what's in the planner;
   - what's unconfirmed;
   - the sources;
   - a reminder: open the page once on wifi and add it to the home screen, so it works offline.

## What the page does (don't rebuild it)

- **Browsing:** a list grouped by area, filters, search, a map (Leaflet and OpenStreetMap), and Near me (sorts by distance from your location).
- **On each card:** a credited photo, walk details and a footpath map link, Directions, Map, Website or Search, Call, Book, Star, Mark done, and personal notes with a star rating.
- **Weather:** the forecast with sunset times (Open-Meteo), and a "rainy-day ideas" button on wet days.
- **Nights & bookings:** night by night, out (booked) or eating in.
- **Share picks:** sends stars, bookings and nights in as a link that the others merge into their own phone.
- **Packing checklist:** tickable lists.
- **Notes:** "My notes" exports to `notes.json` for next time.
- **Offline:** a service worker plus "Add to Home Screen".

All personal state (stars, ticks, bookings, notes, packing) stays in each phone's localStorage under `trip.storagePrefix`.

## Don'ts

- No personal data on the page: no names, home addresses, phone numbers or emails. The holiday base's address is fine.
- Don't fabricate venues, policies, phone numbers or URLs. If unsure, mark `check: true` or leave it out.
- Don't write a day-by-day plan unless asked.
- Don't hotlink or copy non-free images.
- Don't edit `index.html` or `sw.js` for a normal trip. If you change `sw.js`, bump its `VERSION`.
