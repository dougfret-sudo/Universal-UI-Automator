# Universal UI-Automation Engine 🖱️

A high-fidelity **Robotic Process Automation (RPA)** engine designed to bypass heuristic behavioral analysis. This tool uses non-linear pathing and variable latency to simulate human interaction patterns, enabling interoperability in environments without native APIs.

### 🛠️ Core Stealth Features
*   **Human-Centric Motion:** Implements **Bézier Curve** mathematics to generate smooth, non-linear mouse trajectories.
*   **Biometric Simulation:** Adds "Micro-Jitter" and variable click-latencies to mimic natural human hand movements.
*   **Fuzzy Target Logic:** Never clicks the same pixel twice; uses randomized landing zones within UI elements to prevent pattern detection.

### 🚀 Technical Implementation
*   **Language:** Python
*   **Libraries:** PyAutoGUI (Human interaction), Math (Bezier calculations).
*   **Safety Architecture:** Integrated **Hardware Fail-Safe** (moving mouse to corner kills process instantly).

### 🛡️ Verified Stability
Developed and stress-tested in a **hardware-isolated sandbox** (iMac partition) to ensure zero interference with system-level security protocols and 100% stable execution.
