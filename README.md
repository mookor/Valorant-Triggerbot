# Valorant Trigger ![logo](icon.png)
Lightweight screen-trigger with high reaction speed and low CPU usage.

## About
- Works around the crosshair only (small window at the center of the screen)
- Optimized CPU usage: screen capture happens only while the trigger key is held
- Configurable capture rate limit (`target_hz`) to balance speed and load
- Currently detects only red targets
- Windows only. A compiled .exe may be available in Releases

## Installation
1. Install Python 3.10+ on Windows
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Run terminal as Administrator for proper global hotkeys support

## Configuration
All runtime options live in `config.yaml`:

```yaml
offset_x: 5           # half-width of the detection window (in pixels)
offset_y: 5           # half-height of the detection window (in pixels)
trigger_key: 'shift'  # key that enables capture and firing logic while held
shot_key: 'P'         # in-game alternative fire key (bind the same in the game)
sleep_before: 0.005   # delay before firing (seconds)
sleep_after: 0.001    # delay after firing (seconds)
threshold: 5          # red intensity threshold to trigger a shot
icon_path: icon.png   # tray icon path
target_hz: 240        # screen capture frequency limit (Hz)
```

Notes:
- The detection window size is `(offset_x*2) x (offset_y*2)` pixels, centered on the screen
- Lower `target_hz` and/or the offsets to reduce CPU usage
- Increase `threshold` to make the trigger less sensitive, decrease to make it more sensitive

## Usage
1. In Valorant, bind an alternative fire key (e.g., `P`), and set the same key in `config.yaml` → `shot_key: 'P'`
2. Set the trigger key you prefer (defaults to `shift`) → `trigger_key: 'shift'`
3. Launch the app:
   ```bash
   python main.py
   ```
4. Hold the trigger key to enable detection and auto-fire
5. To exit, use the tray icon menu → Exit

## Performance Tips
- Reduce `offset_x/offset_y` to shrink the capture area
- Tune `target_hz` (e.g., 120–300) to match your CPU budget and desired responsiveness
- Keep `sleep_before/sleep_after` minimal for fastest reaction, but adjust to avoid double-firing

## FAQ
### Can I be banned?
Yes. Use at your own risk. Any third-party assistance can lead to penalties.

### Why release this?
Educational purposes. Increased transparency can help developers understand and handle such tools.

### Can I use this cheat?
Technically yes, but please don’t. Don’t ruin the game for others.