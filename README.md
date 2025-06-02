# To Ash Again

A pixel art platformer set in a dreamlike, post-collapse city where ashes drift through broken skies and forgotten powers lie buried in dust.  
Built with Python and Pygame — handcrafted with love, frustration, and CTRL+Z.

---

## ⚙️ How to Play

### 🟣 Option 1: Windows Executable

1. **Download the full project folder** and **rename it exactly**: `To Ash Again`
2. **Place it directly on your Desktop** (recommended)
3. Right-click `To Ash Again.exe` and choose  
   ➤ **"Run as administrator"** or  
   ➤ **"Run anyway"** if prompted by SmartScreen

No Python or setup needed!

---

### 🐍 Option 2: Run with Python (for developers)

#### Prerequisites
* Python 3.10+
* Pygame

#### Install Pygame
```bash
pip install pygame
```

#### Run the Game
```bash
cd files
python main.py
```

Make sure all assets are in the correct folders to avoid path issues.

---

## 🎮 Controls

| Key   | Action                           |
|-------|----------------------------------|
| ← / → | Move left / right                |
| Space | Jump / Double Jump / Glide       |
| Shift | Switch characters (after unlock) |
| R     | Read (trigger special animation) |
| 1–3   | Use item from inventory          |
| Esc   | Pause / Exit                     |

---

## 🌟 Features

### 🧍 Characters
* **Main:** Double Jump
* **Alt:** Jump → Flight → Glide (unlocked later)

### 🗺️ Acts
* Four full acts: **Green**, **Blue**, **Umber**, **Red**
* Each with unique platforms, enemies, and themes

### 👾 Enemies
* **Melee:** Patrol and deal contact damage
* **Ranged:** Shoot projectiles from a distance
* **Boss:** *Infernal Vicar* — aggressive, multi-phase fight

### 🧿 Totem Powers (random sky drops)
* Drift – Dash attack, invincible mid-move
* Ember – Fireball
* Pulse – AoE burst
* Gravity – Pull enemies toward player
* Mending – Heal 1 HP
* 1up – Gain a life

### 📦 Inventory System
* 3 slots (stack-based)
* Powers are lost once used

### 🎬 Cutscenes
* Unlock alternate character via post-Act 2 scene
* Final cutscene in memoryscape

### 🌌 Winning Dimension
* Accessed via purple star
* Walkthrough of all four acts' memories
* Final cup ends the journey

---

## 📁 Project Structure

```plaintext
ToAshAgain/
├── assets/
│   ├── backgrounds/
│   ├── enemies/
│   ├── powers/
│   ├── sprites/
│   └── ui/
├── files/
│   ├── main.py
│   ├── settings.py
│   ├── player.py
│   ├── level.py
│   ├── powers.py
│   ├── enemy.py
│   ├── enemy_data.py
│   ├── game_state.py
│   ├── assets.py
│   ├── cutscene_manager.py
│   ├── home_manager.py
│   ├── win_manager.py
│   ├── screens.py
│   └── act1–4_manager.py
├── To Ash Again.exe
├── _internal/
├── README.md
└── LICENSE
```


---

## 🖼️ Visual Preview

**(Insert GIFs or screenshots here)**  
Tip: Drag and drop `.gif` or `.png` files into this section on GitHub to show off your game!

---

## 🔧 Known Issues / TODOs

* [ ] Implement spike traps
* [ ] Polish collision logic for edge cases
* [ ] Add sound/music support
* [ ] Improve boss projectile hitbox
* [ ] Create visual manual with screenshots

---

## ✍️ Credits

**Created by Hasan Bukhari**  
President, Student Poets Association @ Southern Miss  
Poet, programmer, and pixel punisher.

> "To Ash Again" is a love letter to resilience, duality, and Karachi rooftops.

---

## 📝 License

MIT License – free to play, study, and modify.  
Please credit the original creator if you share or build upon this work.
