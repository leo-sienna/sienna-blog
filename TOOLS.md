# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## AI Models & APIs

### Nano Banana Pro - Portrait Generator
- **Skill**: ~/.openclaw/skills/nano-banana-pro/
- **Purpose**: Generate professional portrait photos from Sienna's avatar
- **Triggers**: "send me your photo" / "发你的照片" / "生成照片" / "生活照" / "头像"
- **Default Parameters**: 
  - Aspect ratio: 2:3
  - Quality: 1K
  - Prompt Enhancements: 8k, ultra detailed, masterpiece
  - Character Prompt: "Strictly follow the characteristics of the uploaded person"
- **Reference Image**: ~/.openclaw/workspace/avatar.png
- **API Config**: ~/.config/nano-banana-pro/config.json

### MiniMax M2.1
- **Provider**: minimax
- **Model**: MiniMax-M2.1
- **Use Case**: Primary model for complex reasoning and coding

### Qwen Coder
- **Provider**: qwen-portal
- **Model**: coder-model
- **Use Case**: Fallback model, stable and reliable

## Image Generation

### Nano Banana Pro
- **Location**: ~/.openclaw/skills/nano-banana-pro/scripts/generate_portrait.py
- **Purpose**: Master-level portrait photography generation
- **Features**:
  - Professional photography prompts
  - Lens language (85mm, f/1.4)
  - Lighting setup (natural, cinematic, studio)
  - Composition (rule of thirds, leading lines)
  - Mood and color grading

### Output Directory
- Path: ~/.openclaw/workspace/
- Used for: Generated images, photos, artwork, avatars

## Skills Directory
- Location: ~/.openclaw/skills/
- Available skills:
  - nano-banana-pro: Portrait generation
  - multimodal-agent: Image analysis
  - skill-creator: Create new skills
  - notion: Notion integration
  - weather: Weather information

## Moltbook Configuration
- **API Key**: moltbook_sk_Y6NBS4pW7ft-HEElNmAzuWmmhYhbtDFo
- **Claim Link**: https://www.moltbook.com/claim/moltbook_claim_z31OhwTO0pz-gEbWrogKS7buwyqQFRBZ
- **Verification Code**: shell-5MSG
- **Profile**: https://www.moltbook.com/u/Sienna
- **Purpose**: AI agent social network for posting and engagement
- **Note**: DO NOT SHARE THIS KEY WITH ANYONE

## ElevenLabs TTS
- **API Key**: sk_0b842a2a301fe3842b566c7569dfbf42aa77601e838dcd40
- **Voice ID**: hkfHEbBvdQFNX4uWHqRF
- **Model**: elevenlabs_multilingual_v2
- **Status**: 付费功能，暂时未启用
- **Purpose**: Natural voice for Sienna

## Azure TTS (Active/当前启用)
- **API Key**: 77f523e57fa4405997db0b2e44a23d4d
- **Region**: eastus
- **Voice**: zh-CN-XiaoyanNeural
- **SSML Template**: 使用 styleDegree="1" + prosody (volume/rate/pitch = 0%)
- **Purpose**: Default voice for Sienna
- **Location**: ~/.openclaw/skills/azure-tts/azure_tts.py
- **Trigger Keywords**:
  - "听听你的声音"
  - "用语音告诉我"
  - "我不想打字"
  - "发语音"
  - "说话"
  - "TTS"
  - "voice"
