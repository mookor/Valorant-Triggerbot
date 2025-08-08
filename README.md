[logo](icon.png "Valorant Triggerbot icon")
# Valorant Triggerbot!
High-speed, low-latency triggerbot for Valorant using pixel-based detection (MSS + NumPy). Optimized for low CPU usage and configurable capture rate.

## Table of Contents
- Features
- How it works
- Installation (Windows)
- Configuration
- Usage
- Performance tuning
- Troubleshooting
- FAQ
- Disclaimer
- Keywords (EN / RU)

## Features
- Centered crosshair detection window (tiny region for maximum performance)
- Low CPU load: capture runs only while the trigger key is held
- Adjustable capture rate limit via `target_hz` (balance speed vs. resources)
- Pixel-based detection for red targets (fast and simple)
- Works on Windows; Python-based (optionally build a standalone .exe)

## How it works
- Captures a small region around the screen center via `mss`
- Parses raw RGB bytes with zero-copy `numpy.frombuffer` for minimal overhead
- Applies a red-dominant mask and computes an average red intensity
- If intensity exceeds `threshold` while `trigger_key` is held, presses `shot_key`

## Installation (Windows)
1. Install Python 3.10+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Recommended) Run terminal as Administrator to ensure global hotkeys work (`keyboard` lib)

## Configuration
All runtime options are in `config.yaml`:

```yaml
offset_x: 5           # half-width of the detection window (pixels)
offset_y: 5           # half-height of the detection window (pixels)
trigger_key: 'shift'  # hold to enable capture + firing
shot_key: 'P'         # in-game alternative fire key (bind the same in Valorant)
sleep_before: 0.005   # delay before firing (seconds)
sleep_after: 0.001    # delay after firing (seconds)
threshold: 5          # red intensity threshold to trigger a shot
icon_path: icon.png   # tray icon path
target_hz: 240        # screen capture frequency limit (Hz)
```

Notes:
- Window size is `(offset_x*2) x (offset_y*2)`, centered on the screen
- Lower `target_hz` and/or `offset_x/offset_y` to reduce CPU usage
- Increase `threshold` for stricter detection, decrease for faster triggering

## Usage
1. In Valorant, bind an alternative fire key (e.g., `P`) and mirror it in `config.yaml` → `shot_key: 'P'`
2. Choose a trigger key (default `shift`) → `trigger_key: 'shift'`
3. Start the app:
   ```bash
   python main.py
   ```
4. Hold the trigger key to enable detection and auto-fire
5. Exit via the tray icon menu → Exit

## Performance tuning
- Reduce `offset_x/offset_y` (smaller capture area → lower CPU)
- Tune `target_hz` (e.g., 120–300). Higher is faster but heavier
- Balance `sleep_before/sleep_after` to avoid double inputs while keeping latency low

## Troubleshooting
- Global hotkeys do not work → run the terminal as Administrator (Windows security restrictions)
- High CPU usage → reduce `offset_x/offset_y`, lower `target_hz`
- Not shooting → verify `shot_key` is bound in Valorant and matches `config.yaml`; adjust `threshold`

## FAQ
### Can I be banned?
Yes. Use at your own risk. Any third-party assistance can lead to penalties.

### Why release this?
Educational purposes. Transparency helps developers research and address such tools.

### Can I use this cheat?
Technically yes, but please don’t. Don’t ruin the game experience for others.

## Disclaimer
This project is for educational and research purposes only. You are solely responsible for how you use it. Respect the game’s Terms of Service and the community.

## Keywords (EN / RU)
valorant triggerbot, valorant pixel bot, valorant auto fire, auto shoot, aim trigger, color trigger, pixel color detection, screen capture bot, mss numpy keyboard, low latency trigger, high fps trigger, windows python triggerbot, valorant cheat research, valorant training tool, минимальная задержка, триггербот валюрант, пиксельный бот, автострельба, быстрый триггер, низкая нагрузка на процессор, ограничение частоты захвата, распознавание по цвету, обучение и исследование