# Roadmap

Planned improvements, in priority order. When you pick one up, do it in the template (app, tools, `AGENTS.md`, validator), apply it to the live trip repo if it's still in use, and tick it off here.

## Before the next trip (most useful)

- [x] **1. Opening hours on the trip dates.** Add per-place opening days and hours to `data.json`, e.g. `"hours": {"mon": "closed", "tue": "12:00-21:00", …}` plus `hoursSource`, and `"seasonal"` notes such as "winter hours from November".
  - **App:** warn on cards and in the booking form when a place is closed on a chosen date ("Closed Mon 26"), and add an "Open today" filter.
  - **Research:** `AGENTS.md` should say to check hours for the exact trip dates, especially Monday and Tuesday closures and the switch to winter hours in October and November.
  - **Validation:** `validate.py` checks the format.
- [x] **2. What's on that week.** Add an `events` list to `data.json`: `{name, date(s), time, place id or address, url, note}`. Cover half-term and Halloween family events, market days (e.g. Monmouth, Ross, Coleford) and natural events (e.g. Severn Bore dates and times near Newnham).
  - **App:** show events on the matching night in Nights & bookings and as a "What's on" filter.
  - **AGENTS.md:** research events for the exact dates; only list ones with a source.
- [x] **3. Emergency essentials.** Always include the 24-hour emergency vet (if a dog is coming) and the nearest 24-hour A&E, alongside minor injuries units, with phone numbers from official sources.
  - **App:** pin an "Emergency" box at the top of Essentials: 999, NHS 111, the A&E, the out-of-hours vet.
  - **Validation:** `validate.py` warns if a trip with a dog has no out-of-hours vet.
- [x] **4. Baby facilities.** Add optional fields `"baby": {"highChairs": true, "changing": true, "buggySpace": "plenty"}` with a source, shown as small icons on cards, plus a "Baby-friendly" filter when babies are coming.
- [x] **5. Dog details.** Add `"dog": {"where": "bar only" | "whole pub" | "outside only", "notes": "water bowls, quiet corner"}`, so dinners can be picked for a nervous dog. Show it on cards.
- [x] **6. Ring-ahead checklist.** A section listing every `check: true` place, with a Call button and a "confirmed" tick (saved per phone), so they can all be rung in one sitting before the trip. `phones.py` should also try contact pages (`/contact`) for venues with no `tel:` link on the home page.
- [x] **7. Prices.** Optional `"price": "£" | "££" | "£££"` for food, and `"cost"` text for parking and entry. Show on cards; filter by price.

## App features

- [ ] **8. Online booking links.** Optional `"booking": "https://…"` (OpenTable, ResDiary, the venue's own system, verified like `web`). Show a "Book online" button next to "Book".
- [ ] **9. Add to calendar.** From Nights & bookings, export bookings as an `.ics` file (one event per booking, with the address, phone and a one-hour reminder). This needs no server.
- [ ] **10. Live shared planner (optional).** Real-time syncing of stars, bookings and nights in between phones. It needs a small shared store (e.g. a free serverless KV or Firebase), with the trip's link acting as the key. Keep "Share picks" as the no-account fallback. Only worth it if the whole group plans together.
- [ ] **11. Offline maps tip.** Add a tip (and an `AGENTS.md` step) to download the area in Google Maps offline maps before travelling. Caching OpenStreetMap tiles in bulk isn't allowed by its tile policy, so the app shouldn't try.
- [ ] **12. Walk routes on the map.** Optional `"walk": {"gpx": "routes/<id>.gpx"}`, drawn on the Leaflet map when that walk is selected. Only for routes from an official source or drawn from OpenStreetMap paths.

## Template quality

- [ ] **13. Automatic page test.** A GitHub Action (and a local command) that loads `index.html` with the trip's `data.json` in a headless browser (e.g. Playwright). It should check there are no console errors, every place renders as a card, the filters work, the map loads and the booking form saves. `AGENTS.md` should run it before publishing.
- [ ] **14. Starter data.** Add `examples/forest-of-dean.json` (the current full example) and make the root `data.json` a minimal, commented starter: one area, one place of each type, empty photos. That way a new trip can't carry over Forest of Dean leftovers. Update `AGENTS.md` and the README to match.

## Done

- Items 1–7: opening hours and closures (`tools/hours.py` plus hand-checked hours), What's on, the Emergency box, baby and dog details, the ring-ahead checklist, prices.

- Data-driven app (`data.json`), real drive times (`geo.py`), credited photos (`photos.py`), phone numbers (`phones.py`), validation and a weekly link check.
- Map, Near me, weather with sunset times, Nights & bookings, Share picks, notes with export, packing checklist, offline / Add to Home Screen.
