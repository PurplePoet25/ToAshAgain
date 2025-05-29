# 🌆 To Ash Again

A pixel art platformer set in a dreamlike, post-collapse city where ashes drift through broken skies and forgotten powers lie buried in dust.
Built with Python and Pygame — handcrafted with love, frustration, and CTRL+Z.

---

## 🎮 Controls

| Key     | Action                           |
| ------- | -------------------------------- |
| `← / →` | Move left / right                |
| `Space` | Jump / Double Jump / Glide       |
| `Shift` | Switch characters (after unlock) |
| `R`     | Read (trigger special animation) |
| `1–3`   | Use item from inventory          |
| `Esc`   | Pause / Exit                     |

---

## 🧠 Features

* 🧝 **Two playable characters** with unique movement styles:

  * **Main**: Double Jump
  * **Alt**: Jump → Flight → Glide (unlocked later)
* 🌍 **Four Acts** (Green, Blue, Umber, Red), each with:

  * Themed backgrounds
  * Unique platform layouts
  * Custom enemy types
* 🦟 **Enemies**:

  * Melee: Patrol and contact damage
  * Ranged: Stationary, shoots projectiles
  * Boss (Infernal Vicar): Aggressive, multi-phase fight
* 🎒 **Inventory system**:

  * Stack-based, 3-slot limit
  * Items are lost when used
* ✨ **Totem powers** (random drops):

  * `Drift` – Dash attack, invincible mid-move
  * `Ember` – Fireball
  * `Pulse` – AoE burst
  * `Gravity` – Pull enemies toward player
  * `Mending` – Heal 1 HP
  * `1up` – Gain a life
* 🎮 **Cutscenes**:

  * Post-act unlocks
  * Final winning sequence
* 🏑 **Endgame dimension**:

  * Unlock via purple star
  * Characters walk through memoryscape of all acts

---

## 🗂️ Project Structure

```
PixelGame/
├── assets/                 # All art, sprite sheets, background images
│   ├── backgrounds/
│   ├── powers/
│   └── sprites/
├── main.py                 # Main game loop
├── game_state.py           # Global state
├── powers.py               # Power logic + effects
├── level.py                # Platform layout per act
├── player.py               # Character behavior
├── actX_manager.py         # Logic per act
├── home_manager.py         # Hub world and unlocking
├── cutscene_manager.py     # Final cutscene logic
└── README.md               # This file
```

---

## 🛠 Installation

### Prerequisites

* Python 3.10+
* Pygame

### Install Pygame

```bash
pip install pygame
```

### Run the Game

```bash
python main.py
```

Make sure all assets are correctly placed and paths aren't broken!

---

## 📸 Visual Preview

***\[Insert GIFs or screenshots here once available]***

> Tip: Use GitHub’s drag-and-drop to add `.gif` or `.png` files into this section.

---

## 🧪 Known Issues / TODOs

* [ ] Implement spike traps
* [ ] Polish collision logic for edge cases
* [ ] Add sound/music support
* [ ] Improve boss projectile hitbox
* [ ] Visual README with game screenshots

---

## ✨ Credits

**Created by Hasan Bukhari**
President of the Student Poets Association @ Southern Miss
Poet, programmer, and pixel punisher.

*“To Ash Again” was built as a love letter to resilience, duality, and Karachi rooftops.*

---

## 📄 License

This game is a personal project. Licensing info coming soon.
Feel free to fork, play, and reach out if you’d like to collaborate.

