# The World in One Picture — Saturday, 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/konzlodon74-dot/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/konzlodon74-dot/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

Entry for the [make.fun bounty "Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121).

## What it is

One front-page image (`entry.png`, 1024×1024) summing up Saturday 21 November 2026:

- **Russian missiles land in Poland** — two cruise missiles and a suspected drone come down in south-east Poland during a huge Russian attack on Ukraine; PM Tusk calls it an intentional provocation and NATO chief Rutte a grave violation.
- **6.8 quake shakes Peru** — a magnitude 6.8 earthquake strikes Junín in the central Andes, 129 km deep, and is felt in Lima, where residents and lawmakers flee buildings; no casualties reported.
- **UK and EU seal biggest post-Brexit deal** — 100,000 youth visas each way, scrapped food checks and linked carbon markets agreed at the Brussels summit.
- **Wall Street slumps as AI selloff deepens** — the S&P 500 falls 3.7% into correction and the Nasdaq drops 5.3% as Nvidia plunges 14% after Reuters reports the SEC is examining its accounting.
- **Denmark thwarts "Russian plot to kill rapper"** — Danish intelligence says Russia plotted to kill Ukrainian-American rapper Kyivstoner at a Copenhagen concert; Denmark expels Moscow's defence attaché.
- **Mamdani sets 2032 to close Rikers Island** — New York's mayor unveils the first comprehensive plan to shut the jail complex.

Stories verified from AP, Reuters, The Guardian and AFP reports of 20–21 November 2026. This is a v1 entry built early on 21 November; a final version with the full day's news will replace it before the deadline.

## How it runs

`main.py` (Python 3.13, standard library only) validates `entry.png` — a whole PNG with verified chunk CRCs, at most 1 MiB, exactly 1024×1024 — and copies it to `/output/entry.png`. It runs with no network and writes the same bytes on every run.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
