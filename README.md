# WhatsApp Notification Sound

A lightweight Firefox extension that replaces WhatsApp Web’s default notification sound with custom tones.

Supports:

- Single sound selection
- Multiple sounds (rotation)
- Random mode

Uses unread message detection to trigger alerts, restoring a feature no longer available in WhatsApp Web.


## Usage

In Mozilla Firefox, simply visit this page and add a temporary add on/extension.
about:debugging#/runtime/this-firefox



---

### Issue & Explanation

Windows 11, Firefox, and WhatsApp Web provide no way to customize notification sounds.  
Typical approaches like DOM listeners or title change detection were unreliable, so this uses unread count polling instead.

To avoid CORS and extension resource issues, audio is embedded as base64.

Helper scripts:
- `bsf.py` → converts audio files in `/sounds` to base64  
- `pictoico.py` → generates multiple icon sizes from a single image  

UI and initial setup were assisted with ChatGPT.  
Hades-themed design :) tee hee
