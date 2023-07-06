class: center, middle, gray-background

# Title

## Autor

Text: CC-BY 4.0

---

.left-column50[
### Streamlines and velocity field

<img src="img/see-how-it-flies/velocity-field.png"
     alt="Velocity Field of a Wing"
     style="width: 300px;" />

.cite[(c) John S. Denker, ["See How It Flies"](https://www.av8n.com/how/)]
]

.right-column50[
### Upwash and downwash

<img src="img/see-how-it-flies/upwash-downwash.png"
     alt="Upwash and Downwash"
     style="width: 300px;" />

.cite[(c) John S. Denker, ["See How It Flies"](https://www.av8n.com/how/)]
]

---

.left-column50[
<img src="img/see-how-it-flies/pressure-near-wing.png"
     alt="Airflow and Pressure Near Wings"
     style="width: 300px;" />

.cite[(c) John S. Denker, ["See How It Flies"](https://www.av8n.com/how/)]
]

.right-column50[
### Airflow and pressure

(write me ...)
]

---

(streamlines in a ram air airfoil)

---

## Differences with airplanes

- wing is flexible/collapsible
- wing is open in front: cell intakes
- there is pressure inside the wing and it varies
- we can change the size of wing during the flight (voluntarily or involuntarily)
- "fuselage" is 8 m below the wing: human is the pendulum weight
- reducing wing loading can make wing collapse
- connection between human and wing is not fixed (slack/tension): inverted flight not possible, nose-dive requires spiraling
- thrust comes from gravity
- altitude is the fuel
- airflow typically comes from below, not from front
- dome/arc/camber
- stability design
- different mechanisms to change angle of attack
- no rudder
- steering

---

<img src="img/lift-drag-coefficients.png"
     alt="Lift and drag coefficients"
     style="width: 600px;" />

.cite[[Pilot’s Handbook of Aeronautical Knowledge, Chapter 5, Aerodynamics of Flight, FAA-H-8083-25B](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak/media/07_phak_ch5.pdf)]

- Data is for a specific airfoil
- Increasing angle of attack (AOA) -> increasing drag and increasing lift
- There is an AOA with optimal glide (optimal L/D ratio)
- A paraglider is typically trimmed to fly close to optimal glide when hands-up
- At a certain AOA, this airfoil stalls

---

<img src="img/drag-vs-speed.png"
     alt="Drag vs. speed"
     style="width: 600px;" />

.cite[[Pilot’s Handbook of Aeronautical Knowledge, Chapter 5, Aerodynamics of Flight, FAA-H-8083-25B](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak/media/07_phak_ch5.pdf)]

- There is an airspeed with optimal glide (minimum drag)
- A paraglider is typically trimmed to fly close to minimal drag when hands-up (and no speed bar applied)

---

(composition of drag: lines, harness, wing, ...)

---

## Brake application

<img src="img/brake-deflection.png"
     alt="Deflection when brake lines are pulled"
     style="width: 600px;" />

.cite[[R. Falquier, T. Lolies, U. Ringertz, Longitudinal Flight Mechanics of Paraglider Systems](https://www.diva-portal.org/smash/get/diva2:1359785/FULLTEXT01.pdf)]

---

## Glide ratio

(add image)

- glide ratio = distance / altitude loss
- typically ~ 10
- launching from 1000 m in still air, no lift or sink, how far can you glide?
- **glide ratio changes with speed** (brake application or speed bar)
- we always glide "down", even when thermalling (surrounding air then rises faster than we sink)
- sail planes can reach glide ratio of 50-60

---

## Glide polar curve

<img src="plots/important-points.svg"
     alt="Glide polar curve and important points along the curve"
     style="width: 600px;" />

- polar curve: relation between horizontal speed and vertical speed
- horizontal speed (brake application or speed bar) and vertical speed are **not independent**

---

<img src="plots/important-points.svg"
     alt="Glide polar curve and important points along the curve"
     style="width: 400px;" />

- slower than min speed: stall
- reducing A lines beyond max speed: frontal collapse
- trim speed is close to best glide ("hands up")
- beginners on modern gliders: do not try to optimize sink with brake application
- min sink is not the same as optimal glide (max distance)
- note how we can read off the glide ratio when looking at the -1.0 m/s vertical speed line
- polar curve depends on how still the air is, altitude, harness, weight, position
- great video: [Andre Bandarra: Polar Curves - Basics](https://www.youtube.com/watch?v=LoTmNHhoQaA)

---

## Polar curves on different gliders

<img src="plots/wing-comparison.svg"
     alt="Polar curves on different gliders"
     style="width: 600px;" />

.cite[inspired by the article "Staying in touch" by Bastienne Wentzel in the Cross Country Magazine (October 2022, p. 34)]

- pushing speed bar increases speed (increases lift) but also reduces AOA (reduces lift)
- modern gliders and higher performance gliders compensate the two better
- high performance gliders are faster and less sinky at higher speed
- there has been a lot of progress in the last 10 years

---

## Flying against headwind

.left-column60[
<img src="plots/polar-headwind.svg"
     alt="Polar curve moved by headwind"
     style="width: 400px;" />
]

.right-column40[
- polar moves to the left

- push speed bar for best glide

- we like a little bit of head wind to start

- shows why we don't want to fly in 10 m/s wind
]

---

## Flying with tailwind

.left-column60[
<img src="plots/polar-tailwind.svg"
     alt="Polar curve moved by tailwind"
     style="width: 400px;" />
]

.right-column40[
- polar moves to the right

- hands up for best glide

- shows why we don't want to land in tailwind
]

---

## Flying in lifting air

.left-column60[
<img src="plots/polar-lift.svg"
     alt="Polar curve moved by lifting air"
     style="width: 400px;" />
]

.right-column40[
- polar moves up

- hands up for best glide
]

---

## Flying in sinking air

.left-column60[
<img src="plots/polar-sink.svg"
     alt="Polar curve moved by sinking air"
     style="width: 400px;" />
]

.right-column40[
- polar moves down

- push speed bar for best glide
]

---

## Effect of adding weight

.left-column60[
<img src="plots/polar-adding-weight.svg"
     alt="Polar curve moved by adding weight"
     style="width: 400px;" />
]

.right-column40[
- polar moves tangentially along the best glide

- glide is unchanged but speeds goes up (**also the stall speed**)

- adding a lot of weight might change shape which would change glide and flight
  characteristics
]

---

## Quiz: what happens when you add 10 kg weight?

- .quote[[ ] Your fly slower]

- .quote[[ ] Your fly faster]

- .quote[[ ] Glide becomes shorter (you land too short)]

- .quote[[ ] Stall speed goes up]

- .quote[[ ] In weak lift you climb less well]

- .quote[[ ] The certification of your glider is still the same]

---

## Roll/pitch/yaw stability

.left-column50[
<img src="img/axes.jpg"
     alt="Three axes: roll, pitch, and yaw"
     style="width: 300px;" />

.cite[From "Nailing the basics of active flying" by Greg Hamerton in the Cross Country Magazine (February/March 2023, p. 36)]
]

.right-column50[
- if wing is pitched/rolled/yawed away from equilibrium, it has the
  **tendency to return to equilibrium** (above your head)
- pilot is the weight on a long pendulum -> tendency to restore
- wing design supports stability (especially beginner wings)
- you will notice reduced stability if you reduce wing span (e.g. during "big
  ears" or "big big ears" maneuver)
- roll/pitch/yaw movements are typically coupled (it is however possible to do them
  separately: dolphining, spiral/looping, heli)
]

---

## Aspect ratio

.left-column50[
<img src="img/low-aspect.jpg"
     alt="Low aspect ratio beginner wing"
     style="width: 250px;" />

.cite[(c) [2018 JackieLou DL](https://pixabay.com/no/photos/paragliding-paraglider-gr%C3%B8nt-seil-3448982/)]

<img src="img/high-aspect.jpg"
     alt="High aspect ratio competition wing"
     style="width: 250px;" />

.cite[(c) 2020 Sebastian Schmied, CC-BY-SA-4.0]
]

.right-column50[
- aspect ratio = span*span / area
- you will never have to compute it, you can look it up for any wing
  ([example 1](https://flyozone.com/paragliders/products/gliders/buzz-z7/),
   [example 2](https://www.advance.swiss/en/products/paragliders/epsilon-dls))
- some example values for orientation:
  - school wings: 4.5 - 5
  - beginner: 5 - 5.5
  - intermediate: 5.5 - 6
  - advanced/sport: 6.5
  - competition: 7.5
- lower aspect: **rounder**, less performance, easier to fly thanks to more stability/rigidity
- higher aspect: **thinner**, less induced drag, more performance (speed,
  better glide, better climb); less stability: more piloting needed to
  prevent deflations and cravats; more dynamic deflations
]
